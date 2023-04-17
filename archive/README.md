# MQTTgateway

A MQTT Gateway that convert all coming message to FIWARE compatible format. The concept is to first send all data to FIWARE platform and then do the data mappings with a mechanism ([multientity](https://github.com/telefonicaid/iotagent-node-lib/blob/9d368e579e161ef49287af29aa7a5112e6579516/doc/advanced-topics.md#multientity-plugin-multientity)) of the platform. Generally, all incoming data will be collected by a single device/entity gateway:xxx. Every sensor data becomes a unique attribute of the gateway, e.g. `tsen001___t`. These attributes can be mapped with the attributes of any concrete entity. The MQTT Gateway will support this mapping process.

## Implementation

There are few options that can realize the concept described above:
- Use the auto provisioning function to let the IoTagent automatically create an attribute for each sensor nodes. Update the attribute with the mapping information.
- Save all sensor nodes. If new sensor nodes come, create new attribute in the gateway:001.

## Getting started

1. Setup a platform locally
2. Run the script dummy_sensor.py
3. Run the script iota_gateway.py
4. View the gateway:001 in IoTagent and ngsi-ld:urn:Gateway:001 in Orion
5. Ceate test entities and do the mapping (should be supported by MQTTgateway later)

## Backlog

- Shared subscriptions can be helpful for the scalability

## Road Map

- test the viability
- implement the basic methods/functions
- implement an API (maybe FAST API) to provide the user interaction (backend)
- implement an GUI (frontend)

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

