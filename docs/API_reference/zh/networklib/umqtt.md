# umqtt - MQTT客户端

模块功能:提供创建MQTT客户端发布订阅功能。

```
QoS级别说明
在MQTT协议中，定义了三个级别的QoS，分别是：
QoS0 – 最多一次，是最低级别；发送者发送完消息之后，并不关心消息是否已经到达接收方；
QoS1 – 至少一次，是中间级别；发送者保证消息至少送达到接收方一次；
QoS2 – 有且仅有一次，是最高级别；保证消息送达且仅送达一次。
```

## 构造函数

### `umqtt.MQTTClient`

```python
class umqtt.MQTTClient(client_id, server, port=0, user=None, password=None, keepalive=0, ssl=False, ssl_params={},reconn=True,version=4)
```

构建mqtt连接对象。

**参数描述：**

* `client_id` - 客户端 ID，字符串类型，具有唯一性。

* `server` - 服务端地址，字符串类型，可以是 IP 或者域名。

* `port` - 服务器端口（可选），整数类型，默认为1883，请注意，MQTT over SSL/TLS的默认端口是8883。

* `user` - （可选) 在服务器上注册的用户名，字符串类型。

* `password` - （可选) 在服务器上注册的密码，字符串类型。

* `keepalive` - （可选）客户端的keepalive超时值，整数类型，默认为0。

* `ssl` - （可选）是否使能 SSL/TLS 支持，布尔值类型。

* `ssl_params` - （可选）SSL/TLS 参数，字符串类型。

* `reconn` - （可选）控制是否使用内部重连的标志，布尔值类型，默认开启为True。

* `version` - （可选）选择使用mqtt版本，整数类型，version=3开启MQTTv3.1，默认version=4开启MQTTv3.1.1。



## 设置相关功能和回调

### `MQTTClient.set_callback`

```python
MQTTClient.set_callback(callback)
```

设置回调函数，收到消息时会被调用。

>回调函数不建议处理阻塞API，会影响mqtt消息接收。


**参数描述：**

* `callback` -  设置异常回调函数，function(topic, data)类型

**示例：**

```python
from umqtt import MQTTClient

def data_cb(topic, data):
    try:
        print("umqtt recv topic[%s] data:%s:"%(topic, data))
    except Exception as e:
        print("Handle error:%s"%str(e))

c = MQTTClient("umqtt_client", "mq.tongxinmao.com", 18830)
c.set_callback(data_cb)
```

### `MQTTClient.error_register_cb`

```python
MQTTClient.error_register_cb(callback)
```

设置异常回调函数，使用内部重连的情况下umqtt内部线程异常时通过回调返回error信息。

**参数描述：**

* `callback` - 设置异常回调函数，function(error)类型

**示例：**
```python
from umqtt import MQTTClient

def err_cb(err):
    print("thread err:%s"%err)
    if err == "reconnect_start":
        print("start reconnect")
    elif err == "reconnect_success":
        print("success reconnect")
    else:
        print("reconnect FAIL")

c = MQTTClient("umqtt_client", "mq.tongxinmao.com", 18830)
c.error_register_cb(err_cb)
```

### `MQTTClient.set_last_will`

```python
MQTTClient.set_last_will(topic,msg,retain=False,qos=0)
```

设置要发送给服务器的遗嘱，客户端没有调用disconnect()异常断开，则发送通知到其他客户端。

**参数描述：**

* `topic` -  mqtt遗嘱主题，字符串类型。

* `msg` -  遗嘱的内容，字符串类型。

* `retain` -  retain = True boker会一直保留消息，默认False，布尔值类型。

* `qos` -  整数类型，消息服务质量(0~1)。


## MQTT连接相关功能

### `MQTTClient.connect`

```python
MQTTClient.connect(clean_session=True)
```

与服务器建立连接，连接失败会导致MQTTException异常。

>mqtt相关操作要在确认connect成功后执行。

**参数描述：**

* `clean_session` -  布尔值类型，可选参数，一个决定客户端类型的布尔值。 如果为True，那么代理将在其断开连接时删除有关此客户端的所有信息。 如果为False，则客户端是持久客户端，当客户端断开连接时，订阅信息和排队消息将被保留。默认为True。

**返回值描述：**

成功返回0，失败则抛出异常。


### `MQTTClient.disconnect`

```python
MQTTClient.disconnect()
```

与服务器断开连接，释放相关资源。


### `MQTTClient.close`

```python
MQTTClient.close()
```

释放socket资源,(注意区别disconnect方法，close只释放socket资源，disconnect包含线程等资源)。

>该方法仅用于在自己实现重连时使用，具体请参照mqtt重连示例代码，正常关闭mqtt连接请使用disconnect。


### `MQTTClient.ping`

```python
MQTTClient.ping()
```

当keepalive不为0且在时限内没有通讯活动，会主动向服务器发送ping包, 检测保持连通性，keepalive为0则不开启。


## 发布订阅相关功能

### `MQTTClient.publish`

```python
MQTTClient.publish(topic, msg, retain=False, qos=0)
```

发布消息到对应topic。

**参数描述：**

