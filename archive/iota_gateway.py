from filip.clients.ngsi_v2.iota import IoTAClient
from filip.models.ngsi_v2.iot import Device, DeviceAttribute, ServiceGroup
from filip.utils.cleanup import clear_iot_agent, clear_context_broker
from filip.models.base import FiwareHeader
import requests
import time
from utils import *
from typing import List

# settings
SERVICE = "test"
SERVICE_PATH = "/"
IOTA_URL = "http://161.35.205.102:4041"
CB_URL = "http://161.35.205.102:1026"

fiware_header = FiwareHeader(service=SERVICE,
                             service_path=SERVICE_PATH)

# TODO there are three places to define the explicit attribute
#  1. iota env (seems like to deactivate the function on service level) no its fault
#  2. service group
#  3. device provisioning


class MqttGateway:
    def __init__(self):
        # TODO what is the better way to save registered topics and arrived attributes?
        #  cache in the object or save to some files(volume)?

        # initialize sensor attributes
        self.sensor_attributes = []
        self.topics = []  # TODO where is it needed?
        # self.topic_converters: List[TopicConverter] = []  # maybe to save the different threads

        # initialize iota client
        s = requests.Session()
        self.iota_client = IoTAClient(
            url=IOTA_URL,
            fiware_header=fiware_header,
            session=s)

        # create gateway device
        self.gateway_device = Device(device_id="gateway:001",
                                     entity_name="ngsi-ld:urn:Gateway:001",
                                     entity_type="Gateway",
                                     protocol="IoTA-JSON",  # TODO maybe change the hard coded part here
                                     transport="MQTT"
                                     )

        # TODO dummy count for the dummy mapping entities
        self.dummy_count = 1

    def clean_up(self):
        # clear the state of your service and scope
        clear_iot_agent(url=IOTA_URL, fiware_header=fiware_header)
        clear_context_broker(url=CB_URL, fiware_header=fiware_header)

    def register_gateway(self):
        self.iota_client.post_device(device=self.gateway_device)

    # create new attribute for each new sensor attribute
    def register_attribute(self, attribute):
        # TODO Update will have to contain the whole gateway device
        #  1. first request? and then attach new attribute?
        #  2. save a filip object up to date? (maybe this idea better, which ensure that the gateway device is under
        #     control)
        print("gateway device")
        print(self.gateway_device.attributes)
        print(f"add attribute: {attribute.name}")
        self.gateway_device.add_attribute(attribute)  # register attribute
        self.iota_client.update_device(device=self.gateway_device)

    # create mapping attributes that can map the gateway attribute with the entity attribute
    def map_attribute(self, attribute_name, entity_name, entity_type, entity_attribute_name):
        """

        Args:
            attribute_name:
                The south bounded attribute name of the gateway device
            entity_name:
                The entity id of the mapping entity
            entity_type:
                The entity type of the mapping entity
            entity_attribute_name:
                The attribute name of the mapping entity

        Returns:

        """
        attribute = self.gateway_device.get_attribute(attribute_name)
        mapping_attribute = DeviceAttribute(
            name=entity_attribute_name,
            type=attribute.type,
            expression="${@"+str(attribute.name)+"}",  # TODO if it works?
            entity_name=entity_name,
            entity_type=entity_type,
            object_id=f"copy{attribute.name}"
            # TODO has to use a unique object ID!
            #  without specification of object id can lead to mismatching problem
            )
        # some tricks to allow duplicated attribute name
        # TODO double check if this code brings negative effects
        self.gateway_device.attributes.append(mapping_attribute)
        self.gateway_device.__setattr__(name='attributes', value=self.gateway_device.attributes)
        self.iota_client.update_device(device=self.gateway_device)

    def is_mapped(self, attribute):
        # check if an attribute is already mapped
        for mapping_attribute in self.gateway_device.attributes:
            if mapping_attribute.entity_name:
                if attribute.name in mapping_attribute.expression:
                    return True  # find the corresponding mapping attribtue
        else:  # if loop over all the attributes and cannot find
            return False

    def get_unmapped_attributes(self):
        # check all attribute and get the list of unmapped attribute
        unmapped = []
        for attribute in self.gateway_device.attributes:
            if attribute.entity_name:
                continue  # do not check the mapping attributes
            if not self.is_mapped(attribute):
                unmapped.append(attribute)
        return unmapped

    def dummy_mapping(self):
        """
        Created for test purpose. The unmapped attributes will be mapped with some dummy entities
        i.e. "entity_id": "urn:ngsi-ld:Test:00X"
             "entity_type": "Test"
                "temperature": {"type": "Number"}
        """
        # TODO create a mapping for testing
        unmapped_attributes = self.get_unmapped_attributes()
        for attribute in unmapped_attributes:
            entity_name = f"urn:ngsi-ld:Test:{self.dummy_count:03}"
            self.dummy_count += 1
            entity_type = "Test"
            entity_attribute_name = "temperature"

            print(f"create mapping for {attribute.name}")
            print(f"input: {attribute.name}, {entity_name}, {entity_type}, {entity_attribute_name}", flush=True)
            self.map_attribute(
                attribute_name=attribute.name,
                entity_name=entity_name,
                entity_type=entity_type,
                entity_attribute_name=entity_attribute_name
            )

    def run(self):
        # main loop
        while True:
            time.sleep(5)  # TODO what is the best sleep time
            print("main loop")

            print("Checking all topic")
            topic_list = load_topics()
            thread_names = [thread.name for thread in threading.enumerate()]
            for topic in topic_list:
                if topic in thread_names:
                    print(f"{topic} already registered")
                else:
                    print(f"Register {topic} and create new client")
                    add_topic(topic, self)

            print("Checking all attribute")
            # TODO just for test
            self.dummy_mapping()


if __name__ == '__main__':
    mqttgateway = MqttGateway()
    mqttgateway.clean_up()

    # TODO where to put these code for group provisioning?
    groups = ServiceGroup(
        service=SERVICE,
        subservice=SERVICE_PATH,
        resource="/iot/json",
        apikey="plugnplay"
    )
    mqttgateway.iota_client.post_groups(service_groups=groups, update=True)

    mqttgateway.register_gateway()
    mqttgateway.run()
