# dataCall - 拨号功能

拨号，指的是PDP Context的激活操作，激活成功后，核心网的PDN网关才会分配一个IP地址给模组。

`dataCall`模块包含了PDP Context配置和获取、激活、去激活以及获取模组的IP信息等功能。模组烧录QuecPython的固件，开机后，默认会自动执行拨号。如果用户配置了APN，则使用用户配置的APN信息进行拨号；否则使用默认APN进行拨号。



> 用户使用不同运营商的SIM卡时，应配置对应运营商的APN信息；如果不配置或者配置错误，可能会导致模组注网失败或拨号失败，模组获取不到IP地址，无法上网。配置APN的方式，参考`dataCall.setPDPContext`方法。



**示例：**

```python
import dataCall
from misc import Power

# 用户需要配置的APN信息，根据实际情况修改
usrConfig = {'apn': '3gnet', 'username': '', 'password': ''}

# 获取第一路的APN信息，确认当前使用的是否是用户指定的APN
pdpCtx = dataCall.getPDPContext(1)
if pdpCtx != -1:
    if pdpCtx[1] != pdpConfig['apn']:
        # 如果不是用户需要的APN，使用如下方式配置
        ret = dataCall.setPDPContext(1, 0, pdpConfig['apn'], pdpConfig['username'], pdpConfig['password'], 0)
        if ret == 0:
            print('APN 配置成功。')
            # 重启后按照配置的信息进行拨号
            Power.powerRestart()  
        else:
            print('APN 配置失败。')
    else:
        print('APN 已经配置过了。')
else:
    print('获取PDP Context失败。')
```



## APN配置与获取功能

### `dataCall.setPDPContext`

```
dataCall.setPDPContext(profileID, ipType, apn, username, password, authType)
```

配置PDP Context相关信息，配置信息掉电保存。拨号时使用该方法配置的参数进行PDP Context激活。

**参数描述：**

* `profileID` - PDP上下文ID，整型值，范围1~3，一般设置为`1`。
* `ipType` - IP协议类型，整型值，取值范围见下表：

| 值   | 含义       |
| ---- | ---------- |
| 0    | IPv4       |
| 1    | IPv6       |
| 2    | IPv4和IPv6 |

- `apn` - 接入点名称，全称Access Point Name，字符串类型，可为空，为空直接写`''`，范围0~64字节。

- `username` - 用户名，字符串类型，可为空，为空直接写`''`，范围0~64字节。

- `password` - 密码，字符串类型，可为空，为空直接写`''`，范围0~64字节。

- `authType` - APN鉴权方式，整型值，取值范围见下表枚举：

| 值   | 含义      |
| ---- | --------- |
| 0    | 表示无    |
| 1    | PAP       |
| 2    | CHAP      |
| 3    | PAP和CHAP |

**返回值描述：**

返回一个整型值，`0`表示设置成功，`-1`表示设置失败。



> 关于BG77/BG95系列的profileID参数范围，在NB网络制式下，实际只支持1~2。
>
> 关于authType参数，仅BG77/BG95系列模组支持值3。当设置username,  password为非空字符串，authType又为`0`会自动变成`2`；当设置username，password为空字符串，authType又为`非0`会自动变成`0`。
>
> 支持该方法的模组：EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95系列。



**示例：**

```python
>>> import dataCall
>>> dataCall.setPDPContext(1, 0, '3gnet', '', '', 0)
0
```



### `dataCall.getPDPContext`

```python
dataCall.getPDPContext(profileID)
```

获取`profileID`对应的那一路PDP Context相关信息。

**参数描述：**

- `profileID` - PDP上下文ID，整型值，范围1~3。


**返回值描述：**

获取失败时，返回一个整型值`-1`；获取成功时，返回一个元组，包含PDP Context相关信息，格式如下：

`(ipType, apn, username, password, authType)`

元组参数描述见`dataCall.setPDPContext`方法的参数描述。



>支持该方法的模组：EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95系列。



**示例：**

```python
>>> import dataCall
>>> dataCall.getPDPContext(1)
(0, '3gnet', '', '', 0)
```



