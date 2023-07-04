from umqtt import MQTTClient
import modem
import checkNet
import utime
from misc import Power

# AccessKey ID : LTAI5tRFwDhmXcmUFH8qoCVR
# AccessKey Secret : ocGC9I5YRf0EoZXJj75b2U42LNkvPj

CLIENT_ID = b'GID_ZHIQIANG@@@001'
SERVER = b'post-cn-zvp262hla07.mqtt.aliyuncs.com'
PORT = 1883
USER = b'Signature|LTAI5tRFwDhmXcmUFH8qoCVR|post-cn-zvp262hla07'
PASSWORD = b'z7VkmcsG9d5hOnMB/N5ITZ5WGeI='

IMEI = 'Chic_YE'  # modem.getDevImei()
SUB_TOPIC = '{}'
PUB_TOPIC = SUB_TOPIC


# def GetDevImei():
#     global IMEI
#     IMEI = modem.getDevImei()
#     print('IMEI:{}'.format(IMEI))


state = 0


def sub_cb(topic, msg):
    global state
    print(
        "Subscribe Recv: Topic={},Msg={}".format(
            topic.decode(),
            msg.decode()))
    state = 1


def MQTT_Init():
    # 创建一个mqtt实例
    c = MQTTClient(
        client_id=CLIENT_ID,
        server=SERVER,
        port=PORT,
        user=USER,
        password=PASSWORD,
        keepalive=30)  # 必须要 keepalive=30 ,否则连接不上
    # 设置消息回调
    c.set_callback(sub_cb)
    # 建立连接
    try:
        c.connect()
    except Exception as e:
        print('!!!,e=%s' % e)
        return
    # c.connect()
    # 订阅主题
    c.subscribe(SUB_TOPIC.format(IMEI))
    # 发布消息
    c.publish(PUB_TOPIC.format(IMEI), b"test publish")

    while True:
        c.wait_msg()
        if state == 1:
            break

    # 关闭连接
    c.disconnect()


def main():
    # GetDevImei()
    MQTT_Init()


if __name__ == '__main__':
    PROJECT_NAME = "QuecPython"
    PROJECT_VERSION = "1.0.0"
    checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)
    checknet.poweron_print_once()
    try:
        checknet.wait_network_connected()
    except BaseException:
        print('Not Net, Resatrting...')
        utime.sleep_ms(200)
        Power.powerRestart()
    main()
