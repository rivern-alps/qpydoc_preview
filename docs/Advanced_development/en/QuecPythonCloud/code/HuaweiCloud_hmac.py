import checkNet
from umqtt import MQTTClient
import modem
from machine import UART
import sim
import hmac
from hashlib import sha256


IMEI = modem.getDevImei()
E_SN = modem.getDevSN()
ESIM = sim.getImsi()

DeviceName = IMEI
DeviceSecret = 'ac4263b86eaf6442997a'
DeviceID = "5fbbb784b4ec2202e982e643"

CLIENT_ID = DeviceID + "_" + DeviceName + "_0_0_2022010507"
SERVER = "a15fbbd7ce.iot-mqtts.cn-north-4.myhuaweicloud.com"
PORT = 1883
USER = DeviceID + "_" + DeviceName
PASSWORD = hmac.new(
    "2022010507".encode('utf-8'),
    DeviceSecret.encode('utf-8'),
    digestmod=sha256).hexdigest()
DEVICE_ID = DeviceID + "_" + DeviceName

state = 0


def sub_cb(topic, msg):
    global state
    print(
        "Subscribe Recv: Topic={},Msg={}".format(
            topic.decode(),
            msg.decode()))
    state = 1


def MQTT_Init():

    c = MQTTClient(
        client_id=CLIENT_ID,
        server=SERVER,
        port=PORT,
        user=USER,
        password=PASSWORD,
        keepalive=30)

    c.set_callback(sub_cb)
    try:
        c.connect()
        c.subscribe('$oc/devices/{}/sys/commands/#'.format(DEVICE_ID))

        msg = b'''{
            "services": [{
                "service_id": "WaterMeterControl",
                "properties": {
                    "state": "T:15c,  H: 85% "
                }
            }
            ]
        }'''
        c.publish('$oc/devices/{}/sys/properties/report'.format(DEVICE_ID), msg)
    except BaseException:
        print('except')
    print('Waiting command')
    while True:
        c.wait_msg()
        if state == 1:
            break

    c.disconnect()


def main():
    MQTT_Init()


if __name__ == "__main__":
    main()
