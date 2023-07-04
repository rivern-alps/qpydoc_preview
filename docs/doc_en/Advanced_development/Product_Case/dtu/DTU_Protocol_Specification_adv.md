## Revision history

| Version | **Date**   | **Author** | **Description** |
| :------ | ---------- | ---------- | --------------------- |
| 1.0     | 2021-11-25 | Chavis Chen | Initial version |

## Summary

In this document, it mainly illustrates following contents: 
-  The format of message that used to communicate with Cloud
-  The message format of all commands that in command mode: Set and query parameter. 
- **dtu_config.json**: Specific illustration of configuring file field. 

## Data format

The **json** format is used to communicate between DTU and Cloud. 

- Down-link message on Cloud 

Command and modbus modes

`{“msg_id”: msg_id, “data”: “1234”[, “cmd_code”: 0X40, “topic_id”: 1]}`

Transparency mode

`{“msg_id”: msg_id, “data”: “1234”}`

Field illustration

msg_id: Message ID, normally combined by time stamp and 3 random numbers. 

data: Message field 

cmd_code：可选字段，填写对应功能码，***<u>并又DTU执行相应的操作</u>***，此字段仅在命令模式下生效

Selectable field, which is used to fill in corresponding function codes. This field will take effect in command mode only. 

topic_id：可选字段，填写mqtt返回需要publish的topic_id，此字段仅在命令模式与使用MQTT/Aliyun/Txyun时生效

Selectable field, which is used to fill in mqtt, in terms of return, the published topic_id is needed. This field will take effect in command mode as well as using MQTT/Aliyun/Txyun. 

- Uplink message on Cloud

Command and modbus modes 

`{“msg_id”: msg_id, “data”: “1234”[, “cmd_code”: 0X40, “status”: 1]}`

Transparency mode

`{“msg_id”: msg_id, “data”: “1234”}`

Field illustration 

msg_id: Message ID, normally combined by time stamp and 3 random numbers.  the same msg_id will be used when replying message. 

data: Message field 

cmd_code：可选字段，填写对应功能码，***<u>并又DTU执行相应的操作</u>***，此字段仅在命令模式下生效

Selectable field, which is used to fill in corresponding function codes. This field will take effect in command mode only. 

status： Selectable field, which will take effect in command mode and be used to reply whether the execution is successful. 

## Command illustration 

**Illustration on function code in protocol ：**

**1. Query DTU, reset DTU and set parameter. The function code of data transparency and returning data is the same.**

**2. For the status code of returned data, please refer to the related status code list. ** 

### Function code list 

| Function Code | Function illustration |
| --- | --- |
| 0x00-0x3f | Query command |
| 0x00 | Query IMEI |
| 0x01 | Query local number |
| 0x02 | Query FW version number |
| 0x03 | Query signal strength                   |
| 0x04 | Query current configuration parameter |
| 0x05 | Diagnose query |
| 0X06 | Query ICCID |
| 0X07 | Query ADC voltage |
| 0X08 | Query GPIO info |
| 0X10 | Query temperature and humidity |
| 0X11 | Query network connection |
| 0X12 | Query network status |
| 0X13 | Query base station location |
| 0x50~0x8f | Set command |
| 0x50 | Protocol SMS transparency |
| 0x51 | Configure password |
| 0x52 | Add IMEI |
| 0x53 | Login server and send registration info |
| 0x54 | FW version |
| 0x55 | Enable auto-upgrade |
| 0x56 | Log output |
| 0x57 | Get configuration parameter by server   |
| 0x58 | Serial port parameter |
| 0x59 | Channel configuration parameter |
| 0x60 | Set APN |
| 0x61 | Set GPIO |
| 0x62 | GPS |
| 0x63 | Data stream |
| 0x64 | Warning |
| 0x65 | Task |
| 0xfd | Stop protocol |
| 0xfe | Enabling DTU, fail to receive command |
| 0xff | Reset                                   |

## Query command 

###  Query IMEI

**Illustration：** 

IMEI of DTU 

Function code: 0x00

Returned data

`{"code": 0x00 , "data": "123456789012345" , "success":1}`

Field 

| **Field** | **Type** | **Indication** |
| --- | --- | --- |
| code | str | Status code (once failed to query IMEI, refer to status code list to locate the exact error) |
| data | str | Return IMEI |
| success | int | 0 failure 1 success |

### Query local code 

**Illustration：**

