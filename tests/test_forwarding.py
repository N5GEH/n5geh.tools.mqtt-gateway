import json
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

        self.value_1 = random.random()
        self.payload_dict1 = {
            "data1": self.value_1
        }

        self.value_2 = random.random()
        self.payload_dict2 = {
            "level1": {
                "level2": {
                    "level3": {
                        "data1": self.value_1
                    }
                }
            }
        }

        # create other json path
        self.matched_datapoint2 = Datapoint(
            **{
                "object_id": "dp_forwarding:001",
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
        self.value_3 = random.random()
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
        # query data from CB
        res2 = self.cbc.get_attribute_value(
            entity_id=self.matched_datapoint.entity_id,
            entity_type=self.matched_datapoint.entity_type,
            attr_name=self.matched_datapoint.attribute_name
        )
        # compare
        self.assertEqual(res2, self.value_2)

    def test_explicit_jsonpath(self):
        # send data to registered and matched datapoint via mqtt
        self.mqttc.publish(
            topic=self.matched_datapoint.topic,
            payload=json.dumps(self.payload_dict3)
        )
        # query data from CB
        res3 = self.cbc.get_attribute_value(
            entity_id=self.matched_datapoint2.entity_id,
            entity_type=self.matched_datapoint2.entity_type,
            attr_name=self.matched_datapoint2.attribute_name
        )
        # compare
        self.assertEqual(res3, self.value_3)

        # TODO send data to unmatched datapoint via mqtt
        # TODO query datapoint from CB

        # TODO send data to unregistered datapoint via mqtt
        # TODO query datapoint from CB

