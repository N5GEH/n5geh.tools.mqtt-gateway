import json
import requests
import re
import pydantic
import logging
import importlib
from backend.api.main import Datapoint
from test_settings import settings
from tests.test_init import TestInit


class TestCRUD(TestInit):
    """
    Test for data points CRUD
    """

    def setUp(self) -> None:
        super(TestCRUD, self).setUp()
        logging.basicConfig(level=logging.DEBUG)
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
                "entity_id": "EntityID",
                "entity_type": "EntityType",
                "attribute_name": "AttributeName"
            }
        )
        response2 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint2.json())
        object_id2 = response2.json()["object_id"]
        self.assertTrue(response2.ok)

        # create not matched with connected flag set to True, should fail
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
                "jsonpath": "$..data5"
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

        # Fetch the existing datapoint to use as a basis for updates
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        datapoint_basis = Datapoint(
            **json.loads(response.text)
        )

        # Attempt to update the topic and ensure it fails due to missing entity information
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

        # Ensure the response indicates failure
        self.assertFalse(response1.ok)
        self.assertEqual(response1.status_code, 400)
        self.assertIn("entity_id, entity_type, and attribute_name cannot be null", response1.text)

        # Perform a valid update with correct entity information
        datapoint_basis_update = Datapoint(
            jsonpath=datapoint_basis.jsonpath,
            topic=datapoint_basis.topic,
            entity_id=self.test_entity.id,
            entity_type=self.test_entity.type,
            attribute_name=self.test_entity.get_attribute_names().pop(),
        )
        response2 = requests.request("PUT", settings.GATEWAY_URL + "/data/" + object_id, headers=headers,
                                     data=datapoint_basis_update.json())
        self.assertTrue(response2.ok)

        # Verify the update result
        datapoint_basis2: Datapoint = datapoint_basis.copy()
        datapoint_basis2.entity_id = self.test_entity.id
        datapoint_basis2.entity_type = self.test_entity.type
        datapoint_basis2.attribute_name = self.test_entity.get_attribute_names().pop()
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)

        updated_datapoint = Datapoint(**json.loads(response.text))

        self.assertEqual(
            datapoint_basis2.entity_id,
            updated_datapoint.entity_id
        )
        self.assertEqual(
            datapoint_basis2.entity_type,
            updated_datapoint.entity_type
        )
        self.assertEqual(
            datapoint_basis2.attribute_name,
            updated_datapoint.attribute_name
        )

    def test_match_datapoints(self):
        headers = {
            'Accept': 'application/json'
        }

        # Create matched datapoint
        matched_datapoint = Datapoint(
            **{
                "topic": "topic/of/match",
                "jsonpath": "$..data_match",
                "connected": True,
                "entity_id": "dp:001",
                "entity_type": "Device",
                "attribute_name": "temperature"
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                    data=matched_datapoint.json())
        object_id = response.json()["object_id"]
        logging.info(f"Created matched datapoint with object_id: {object_id}")
        logging.info(f"Response for matched datapoint creation: {response.json()}")
        self.assertTrue(response.ok)

        # Verify match status
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id + "/status")
        logging.info(f"Match status response for matched datapoint: {response.json()}")
        self.assertTrue(response.ok)
        self.assertTrue(response.json())

        # Create non-matched datapoint
        unmatched_datapoint = Datapoint(
            **{
                "topic": "topic/of/match",
                "jsonpath": "$..data_nomatch",
                "connected": True,
                "entity_id": "NonExistentEntityID",
                "entity_type": "NonExistentType",
                "attribute_name": "NonExistentAttribute"
            }
        )
        response = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                    data=unmatched_datapoint.json())
        object_id = response.json()["object_id"]
        logging.info(f"Created non-matched datapoint with object_id: {object_id}")
        logging.info(f"Response for non-matched datapoint creation: {response.json()}")
        self.assertTrue(response.ok)

        # Verify non-match status
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id + "/status")
        logging.info(f"Match status response for non-matched datapoint: {response.json()}")
        self.assertTrue(response.ok)
        self.assertFalse(response.json())

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
            try:
                datapoint = Datapoint(
                    **{
                        "object_id": invalid_id,
                        "topic": "topic/of/id_test",
                        "jsonpath": "$..data1"
                    }
                )
                response = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                            data=datapoint.json())
            except Exception as e:
                print(f"Testing invalid_id: {invalid_id} - Expected Validation Error: {str(e)}")
                self.assertTrue(isinstance(e, pydantic.error_wrappers.ValidationError))

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


    def test_partial_update_patch(self):
        headers = {
            'Accept': 'application/json'
        }
        object_id = self.unmatched_object_id

        # Perform initial GET to fetch the existing datapoint
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        datapoint_basis = Datapoint(
            **json.loads(response.text)
        )

        # Test case 1: Successful partial update of entity_id and attribute_name
        update_data = {
            "entity_id": "NewEntityID",
            "attribute_name": "NewAttributeName"
        }
        response = requests.request("PATCH", settings.GATEWAY_URL + "/data/" + object_id,
                                    headers=headers,
                                    data=json.dumps(update_data))
        self.assertTrue(response.ok)

        # Verify the update
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        updated_datapoint = Datapoint(
            **json.loads(response.text)
        )
        self.assertEqual(updated_datapoint.entity_id, update_data["entity_id"])
        self.assertEqual(updated_datapoint.attribute_name, update_data["attribute_name"])

        # Test case 2: Attempt to update forbidden fields jsonpath and topic
        forbidden_update_data = {
            "jsonpath": "$..new_jsonpath",
            "topic": "new/topic"
        }
        response = requests.request("PATCH", settings.GATEWAY_URL + "/data/" + object_id,
                                    headers=headers,
                                    data=json.dumps(forbidden_update_data))
        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 400)

        # Verify that jsonpath and topic are unchanged
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        updated_datapoint = Datapoint(
            **json.loads(response.text)
        )
        self.assertEqual(updated_datapoint.jsonpath, datapoint_basis.jsonpath)
        self.assertEqual(updated_datapoint.topic, datapoint_basis.topic)

        # Test case 3: Provide only entity_id without attribute_name
        invalid_update_data1 = {
            "entity_id": "AnotherNewEntityID"
        }
        response = requests.request("PATCH", settings.GATEWAY_URL + "/data/" + object_id,
                                    headers=headers,
                                    data=json.dumps(invalid_update_data1))
        # Check if attribute_name is set
        self.assertTrue("attribute_name" in response.json())
        self.assertEqual(response.status_code, 200)

        # Test case 4: Provide only attribute_name without entity_id
        invalid_update_data2 = {
            "attribute_name": "AnotherNewAttributeName"
        }
        response = requests.request("PATCH", settings.GATEWAY_URL + "/data/" + object_id,
                                    headers=headers,
                                    data=json.dumps(invalid_update_data2))
        # Check if attribute_name is set
        self.assertTrue("entity_id" in response.json())
        self.assertEqual(response.status_code, 200)

        # Test case 5: Attempt to update matchDatapoint field
        invalid_update_data3 = {
            "matchDatapoint": True
        }
        response = requests.request("PATCH", settings.GATEWAY_URL + "/data/" + object_id,
                                    headers=headers,
                                    data=json.dumps(invalid_update_data3))
        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 400)

        # Test case 6: Update entity_type field
        update_entity_type_data = {
            "entity_type": "NewEntityType"
        }
        response = requests.request("PATCH", settings.GATEWAY_URL + "/data/" + object_id,
                                    headers=headers,
                                    data=json.dumps(update_entity_type_data))
        self.assertTrue(response.ok)

        # Verify the entity_type update
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        updated_datapoint = Datapoint(
            **json.loads(response.text)
        )
        self.assertEqual(updated_datapoint.entity_type, update_entity_type_data["entity_type"])

        # Test case 7: Update description field
        update_description_data = {
            "description": "Updated description"
        }
        response = requests.request("PATCH", settings.GATEWAY_URL + "/data/" + object_id,
                                    headers=headers,
                                    data=json.dumps(update_description_data))
        self.assertTrue(response.ok)

        # Verify the description update
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        updated_datapoint = Datapoint(
            **json.loads(response.text)
        )
        self.assertEqual(updated_datapoint.description, update_description_data["description"])

    def test_delete(self):
        object_id = self.unmatched_object_id
        response = requests.request("DELETE", settings.GATEWAY_URL + "/data/" + object_id)
        self.assertTrue(response.ok)
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        self.assertFalse(response.ok)

    def test_get_status(self):
        response = requests.request("GET", settings.GATEWAY_URL+"/system/status")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("overall_status", data)
        self.assertIn("checks", data)
        self.assertIn("orion", data["checks"])
        self.assertIn("postgres", data["checks"])
        self.assertIn("redis", data["checks"])
        # Check if overall_status is "healthy"
        self.assertEqual(data["overall_status"], "healthy")

    def test_get_version_info(self):
        response = response = requests.request("GET", settings.GATEWAY_URL+"/system/version")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("application_version", data)
        self.assertIn("dependencies", data)
        dependencies = ["fastapi", "aiohttp", "asyncpg", "pydantic", "redis", "uvicorn"]
        for dep in dependencies:
            self.assertIn(dep, data["dependencies"])
            self.assertEqual(data["dependencies"][dep], importlib.metadata.version(dep))

    def test_get_datapoints_by_filters(self):
        headers = {
            'Accept': 'application/json'
        }

        # Test the get_datapoints_by_filters with valid filters
        filters = {"topic": "topic/of/dp_basis:002", "jsonpath": "$..data2"}
        response = requests.request("GET", settings.GATEWAY_URL + "/data", headers=headers, params=filters)
        self.assertTrue(response.ok)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(response.json()[0]['topic'], filters['topic'])
        self.assertEqual(response.json()[0]['jsonpath'], filters['jsonpath'])

        # Test the get_datapoints_by_filters with no filters
        response = requests.request("GET", settings.GATEWAY_URL + "/data", headers=headers, params={})
        self.assertTrue(response.ok)
        self.assertIsInstance(response.json(), list)

        # Test the get_datapoints_by_filters with nonexistent filters
        filters = {"nonexistent": "value"}
        response = requests.get(settings.GATEWAY_URL + "/data", headers=headers, params=filters)
        self.assertTrue(response.ok)
        print(response.json())
        self.assertIsInstance(response.json(), list)

        # Test the get_datapoints_by_filters with invalid filters
        filters = {"topic": 123, "jsonpath": 456}
        response = requests.request("GET", settings.GATEWAY_URL + "/data", headers=headers, params=filters)
        self.assertTrue(response.ok)
        self.assertEqual(response.json(), [])
