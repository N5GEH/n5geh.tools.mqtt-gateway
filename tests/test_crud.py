import json
import requests
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
                "object_id": "dp_crud:001",
                "topic": "topic/of/crud",
                "jsonpath": "$../data1"
            }
        )
        response1 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint1.json())
        self.assertTrue(response1.ok)

        # create matched
        datapoint2 = Datapoint(
            **{
                "object_id": "dp_crud:002",
                "topic": "topic/of/crud",
                "jsonpath": "$../data2",
                "matchDatapoint": True,
                "entity_id": "EntityID",
                "entity_type": "EntityType",
                "attribute_name": "AttributeName"
            }
        )
        response2 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint2.json())
        self.assertTrue(response2.ok)

        # create not matched while checked matched flag
        datapoint3 = Datapoint(
            **{
                "object_id": "dp_crud:003",
                "topic": "topic/of/crud",
                "jsonpath": "$../data3",
                "matchDatapoint": True
            }
        )
        response3 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint3.json())
        self.assertFalse(response3.ok)

        # create matched DP while left match flag unchecked
        datapoint4 = Datapoint(
            **{
                "object_id": "dp_crud:004",
                "topic": "topic/of/crud",
                "jsonpath": "$../data4",
                "matchDatapoint": False,
                "entity_id": "EntityID",
                "entity_type": "EntityType",
                "attribute_name": "AttributeName"
            }
        )
        response4 = requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                                     data=datapoint4.json())
        self.assertTrue(response4.ok)

    def test_read(self):
        headers = {
            'Accept': 'application/json'
        }
        object_id = "dp_crud:005"
        datapoint5 = Datapoint(
            **{
                "object_id": object_id,
                "topic": "topic/of/crud",
                "jsonpath": "$../dat5"
            }
        )
        requests.request("POST", settings.GATEWAY_URL + "/data", headers=headers,
                         data=datapoint5.json())
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        self.assertEqual(
            datapoint5,
            Datapoint(
                **json.loads(response.text)
            )
        )

    def test_update(self):
        headers = {
            'Accept': 'application/json'
        }
        object_id = "dp_basis:002"
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        datapoint_basis = Datapoint(
            **json.loads(response.text)
        )

        # update topic
        datapoint_basis1 = datapoint_basis.copy()
        datapoint_basis1.topic = datapoint_basis1.topic + "/updated"
        response1 = requests.request("PUT", settings.GATEWAY_URL + "/data/" + object_id,
                                     headers=headers,
                                     data=datapoint_basis1.json()
                                     )
        self.assertFalse(response1.ok)

        # match datapoint
        datapoint_basis_update = DatapointUpdate(
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

    def test_delete(self):
        object_id = "dp_basis:002"
        response = requests.request("DELETE", settings.GATEWAY_URL + "/data/" + object_id)
        self.assertTrue(response.ok)
        response = requests.request("GET", settings.GATEWAY_URL + "/data/" + object_id)
        self.assertFalse(response.ok)
