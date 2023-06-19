
import log
import utime
import checkNet
from aLiYun import aLiYun

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_AliYin_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)


# 设置日志输出级别
log.basicConfig(level=log.INFO)
aliYun_log = log.getLogger("ALiYun")

productKey = "a1llZotKkCm"  # 产品标识(参照阿里云应用开发指导)
productSecret = None  # 产品密钥（使用一机一密认证时此参数传入None，参照阿里云应用开发指导)
DeviceName = "11111"  # 设备名称(参照阿里云应用开发指导)
# 设备密钥（使用一型一密认证此参数传入None，免预注册暂不支持，需先在云端创建设备，参照阿里云应用开发指导)
DeviceSecret = "03c5e91aea167edead7d381d4b41ed71"

state = 1

# 回调函数


def sub_cb(topic, msg):
    global state
    aliYun_log.info(
        "Subscribe Recv: Topic={},Msg={}".format(
            topic.decode(), msg.decode()))
    state -= 1


if __name__ == '__main__':
    '''
    手动运行本例程时，可以去掉该延时，如果将例程文件名改为main.py，希望开机自动运行时，需要加上该延时,
    否则无法从CDC口看到下面的 poweron_print_once() 中打印的信息
    '''
    utime.sleep(5)
    checknet.poweron_print_once()
    '''
    如果用户程序包含网络相关代码，必须执行 wait_network_connected() 等待网络就绪（拨号成功）；
    如果是网络无关代码，可以屏蔽 wait_network_connected()
    【本例程必须保留下面这一行！】
    '''
    checknet.wait_network_connected()

    # 创建aliyun连接对象
    ali = aLiYun(productKey, productSecret, DeviceName, DeviceSecret)

    # 设置mqtt连接属性
    clientID = b'11111clientID'  # 自定义字符（不超过64）
    ali.setMqtt(clientID, clean_session=False, keepAlive=300)

    # 设置回调函数
    ali.setCallback(sub_cb)
    topic = '/broadcast/a1llZotKkCm/123'  # 云端自定义或自拥有的Topic
    # 订阅主题
    ali.subscribe(topic)
    # 发布消息
    ali.publish(topic, "hello world")
    # 运行
    ali.start()

    while True:
        if state:
            pass
        else:
            ali.disconnect()
            break
