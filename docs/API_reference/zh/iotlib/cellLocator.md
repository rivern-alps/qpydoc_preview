# cellLocator - 基站定位

该模块提供基站定位功能，获取模组经纬度坐标信息。



>当前仅EC600S/EC600N/EC800N/EC200U/EC600U系列支持该功能。



## 获取坐标信息

### `cellLocator.getLocation`

```python
cellLocator.getLocation(serverAddr, port, token, timeout [, profileIdx])
```

该方法用于获取模组经纬度坐标信息。

**参数描述：**

* `serverAddr` - 服务器域名，字符串类型，长度必须小于255 bytes，目前仅支持 “[www.queclocator.com”](http://www.queclocator.xn--com-9o0a/)。
* `port` - 服务器端口，整型值，目前仅支持 80 端口。
* `token` - 密钥，字符串类型，16位字符组成，需要申请。
* `timeout` -设置超时时间，整型值，范围1-300s，默认300s。
* `profileIdx` - PDP上下文ID，整型值，可选参数，默认为当前拨号成功的那一路，设置其他值可能需要专用apn与密码才能设置成功；<br>范围如下：EC600N/EC600S/EC800N，范围：1 ~ 8；EC200U/EC600U，范围：1 ~ 7。

**返回值描述：**

 成功返回经纬度坐标信息，元组格式：`(longtitude, latitude, accuracy)`，`(0.0, 0.0, 0)`表示未获取到有效坐标信息；

`longtitude` ： 经度

`latitude` ：纬度

`accuracy` ：精确度，单位米

失败返回错误码说明如下：

`1` – 初始化失败

`2` – 服务器地址过长（超过255字节）

`3` – 密钥长度错误，必须为16字节

`4` – 超时时长超出范围，支持的范围（1 ~ 300）s

`5` – 指定的PDP网络未连接，请确认PDP是否正确

`6` – 获取坐标出错。

**示例：**

```python
>>> import cellLocator
>>> cellLocator.getLocation("www.queclocator.com", 80, "xxxxxxxxxxxxxxxx", 8, 1)
(117.1138, 31.82279, 550)
# 上面使用的密钥"xxxxxxxxxxxxxxxx"指代token，具体需要向移远申请
```
