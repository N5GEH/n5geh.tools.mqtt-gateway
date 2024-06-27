import json
import requests
import sys
import re

sys.path.append("../../n5geh.tools.mqtt-gateway")

from backend.api.main import Datapoint, DatapointUpdate
from test_settings import settings
from tests.test_init import TestInit

class TestCRUD(TestInit):
    """
    Test for data points CRUD
    """

    def setUp(self) -> None:
        super(TestCRUD, self).setUp()
        pass

    def test_create(self):
        headers = {
            'Accept': 'application/json'
        }

        # create not matched
        datapoint1 = Datapoint(
            **{
                "topic": "topic/of/crud",
                "jsonpath": "$..data1"
            }
        )
        response1 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint1.json())
        object_id1 = response1.json()["object_id"]
        self.assertTrue(response1.ok)

        # create matched
        datapoint2 = Datapoint(
            **{
                "topic": "topic/of/crud",
                "jsonpath": "$..data2",
                "connected": True,
                "entity_id": "EntityID",
                "entity_type": "EntityType",
                "attribute_name": "AttributeName"
            }
        )
        response2 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint2.json())
        object_id2 = response2.json()["object_id"]
        self.assertTrue(response2.ok)

        # create not matched while checked connected flag
        datapoint3 = Datapoint(
            **{
                "topic": "topic/of/crud",
                "jsonpath": "$..data3",
                "connected": True
            }
        )
        response3 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint3.json())
        self.assertFalse(response3.ok)

        # create matched DP while left connected flag unchecked
        datapoint4 = Datapoint(
            **{
                "topic": "topic/of/crud",
                "jsonpath": "$..data4",
                "connected": False,
                "entity_id": "EntityID",
                "entity_type": "EntityType",
                "attribute_name": "AttributeName"
            }
        )
        response4 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint4.json())
        object_id4 = response4.json()["object_id"]
        self.assertTrue(response4.ok)

    def test_read(self):
        headers = {
            'Accept': 'application/json'
        }
        datapoint5 = Datapoint(
            **{
                "topic": "topic/of/crud",
                "jsonpath": "$..dat5"
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                         data=datapoint5.json())
        object_id = response.json()["object_id"]
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)

        self.assertEqual(
            datapoint5.json(include={"topic", "jsonpath"}),
            Datapoint(
                **json.loads(response.text)
            ).json(include={"topic", "jsonpath"})
        )

    def test_duplicated(self):
        """
        Test duplicated data points. Duplicated data points are the points
        that have the same `topic` and `jsonpath`.

        Right now the gateway will accept duplicated data points, because
        it reflects a use case that one single data point can be matched
        to different attributes.
        """
        headers = {
            'Accept': 'application/json'
        }

        # create data point 6
        datapoint6 = Datapoint(
            **{
                "topic": "topic/of/crud",
                "jsonpath": "$..dat6"
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL + "/data",
                                    headers=headers, data=datapoint6.json())
        object_id_6 = response.json()["object_id"]

        # create duplicated dp with data dp 6
        response = requests.request("POST", settings.GATEWAY_URL + "/data",
                                    headers=headers, data=datapoint6.json())
        self.assertTrue(response.ok)

    def test_update(self):
        headers = {
            'Accept': 'application/json'
        }

        object_id = self.unmatched_object_id

        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        datapoint_basis = Datapoint(
            **json.loads(response.text)
        )

        # update topic, should be rejected
        datapoint_basis1 = datapoint_basis.copy()
        datapoint_basis1.topic = datapoint_basis1.topic + "/updated"
        datapoint_basis1.entity_id = None  # Ensure this triggers a failure
        datapoint_basis1.entity_type = None  # Ensure this triggers a failure
        datapoint_basis1.attribute_name = None  # Ensure this triggers a failure
        update_data = datapoint_basis1.json()
        response1 = requests.request("PUT", settings.GATEWAY_URL + "/data/" + object_id, headers=headers,
                                     data=update_data)

        # Log the request and response for debugging
        print(f"Request data for update: {update_data}")
        print(f"Response1 status code: {response1.status_code}")
        print(f"Response1 content: {response1.text}")

        self.assertFalse(response1.ok)

        # connected
        datapoint_basis_update = DatapointUpdate(
            entity_id=self.test_entity.id,
            entity_type=self.test_entity.type,
            attribute_name=self.test_entity.get_attribute_names().pop(),
        )
        response2 = requests.request("PUT", settings.GATEWAY_URL + "/data/" + object_id, headers=headers,
                                     data=datapoint_basis_update.json())
        self.assertTrue(response2.ok)

        # check update result
        datapoint_basis2: Datapoint = datapoint_basis.copy()
        datapoint_basis2.entity_id = self.test_entity.id
        datapoint_basis2.entity_type = self.test_entity.type
        datapoint_basis2.attribute_name = self.test_entity.get_attribute_names().pop()
        # datapoint_basis2.connected = True
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        self.assertEqual(
            datapoint_basis2.dict().pop("connected"),
            json.loads(response.text).pop("connected")
        )

    def test_delete(self):
        object_id = self.unmatched_object_id
        response = requests.request("DELETE", settings.GATEWAY_URL + "/data/" + object_id)
        self.assertTrue(response.ok)
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        self.assertFalse(response.ok)

    def test_match_datapoints(self):
        headers = {
            'Accept': 'application/json'
        }

        # create matched datapoint
        datapoint = Datapoint(
            **{
                "topic": "topic/of/match",
                "jsonpath": "$..data_match",
                "connected": True,
                "entity_id": "dp:001",
                "entity_type": "Device",
                "attribute_name": "temperature"
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers, data=datapoint.json())
        object_id = response.json()["object_id"]
        print(f"Created matched datapoint with object_id: {object_id}")
        print(f"Response for matched datapoint creation: {response.json()}")
        self.assertTrue(response.ok)

        # verify match status
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id + "/status")
        print(f"Match status response for matched datapoint: {response.json()}")
        self.assertTrue(response.ok)
        self.assertTrue(response.json())

        # create non-matched datapoint
        datapoint = Datapoint(
            **{
                "topic": "topic/of/match",
                "jsonpath": "$..data_nomatch",
                "connected": True,
                "entity_id": "NonExistentEntityID",
                "entity_type": "NonExistentType",
                "attribute_name": "NonExistentAttribute"
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers, data=datapoint.json())
        object_id = response.json()["object_id"]
        print(f"Created non-matched datapoint with object_id: {object_id}")
        print(f"Response for non-matched datapoint creation: {response.json()}")
        self.assertTrue(response.ok)

        # verify non-match status
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id + "/status")
        print(f"Match status response for non-matched datapoint: {response.json()}")
        self.assertTrue(response.ok)
        self.assertFalse(response.json())

    def test_object_id_unique(self):
        headers = {
            'Accept': 'application/json'
        }

        # create first datapoint
        datapoint1 = Datapoint(
            **{
                "object_id": "unique_id",
                "topic": "topic/of/id_test",
                "jsonpath": "$..data1"
            }
        )
        response1 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint1.json())
        self.assertTrue(response1.ok)

        # try to create second datapoint with same object_id
        datapoint2 = Datapoint(
            **{
                "object_id": "unique_id",
                "topic": "topic/of/id_test",
                "jsonpath": "$..data2"
            }
        )
        response2 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint2.json())
        self.assertFalse(response2.ok)

    def test_object_id_immutable(self):
        headers = {
            'Accept': 'application/json'
        }

        # create datapoint
        datapoint = Datapoint(
            **{
                "topic": "topic/of/id_test",
                "jsonpath": "$..data1"
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                    data=datapoint.json())
        object_id = response.json()["object_id"]
        self.assertTrue(response.ok)

        # try to update object_id
        update_data = {
            "object_id": "new_id",
            "jsonpath": "$..data1_updated",
            "topic": "topic/of/id_test/updated",
        }
        response = requests.request("PUT", settings.GATEWAY_URL + "/data/" + object_id, headers=headers,
                                    data=json.dumps(update_data))
        self.assertFalse(response.ok)

    def test_object_id_character_set(self):
        headers = {
            'Accept': 'application/json'
        }

        valid_ids = ["valid_id_123", "valid-id-123", "valid:id:123", "valid_id-123"]
        invalid_ids = ["invalid id", "invalid*id", "invalid?id", "invalid/id"]

        # test valid ids
        for valid_id in valid_ids:
            datapoint = Datapoint(
                **{
                    "object_id": valid_id,
                    "topic": "topic/of/id_test",
                    "jsonpath": "$..data1"
                }
            )
            response = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                        data=datapoint.json())
            print(f"Testing valid_id: {valid_id} - Response: {response.status_code}")
            self.assertTrue(response.ok)

        # test invalid ids
        for invalid_id in invalid_ids:
            datapoint = Datapoint(
                **{
                    "object_id": invalid_id,
                    "topic": "topic/of/id_test",
                    "jsonpath": "$..data1"
                }
            )
            response = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                        data=datapoint.json())
            print(f"Testing invalid_id: {invalid_id} - Response: {response.status_code}")
            self.assertEqual(response.status_code, 422)

    def test_object_id_auto_generation(self):
        headers = {
            'Accept': 'application/json'
        }

        # create datapoint without specifying object_id
        datapoint = Datapoint(
            **{
                "topic": "topic/of/id_test",
                "jsonpath": "$..data1"
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                    data=datapoint.json())
        self.assertTrue(response.ok)
        object_id = response.json()["object_id"]
        self.assertTrue(re.match(r'^[a-zA-Z0-9]{6}$', object_id))

        # verify the auto-generated object_id does not already exist
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        self.assertTrue(response.ok)