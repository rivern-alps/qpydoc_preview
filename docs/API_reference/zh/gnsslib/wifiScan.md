# wifiScan - WiFi扫描

`wifiScan`模块提供了同步和异步两种方式来扫描模组周边的WiFi热点信息。



> 支持`wifiScan`功能的模组：
>
> EC100Y/EC200N/EC600N/EC600S/EC600M部分系列/EC800M部分系列/EC800N/EG912N/EG915N/EG810M/EC600G/EC800G/EC200U/EC600U部分系列/EG912U/EG915U系列模组。
>
> EC600M系列模组中，EC600MCN_LC/EC600MCN_LF不支持`wifiScan`；
>
> EC800M系列模组中，EC800MCN_GC/EC800MCN_LC/EC800MCN_LF不支持`wifiScan`；
>
> EC600U系列模组中，EC600UEC_AC不支持`wifiScan`。



## 开启或关闭扫描功能

### `wifiScan.control`

```python
wifiScan.control(option)
```

开启或者关闭WiFi扫描功能。

**参数描述：**

* `option` - 控制选项，整型值，`0`表示关闭WiFi扫描功能，`1`表示开启WiFi扫描功能。

**返回值描述：**

返回一个整型值，`0`表示成功，`-1`表示失败。

**示例：**

```python
>>> import wifiScan
>>> wifiScan.control(1) # 开启 wifiScan 功能
0
>>> wifiScan.control(0) # 关闭 wifiScan 功能
0
```



### `wifiScan.getState`

```python
wifiScan.getState()
```

获取WiFi扫描功能的当前状态是开启还是关闭。

**返回值描述：**

WiFi扫描功能已开启则返回`True`，未开启返回`False`。



## 扫描参数配置与获取功能

### `wifiScan.setCfgParam`

```python
wifiScan.setCfgParam(timeout, round, maxNums[, priority])
```

设置WiFi扫描参数。

**参数描述：**

* `timeout` - 超时时间，整型值；当触发超时会主动上报已扫描到的热点信息，若在超时前扫描到设置的热点个数会结束扫描并返回扫描结果。参数范围：4~60s。
* `round` - 扫描轮数，整型值，达到扫描轮数后，会结束扫描并返回扫描结果。参数范围：1~3次。
* `maxNums` - 最大扫描数量，整型值，当扫描热点数量达到设置的最大个数，会结束扫描并返回扫描结果。参数范围：4~30个。
* `priority` - 扫描业务的优先级，整型值，可选参数，范围0~1。`0`表示网络业务优先，`1`表示WiFi扫描业务优先。网络业务优先时，当有数据业务发起时会中断WiFi扫描。WiFi扫描业务优先时，当有数据业务发起时，不会建立RRC连接，保障WiFi扫描正常执行，扫描结束后才会建立RRC连接。

**返回值描述：**

返回一个整型值，`0`表示设置成功，`-1`表示设置失败。



> EC200U/EC600U/EG912U/EG915U/EC600G/EC800G系列模组不支持priority参数，使用时可不填该参数。



### `wifiScan.getCfgParam`

```python
wifiScan.getCfgParam()
```

获取WiFi扫描参数。

**返回值描述：**

成功返回一个元组，失败返回整型` -1`。返回值参数描述见`wifiScan.setCfgParam`方法的参数描述，返回元组格式如下：

`(timeout, round, maxNums, priority)`



## 回调注册功能

### `wifiScan.setCallback`

```python
wifiScan.setCallback(fun)
```

注册回调函数。使用异步扫描时，需要注册回调函数，扫描结果通过回调函数返回给用户。

**参数描述：**

* `fun` - 回调函数名，回调函数格式以及回调函数的参数说明如下：

```python
def wifiscanCallback(args):
	pass
```

回调函数参数描述：

| 参数 | 类型 | 含义                                                         |
| ---- | ---- | ------------------------------------------------------------ |
| args | 元组 | 包含扫描到的WiFi热点数量和热点信息，形式如下：<br>`(nums,  [(mac, rssi),...,(mac, rssi)])`<br>`nums` - 整型值，表示扫描到的热点数量<br>`mac` - 字符串类型，表示WiFi无线接入点的MAC地址<br>`rssi` - 整型值，表示WiFi热点信号强度 |

**返回值描述：**

返回一个整型值，`0`表示注册成功，`-1`表示注册失败。



## 启动扫描功能

### `wifiScan.asyncStart`

```python
wifiScan.asyncStart()
```

开始异步扫描，扫描结果通过用户注册的回调函数返回。

**返回值描述：**

返回一个整型值，`0`表示执行成功，`-1`表示执行失败。

**示例：**

```python
import wifiScan

def wifiscanCallback(args):
	print('wifi list:{}'.format(args))
wifiScan.setCallback(wifiscanCallback)

wifiScan.control(1)
wifiScan.asyncStart()

'''
执行结果：
wifi list:(2, [('F0:B4:29:86:95:C7', -79),('44:00:4D:D5:26:E0', -92)])
'''
```



### `wifiScan.start`

```python
wifiScan.start()
```

开始同步扫描，扫描结束后直接返回扫描结果。由于是同步接口，所以扫描未结束时，程序会阻塞在该接口中。

**返回值描述：**

扫描成功时返回一个元组，失败返回整型`-1`。成功时返回值格式如下：

`(wifiNums, [(mac, rssi), ... , (mac, rssi)])`

| 参数     | 类型   | 说明                   |
| -------- | ------ | ---------------------- |
| wifiNums | 整型   | 扫描到的 WiFi 热点数量 |
| mac      | 字符串 | WiFi 热点的MAC地址     |
| rssi     | 整型   | 信号强度               |

**示例：**

```python
>>> wifiScan.start()
(7, [('34:CE:00:09:E5:A8', -30), ('30:FC:68:E2:2D:F7', -44), ('12:CA:41:D4:B2:50', -54), ('D0:DB:B7:90:2D:07', -58), ('00:03:7F:12:CB:CB', -61), ('60:38:E0:C2:84:D9', -62), ('08:4F:0A:05:22:8F', -63)])
```

