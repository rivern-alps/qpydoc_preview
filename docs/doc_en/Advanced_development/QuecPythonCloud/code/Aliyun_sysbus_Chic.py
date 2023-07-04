
import utime
import checkNet
from aLiYun import aLiYun
import _thread
import sys_bus


class SYSTOPIC_Class(object):
    RRPC = "rrpc"
    OTA = "ota"
    PUB = "pub"
    SUB = "sub"


class aliyun_Class(object):
    def __init__(self):
        aliyun_Class.inst = self
        self.productKey = "a1llZotKkCm" 
        self.productSecret = 'mj7qKfEn73y07gyK'  
        self.DeviceSecret = None  
        self.DeviceName = "Chic_001"

        self.subscribe_topic1 = "/" + self.productKey + \
            "/" + self.DeviceName + "/user/123"
        self.subscribe_topic2 = "/" + self.productKey + "/" + self.DeviceName + "/user/qq"
        self.publish_topic1 = "/" + self.productKey + "/" + self.DeviceName + "/user/qq"

        self.ali = aLiYun(
            self.productKey,
            self.productSecret,
            self.DeviceName,
            self.DeviceSecret)
        
        clientID = b'clientID' 
        ret = self.ali.setMqtt(
            clientID,
            clean_session=False,
            keepAlive=60,
            reconn=True)  # False True

        self.ali.setCallback(self.ali_sub_cb)

    def ali_sub_cb(self, topic, msg): 
        if topic.decode().find(SYSTOPIC.RRPC) != -1:
            sys_bus.publish(SYSTOPIC.RRPC, {"topic": topic, "msg": msg})
        elif topic.decode().find(SYSTOPIC.OTA) != -1:
            sys_bus.publish(SYSTOPIC.OTA, {"topic": topic, "msg": msg})
        else:
            sys_bus.publish(SYSTOPIC.SUB, {"topic": topic, "msg": msg})

    def ali_start(self):
        self.ali.start()
        print('Runing')
        # aLiYun.disconnect()

    def ali_subscribe_topic(self):
        self.ali.subscribe(self.subscribe_topic1, qos=0)
        self.ali.subscribe(self.subscribe_topic2, qos=0)

    def ali_publish(self, topic, msg):
        ret = self.ali.getAliyunSta()
        # print(ret)
        if ret == 0:
            try:
                self.ali.publish(msg.get('topic'), msg.get("msg"), qos=0)
            except BaseException:
                print('!!!!!!')


class Handler(object):
    @classmethod
    def sub(cls, topic, msg):
        print(
            "Subscribe Recv: Topic={},Msg={}".format(
                msg.get('topic').decode(),
                msg.get("msg").decode()))

    @classmethod
    def pub(cls, msg):
        while True:
            sys_bus.publish(SYSTOPIC.PUB, msg)
            utime.sleep_ms(2000)

    @classmethod
    def ota(cls, topic, msg):
        msg = {"topic": "xxx", "msg": "xxx"}
        sys_bus.publish_sync(SYSTOPIC.PUB, msg)

    @classmethod
    def rrpc(cls, topic, msg):
        msg = {"topic": "xxx", "msg": "xxx"}
        sys_bus.publish(SYSTOPIC.PUB, msg)


if __name__ == '__main__':
    PROJECT_NAME = "QuecPython"
    PROJECT_VERSION = "1.0.0"
    checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)
    checknet.poweron_print_once()
    checknet.wait_network_connected()

    aliyunClass = aliyun_Class()
    aliyunClass.ali_subscribe_topic()

    SYSTOPIC = SYSTOPIC_Class()
    sys_bus.subscribe(SYSTOPIC.RRPC, Handler.rrpc)
    sys_bus.subscribe(SYSTOPIC.OTA, Handler.ota)
    sys_bus.subscribe(SYSTOPIC.SUB, Handler.sub)
    sys_bus.subscribe(SYSTOPIC.PUB, aliyunClass.ali_publish)

    tuple = ({"topic": aliyunClass.publish_topic1, "msg": "hello world"},)
    _thread.start_new_thread(Handler.pub, tuple)

    aliyunClass.ali_start()