Query the number of SIM card 

Function code: 0x01

Returned data

`{"code": 0x01 , "data": "17201593988" , "success":1}`

| **Field** | **Type** | **Indication** |
| --- | --- | --- |
| code | Str | Status code |
| data | str | Phone number of SIM card |
| success | int | 0 failure 1 success |

### Query FW version number 

**Illustration：**

Query current FW version number (When enabling fota upgrade, if the firmware version is smaller than the server version, the upgrade will not be performed )

Format of FW version number: v 1 

Function code: 0x02

Returned data 

`{"code": 0x02 , "data": "v 1" , "success":1}`

| **Field** | **Type** | **Indication ** |
| --- | --- | --- |
| code | str | Status code |
| data | str | FW version number |
| success | int | 0  failure  1  success |

### Query signal quality

**Illustration：**

The range of network signal quality is from 0 to 31. The bigger value, the better signal quality

Function code: 0x03

Returned data

`{"code": 0x03 , "data": " CSQ17 " , "success":1}`

| **Field** | Type | **Indication** |
| --- | --- | --- |
| code | byte | Status code |
| data | str | CSQ1~CSQ31 |
| success | int | 0 Failure 1 success |

### Query current configuration parameter 

Function code: 0x04

Data 

```
{ "password": "012345",

"data":{}

}
```
Returned data

`{"code": 0x04 , "data": " req config " , "success":1}`

| **Field** | **String** | **Indication** |
| --- | --- | --- |
| code | byte | Status code |
| data | str | req config |
| success | int | 0 Failure 1 Success |

### Diagnose query

Illustration: Query the error report of running DTU currently

Function code: 0x05

Returned data

```
{"code":0x05,

"data":[{"func_code": "0x01" , "error_code": " 6001"}],

"success":1}
```

| **Field** | **Type** | **Indication** |
| --- | --- | --- |
| code | str | Status code |
| func_code | str | Function code |
| error_code | str | Error code |
| success | int | 0 Failure 1 Success |

### Query iccid 

Illustration: Query iccid 

Function code: 0x06

Returned data

```
{"code":0x06,

"data": "12456465486561516515153",

"status":1}
```

| **Field** | **Type** | **Indication** |
| --- | --- | --- |
| code | int | Status code |
| data | str | Function code |
| status | str | 0 Failure 1 Success |

### Query ADC 

Illustration: query adc

Function code: 0x07

Returned data