## 开机自动拨号功能

### `dataCall.setAutoActivate`

```python
dataCall.setAutoActivate(profileID, enable)
```

设置`profileID`指定的那一路开机是否自动进行PDP Context激活。

**参数描述：**

- `profileID` - PDP上下文ID，整型值，范围1~3。

- `enable` - 控制模组是否在开机时自动进行PDP Context激活，整型值，`0`表示关闭，`1`表示使能。



>如果用户没有使用`dataCall.setAutoActivate`方法和`dataCall.setAutoConnect`配置过，则默认开机对profileID为1的那一路进行自动激活和使能重连；否则按照用户的配置执行。
>
>支持该方法的模组：EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95系列。



**示例：**

```python
>>> import dataCall
>>> dataCall.setAutoActivate(1, 0) # 关闭profileID为1的那一路开机自动激活PDP Context功能
>>> dataCall.setAutoActivate(1, 1) # 开启profileID为1的那一路开机自动激活PDP Context功能
```



## 拨号重连功能

### `dataCall.setAutoConnect`

```python
dataCall.setAutoConnect(profileID, enable)
```

设置`profileID`指定的那一路是否使能自动重连功能。自动重连功能是指，因网络异常、信号差等异常场景导致模组与网络断开连接，当异常场景恢复正常后，模组自动进行拨号重连的行为。

**参数描述：**

- `profileID` - PDP上下文ID，整型值，范围1~3。

- `enable` - 控制是否使能自动重连，整型值，`0`表示关闭，`1`表示使能。



> 如果用户没有使用`dataCall.setAutoActivate`方法和`dataCall.setAutoConnect`配置过，则默认开机对profileID为1的那一路进行自动激活和使能重连；否则按照用户的配置执行。
>
> 支持该方法的模组：EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95系列。



**示例：**

```python
>>> import dataCall
>>> dataCall.setAutoConnect(1, 0) # 关闭profileID为1的那一路自动重连功能
>>> dataCall.setAutoConnect(1, 1) # 开启profileID为1的那一路自动重连功能
```



## DNS配置功能

### `dataCall.setDNSServer`

```python
dataCall.setDNSServer(profileID, simID, priDNS, secDNS)
```

配置DNS服务器地址。模组拨号成功后，会自动获取DNS服务器地址，一般无需用户再重新配置。如模组自动获取的DNS服务器地址不可用，可使用该方法重新配置。

**参数描述：**

- `profileID` - PDP上下文ID，整型值，范围1~3。

- `simID` - SIM卡卡槽编号，整型值，`0`表示SIM0，`1`表示SIM1，目前仅支持`0`。

- `priDNS` - 主要DNS服务器地址，字符串类型。

- `secDNS` - 辅助DNS服务器地址，字符串类型。

**返回值描述：**

返回一个整型值，`0`表示配置成功，`-1`表示配置失败。



>支持该方法的模组：
>
>EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC200A/EC200U/EC600U/EG912U/EG915U系列。



**示例：**

```python
>>> import dataCall
>>> dataCall.setDNSServer(1, 0, "8.8.8.8", "114.114.114.114")
0
```



## 回调注册功能

### `dataCall.setCallback`

```python
dataCall.setCallback(fun)
```

注册回调函数。当网络状态发生变化时，如网络断开、拨号重连成功时，会触发注册的回调函数，告知用户网络状态。

**参数描述：**

* `fun` - 回调函数名，回调函数格式以及回调函数的参数说明如下：

```python
def netCallback(args):
	pass
```

| 参数    | 类型 | 含义                                             |
| ------- | ---- | ------------------------------------------------ |
| args[0] | 整型 | PDP上下文ID，表示当前是哪一路PDP网络状态发生变化 |
| args[1] | 整型 | 网络状态，0表示网络断开，1表示网络连接成功       |

**返回值描述：**

返回一个整型值，`0`表示注册成功，`-1`表示注册失败。



> 支持该方法的模组：
>
> EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95系列



**示例：**

