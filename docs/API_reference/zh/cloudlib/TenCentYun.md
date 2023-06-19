# TenCentYun- 腾讯云服务

该模块提供腾讯云物联网套件客户端功能,目前的产品节点类型仅支持“设备”，设备认证方式支持“一机一密”和“动态注册认证”。

>BC25PA系列不支持该功能。

## 初始化腾讯云

### `TXyun`

```python
TXyun(productID, devicename, devicePsk, ProductSecret)
```

配置腾讯云物联网套件的产品信息和设备信息。

**参数描述：**


* `productID` -  产品标识（唯一ID） ，字符串类型
* `devicename` -  设备名称 ，字符串类型
* `devicePsk` -  设备密钥（一型一密认证方案时此参数传入None），字符串类型，可选参数,默认为None
* `ProductSecret` -  产品密钥，字符串类型，一机一密认证方案时，此参数传入None<br/>一型一密认证方案时，此参数传入真实的产品密钥



**返回值描述：**

返回TXyun连接对象。

## 设置相关功能和回调

### `TXyun.setMqtt`

```python
TXyun.setMqtt(clean_session, keepAlive=300,reconn=True)
```

设置MQTT数据通道的参数

**参数描述：**

* `clean_session` -  产品标识（唯一ID），布尔值类型，如果为True，<br />那么代理将在其断开连接时删除有关此客户端的所有信息。 如果为False，则客户端是持久客户端，当客户端断开连接时，订阅信息和排队消息将被保留。默认为False
* `keepAlive` -  通信之间允许的最长时间段（以秒为单位），整型类型，默认为300，范围（60-1000），建议300以上 
* `reconn` -  （可选）控制是否使用内部重连的标志，布尔值类型，默认开启为True 

**返回值描述：**

成功返回整型值0，失败返回整型值-1。

### `TXyun.setCallback`

```python
TXyun.setCallback(callback)
```

注册回调函数。

**参数描述：**

* `callback` -  设置消息回调函数，function类型，当服务端响应时触发该方法

**回调函数参数**

* `topic` -  mqtt topic主题，字符串类型
* `msg` -  需要发送的数据，字符串类型

**返回值描述：**

无

### `TXyun.error_register_cb`

```python
TXyun.error_register_cb(callback)
```

设置异常回调函数，腾讯云以及umqtt内部线程异常时通过回调返回error信息，该方法在设置不使用内部重连的情况下才可触发回调

**参数描述：**

* `callback` -  设置异常回调函数，function类型

**回调函数参数**

* `msg` -  异常信息，字符串类型

**返回值描述：**

无

**示例：**


```python
from TenCentYun import TXyun

def err_cb(err):
    print("thread err:")
    print(err)

tenxun = TXyun(productID, devicename, devicePsk, ProductSecret)
tenxun.error_register_cb(err_cb)
```

## 订阅发布功能

### `TXyun.subscribe`

```python
TXyun.subscribe(topic,qos)
```

订阅mqtt主题。

**参数描述：**

* `topic` -  mqtt topic主题，字符串类型
* `qos` -  MQTT消息服务质量（默认0，可选择0或1），整型类型 <br />0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker

**返回值描述：**

成功返回整型值0，失败返回整型值-1。


### `TXyun.publish`

```python
TXyun.publish(topic,msg, qos=0)
```

发布消息。

**参数描述：**

* `topic` -  mqtt topic主题，字符串类型
* `msg` -  需要发送的数据，字符串类型
* `qos` -  MQTT消息服务质量（默认0，可选择0或1），整型类型 <br />0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker

**返回值描述：**

成功返回整型值0，失败返回整型值-1。


## 启停服务相关功能

### `TXyun.start`

```python
TXyun.start()
```

运行连接。

**参数描述：**

无

**返回值描述：**

无

### `TXyun.disconnect`

```python
TXyun.disconnect()
```

关闭连接。

**参数描述：**

无

**返回值描述：**

无

### `TXyun.ping`

```python
TXyun.ping()
```

发送心跳包

**参数描述：**

无

**返回值描述：**

无

### `TXyun.getTXyunsta`

```python
TXyun.getTXyunsta()
```

获取腾讯云连接状态

注意：BG95平台不支持该功能。

**参数描述：**

无

**返回值描述：**

* 0 ：连接成功

* 1：连接中

* 2：服务端连接关闭

* -1：连接异常



**示例：**


```python
from TenCentYun import TXyun
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_TencentYun_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
txyun_log = log.getLogger("TenCentYun")

'''
腾讯云物联网套件客户端功能
'''
productID = ""  # 产品标识（参照接入腾讯云应用开发指导）
devicename = ""   # 设备名称（参照接入腾讯云应用开发指导）
devicePsk = ""   # 设备密钥（一型一密认证此参数传入None， 参照接入腾讯云应用开发指导）
ProductSecret = None   # 产品密钥（一机一密认证此参数传入None，参照接入腾讯云应用开发指导）

tenxun = TXyun(productID, devicename, devicePsk, ProductSecret)  # 创建连接对象
state = 5

def sub_cb(topic, msg):   # 云端消息响应回调函数
    global state
    txyun_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    state -= 1


if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        txyun_log.info('Network connection successful!')

        tenxun.setMqtt()  # 设置mqtt
        tenxun.setCallback(sub_cb)   # 设置消息回调函数
        topic = ""  # 输入自定义的Topic
        tenxun.subscribe(topic)   # 订阅Topic
        tenxun.start()
        tenxun.publish(topic, "hello world")   # 发布消息

        while 1:
            if state:
                pass
            else:
                tenxun.disconnect()
                break
    else:
        txyun_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))

```