```
{"code":0x07,

"data": "3.7",

"status":1}`
```
| **Field** | Type | **Indication** |
| --- | --- | --- |
| code | int | Status code |
| data | str | ADC voltage |
| status | str | 0 Failure 1 Success |

### Query GPIO

Illustration: query GPIO 

Function code: 0x08

Returned data

```
{"code":0x08,

"data": "gpio_msg",

"status":1}
```

| **Field** | Type | **Indication**               |
| --- | --- | --- |
| code | int | Status code                |
| data | str | Info by GPIO |
| status | str | 0 Failure 1 Success |

### Query humidity and temperature

Illustration: Query temperature and humidity

Function code: 0x010

Returned data

```
{"code":0x10,
"data": {"temperature": 26.0, "humidity": 60.0},
"status":1}
```

| Field  | Type | **Indication**                                          |
| --- | --- | --- |
| code | int | Status code |
| data | dict | Temperature and humidity info{"temperature": temp, &##39;humidity&##39;: humid}<br / |
| status | str | 0 Failure 1 Success |

### Query network connection

Illustration: Query network connection, each connection type returns one corresponding connection status

Function code: 0x11

Returned data

```
{"code":0x11,
"data": "200",
"status":1}
```

| **Field** | Type | **Indication**                     |
| --- | --- | --- |
| code | int | Status code |
| data | str | Network connection status |
| status | str | 0 Failure 1 Success |

### Query network status 

Illustration: Query network connection and return base station info 

Function code : 0x12

Returned data

```
{"code":0x12,

"data": ([], [], [(0, 14071232, 1120, 0, 123….),

"status":1}
```

| **Field | Type   | **Indication**            |
| --- | --- | --- |
| code | int | Status code |
| data | turple | Base connection |
| status | str | 0 Failure 1 Success |

### Query base station location 

Illustration: query base station location info 

Function code: 0x13

Returned data

```
{"code":0x13,

"data": (117.1138, 31.82279, 550) ,

"status":1}
```

| Field  | Type | **Indication**                |
| --- | --- | --- |
| code | int | Status code |
| data | str | Base station location |
| status | str | 0  Failure 1 Success |

## Reset command 

Function code:  0xff

Data 

```
{ Password: "012345",

"data":{}

}
```

Returned data

`{"code": 0x06 , "data": " reset dtu " , "success":1}`

| Field   | Type | **Indication**            |
| --- | --- | --- |
| code | Str | Status code |
| data | str | reset dtu |
| success | int | 0 Failure 1 Success |

## Set command 

### Basic setting 

#### Message SMS transparency 

Function code: 0x50

Data 

- Number: 32 bytes to identify targeted phone number, if 32 bytes are not available, 0x00 shall be supplemented. 
- Content: at maximum 1024 bytes, which serves as SMS.   
```
{

"password":"",

"data":{

message: {"number":"12123123", -- Target number 

"data:" " -- Send SM 

}
}
}
```

Returned data

`{"code": 0x50 , "data": " " , "success":1}`

| **Field** | Type | **Indication**         |
| --- | --- | --- |
| code | str | Status code |
| data | str | Received message |
| success | int | 0  Failure   1 Success |

**Configure password**

**Illustration：**

Query IMEI, local number and FW version number. In addition, the password is not needed when querying signal strength。 

Querying the current configuration parameter and modifying the bound channel of transparency, the password is needed. 

Enabling auto-grade, the password is needed

Function code: 0x51

Data

```
{
"password":" ",
"data":{ "password": "012345"}
}
```
Note:  The initial password is the last six numbers of FW IMEI. 

Such as IMEI: 123456789012345, the initial password is 012345

| **Field** | **Indication** |
| --- | --- |
| password | Current password |
| data | Password after modification |

Returned data

`{"code": 0x51 , "data": " " , "success":1}`

| **Field** | **Indication** |
| --- | --- |
| code | Status code |
| data ||
| Success |0 Failure 1 Success|
**Login server and send registration info** 

**Illustration**

Login server and send registration info for the first time

Function code: 0X53

Data 

```
{
"password":"",
"data":{"reg": 1}
}
```

| **Reg**| **Value** |
| --- | --- |
| 0 | Do not send{ "reg": 0} |
| 1 | { "reg": 1}Send following json data under the circumstance of getting access to server for the first time<br /> {"csq":rssi,"imei":imei,"iccid":iccid,"ver":version} csq - signal quality, imei - FW IMEI, iccid - ICCID of SIM card,  ver - FW version |
| Assign | { "reg": "Assigned registration info"} |

Returned data

`{"code": 0x53 , "data": " " , "success":1}`

| **Field** | **Type** | **Indication** |
| --- | --- | --- |
| code | str | Status code |
| data | str | send reg |
| success | int | 0  Failure 1 Success |

#### FW version

**Illustration：**

Modify FW version to execute fota upgrade (When enabling fota upgrade, if the firmware version is smaller than the server version, the upgrade will not be performed )

Function code: 0x54

Data

```
{
"password":"",
"data":{
" version ": "100" --- Version number（digital string is used) 
}
}
```

Returned data

`{"code": 0x54 , "data": " " , "success":1}`

| **Field** | **Type** | **Indication** |
| --- | --- | --- |
| code | Str | Status code |
| data | str | FW version           |
| success | int | 0  Failure 1 Success |

#### Enable auto fota upgrade

**Illustration：**

Fota upgrade switch

Function code: 0x55

Data 

```
{
"password":"",
"data":{
"fota": 1 -- 0 off/ 1 on（int type）
}
}
```
Returned data

`{"code": 0x55 , "data": " fota" , "success":1}`

| Field | **Type** | **Indication** |
| --- | --- | --- |
| code | str | Status code |
| data | str | fota |
| success | int | 0 Failure 1 Success |

#### Output log 

**Illustration ：**

Printing log record via serial port, however, it does not support yet. For log output, please connect Debug port. 

Function code: 0x56

Data

```
{
"password":"",
"data":{
{"nolog": 1} Enbale log 0 off/1 on（int type）
}
}
```
Returned data

`{"code": "20000" , "data": "log " , "success":1}`

| Field | **Type** | **Indication**           |
| --- | --- | --- |
| code | Str | Status code |
| data | str | log |
| success | int | 0 Failure 1 Success |

#### Get configuration parameter via server 

Function code: 0x57

Data

```
{
"password":"",
"data":{
{" service_acquire"：0}
}
}
```
Note: In local configuration, getting parameter configuration from server is enabled by default. 

| **Field** | **Type** | **Indication** |
| --- | --- | --- |
| service_acquire | Int | Get configuration parameter via server. 0 off/1 on |

Returned data

`{"code": "20000" , "data": "service acquire " , "success":1}`

| Field | **Type** | **Indication**           |
| --- | --- | --- |
| code | Str | Status code |
| data | str | service acquire |
| success | int | 0 Failure 1 Success |

#### Parameter on serial port 

Function code: 0x58

Data

```
{"password": ""
"data":{
"uconf": {
"0": {
"baudrate": "115200",
"databits": "8",
"parity": "0",
"stopbits": "1",
"flowctl": "0"
}
}}
```
Returned data

`{"code": "20000" , "data": " " , "success":1}`

| Field | **Type** | **Indication**           |
| --- | --- | --- |
| code | Str | Status code |
| data | str | uconf |
| success | int | 0  Failure 1 Success |

#### Configure channel parameter 

Function code: 0x59

Data

```
{"password":"",
"data":{
"conf":"1": {
"protocol": "aliyun",
"type": "mos",
"keepAlive": "",
"clientID": "0",
"Devicename": "ec600n",
"ProductKey": "gbh26bFEA4M",
"DeviceSecret": "b7ff5acc0671d40adfd0eff57e7605f6",
"ProductSecret": "",
"cleanSession": true,
"qos": "1",
"subscribe": {"0": "/gbh26bFEA4M/ec600n/user/subtest"},
"publish": {"0": "/gbh26bFEA4M/ec600n/user/pubtest"},
"serialID": "0"}
}}
```
**For the configuration parameter of corresponding channel, refer to the Chapter 6.2.10.1 on < specification on configuring channel >.** 

Returned data

`{"code": "20000" , "data": " " , "success":1}`

| Field | **Type** | **Indication**           |
| --- | --- | --- |
| code | str | Status code |
| data | str | conf |
| success | int | 0 Failure 1 Success |

##### Specification on configuring channel 

###### HTTP parameter
```
{
"protocol": "http",
"method": "get",
"url": "http://httpbin.org/get",
"reg_data": "",
"timeout": "",
"serialID": 1
}
```
| Field | **Type** | Indication                                               |
| --- | --- | --- |
| http | str | Http flag of communication method |
| method | str | Method to submit request |
| url | str | Address and parameter of HTTP request |
| timeout | int | The longest waiting time for HTTP request |
| serialD | int | Bound serial port number (1-2) of HTTP |

###### SOCKET TCP parameter 
```
{
"protocol": "tcp",
"ping": "",
"heartbeat": 30,
"url": "220.180.239.212",
"port": "8305",
"keepAlive": 300,
"serialID": 2
}
```
| Field | **Type** | Indication                                    |
| --- | --- | --- |
| tcp | str | TCP flag of Socket. |
| ping | str | Heart-beat package assigned by user, limited to digital and letter, suggested 2-4 bytes. |
| time | int | The "0" refers to shutdown heart-beat, suggested 60s to 300s. |
| url | str | Address and domain name of socket |
| port | int | Port number of socket server |
| KeepAlive | int | The longest time of link OT, the unit is s. Default as 300s. |
| serialD | int | Serial port number (1-2) bound to tcp/udp                    |

###### SOCKET UDP Parameter
```
{
"protocol": "tcp",
"ping": "",
"heartbeat": 30,
"url": "220.180.239.212",
"port": "8305",
"keepAlive": 300,
"serialID": 2
}
```
| 字段Field | **类型Type** | 含义Indication                                               |
| --- | --- | --- |
| udp | str | Socket的udp协议标识 UDP flag of Socket. |
| ping | str | 用户自定义的心跳包,只支持数字和字母,建议2-4个字节 Heart-beat package assigned by user, limited to digital and letter, suggested 2-4 bytes. |
| time | int | 0为关闭心跳包，建议60s-300s 0 refers to shutdown heart-beat, suggested 60s to 300s. |
| url | str | socket的地址或域名 Address and domain name of socket |
| port | int | socket服务器的端口号 port number of socket server |
| KeepAlive | int | 链接超时最大时间单位秒,默认300秒 (60~600) The longest time of link OT, the unit is s. Default as 300s（range from 60 to 600). |
| serialD | int | tcp/udp绑定的串口号(1~2) serial port number (1-2) bound to tcp/udp |

###### MQTT参数 MQTT parameter 
```
{
"protocol": "mqtt",
"clientID": "test_mqtt",
"keepAlive": 0,
"url": "broker-cn.emqx.io",
"port": "1883",
"cleanSession": true,
"subscribe": {"0": "/python/mqtt"},
"publish": {"0": "/python/mqtt"},
"qos": "0",
"retain": "1",
"serialID": "1"
}
```
| 字段Field    | **类型Type** | 含义Indication                                               |
| --- | --- | --- |
| mqtt | str | 表示MQTT协议 MQTT |
| clentID | str | 自定义客户端ID，使用IMEI做客户端ID此处留空 Assigned client ID. Please make it vacant if the IMEI is used as client terminal |
| keepAlive | int | 客户端的keepalive超时值。 默认为60秒 Keepalive of client terminal, default as 60s |
| address | str | MQTT的地址或域名The address and domain name of MQTT |
| port | int | socket服务器的端口号 The port number of socket server |
| cleanSession | int | MQTT是否保存会话标志位,0持久会话,1离线自动销毁 Whether the session flag is saved by MQTT, 0- continuous session, 1- delete automatically when offline |
| Sub | str | 订阅主题 Subscribe topic |
| pub | str | 发布主题Publish topic |
| qos | int | MQTT的QOS级别,默认0 QOS of MQTT, default as 0 |
| retain | int | MQTT的publish参数retain，默认0 Retain the parameter published by MQTT, default as 0 |
| serialD | int | MQTT通道捆绑的串口ID (1~3) Bound serial port ID of MQTT channel |

###### 阿里云参数Aliyun parameter 
```
{
"protocol": "aliyun",
"type": "mos",
"keepAlive": "",
"clientID": "test_mos",
"Devicename": "light01",
"ProductKey": "a1QNbCDxIWM",
"DeviceSecret": "0bceb8010ade0df2e6989982e63f7601",
"ProductSecret": "",
"cleanSession": true,
"qos": "1",
"subscribe": {"0": "/a1QNbCDxIWM/light01/user/get"},
"publish": {"0": "/a1QNbCDxIWM/light01/user/update"},
"serialID": "1"
}
```
| **字段**Field | **类型**Type | **含义**Indication |
| --- | --- | --- |
| aliyun | Str | 阿里云IOT的标识 IoT identifier of Aliyun |
| type | str | 一型一密tas/一机一密mos unique-certificate-per-device authentication tas/unique-certificate-per-product authentication mos |
| keepAlive | int | 通信之间允许的最长时间段（以秒为单位）,默认为300，范围（60-1200）使用默认值就填""或者" " Longest time permitted when communication, default as 300. It ranges from 60 to 1200. Just fill punctuation marks "" or " " if the default value is used. |
| clientID | str | clientID ,自定义字符（不超过64）Client ID, the assigned characters(at most 64) |
| Devicename | str | 设备名称 Device name |
| ProductKey | str | 产品密钥Product key |
| DeviceSecret | str | 设备密钥（使用一型一密认证此参数传入"")Device secret (Upload when unique-certificate-per-device authentication is deployed ) |
| ProductSecret | str | 产品密钥（使用一机一密认证时此参数传入"")Product secret (Upload when unique-certificate-per-product authentication  ) |
| cleanSession | int | MQTT 保存会话标志位( 0则客户端是持久客户端，当客户端断开连接时，订阅信息和排队消息将被保留, 1代理将在其断开连接时删除有关此客户端的所有信息 ) Save session flag by MQTT (0- perpetual client terminal, once disconnected , the subscribed message and queue will be saved. 1- once disconnected, the agency will delete all info related to this client terminal) |
| QOS | int | MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试 1：发送者最少发送一次消息，确保消息到达Broker <br />QOS of MQTT(Default as 0, 0 or 1 is available ) 0: Transmit message for one time without trying again. 1- Transmit message at least one time to guarantee the message arrives at Broker. |
| subTopic | str | 订阅主题Subscribe topic |
| pubTopic | str | 发布主题Publish topic |
| serialD | int | MQTT通道捆绑的串口ID (1~3) Bound serial port ID of MQTT channel(1-3) |

###### 腾讯云参数Txyun parameter 
```
{
"protocol": "txyun",
"type": "mos",
"keepAlive": "",
"clientID": "test_tx_mos",
"Devicename": "Smart_test01",
"ProductKey": "H7MBLRYXN9",
"DeviceSecret": "89c7tXT3s3grZTr/YFjxSg==",
"ProductSecret": "",
"cleanSession": true,
"qos": "1",
"subscribe": {"0": "H7MBLRYXN9/Smart_test01/control"},
"publish": {"0": "H7MBLRYXN9/Smart_test01/event"},
"serialID": "1"
}
```
| **字段** Field | **类型**Type | **含义**Indication |
| --- | --- | --- |
| txyun | str | 腾讯云IOT的标识 IoT identifier of Txyun |
| type | str | 一型一密tas/一机一密mos unique-certificate-per-device authentication tas/unique-certificate-per-product authentication mos |
| keepAlive | int | 通信之间允许的最长时间段（以秒为单位）,默认为300，范围（60-1200）使用默认值就填""或者" "。Longest time permitted when communication, default as 300. It ranges from 60 to 1200. Just fill punctuation marks "" or " " if the default value is used. |
| clientID | str | clientID ,自定义字符（不超过64）Client ID, the assigned characters (at most 64) |
| Devicename | str | 设备名称 Device name |
| ProductKey | str |产品密钥Product key|
 |
| DeviceSecret | str | 设备密钥（使用一型一密认证此参数传入"") |Device secret (Upload when unique-certificate-per-device authentication is deployed )
| ProductSecret | str | 产品密钥（使用一机一密认证时此参数传入"") |Product secret (Upload when unique-certificate-per-product authentication  )
| cleanSession | int | MQTT 保存会话标志位( 0则客户端是持久客户端，当客户端断开连接时，订阅信息和排队消息将被保留, 1代理将在其断开连接时删除有关此客户端的所有信息 ) | Save session flag by MQTT (0- perpetual client terminal, once disconnected , the subscribed message and queue will be saved. 1- once disconnected, the agency will delete all info related to this client terminal)
| QOS | int | MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试 1：发送者最少发送一次消息，确保消息到达Broker |QOS of MQTT(Default as 0, 0 or 1 is available ) 0: Transmit message for one time without trying again. 1- Transmit message at least one time to guarantee the message arrives at Broker. 
| subTopic | str | 订阅主题 |Subscribe topic
| pubTopic | str | 发布主题 |Publish topic 
| serialD | int | MQTT通道捆绑的串口ID (1~3) |Bound serial port ID of MQTT channel(1-3)

## Set APN 

Illustration: This command is limited to the scenario that the same SIM card is not configured or used simultaneously. 

Function code: 0x60

Data

```
{
"password":" ",
"data":{"apn": ["", "", ""]}
}
```
Illustration on apn list 

First parameter of the list : APN name 

Second parameter of the list : User name of APN

Third parameter of the list : APN password

Returned data 

`{"code": 0x60 , "status":1}`

| Field | Type | Indication |
| --- | --- | --- |
| code | Str | Status code |
| data | str | set apn |
| success | int | 0 Failure 1 Success |

## GPIO pins

Function code: 0x61

Data 
```
{"password": " ",
"data":{"pins":[
"pio2", -- GPIO for network LED (pio1~pio128)
"pio4", -- GPIO used to notify that the server has been attached (pio1~pio128)
"pio4" --  GPIO GPIO used to reset DTU parameter(pio1~pio128)
]}}
```
Returned data 

`{"code": 0x61 , "status":1}`

| Field | Type | Indication |
| --- | --- | --- |
| code | Str | Status code |
| data | str | set gpio pins |
| success | int | 0 Failure  1 Success |

## OTA

Function code: 0x62

Data 
```
{"password": " ",
"data":{"ota":1
}
```
Returned data 

`{"code": 0x62 , "status":1}`

| **Field** | **Type** | Indication |
| --- | --- | --- |
| code | Str | Status code |
| data | str | OTA status |
| success | int | 0  Failure 1 Success |

## Set parameter 

Function code: 0x63

Data 
```
{"password": " ",
"data":{ Complete configuration file（omitted）
}
```
Returned data contents 

`{"code": 0x63 ,"status":1}`

| Field | Type | Indication                  |
| --- | --- | --- |
| code | Str | Status code |
| data | dict | Complete configuration file |
| status | int | 0 Failure 1 Success |