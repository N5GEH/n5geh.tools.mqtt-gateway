import unittest
from filip.utils.cleanup import clear_context_broker
from paho.mqtt.client import Client, MQTTv5
from backend.api.main import Datapoint
from filip.clients.ngsi_v2.cb import ContextBrokerClient
from filip.models.ngsi_v2.context import ContextEntity
from filip.models.base import FiwareHeader
from test_settings import settings
import requests


class TestInit(unittest.TestCase):
    """
    Test for data points CRUD
    """

    def setUp(self) -> None:
        headers = {
            'Accept': 'application/json'
        }
        self.fiware_header = FiwareHeader(
            service=settings.FIWARE_SERVICE,
            service_path=settings.FIWARE_SERVICEPATH
        )
        self.health_check()
        self.clean_up()

        # create test entity
        attr1 = {'attr1': {'value': 0,
                           'type': 'Number'}}
        self.test_entity = ContextEntity(
            id="Test:001",
            type="Test",
            **attr1
        )
        self.cbc = ContextBrokerClient(fiware_header=self.fiware_header,
                                       url=settings.ORION_URL)
        self.cbc.post_entity(entity=self.test_entity)

        # create basis data points
        unmatched_datapoint = Datapoint(
            **{
                "object_id": "dp_basis:002",
                "topic": "topic/of/dp_basis:002",
                "jsonpath": "$../data2"
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL+"/data", headers=headers,
                                    data=unmatched_datapoint.json())

        matched_datapoint = Datapoint(
            **{
                "object_id": "dp_basis:001",
                "topic": "topic/of/dp_basis:001",
                "jsonpath": "$../data1",
                "matchDatapoint": True,
                "entity_id": self.test_entity.id,
                "entity_type": self.test_entity.type,
                "attribute_name": self.test_entity.get_attribute_names().pop()
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL+"/data", headers=headers,
                                    data=matched_datapoint.json())

        # initialize MQTT client
        self.mqttc = Client(protocol=MQTTv5)
        self.mqttc.connect(
            host=settings.MQTT_HOST,
            port=settings.MQTT_PORT
        )

    def clean_up(self):
        clear_context_broker(fiware_header=self.fiware_header,
                             url=settings.ORION_URL)
        response = requests.request("DELETE", settings.GATEWAY_URL+"/data")

    def health_check(self):
        # health check, if not accessible give warning
        response = requests.request("GET", settings.GATEWAY_URL+"/data")
        if not response.ok:
            response.raise_for_status()

    def tearDown(self) -> None:
        """
        Cleanup test server
        """
        self.cbc.close()
        self.clean_up()
