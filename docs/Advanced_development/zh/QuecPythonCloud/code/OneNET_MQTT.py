from umqtt import MQTTClient

# 连接协议	证书	地址	端口	说明
# MQTT	证书下载	mqttstls.heclouds.com	8883	加密接口
# MQTT	  -	        mqtts.heclouds.com	    1883	非加密接口

# 参数	是否必须	参数说明
# clientId	是	设备名称
# username	是	平台分配的产品ID
# password	是	填写经过 key 计算的 token

SERVER = b'mqtts.heclouds.com'
PORT = 1883
CLIENT_ID = b'Chic_D'
USER = b'469948'
PASSWORD = b'version=2018-10-31&res=products%2F469948%2Fdevices%2FChic_D&et=1673053248&method=sha1&sign=prIMDQ23WFI6PMj2IWpaRJJL4eE%3D'

IMEI = None  # modem.getDevImei()
SUB_TOPIC = '$sys/469948/Chic_D/dp/post/json/+'
PUB_TOPIC = '$sys/469948/Chic_D/dp/post/json'

def GetDevImei():
    global IMEI
    # IMEI = modem.getDevImei()
    IMEI = '001'
    print(IMEI)

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
        c.connect()  # c.connect(clean_session=True)
    except Exception as e:
        print('!!!,e=%s' % e)
        return
    print('connected')

    # 订阅主题
    c.subscribe(SUB_TOPIC.format(IMEI))
    # 发布消息
    Payload = '''
    {
        "id": 123,
        "dp": {
            "temperatrue": [{
                "v": 30,
            }],
            "power": [{
                "v": 4.5,
            }]
        }
    }'''
    c.publish(PUB_TOPIC.format(IMEI), Payload)

    while True:
        c.wait_msg()
        if state == 1:
            break

    # 关闭连接
    c.disconnect()


def main():
    # GetDevImei()
    MQTT_Init()


if __name__ == "__main__":
    main()
