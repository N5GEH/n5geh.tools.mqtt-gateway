from test_init import TestInit
from test_settings import settings
import requests


class TestForwarding(TestInit):
    """
    Test for data points CRUD
    """

    def setUp(self) -> None:
        super(TestForwarding, self).setUp()

    def test_forwarding(self):
        pass
        # TODO send data to registered and matched datapoint via mqtt
        # response = requests.request("POST", settings.GATEWAY_URL+"/data", headers=headers,
        #                             data=unmatched_datapoint.json())
        # TODO query datapoint from CB
        # response = requests.request("GET", settings.GATEWAY_URL+"/data", headers=headers,
        #                             data=unmatched_datapoint.json())

        # TODO send data to unmatched datapoint via mqtt
        # TODO query datapoint from CB

        # TODO send data to unregistered datapoint via mqtt
        # TODO query datapoint from CB

