import paho.mqtt.client as mqtt
import json
import time
from filip.clients.ngsi_v2 import ContextBrokerClient, IoTAClient, QuantumLeapClient
from filip.clients.mqtt import IoTAMQTTClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import Device, DeviceAttribute, ServiceGroup
from filip.utils.cleanup import clear_context_broker, clear_iot_agent
from gateway.gateway import Gateway

payload = {
  "end_device_ids": {
    "device_id": "eui-a81758fffe0482a0",
    "application_ids": {
      "application_id": "test-mqtt-gateway-jdu"
    },
    "dev_eui": "A81758FFFE0482A0",
    "join_eui": "70B3D57ED002454F",
    "dev_addr": "260B6C4D"
  },
  "correlation_ids": [
    "as:up:01GWP5S8M4XT01E30DV0JX268M",
    "gs:conn:01GWM6AA67M2XTTFMTGSHGCP4T",
    "gs:up:host:01GWM6AAAR5158HTW289Z4V02N",
    "gs:uplink:01GWP5S8DKWWE5VT69M4RDK8TA",
    "ns:uplink:01GWP5S8DNF27X85QH2ZX0R9FZ",
    "rpc:/ttn.lorawan.v3.GsNs/HandleUplink:01GWP5S8DN5YAD68NVPJVTEHN0",
    "rpc:/ttn.lorawan.v3.NsAs/HandleUplink:01GWP5S8M4QF2906E44HQ3RPCH"
  ],
  "received_at": "2023-03-29T07:54:41.156303944Z",
  "uplink_message": {
    "session_key_id": "AYcojY1QHWhSvyftdWD6DQ==",
    "f_port": 5,
    "f_cnt": 243,
    "frm_payload": "AQDDAikEAEwFAAcN3REA",
    "decoded_payload": {
      "humidity": 41,
      "light": 76,
      "motion": 0,
      "occupancy": 0,
      "temperature": 19.5,
      "vdd": 3549
    },
    "rx_metadata": [
      {
        "gateway_ids": {
          "gateway_id": "aixnerd-bvd",
          "eui": "3436323821002C00"
        },
        "time": "2023-03-29T07:52:47.923841Z",
        "timestamp": 1012011900,
        "rssi": -111,
        "channel_rssi": -111,
        "snr": 0.5,
        "location": {
          "latitude": 50.786662677133556,
          "longitude": 6.080043926583554,
          "altitude": 297,
          "source": "SOURCE_REGISTRY"
        },
        "uplink_token": "ChkKFwoLYWl4bmVyZC1idmQSCDQ2MjghACwAEPymyOIDGgwIwN2PoQYQ1L/uwwMg4LjwhLrtDw==",
        "channel_index": 4,
        "received_at": "2023-03-29T07:54:40.931424018Z"
      },
      {
        "gateway_ids": {
          "gateway_id": "eui-7276ff00390401a5-2",
          "eui": "7276FF00390401A5"
        },
        "time": "2023-03-29T07:54:40.882231Z",
        "timestamp": 2120758403,
        "rssi": -45,
        "channel_rssi": -45,
        "snr": 10.5,
        "uplink_token": "CiQKIgoWZXVpLTcyNzZmZjAwMzkwNDAxYTUtMhIIcnb/ADkEAaUQg+mg8wcaDAjA3Y+hBhCcnKDFAyC4v7S43D0=",
        "channel_index": 1,
        "received_at": "2023-03-29T07:54:38.670753107Z"
      },
      {
        "gateway_ids": {
          "gateway_id": "mikrotik-ts-ac",
          "eui": "323433363F003E00"
        },
        "time": "2023-03-29T07:54:40.908189Z",
        "timestamp": 1422174820,
        "rssi": -79,
        "channel_rssi": -79,
        "snr": 9.25,
        "location": {
          "latitude": 50.77056505079017,
          "longitude": 6.084591150283814,
          "source": "SOURCE_REGISTRY"
        },
        "uplink_token": "ChwKGgoObWlrcm90aWstdHMtYWMSCDI0MzY/AD4AEOTUkqYFGgwIwN2PoQYQ2rPzzQMgoK3mgbKaBQ==",
        "channel_index": 4,
        "received_at": "2023-03-29T07:54:40.951077424Z"
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
      "frequency": "867300000",
      "timestamp": 1012011900,
      "time": "2023-03-29T07:52:47.923841Z"
    },
    "received_at": "2023-03-29T07:54:40.949193829Z",
    "consumed_airtime": "0.066816s",
    "version_ids": {
      "brand_id": "elsys",
      "model_id": "ers-eye",
      "hardware_version": "1.0",
      "firmware_version": "1.0",
      "band_id": "EU_863_870"
    },
    "network_ids": {
      "net_id": "000013",
      "tenant_id": "ttn",
      "cluster_id": "eu1",
      "cluster_address": "eu1.cloud.thethings.network"
    }
  }
}


temperature_sensor = Device(device_id='device:001',
                            entity_name='urn:ngsi-ld:Device:001',
                            entity_type='TemperatureSensor',
                            protocol='IoTA-JSON',
                            transport='MQTT',
                            attributes=[DeviceAttribute(name='temperature',
                                                        object_id='t',
                                                        type='Number')])

def initial_setup() -> IoTAClient | ContextBrokerClient:
    fiware_header = FiwareHeader(service=config['gateway_setup']['fiware_service'],
                                 service_path=config['gateway_setup']['fiware_servicepath'])
    clear_iot_agent(f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_port']}", fiware_header=fiware_header)
    clear_context_broker((f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['orion_port']}"), fiware_header=fiware_header)
    iotac = IoTAClient(f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_port']}", fiware_header=fiware_header)
    cbc = ContextBrokerClient(f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['orion_port']}", fiware_header=fiware_header)
    return iotac, cbc


def main():
    iotac, cbc = initial_setup()
    iotac.post_device(device=temperature_sensor, update=True)
    mqtt_gateway = Gateway()
    for i in range(3):
        time.sleep(1)
        print(f"Publishing {i}")
        mqtt_gateway.publish("/gateway", json.dumps({"device_id": temperature_sensor.device_id, "temperature": i, "timestamp": time.time()}))
        time.sleep(3)
    print(mqtt_gateway.device_topics)
    mqtt_gateway.remove_device_topic(temperature_sensor.device_id)
    print(mqtt_gateway.device_topics)

if __name__ == '__main__':
    config = json.load(open('config.json'))
    main()
