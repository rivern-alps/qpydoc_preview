
# WLAN - 无线局域网相关功能

`WLAN`模块包含无线局域网控制及网络配置功能。主要是针对不同类型无线网卡提供统一的管理方式。

> 当前支持此功能模组：EC600N系列<br>当前支持此功能网卡：ESP8266无线网卡 

**示例：**

以ESP8266为例，根据不同应用场景，分别展示以`station`模式、`ap`模式、`web配网`模式下无线网卡初始化使用过程。

**station客户端模式：**
```python
# 在station工作模式下，无线网卡连接路由器的WiFi，由路由器分配IP等信息，使模组通过无线网卡连接外部网络。
>>> from usr.WLAN import ESP8266
>>> from machine import UART


# 加载ESP8266网卡驱动，并初始化网卡相关配置
>>> ESP8266 = ESP8266(UART.UART2, ESP8266.STA)

# 配置无线网卡以station模式启动并连接WiFi热点
>>> ESP8266.station('wifiname','wifipassword')
0

# 查看无线网卡的IP信息
>>> ESP8266.ipconfig()
 ('172.16.1.2', '255.255.255.0', '172.16.1.1', 1500, '0.0.0.0',
'0.0.0.0')

# 配置DNS服务器
>>> ESP8266.set_dns('8.8.8.8','114.114.114.114')
0

# 查看无线网卡的IP信息，可以看到DNS已被配置成功
>>> ESP8266.ipconfig()
('172.16.1.2', '255.255.255.0', '172.16.1.1', 1500, '8.8.8.8',
'114.114.114.114')

# 设置无线网卡作为默认网卡，使用无线网卡进行网络通信
>>> ESP8266.set_default_NIC('172.16.1.2')
0

# 获取当前网卡状态 返回“1”说明无线网卡已连接WiFi，返回“2”说明未连接WiFi
>>> ESP8266.status()
1

# 此时可以启动其他网络服务，并通过无线网络进行网络访问
```



**AP接入点模式：**
```python
# 在ap工作模式下，无线网卡开启ap热点，使用模组的4G网络 连接外网，并为连接到热点的终端设备分配IP信息，其他终端设备即可连接外部网络。
>>> from usr.WLAN import ESP8266
>>> from machine import UART
>>> import dataCall


# 加载ESP8266网卡驱动，并初始化网卡相关配置
>>> ESP8266 = ESP8266(UART.UART2, ESP8266.AP)

# 配置无线网卡以ap模式启动WiFi热点
>>> ESP8266.ap('wifiname','wifipassword')
0

#获取拨号信息
>>> Info = dataCall.getInfo(1,0)

#设置默认网卡，ap模式下设置4G为默认网卡
>>> ESP8266.set_default_NIC(Info[2][2])
0

#添加路由信息，设置网卡转发规则
>>> ESP8266.router_add('192.168.4.0', '255.255.255.0')
0

# 获取当前网卡状态 返回“4”说明无线网卡已启用ap热点模式
>>> ESP8266.status()
4

# 此时可用其他终端设备连接ap热点，进行网络访问
```



**web配网模式：**
```python
# 在web配网模式下，可以使用手机等设备连接无线网卡的WiFi热点，通过浏览器进入web页面，配置无线网卡的网络信息。
>>> from usr.WLAN import ESP8266
>>> from machine import UART


# 初始化网卡，以下为使用web配置sta模式；若使用web配置ap模式，需把模式字段设置为ESP8266.AP
>>> ESP8266 = ESP8266(UART.UART2, ESP8266.STA)

# 获取当前网卡状态
>>> ESP8266.status()
2

# 配置web配网模式热点的信息
>>> ESP8266.web_config('admin','adminpwd')
0

# 获取当前网卡状态 返回“3”表示web配网已启用，可以使用web配网模式
>>> ESP8266.status()
3

# 此时可用其他终端设备连接配网热点，登录web界面(网址: 192.168.4.1)进行网络配置
```


## Classes
- [class ESP8266 – ESP8266无线网络控制](./WLAN.ESP8266.md)