* `topic` -  mqtt 消息主题，字符串类型

* `msg` -  需要发送的数据，字符串类型

* `retain` -  布尔值类型，默认为False, 发布消息时把retain设置为true，即为保留信息。<br />MQTT服务器会将最近收到的一条RETAIN标志位为True的消息保存在服务器端, 每当MQTT客户端连接到MQTT服务器并订阅了某个topic，如果该topic下有Retained消息，那么MQTT服务器会立即向客户端推送该条Retained消息 <br />特别注意：MQTT服务器只会为每一个Topic保存最近收到的一条RETAIN标志位为True的消息！也就是说，如果MQTT服务器上已经为某个Topic保存了一条Retained消息，当客户端再次发布一条新的Retained消息，那么服务器上原来的那条消息会被覆盖！ |

* `qos` -  整数类型， MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker

**返回值描述：**

成功返回布尔型True，失败返回布尔型False。


### `MQTTClient.subscribe`

```python
MQTTClient.subscribe(topic,qos)
```

订阅mqtt主题。

**参数描述：**

* `topic` -  mqtt topic主题，字符串类型。

* `qos` -  MQTT消息服务质量（默认0，可选择0或1），整数类型 <br />0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker。


### `MQTTClient.wait_msg`

```python
MQTTClient.wait_msg()
```

阻塞等待服务器消息响应。


### `MQTTClient.get_mqttsta`

```python
MQTTClient.get_mqttsta()
```

获取mqtt连接状态。

注意：BG95平台不支持该API。

>如果用户调用了 disconnect() 方法之后，再调用 MQTTClient.get_mqttsta() 会返回-1，因为此时创建的对象资源等都已经被释放。


**返回值描述：**

0：连接成功。

1：连接中。

2：服务端连接关闭。

-1：连接异常。


**示例：**

```python
'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2020-04-24 17:06:08
@Description: example for module umqtt
@FilePath: example_mqtt_file.py
'''
from umqtt import MQTTClient
import utime
import log
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_MQTT_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
mqtt_log = log.getLogger("MQTT")


state = 0

def sub_cb(topic, msg):
    global state
    mqtt_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    state = 1


if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        mqtt_log.info('Network connection successful!')

        # 创建一个mqtt实例
        c = MQTTClient("umqtt_client", "mq.tongxinmao.com", 18830)
        # 设置消息回调
        c.set_callback(sub_cb)
        #建立连接
        c.connect()
        # 订阅主题
        c.subscribe(b"/public/TEST/quecpython")
        mqtt_log.info("Connected to mq.tongxinmao.com, subscribed to /public/TEST/quecpython topic" )
        # 发布消息
        c.publish(b"/public/TEST/quecpython", b"my name is Quecpython!")
        mqtt_log.info("Publish topic: /public/TEST/quecpython, msg: my name is Quecpython")

        while True:
            c.wait_msg()  # 阻塞函数，监听消息
            if state == 1:
                break
        # 关闭连接
        c.disconnect()
    else:
        mqtt_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))

```

**MQTT断网异常重连示例**

特别说明：

1.下面示例代码中mqtt的reconn参数用于控制使用或关闭umqtt内部的重连机制，默认为True，使用内部重连机制。

2.如需测试或使用外部重连机制可参考此示例代码，测试前需将reconn=False,否则默认会使用内部重连机制！

