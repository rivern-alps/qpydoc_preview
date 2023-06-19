
# class ESP8266 - ESP8266无线网络控制

该类用于控制`ESP8266`型号无线网卡设备。

## 构造函数

### `ESP8266`

```python
class ESP8266(uart=UART.UART1, mod=ESP8266.STA， callback=None)
```

加载ESP8266驱动，初始化虚拟网卡，并返回ESP8266对象。

**参数描述：**
- `uart` - 整型值，模组UART口选择，表示模组与ESP8266所连接的`串口号`，默认使用`UART1`。
- `mode` - 整型值，无线网卡工作模式配置，用来指定ESP8266的`工作模式`，STA客户端模式为ESP8266.STA，AP接入点模式为ESP8266.AP，默认使用`STA客户端`模式。
- `callback` - 回调函数名。设置回调函数，用于`网络变化`以及`ota升级`通知，默认为未开启。

**callback参数描述：**
- `content` - 字符串类型，用户回调，表示上报消息内容

**上报消息内容描述：**

开启用户回调后，模组会在ota升级和sta模式连接变化时进行消息上报，以下是上报信息描述。

`ota`信息上报：
- `ota,begin` - ota升级开始
- `ota,downloading,xx` - ota升级下载百分比
- `ota,restart` - ota升级下载完成进行重启
- `ota,err_code,x` - ota升级错误码，以下是对错误码(x)的描述：
    - `1` - url解析失败
    - `2` - 连接http服务器失败
    - `3` - 为GET请求分配内存失败
    - `4` - 发送GET请求到服务器失败
    - `5` - 升级开始时错误
    - `6` - 接收数据失败
    - `7` - ota文件写入失败
    - `8` - 升级结束时错误
    - `9` - 设置boot分区失败

`station`模式网络连接变化上报：
- `station, connected` - wifi已连接
- `station, disconnected` - wifi断开连接

**示例：**

```python
# callback使用示例
from usr.WLAN import ESP8266
from machine import UART

def cb(args):
    content = args
    print('wifi content:{}'.format(content))

ESP8266 = ESP8266(UART.UART2, ESP8266.STA, cb)

```


## 方法

### `ESP8266.status`

```python
ESP8266.status()
```

获取无线网卡状态信息，用以判断无线网卡当前工作模式。

**返回值描述：**

返回整型值，具体说明如下：
- `0` - esp8266 设备不存在
- `1` - esp8266 station模式已连接
- `2` - esp8266 station模式未连接
- `3` - esp8266 web配网模式
- `4` - esp8266 ap模式
- `5` - esp8266 ota升级中




### `ESP8266.version`

```python
ESP8266.version()
```

获取无线网卡当前固件版本信息

**返回值描述：**

返回字符串类型，格式为(sdk, model, version, time),具体说明如下：
- `sdk` - sdk信息
- `model` - 无线网卡型号
- `version` - 版本号
- `time` - 版本时间



### `ESP8266.ipconfig`

```python
ESP8266.ipconfig()
```

获取网卡当前网络配置信息(IP地址、DNS服务器等信息)

**返回值描述：**

 返回元组类型，格式为 (ip, subnet, gateway, mtu, primary_dns, secondary_dns)，具体说明如下：

- `ip` - 字符串类型，ip地址
- `subnet` - 字符串类型，子网掩码
- `gateway` - 字符串类型，网关
- `mtu` - 整型值，最大传输单元
- `primary_dns` - 字符串类型，DNS服务器主地址
- `secondary_dns` - 字符串类型，DNS服务器辅地址



### `ESP8266.station`

```python
ESP8266.station(username，password)
```

使无线网卡以`station`工作模式启动，连接指定wifi。

**参数描述：**

- `username` - 字符串类型，填写所要连接的 `WiFi` 的名称（1~32 个字符）
- `password` - 字符串类型，填写所要连接的 `WiFi` 的密码（8~64 个字符）

**返回值描述：**

- 配置成功返回`0`，配置失败返回其他值。



### `ESP8266.ap`

```python
ESP8266.ap(username，password)
```

使无线网卡以`ap`工作模式启动，作为无线热点。

> ap模式理论最多支持`10`个终端设备接入。

**参数描述：**

- `username` - 字符串类型，配置 `WiFi热点` 的名称（1~32 个字符）
- `password` - 字符串类型，配置 `WiFi热点` 的密码（8~64 个字符）

**返回值描述：**

- 配置成功返回`0`，配置失败返回其他值。



### `ESP8266.web_config`

```python
ESP8266.web_config(username，password)
```

使无线网卡以`web 配网`工作模式启动，用户可通过web页面进行网络配置。

> 启用配网功能后，需使用手机/电脑等终端设备通过无线网络连接至无线网卡(用户自定义名称和密码)，然后通过浏览器输入192.168.4.1进入配网页面。

**参数描述：**

- `username` - 字符串类型，配置 `配网热点` 的名称（1~32 个字符）
- `password` - 字符串类型，配置 `配网热点` 的密码（8~64 个字符）

**返回值描述：**

- 配置成功返回`0`，配置失败返回其他值。



### `ESP8266.ota`

```python
ESP8266.ota(url)
```

开启`ota`后，网卡将更新新版本固件

> 当前仅支持sta模式下进行ota升级；且升级过程中只可查询当前状态，不可进行其他操作。

**参数描述：**

- `url` - 字符串类型，填写网址地址，表示固件下载地址，当前仅支持 http 协议，最长 256 字节。

**返回值描述：**

- 执行成功返回`0`，执行失败返回其他值。


**示例：**

```python

url='http://www.example.com/fota.bin'

ESP8266.ota(url)

```



### `ESP8266.stop`

```python
ESP8266.stop()
```

释放掉为无线网卡所配置的虚拟网卡

**返回值描述：**

- 释放成功返回`0`，释放失败返回其他值。



### `ESP8266.set_default_NIC`

```python
ESP8266.set_default_NIC(ip_str)
```

指定网卡进行网络转发

**参数描述：**

- `ip_str` - 字符串类型，所要设置默认转发网卡的网卡 ip 地址，如：'192.168.1.100'

**返回值描述：**

- 配置成功返回`0`，配置失败返回其他值。



### `ESP8266.set_dns`

```python
ESP8266.set_dns(pri_dns, sec_dns)
```

指定无线网卡的`dns`服务器进行地址解析

**参数描述：**

- `pri_dns` - 字符串类型，设置无线网卡的`首选 dns` 服务器，默认为 `8.8.8.8`
- `sec_dns` - 字符串类型，设置无线网卡的`备选 dns` 服务器，默认为 `114.114.114.114`

**返回值描述：**

- 配置成功返回`0`，配置失败返回其他值。



### `ESP8266.router_add`

```python
ESP8266.router_add(ip, mask)
```

设置无线网卡路由转发规则

**参数描述：**

- `ip` - 字符串类型，设置 `ap` 模式的网段，默认为 192.168.4.1
- `mask` - 字符串类型，设置子网掩码，默认为 255.255.255.0

**返回值描述：**

- 配置成功返回`0`，配置失败返回其他值。
