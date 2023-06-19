
import utime
import checkNet
from TenCentYun import TXyun
import _thread
import sys_bus

class SYSTOPIC_Class(object):
    RRPC = "rrpc"
    OTA = "ota"
    PUB = "pub"
    SUB = "sub"

class TXyun_Class(object):
    def __init__(self):
        self.productID = "X3Z30XABBU"  # 产品标识
        self.devicename = "001"   # 设备名称
        self.devicePsk = None   # 设备密钥（一型一密认证此参数传入None）
        self.ProductSecret = 'TeXbX8bZ40vutWHGxfUGJEZS'   # 产品密钥（一机一密认证此参数传入None）

        # 输入自定义的Topic
        self.subscribe_topic1 = 'X3Z30XABBU/{}/data'.format(self.devicename)
        self.publish_topic1 = 'X3Z30XABBU/{}/data'.format(self.devicename)

        self.tenxun = TXyun(
            self.productID,
            self.devicename,
            self.devicePsk,
            self.ProductSecret)  # 创建连接对象
        self.tenxun.setMqtt()  # 设置mqtt
        self.tenxun.setCallback(self.sub_cb)  # 设置消息回调函数

    def sub_cb(self, topic, msg):   # 云端消息响应回调函数
        if topic.decode().find(SYSTOPIC.RRPC) != -1:
            sys_bus.publish(SYSTOPIC.RRPC, {"topic": topic, "msg": msg})
        elif topic.decode().find(SYSTOPIC.OTA) != -1:
            sys_bus.publish(SYSTOPIC.OTA, {"topic": topic, "msg": msg})
        else:
            sys_bus.publish(SYSTOPIC.SUB, {"topic": topic, "msg": msg})

    def TXyun_start(self):
        # 运行
        self.tenxun.start()
        print('start')

    def TXyun_subscribe_topic(self):
        # 订阅主题
        self.tenxun.subscribe(self.subscribe_topic1, qos=0)
        # self.tenxun.subscribe(self.subscribe_topic2, qos=0)

    def TXyun_publish(self, topic, msg):
        try:
            self.tenxun.publish(msg.get('topic'), msg.get("msg"), qos=0)
        except BaseException:
            print('！！！！！！！！！！发送失败')

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
        """处理完ota的信息后，同步发送"""
        msg = {"topic": "xxx", "msg": "xxx"}
        """同步publish，同步情况下会等待所有topic对应的处理函数处理完才会退出"""
        sys_bus.publish_sync(SYSTOPIC.PUB, msg)

    @classmethod
    def rrpc(cls, topic, msg):
        """发布rrpc执行下列操作"""
        msg = {"topic": "xxx", "msg": "xxx"}
        """异步publish， """
        sys_bus.publish(SYSTOPIC.PUB, msg)

if __name__ == '__main__':
    PROJECT_NAME = "QuecPython"
    PROJECT_VERSION = "1.0.0"
    checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)
    checknet.poweron_print_once()
    checknet.wait_network_connected()

    TXyunClass = TXyun_Class()
    TXyunClass.TXyun_subscribe_topic()

    SYSTOPIC = SYSTOPIC_Class()
    sys_bus.subscribe(SYSTOPIC.RRPC, Handler.rrpc)
    sys_bus.subscribe(SYSTOPIC.OTA, Handler.ota)
    sys_bus.subscribe(SYSTOPIC.SUB, Handler.sub)
    sys_bus.subscribe(SYSTOPIC.PUB, TXyunClass.TXyun_publish)

    msg = '{{"DeviceName":"{}","msg":"test publish"}}'.format(TXyunClass.devicename)
    tuple = ({"topic": TXyunClass.publish_topic1, "msg": msg},)
    _thread.start_new_thread(Handler.pub, tuple)

    TXyunClass.TXyun_start()