```python
import dataCall

def netCallback(args):
    pdp = args[0]
    datacallState = args[1]
    if datacallState == 0:
        print('### network {} disconnected.'.format(pdp))
    elif datacallState == 1:
        print('### network {} connected.'.format(pdp))
        
dataCall.setCallback(netCallback)
```



## 激活与去激活功能

### `dataCall.activate`

```
dataCall.activate(profileID)
```

激活`profileID`指定的那一路PDP Context。

**参数描述：**

- `profileID` - PDP上下文ID，整型值，范围1~3。


**返回值描述：**

返回一个整型值，`0`表示激活成功，`-1`表示激活失败。



> 模组会在开机时自动进行PDP Context激活，一般不需要用户执行激活操作。如用户关闭了开机自动进行PDP Context激活的功能，则需要用户调用此方法来进行PDP Context激活操作。
>
> 支持该方法的模组：EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95系列。



**示例：**

```python
>>> import dataCall
>>> dataCall.setPDPContext(1, 0, '3gnet', '', '', 0) # 激活之前，应该先配置APN，这里配置第1路的APN
0
>>> dataCall.activate(1) # 激活第1路
0
```



### `dataCall.deactivate`

```
dataCall.deactivate(profileID)
```

去激活`profileID`指定的那一路PDP Context。

**参数描述：**

- `profileID` - PDP上下文ID，整型值，范围1~3。

**返回值描述：**

返回一个整型值，`0`表示去激活成功，`-1`表示去激活失败。



> 支持该方法的模组：EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95系列。



## 获取拨号信息功能

### `dataCall.getInfo`

```python
dataCall.getInfo(profileID, ipType)
```

获取拨号信息，包括拨号状态、IP地址、DNS服务器地址等。

**参数描述：**

- `profileID` - PDP上下文ID，整型值，范围1~3。
- `ipType` - IP协议类型，整型值，取值范围见下表：

| 值   | 含义       |
| ---- | ---------- |
| 0    | IPv4       |
| 1    | IPv6       |
| 2    | IPv4和IPv6 |

**返回值描述：**

获取失败返回整形值`-1`，获取成功返回一个元组，包含拨号信息，具体说明如下：

`ipType`为0或1，返回值格式为：

`(profileID, ipType, [state, reconnect, addr, priDNS, secDNS])`

| 参数      | 类型   | 含义                                                         |
| --------- | ------ | ------------------------------------------------------------ |
| profileID | 整型   | PDP上下文ID                                                  |
| ipType    | 整型   | IP协议类型，有如下几个值：<br>0表示IPv4<br>1表示IPv6<br>2表示IPv4和IPv6 |
| state     | 整型   | IPv4或IPv6的拨号状态<br>0表示未拨号或拨号失败<br>1表示拨号成功 |
| reconnect | 整型   | 拨号重连标志，保留参数，暂未使用                             |
| addr      | 字符串 | IPv4或IPv6的地址，具体取决于输入参数ipType的值：<br>ipType为0，addr为IPv4地址<br>ipType为1，addr为IPv6地址 |
| priDNS    | 字符串 | 主要DNS服务器地址                                            |
| secDNS    | 字符串 | 辅助DNS服务器地址                                            |

`ipType`为2，返回值格式为：

`(profileID, ipType, [state, reconnect, ipv4Addr, priDNS, secDNS], [state, reconnect, ipv6Addr, priDNS, secDNS])`

返回的元组中，第一个列表包含的是IPv4的拨号信息，第二个列表包含的是IPv6的拨号信息。



>返回值 `(1, 0, [0, 0, '0.0.0.0', '0.0.0.0', '0.0.0.0'])` 表示当前没有拨号或者拨号没有成功。
>
>支持该方法的模组：EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95/BC25/BC95系列。
>
>由于需要向老版dataCall.getInfo兼容，实际profileID的最大值是大于3的，具体以实际能够查询的profileID为准。



**示例：**

```python
>>> import dataCall
>>> dataCall.getInfo(1, 0)
(1, 0, [1, 0, '10.91.44.177', '58.242.2.2', '218.104.78.2'])
```


