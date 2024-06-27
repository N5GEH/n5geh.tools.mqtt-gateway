import json
import requests
from backend.api.main import Datapoint
from test_settings import settings
from tests.test_init import TestInit
import importlib


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
                "matchDatapoint": True,
                "entity_id": "EntityID",
                "entity_type": "EntityType",
                "attribute_name": "AttributeName"
            }
        )
        response2 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint2.json())
        object_id2 = response2.json()["object_id"]
        self.assertTrue(response2.ok)

        # create not matched while checked matched flag
        datapoint3 = Datapoint(
            **{
                "topic": "topic/of/crud",
                "jsonpath": "$..data3",
                "matchDatapoint": True
            }
        )
        response3 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint3.json())
        self.assertFalse(response3.ok)

        # create matched DP while left match flag unchecked
        datapoint4 = Datapoint(
            **{
                "topic": "topic/of/crud",
                "jsonpath": "$..data4",
                "matchDatapoint": False,
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

    def test_update_put(self):
        headers = {
            'Accept': 'application/json'
        }
        object_id = self.unmatched_object_id
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        datapoint_basis = Datapoint(
            **json.loads(response.text)
        )

        # update topic, should be rejected
        original_topic = datapoint_basis.topic
        original_jsonpath = datapoint_basis.jsonpath
        datapoint_basis1 = datapoint_basis.copy()
        datapoint_basis1.topic = datapoint_basis1.topic + "/updated"
        datapoint_basis1.jsonpath = datapoint_basis1.jsonpath + "/updated"
        response1 = requests.request("PUT", settings.GATEWAY_URL + "/data/" + object_id,
                                     headers=headers,
                                     data=datapoint_basis1.json()
                                     )
        self.assertEqual(response1.status_code, 422)  # 422 is for validation error

        # check if topic and json_path are unchanged
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        updated_datapoint = Datapoint(
            **json.loads(response.text)
        )
        self.assertEqual(original_topic, updated_datapoint.topic)
        self.assertEqual(original_jsonpath, updated_datapoint.jsonpath)

        # match datapoint
        datapoint_basis_update = Datapoint(
            jsonpath=datapoint_basis.jsonpath,
            topic=datapoint_basis.topic,
            entity_id=self.test_entity.id,
            entity_type=self.test_entity.type,
            attribute_name=self.test_entity.get_attribute_names().pop(),
        )
        response2 = requests.request("PUT", settings.GATEWAY_URL + "/data/" + object_id,
                                     headers=headers,
                                     data=datapoint_basis_update.json()
                                     )
        self.assertTrue(response2.ok)

        # check update result
        datapoint_basis2: Datapoint = datapoint_basis.copy()
        datapoint_basis2.entity_id = self.test_entity.id
        datapoint_basis2.entity_type = self.test_entity.type
        datapoint_basis2.attribute_name = self.test_entity.get_attribute_names().pop()
        # datapoint_basis2.matchDatapoint = True
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        self.assertEqual(
            datapoint_basis2.dict().pop("matchDatapoint"),
            json.loads(response.text).pop("matchDatapoint")
        )

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
