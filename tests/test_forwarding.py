import json
import time
from filip.models.ngsi_v2.context import ContextEntity
from backend.api.main import Datapoint
from test_init import TestInit
from test_settings import settings
import requests
import random


class TestForwarding(TestInit):
    """
    Test for data points CRUD
    """

    def setUp(self) -> None:
        super(TestForwarding, self).setUp()
        headers = {
            'Accept': 'application/json'
        }

        self.value_1 = round(random.random(), 4)
        self.payload_dict1 = {
            "data1": self.value_1
        }

        self.value_2 = round(random.random(), 4)
        self.payload_dict2 = {
            "level1": {
                "level2": {
                    "level3": {
                        "data1": self.value_2
                    }
                }
            }
        }

        # create other json path
        self.matched_datapoint2 = Datapoint(
            **{
                "topic": "topic/of/dp_forwarding:001",
                "jsonpath": "$.level1.level2.level3.data1",
                "matchDatapoint": True,
                "entity_id": self.test_entity.id,
                "entity_type": self.test_entity.type,
                "attribute_name": self.test_entity.get_attribute_names().pop()
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL+"/data", headers=headers,
                                    data=self.matched_datapoint2.json())
        self.value_3 = round(random.random(), 4)
        self.payload_dict3 = {
            "level1": {
                "level2": {
                    "level3": {
                        "data1": self.value_3
                    }
                }
            }
        }

        self.value_unmatch = random.random()
        self.payload_unmatch = {
                "data2": self.value_unmatch
        }

    def test_plain_payload(self):
        # plain payload
        # send data to registered and matched datapoint via mqtt
        self.mqttc.publish(
            topic=self.matched_datapoint.topic,
            payload=json.dumps(self.payload_dict1)
        )
        time.sleep(1)
        # query data from CB
        res1 = self.cbc.get_attribute_value(
            entity_id=self.matched_datapoint.entity_id,
            entity_type=self.matched_datapoint.entity_type,
            attr_name=self.matched_datapoint.attribute_name
        )
        # compare
        self.assertEqual(res1, self.value_1)

    def test_nested_payload(self):
        # send data to registered and matched datapoint via mqtt
        self.mqttc.publish(
            topic=self.matched_datapoint.topic,
            payload=json.dumps(self.payload_dict2)
        )
        time.sleep(1)
        # query data from CB
        res2 = self.cbc.get_attribute_value(
            entity_id=self.matched_datapoint.entity_id,
            entity_type=self.matched_datapoint.entity_type,
            attr_name=self.matched_datapoint.attribute_name
        )
        # compare
        self.assertEqual(res2, self.value_2)

    def test_duplicated_datapoint(self):
        headers = {
            'Accept': 'application/json'
        }

        # create new entity in CB
        attrs = {'attr1': {'value': 0,
                           'type': 'Number'},
                 'attr2': {'value': 0,
                           'type': 'Number'}
                 }
        test_duplicate_entity = ContextEntity(
            id="TestDuplicate:001",
            type="TestDuplicate",
            **attrs
        )
        self.cbc.post_entity(entity=test_duplicate_entity)

        # create duplicated point 1
        datapoint_duplicated_1 = Datapoint(
            **{
                "topic": "topic/of/dp_forwarding_duplicate:001",
                "jsonpath": "$..duplicate_data",
                "matchDatapoint": True,
                "entity_id": test_duplicate_entity.id,
                "entity_type": test_duplicate_entity.type,
                "attribute_name": "attr1"
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL + "/data",
                                    headers=headers, data=datapoint_duplicated_1.json())
        object_id_1 = response.json()["object_id"]

        # create duplicated point 2
        datapoint_duplicated_2 = datapoint_duplicated_1.copy()
        datapoint_duplicated_2.attribute_name = "attr2"
        response = requests.request("POST", settings.GATEWAY_URL + "/data",
                                    headers=headers, data=datapoint_duplicated_2.json())
        object_id_2 = response.json()["object_id"]

        # publish data
        value = round(random.random(), 4)
        duplicated_payload = {
                "level1": {
                    "level2": {
                        "level3": {
                            "duplicate_data": value
                        }
                    }
                }
            }
        # publish data
        self.mqttc.publish(
            topic=datapoint_duplicated_1.topic,
            payload=json.dumps(duplicated_payload)
        )
        time.sleep(1)

        # both attribute should receive data
        res1 = self.cbc.get_attribute_value(
            entity_id=datapoint_duplicated_1.entity_id,
            entity_type=datapoint_duplicated_1.entity_type,
            attr_name=datapoint_duplicated_1.attribute_name
        )
        self.assertEqual(res1, value)

        res2 = self.cbc.get_attribute_value(
            entity_id=datapoint_duplicated_2.entity_id,
            entity_type=datapoint_duplicated_2.entity_type,
            attr_name=datapoint_duplicated_2.attribute_name
        )
        self.assertEqual(res2, value)

    def test_explicit_jsonpath(self):
        # send data to registered and matched datapoint via mqtt
        self.mqttc.publish(
            topic=self.matched_datapoint.topic,
            payload=json.dumps(self.payload_dict3)
        )
        time.sleep(1)
        # query data from CB
        res3 = self.cbc.get_attribute_value(
            entity_id=self.matched_datapoint2.entity_id,
            entity_type=self.matched_datapoint2.entity_type,
            attr_name=self.matched_datapoint2.attribute_name
        )
        # compare
        self.assertEqual(res3, self.value_3)
