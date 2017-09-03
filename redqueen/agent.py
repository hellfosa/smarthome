import paho.mqtt.client as mqtt
import requests
import yaml
import argparse
import re

######## global variables block ########
device_online = []

######## parsing arguments ########
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mqtt_server', help='address of mqtt server, without port, default 1883, example => 127.0.0.1', nargs='?')
    parser.add_argument('-s', '--smarthome_server', help='adress of smarthome server, example => sm.localdomain', nargs='?')
    parser.add_argument('-u', '--username', help='username of smarthome server ', nargs='?')
    parser.add_argument('-p', '--apikey', help='apikey of username to access to smarthome server', nargs='?')
    return parser

######## main program body ########
def get_channels():
    headers = {'Content-Type': 'application/json'}
    url = 'http://{0}/api/v1/device/?format=json&username={1}&api_key={2}'.format(args.smarthome_server, args.username, args.apikey)
    try:
        r = requests.get(url, headers=headers).json()
    except:
        print('Sorry, I can\'t connect to smarthome server. May be you lost your username or apikey?')
    else:
        for device in r['objects']:
            dev = {}
            dev['channel'] = device['channel']
            dev['action'] = device['action']
            device_online.append(dev)
        return r

def push_message(channel, signal):
    headers = {'Content-Type': 'application/json'}
    data = {'channel': channel, 'signal': signal}
    url = 'http://{0}/api/v1/message/?format=json&username={1}&api_key={2}'.format(args.smarthome_server, args.username, args.apikey)
    try:
        r = requests.post(url, headers=headers, json=data)
    except(ConnectionError):
        print('Sorry, I can\'t connect to smarthome server. May be you lost your username or apikey?')
    else:
        return r

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for device in device_online:
        client.subscribe(device['channel'], qos=0)

def on_message(client, userdata, msg):
    message = yaml.load(msg.payload.decode())
    try:
        if message[0].get('action') == 'GET':
            check_message(msg.topic, message[0].get('value'))
        else:
            print('sorry, no data for you')
    except(AttributeError):
            print('Blank request?')
    except:
            print('Bad request - {0}'.format(message[0].get('value')))

def check_message(topic, message):
    if re.search('humidity|temperature', topic) is not None:
        if message >= 0 and message <= 100:
            push_message(topic, message)
        else:
            print('Your data has a mistake - {0}, do nothing'.format(message))
    elif re.search('co2|CO2', topic) is not None:
        if message >=425 and message <= 3000:
            push_message(topic, message)
        else:
            print('Your data has a mistake - {0}, do nothing'.format(message))
    elif re.search('pressure', topic) is not None:
        if message >=700 and message <= 800:
            push_message(topic, message)
        else:
            print('Your data has a mistake - {0}, do nothing'.format(message))
    else:
        print("It is bullshit channel! - {0}".format(topic))

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    get_channels()

    try:
        client = mqtt.Client()
        client.connect(args.mqtt_server, 1883, 60)
    except:
        print("Sorry, I can\'t connect to mqtt server. Check this shit.")
        print('Try run with "-h"')
    else:
        client.on_connect = on_connect
        client.on_message = on_message
        client.loop_forever()