```python
'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2021-05-25 17:06:08
@Description: example for module umqtt
@FilePath: example_mqtt_file.py
'''
'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
import utime
import log
import net
import _thread
import checkNet
import dataCall
from umqtt import MQTTClient

PROJECT_NAME = "QuecPython_MQTT_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 调用disconnect后会通过该状态回收线程资源
TaskEnable = True
# 设置日志输出级别
log.basicConfig(level=log.INFO)
mqtt_log = log.getLogger("MQTT")


# 封装mqtt，使其可以支持更多自定义逻辑
class MqttClient():
    '''
    mqtt init
    '''

    # 说明：reconn该参数用于控制使用或关闭umqtt内部的重连机制，默认为True，使用内部重连机制。
    # 如需测试或使用外部重连机制可参考此示例代码，测试前需将reconn=False,否则默认会使用内部重连机制！
    def __init__(self, clientid, server, port, user=None, password=None, keepalive=0, ssl=False, ssl_params={},
                 reconn=True):
        self.__clientid = clientid
        self.__pw = password
        self.__server = server
        self.__port = port
        self.__uasename = user
        self.__keepalive = keepalive
        self.__ssl = ssl
        self.__ssl_params = ssl_params
        self.topic = None
        self.qos = None
        # 网络状态标志
        self.__nw_flag = True
        # 创建互斥锁
        self.mp_lock = _thread.allocate_lock()
        # 创建类的时候初始化出mqtt对象
        self.client = MQTTClient(self.__clientid, self.__server, self.__port, self.__uasename, self.__pw,
                                 keepalive=self.__keepalive, ssl=self.__ssl, ssl_params=self.__ssl_params,
                                 reconn=reconn)

    def connect(self):
        '''
        连接mqtt Server
        '''
        self.client.connect()
        # 注册网络回调函数，网络状态发生变化时触发
        flag = dataCall.setCallback(self.nw_cb)
        if flag != 0:
            # 回调注册失败
            raise Exception("Network callback registration failed")

    def set_callback(self, sub_cb):
        '''
        设置mqtt回调消息函数
        '''
        self.client.set_callback(sub_cb)

    def error_register_cb(self, func):
        '''
        注册一个接收umqtt内线程异常的回调函数
        '''
        self.client.error_register_cb(func)

    def subscribe(self, topic, qos=0):
        '''
        订阅Topic
        '''
        self.topic = topic  # 保存topic ，多个topic可使用list保存
        self.qos = qos  # 保存qos
        self.client.subscribe(topic, qos)

    def publish(self, topic, msg, qos=0):
        '''
        发布消息
        '''
        self.client.publish(topic, msg, qos)

    def disconnect(self):
        '''
        关闭连接
        '''
        global TaskEnable
        # 关闭wait_msg的监听线程
        TaskEnable = False
        # 关闭之前的连接，释放资源
        self.client.disconnect()

    def reconnect(self):
        '''
        mqtt 重连机制(该示例仅提供mqtt重连参考，根据实际情况调整)
        PS：1.如有其他业务需要在mqtt重连后重新开启，请先考虑是否需要释放之前业务上的资源再进行业务重启
            2.该部分需要自己根据实际业务逻辑添加，此示例只包含mqtt重连后重新订阅Topic
        '''
        # 判断锁是否已经被获取
        if self.mp_lock.locked():
            return
        self.mp_lock.acquire()
        # 重新连接前关闭之前的连接，释放资源(注意区别disconnect方法，close只释放socket资源，disconnect包含mqtt线程等资源)
        self.client.close()
        # 重新建立mqtt连接
        while True:
            net_sta = net.getState()  # 获取网络注册信息
            if net_sta != -1 and net_sta[1][0] == 1:
                call_state = dataCall.getInfo(1, 0)  # 获取拨号信息
                if (call_state != -1) and (call_state[2][0] == 1):
                    try:
                        # 网络正常，重新连接mqtt
                        self.connect()
                    except Exception as e:
                        # 重连mqtt失败, 5s继续尝试下一次
                        self.client.close()
                        utime.sleep(5)
                        continue
                else:
                    # 网络未恢复，等待恢复
                    utime.sleep(10)
                    continue
                # 重新连接mqtt成功，订阅Topic
                try:
                    # 多个topic采用list保存，遍历list重新订阅
                    if self.topic is not None:
                        self.client.subscribe(self.topic, self.qos)
                    self.mp_lock.release()
                except:
                    # 订阅失败，重新执行重连逻辑
                    self.client.close()
                    utime.sleep(5)
                    continue
            else:
                utime.sleep(5)
                continue
            break  # 结束循环
        # 退出重连
        return True

    def nw_cb(self, args):
        '''
        dataCall 网络回调
        '''
        nw_sta = args[1]
        if nw_sta == 1:
            # 网络连接
            mqtt_log.info("*** network connected! ***")
            self.__nw_flag = True
        else:
            # 网络断线
            mqtt_log.info("*** network not connected! ***")
            self.__nw_flag = False

    def __listen(self):
        while True:
            try:
                if not TaskEnable:
                    break
                self.client.wait_msg()
            except OSError as e:
                # 判断网络是否断线
                if not self.__nw_flag:
                    # 网络断线等待恢复进行重连
                    self.reconnect()
                # 在socket状态异常情况下进行重连
                elif self.client.get_mqttsta() != 0 and TaskEnable:
                    self.reconnect()
                else:
                    # 这里可选择使用raise主动抛出异常或者返回-1
                    return -1

    def loop_forever(self):
        _thread.start_new_thread(self.__listen, ())

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

    def sub_cb(topic, msg):
        # global state
        mqtt_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    
    c = MqttClient("umqtt_client_753", "mq.tongxinmao.com", 18830, reconn=False)
    
    def err_cb(error):
        '''
        接收umqtt线程内异常的回调函数
        '''
    	mqtt_log.info(error)
    	c.reconnect() # 可根据异常进行重连
        
    # c = MqttClient("umqtt_client_753", "mq.tongxinmao.com", 18830, reconn=False)
    # 设置消息回调
    c.set_callback(sub_cb)
    # 设置异常回调
    c.error_register_cb(err_cb)
    # 建立连接
    c.connect()
    # 订阅主题
    c.subscribe(b"/public/TEST/quecpython758")
    mqtt_log.info("Connected to mq.tongxinmao.com, subscribed to /public/TEST/quecpython topic")
    # 发布消息
    c.publish(b"/public/TEST/quecpython758", b"my name is Quecpython!")
    mqtt_log.info("Publish topic: /public/TEST/quecpython758, msg: my name is Quecpython")
    # 监听mqtt消息
    c.loop_forever()
    # 等待5s接收消息
    # PS:如果需要测试重连，包括服务器断开连接等情况，请注释掉c.disconnect()和utime.sleep(5)
    # utime.sleep(5)
    # 关闭连接
    # c.disconnect()
```