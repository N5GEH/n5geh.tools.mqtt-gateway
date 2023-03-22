import requests
import json

def main():
    config = json.load(open('config.json'))
    s = requests.Session()
    orion = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['orion_port']}"
    iota_7896 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_http_port']}"
    iota_4041 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_port']}"
    # Get list of services
    r = s.get(iota_4041 + '/iot/services', headers={'fiware-service': 'openiot',
                                                   'fiware-servicepath': '/'})
    print(r.text + '\n------------------')
        
    # Create a service group
    r = s.post(iota_4041 + '/iot/services', headers={'Content-Type': 'application/json',
                                                     'fiware-service': 'openiot',
                                                     'fiware-servicepath': '/'},
                data=json.dumps({'services': [{'apikey': '4jggokgpepnvsb2uv4s40d59ov',
                                            "cbroker": orion,
                                            "entity_type": "thing",
                                            "resource": "/iot/json"}]}))
    print(str(r.status_code) + '\n------------------')
    
    # Provision a sensor
    r = s.post(iota_4041 + '/iot/devices', headers={'Content-Type': 'application/json',
                                                    'fiware-service': 'openiot',
                                                    'fiware-servicepath': '/'},
               data=json.dumps({'devices': [{'device_id': 'device010',
                                             'entity_name': 'urn:ngsi-ld:Device:010',
                                             'entity_type': 'Device',
                                             'timezone': 'Europe/Berlin',
                                             'attributes': [{'object_id': 't',
                                                             'name': 'temperature',
                                                             'type': 'Float'}]}]}))
    print(r.text + ' ' + str(r.status_code) + '\n------------------')
    
    # Try to send a measurement using the 7896 port
    r = s.post(iota_7896 + '/iot/json?&k=4jggokgpepnvsb2uv4s40d59ov&i=device010',
               headers={'Content-Type': 'application/json'},
               data=json.dumps({'t': 20.401}))
    print(r.text + ' ' + str(r.status_code) + '\n------------------')
    
    # check Orion for the entity
    r = s.get(orion + '/v2/entities/urn:ngsi-ld:Device:010', headers={'fiware-service': 'openiot',
                                                                      'fiware-servicepath': '/'})
    print(r.text)
    
    
    
if __name__ == '__main__':
    main()