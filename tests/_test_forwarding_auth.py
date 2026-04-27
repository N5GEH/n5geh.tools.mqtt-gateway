import json
import time
import random
import unittest
import requests
from paho.mqtt.client import Client, CallbackAPIVersion
from filip.clients.ngsi_v2 import ContextBrokerClient
from filip.models.ngsi_v2 import ContextEntity
from filip.models.base import FiwareHeaderSecure
from filip.utils.cleanup import clear_context_broker
from tests.test_settings import settings


def _missing_auth_settings():
    missing = []
    if not settings.AUTH_SERVER_URL:
        missing.append("AUTH_SERVER_URL")
    if not settings.AUTH_REALM:
        missing.append("AUTH_REALM")
    if not settings.AUTH_CLIENT_ID:
        missing.append("AUTH_CLIENT_ID")
    if not settings.AUTH_CLIENT_SECRET:
        missing.append("AUTH_CLIENT_SECRET")
    return missing


def _get_access_token():
    token_url = (
        f"{str(settings.AUTH_SERVER_URL).rstrip('/')}/realms/"
        f"{settings.AUTH_REALM}/protocol/openid-connect/token"
    )
    payload = {
        "grant_type": "client_credentials",
        "client_id": settings.AUTH_CLIENT_ID,
        "client_secret": settings.AUTH_CLIENT_SECRET,
    }
    response = requests.post(token_url, data=payload, timeout=15)
    response.raise_for_status()
    data = response.json()
    token = data.get("access_token")
    if not token:
        raise RuntimeError("No access_token in token response")
    return token


class TestForwardingAuth(unittest.TestCase):
    """
    Forwarding test against a gateway configured for a protected Orion endpoint.
    """

    def setUp(self) -> None:
        if not settings.AUTH_ENABLED:
            self.skipTest("Auth disabled. Set AUTH_ENABLED=true to run this test.")

        missing = _missing_auth_settings()
        if missing:
            self.skipTest(f"Missing auth settings: {', '.join(missing)}")

        self.token = _get_access_token()
        self.service = settings.FIWARE_SERVICE
        self.fiware_header = FiwareHeaderSecure(
            service=self.service,
            service_path=settings.FIWARE_SERVICEPATH,
            authorization=f"Bearer {self.token}"
        )
        self.cbc = ContextBrokerClient(
            url=settings.ORION_URL,
            fiware_header=self.fiware_header
        )

        self.health_check()
        self.clean_up()

        # create test entity in Orion
        self.entity_id = "TestAuth:001"
        self.entity_type = "TestAuth"
        self.test_entity = ContextEntity(
            id=self.entity_id,
            type=self.entity_type,
            attr1={"value": 0, "type": "Number"}
        )
        self.cbc.post_entity(entity=self.test_entity)

        # create datapoint in gateway
        headers = {"Accept": "application/json"}
        datapoint_payload = {
            "topic": "topic/of/dp_auth_forwarding:001",
            "jsonpath": "$.data1",
            "entity_id": self.entity_id,
            "entity_type": self.entity_type,
            "attribute_name": "attr1",
            "fiware_service": self.service,
        }
        response = requests.post(
            f"{str(settings.GATEWAY_URL)}/data",
            headers=headers,
            data=json.dumps(datapoint_payload),
            timeout=15,
        )
        if not response.ok:
            response.raise_for_status()
        self.matched_topic = datapoint_payload["topic"]

        # initialize MQTT client
        self.mqttc = Client(callback_api_version=CallbackAPIVersion.VERSION1)
        self.mqttc.connect(host=settings.MQTT_HOST, port=settings.MQTT_PORT)

    def tearDown(self) -> None:
        self.clean_up()
        self.cbc.close()

    def clean_up(self):
        clear_context_broker(fiware_header=self.fiware_header,
                             url=settings.ORION_URL)
        requests.delete(f"{str(settings.GATEWAY_URL)}/data", timeout=15)

    def health_check(self):
        try:
            response = requests.get(f"{str(settings.GATEWAY_URL)}/data", timeout=15)
        except requests.RequestException as exc:
            self.skipTest(f"Gateway not reachable: {exc}")
        if not response.ok:
            response.raise_for_status()

    def test_forwarding_with_auth(self):
        value = round(random.random(), 4)
        payload = {"data1": value}
        self.mqttc.publish(
            topic=self.matched_topic,
            payload=json.dumps(payload)
        )
        time.sleep(1)

        entity = self.cbc.get_entity(entity_id=self.entity_id)
        self.assertEqual(entity.attr1.value, value)
