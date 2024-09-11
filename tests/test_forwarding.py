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
                "connected": True,
                "entity_id": self.test_entity.id,
                "entity_type": self.test_entity.type,
                "attribute_name": self.test_entity.get_attribute_names().pop()
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL +"/data", headers=headers,
                                    data=self.matched_datapoint2.model_dump_json())
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

        self.value_arm = True
        attr_arm = {'attr1':
                        {'value': int(self.value_arm)-1,
                         'type': 'Number'}
                    }
        self.arm_entity = ContextEntity(
            id="Test:arm",
            type="Test",
            **attr_arm
        )
        self.cbc.post_entity(entity=self.arm_entity)
        time.sleep(1)

        self.matched_datapoint_arm = Datapoint(
            **{
                "topic": "v3/airroommonitoring@ttn/devices/eui-00xxxxxxxxxxxxxxxf/up",
                "jsonpath": "$.uplink_message.decoded_payload.bytes.channelA.value",
                "connected": True,
                "entity_id": self.arm_entity.id,
                "entity_type": self.arm_entity.type,
                "attribute_name": self.arm_entity.get_attribute_names().pop()
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL +"/data", headers=headers,
                                    data=self.matched_datapoint_arm.model_dump_json())

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
        """
        Test the functionality to allow one single mqtt data point to be forwarded
        to multiple FIWARE attributes.
        """
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
                "connected": True,
                "entity_id": test_duplicate_entity.id,
                "entity_type": test_duplicate_entity.type,
                "attribute_name": "attr1"
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL + "/data",
                                    headers=headers, data=datapoint_duplicated_1.model_dump_json())
        object_id_1 = response.json()["object_id"]

        # create duplicated point 2
        datapoint_duplicated_2 = datapoint_duplicated_1.model_copy()
        datapoint_duplicated_2.attribute_name = "attr2"
        response = requests.request("POST", settings.GATEWAY_URL + "/data",
                                    headers=headers, data=datapoint_duplicated_2.model_dump_json())
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

    def test_arm_forwarding(self):
        payload = {
                    "end_device_ids": {
                        "device_id": "eui-00xxxxxxxxxxxxxxxf",
                        "application_ids": {
                            "application_id": "airroommonitoring"
                        },
                        "dev_eui": "00xxxxxxxxxxxxxxxF",
                        "join_eui": "0018B24452494331",
                        "dev_addr": "260B10AA"
                    },
                    "correlation_ids": [
                        "gs:uplink:01HQQQ247V0RAVH1MXA98Z301K"
                    ],
                    "received_at": "2024-02-28T11:19:41.260320763Z",
                    "uplink_message": {
                        "session_key_id": "AY1a+0y8iqaXm1/oeZfIvg==",
                        "f_port": 1,
                        "f_cnt": 41,
                        "frm_payload": "QCAAAQABAAEAACY=",
                        "decoded_payload": {
                            "bytes": {
                                "channelA": {
                                    "currentState": False,
                                    "previousFrameState": True,
                                    "value": self.value_arm
                                },
                                "decodingInfo": "true: ON/CLOSED, false: OFF/OPEN",
                                "type": "0x40 Dry Contacts data"
                            }
                        },
                        "rx_metadata": [
                            {
                                "gateway_ids": {
                                    "gateway_id": "eui-7276ff0039040013",
                                    "eui": "7276FF0039040013"
                                },
                                "time": "2023-04-25T08:43:29.036038Z",
                                "timestamp": 3359704092,
                                "rssi": -41,
                                "channel_rssi": -41,
                                "snr": 8.2,
                                "location": {
                                    "latitude": 50.79013458818246,
                                    "longitude": 6.051640212535858,
                                    "altitude": 150,
                                    "source": "SOURCE_REGISTRY"
                                },
                                "uplink_token": "CiIKIAoUZXVpLTcyNzZmZjAwMzkwNDAwMTMSCHJ2/wA5BAATEJyIhMIMGgsIza38rgYQivzUGCDgmuDv47+yAQ==",
                                "channel_index": 7,
                                "received_at": "2024-02-28T11:19:38.771196836Z"
                            },
                            {
                                "gateway_ids": {
                                    "gateway_id": "aixnerd-bvd",
                                    "eui": "3436323821002C00"
                                },
                                "time": "2024-02-28T11:16:13.034372Z",
                                "timestamp": 361599515,
                                "rssi": -114,
                                "channel_rssi": -114,
                                "snr": -7,
                                "location": {
                                    "latitude": 50.786662677133556,
                                    "longitude": 6.080043926583554,
                                    "altitude": 297,
                                    "source": "SOURCE_REGISTRY"
                                },
                                "uplink_token": "ChkKFwoLYWl4bmVyZC1idmQSCDQ2MjghACwAEJuktqwBGgsIza38rgYQ88nIGyD48oqIw5dP",
                                "channel_index": 2,
                                "received_at": "2024-02-28T11:19:41.042920949Z"
                            },
                            {
                                "gateway_ids": {
                                    "gateway_id": "eui-58a0cbfffe804543",
                                    "eui": "58A0CBFFFE804543"
                                },
                                "time": "2024-02-28T11:19:41.036648035Z",
                                "timestamp": 1212161827,
                                "rssi": -110,
                                "channel_rssi": -110,
                                "snr": -2.25,
                                "location": {
                                    "latitude": 50.789513831131764,
                                    "longitude": 6.049510538578034,
                                    "source": "SOURCE_REGISTRY"
                                },
                                "uplink_token": "CiIKIAoUZXVpLTU4YTBjYmZmZmU4MDQ1NDMSCFigy//+gEVDEKO+gMIEGgsIza38rgYQiOPgJCC4webTo5EG",
                                "received_at": "2024-02-28T11:19:41.023389265Z"
                            }
                        ],
                        "settings": {
                            "data_rate": {
                                "lora": {
                                    "bandwidth": 125000,
                                    "spreading_factor": 7,
                                    "coding_rate": "4/5"
                                }
                            },
                            "frequency": "868500000",
                            "timestamp": 3359704092,
                            "time": "2023-04-25T08:43:29.036038Z"
                        },
                        "received_at": "2024-02-28T11:19:41.052399023Z",
                        "consumed_airtime": "0.061696s",
                        "version_ids": {
                            "brand_id": "adeunis",
                            "model_id": "dry-contact",
                            "hardware_version": "1.00",
                            "firmware_version": "1.0",
                            "band_id": "EU_863_870"
                        },
                        "network_ids": {
                            "net_id": "000013",
                            "ns_id": "EC656E0000000181",
                            "tenant_id": "ttn",
                            "cluster_id": "eu1",
                            "cluster_address": "eu1.cloud.thethings.network"
                        }
                    }
                }
        topic = self.matched_datapoint_arm.topic

        self.mqttc.publish(
            topic=topic,
            payload=json.dumps(payload)
        )
        time.sleep(1)
        res = self.cbc.get_attribute_value(
            entity_id=self.matched_datapoint_arm.entity_id,
            entity_type=self.matched_datapoint_arm.entity_type,
            attr_name=self.matched_datapoint_arm.attribute_name
        )
        # compare
        self.assertEqual(res, self.value_arm)

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

    def test_zero_datapoint(self):
        value_new = round(random.random(), 4)
        self.mqttc.publish(
            topic=self.matched_datapoint.topic,
            payload=json.dumps({"data1": value_new})
        )
        time.sleep(1)
        # query data from CB
        res1 = self.cbc.get_attribute_value(
            entity_id=self.matched_datapoint.entity_id,
            entity_type=self.matched_datapoint.entity_type,
            attr_name=self.matched_datapoint.attribute_name
        )
        # compare
        self.assertEqual(res1, value_new)

        zero_like_values = [0, False, "0"]
        for zero_value in zero_like_values:
            self.mqttc.publish(
                topic=self.matched_datapoint.topic,
                payload=json.dumps({"data1": zero_value})
            )
            time.sleep(1)
            # query data from CB
            res1 = self.cbc.get_attribute_value(
                entity_id=self.matched_datapoint.entity_id,
                entity_type=self.matched_datapoint.entity_type,
                attr_name=self.matched_datapoint.attribute_name
            )
            # compare
            self.assertEqual(res1, zero_value)

    def test_removed_datapoints(self):
        """
        Test whether data point will still be forwarded after being deleted
        """
        value_new = round(random.random(), 4)
        self.payload_dict1["data1"] = value_new

        object_id = self.matched_object_id
        response = requests.request("DELETE", settings.GATEWAY_URL + "/data/" + object_id)

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
        self.assertNotEqual(res1, value_new)
