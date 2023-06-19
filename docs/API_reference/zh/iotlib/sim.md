# sim - SIM卡功能

该模块提供sim卡相关功能的接口，如查询sim卡状态、iccid、imsi、电话号码等。



> 能成功获取IMSI、ICCID、电话号码的前提是SIM卡状态为1，可通过sim.getStatus()查询。



## 通用SIM访问功能

### `sim.genericAccess`

```
sim.genericAccess(simId, cmd)
```

通用SIM访问接口 ，用于发送csim指令直接和sim卡交互。

**参数描述：**

* `simId` - SIM卡卡槽编号，整型值，0表示SIM0，1表示SIM1，目前仅支持0。
* `cmd` - 移动终端以GSM 51.011中描述的格式传递给SIM的命令，字符串类型。

**返回值描述：**

成功：  返回元组数据。格式`(len，data)`，其中`len`为整型，表示`data`的长度。`data`为字符串类型，表示返回的数据内容。

失败：  返回整型值`-1`。



> 仅EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N系列支持该方法。



**示例：**

```python
>>> import sim
>>> sim.genericAccess(0,'80F2000016')
(48, '623E8202782183027FF08410A0000000871002FF86FF9000')
```



## 获取SIM卡信息

### `sim.getImsi`

```python
sim.getImsi()
```

该方法用于获取sim卡的IMSI。


**返回值描述：**

成功： 返回字符串类型，值为`IMSI`。

失败： 返回整型值`-1`。

**示例：**

```python
>>> import sim
>>> sim.getImsi()
'460105466870381'
```



### `sim.getIccid`

```python
sim.getIccid()
```

该方法用于获取sim卡的ICCID。

**返回值描述：**

成功： 返回字符串类型，数据值为`ICCID`。

失败： 返回整型值`-1`。

**示例：**

```python
>>> import sim
>>> sim.getIccid()
'89860390845513443049'
```



### `sim.getPhoneNumber`

```python
sim.getPhoneNumber()
```

该方法用于获取sim卡的电话号码，需要先进行写入本SIM卡电话卡号码。

**返回值描述：**

成功： 返回字符串数据类型的电话号码。

失败： 返回整型值`-1`。



>BC25系列不支持此方法



**示例：**

```python
>>> import sim
>>> sim.getPhoneNumber()
'+8618166328752'
```



## 查询SIM卡状态

### `sim.getStatus`

```python
sim.getStatus()
```

该方法用于查询当前SIM卡状态。

**返回值描述：**

sim卡状态码，整型值，具体说明如下：

| 返回值 | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| 0      | SIM卡不存在/被移除                                           |
| 1      | SIM已经准备好                                                |
| 2      | SIM卡已锁定，等待CHV1密码                                    |
| 3      | SIM卡已被阻拦，需要CHV1密码解锁密码                          |
| 4      | 由于SIM/USIM个性化检查失败，SIM卡被锁定                      |
| 5      | 由于PCK错误导致SIM卡被阻拦，需要MEP密码解除阻拦              |
| 6      | 需要隐藏电话簿条目的密钥                                     |
| 7      | 需要解锁隐藏密钥的编码                                       |
| 8      | SIM卡已锁定，等待CHV2密码                                    |
| 9      | SIM卡被阻拦，需要CHV2解锁密码                                |
| 10     | 由于网络个性化检查失败，SIM卡被锁定                          |
| 11     | 由于NCK不正确，SIM卡被阻拦，需要MEP解锁密码                  |
| 12     | 由于子网络锁个性化检查失败，SIM卡被锁定                      |
| 13     | 由于错误的NSCK，SIM卡被阻拦，需要MEP解锁密码                 |
| 14     | 由于服务提供商个性化检查失败，SIM卡被锁定                    |
| 15     | 由于SPCK错误，SIM卡被阻拦，需要MEP解锁密码                   |
| 16     | 由于企业个性化检查失败，SIM卡被锁定                          |
| 17     | 由于CCK不正确，SIM卡被阻止，需要MEP解锁密码                  |
| 18     | SIM正在初始化，等待完成                                      |
| 19     | 有以下六种情况会导致此错误返回码。</br>1、由于CHV1、CHV2、通用的PIN的使用被阻拦，此三种情况。</br>2、由于使用代码解锁CHV1、CHV2、通用的PIN被阻拦，此三种情况。|
| 20     | SIM卡无效                                                    |
| 21     | 未知状态                                                     |



## PIN码验证功能

### `sim.enablePin`

```python
sim.enablePin(pin)
```

该方法用于开启PIN码验证。开启后需要输入正确的PIN码进行验证，成功后，sim卡才能正常使用。需要注意最多3次尝试机会，连续3次错误后sim卡被锁定，需要PUK来解锁。

**参数描述：**

- `pin` - PIN码，字符串类型，一般默认是"1234"，最大长度不超过15位数字。

**返回值描述：**

返回一个整型值，`0`表示成功，`-1`表示失败。

**示例：**

```python
>>> sim.enablePin("1234")
0
```



### `sim.disablePin`

```python
sim.disablePin(pin)
```

该方法用于取消PIN码验证。

**参数描述：**

- `pin` - PIN码，字符串类型，一般默认是"1234"，最大长度不超过15位数字。

**返回值描述：**

返回一个整型值，`0`表示成功，`-1`表示失败。

**示例：**

```python
>>> import sim
>>> sim.disablePin("1234")
0
```



### `sim.verifyPin`

```python
sim.verifyPin(pin)
```

PIN码验证：用于SIM卡开启PIN码验证后，如果需要启用SIM卡，可以调用此方法来临时使本次的SIM卡正常使用，下次开机需要重新调用此方法进行验证(或者可以调用取消PIN验证的接口，重新开机后不需要重新PIN验证)。

**参数描述：**

- `pin` - PIN码，字符串类型，一般默认是"1234"，最大长度不超过15位数字。

**返回值描述：**

返回一个整型值，`0`表示成功，`-1`表示失败。

**示例：**

```python
>>> import sim
>>> sim.verifyPin("1234")
0
```



### `sim.changePin`

```python
sim.changePin(oldPin, newPin)
```

该方法用于更改sim卡PIN码。

**参数描述：**

- `oldPin` - 旧的PIN码，字符串类型，最大长度不超过15位数字。
- `newPin` - 新的PIN码，字符串类型，最大长度不超过15位数字。

**返回值描述：**

返回一个整型值，`0`表示成功，`-1`表示失败。

**示例：**

```python
>>> import sim
>>> sim.changePin("1234", "4321")
0
```



## SIM卡解锁

### `sim.unblockPin`

```python
sim.unblockPin(puk, newPin)
```

该方法用于SIM卡解锁：当多次输入PIN码错误需要用PUK码解锁。如果PUK码输入错误10次，SIM卡将永久锁定自动报废。

**参数描述：**

- `puk` - PUK码，字符串类型，长度8位数字，最大长度不超过15位数字。
- `newPin` - 新PIN码，字符串类型，最大长度不超过15位数字。

**返回值描述：**

返回一个整型值，`0`表示成功，`-1`表示失败。

**示例：**

```python
>>> import sim
>>> sim.unblockPin("12345678", "0000")
0
```



## 电话簿功能

### `sim.readPhonebook`

```python
sim.readPhonebook(storage, start, end, username)
```

读电话簿：用于获取指定存储位置上的电话本中的一条或多条电话号码记录。

**参数描述：**

- `storage` -电话号码存储位置，整型值，可选参数值如下：

| 值   | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| 0    | 拨号列表                                                     |
| 1    | 紧急电话号码                                                 |
| 2    | 固定拨号号码                                                 |
| 3    | 上次拨打电话号码                                             |
| 4    | 未接来电                                                     |
| 5    | 终端设备电话薄                                               |
| 6    | 终端设备电话薄和SIM/USIM电话薄                               |
| 7    | 本SIM卡电话号码(需要获取正确的电话号码进行写入)              |
| 8    | 已接来电                                                     |
| 9    | 本SIM卡电话薄                                                |
| 10   | 选择应用电话薄(如果USIM的应用已激活将选用ADF SUIM下的DF电话薄) |
| 11   | SIM卡中的MBDN                                                |
| 12   | SIM卡中的MN                                                  |
| 13   | 系统拨叫号码，网络服务拨号                                   |
| 14   | 来电信息                                                     |
| 15   | 呼出信息                                                     |

- `start` - 需要读取电话号码记录的起始编号，整型值，`start`为 `0` 表示不使用编号获取电话号码记，`start`应小于等于`end`。
- `end` - 需要读取电话号码记录的结束编号，整型值，必须满足：`end - start <= 20`。
- `username` - 电话号码中的用户名，字符串类型，当 start为 0 时有效，暂不支持中文，最大长度不超过30字节。

**返回值描述：**

成功： 返回元组数据，格式`(record_number, [(index, username, phone_number), ... , (index, username, phone_number)])`，具体如下：

| 参数            | 类型   | 含义                 |
| --------------- | ------ | -------------------- |
| `record_number` | 整型   | 读取的记录数量       |
| `index`         | 整型   | 在电话簿中的索引位置 |
| `username`      | 字符串 | 电话号码的用户名     |
| `phone_number`  | 字符串 | 电话号码             |

失败：返回整型值`-1`。



>- EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600MCNLE/EC600MCNLA/EC800MCNLA/EC800MCNLE/EC800MCNGA/EG810M/EC200A系列支持此方法。
>
>- 按username进行匹配时，并不是按完整的单词进行匹配，只要电话簿中已有记录的name是以username开头，那么就会匹配上。



**示例：**

```python
>>> import sim
>>> sim.readPhonebook(9, 1, 4, "")
(4,[(1,'Tom','15544272539'),(2,'Pony','15544272539'),(3,'Jay','18144786859'),(4,'Pondy','15544282538')])
>>> sim.readPhonebook(9, 0, 0, "Tom")
(1, [(1, 'Tom', '18144786859')])
>>> sim.readPhonebook(9, 0, 0, "Pony")
(1, [(2, 'Pony', '17744444444')])
>>> sim.readPhonebook(9, 0, 0, "Pon") #注意，这里只要是包含了‘pon’,都会被匹配上
(2, [(2, 'Pony', '17744444444'),(4,'Pondy','15544282538')])
```



### `sim.writePhonebook`

```python
sim.writePhonebook(storage, index, username, number)
```

写电话簿：用于向选定的存储位置，写入一条电话记录。

**参数描述：**

- `storage` - 电话号码存储位置，整型值，具体可选参数同上`sim.readPhonebook`中的`storage` ：

- `index` - 需要写入电话号码记录的在电话簿中的编号，整型值，范围`1 ~ 500`。
- `username` - 电话号码的用户名，字符串类型，长度范围不超过30字节，暂不支持中文名。
- `number` - 电话号码，字符串类型，最大长度不超过20字节。

**返回值描述：**

返回一个整型值，`0`表示成功，`-1`表示失败。



> EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600MCNLE/EC600MCNLA/EC800MCNLA/EC800MCNLE/EC800MCNGA/EG810M/EC200A系列支持此方法。



**示例：**

```python
>>> import sim
>>> sim.writePhonebook(9, 1, 'Tom', '18144786859')
0
```



## 热插拔功能

### `sim.setSimDet`

```python
sim.setSimDet(switch, triggerLevel)
```

SIM卡热插拔开关：用于设置SIM卡热插拔相关配置。

**参数描述：**

- `switch` - 开启或者关闭SIM卡热插拔功能，整型值，`0`：关闭 , `1`：打开。
- `triggerLevel` - 整型值，根据SIM卡实际的在位电平进行设置，如果SIM卡插入时在位电平为高则设置为1，如果为低设置为0。

**返回值描述：**

返回一个整型值，`0`表示成功，`-1`表示失败。



> BC25/EG810M系列不支持此方法。
>
> EC600M/EC800M中除了LA/LE/GA系列支持，其它系列均不支持此方法。
>
> EC600E/EC800E/EC600U/EC200U/EG912/EC800G系列设置成热插拔后掉电不保存。



**示例：**

```python
>>> import sim
>>> sim.setSimDet(1, 0)
0
```



### `sim.getSimDet`

```python
sim.getSimDet()
```

该方法用于获取SIM卡热插拔相关配置。


**返回值描述：**

成功： 返回元组数据，格式`(detenable, insertlevel)`，具体说明如下：

| 参数          | 类型 | 含义                                           |
| ------------- | ---- | ---------------------------------------------- |
| `detenable`   | 整型 | 开启或者关闭SIM卡热插拔功能，0：关闭 ，1：打开 |
| `insertlevel` | 整型 | 高低电平配置(0/1)                              |

失败： 返回`-1`。



>BC25/EG810M系列不支持此方法。
>
>EC600M/EC800M中除了LA/LE/GA系列支持，其它系列均不支持此方法。



**示例：**

```python
>>> import sim
>>> sim.getSimDet()
(1, 0)
```



## SIM卡切卡功能

### `sim.getCurSimid`

```python
sim.getCurSimid()
```

该方法用于获取当前卡的SIM卡卡槽编号(simId)。

**返回值描述：**

成功： 返回当前`simId`(`0`或`1`，分别表示`SIM1`或者`SIM2`)。

失败： 返回`-1`。



>支持该方法的模组：EC600M/EC800M/EC600E/EC800E系列。
>
>其中EC800MCNGA不支持该功能



**示例：**

```python
>>> import sim
>>> sim.getCurSimid()   #获取当前卡，当前是卡1
0
```



### `sim.switchCard`

```python
sim.switchCard(simId)
```

该方法用于sim卡切卡。

**参数描述：**

- `simId` - SIM卡卡槽编号，整型值，0表示SIM1，1表示SIM2。

**返回值描述：**

返回一个整型值，`0`表示成功，`-1`表示失败。



>支持该方法的模组：EC600M/EC800M/EC600E/EC800E系列。
>
>其中EC800MCNGA不支持该功能。



**示例：**

```python
>>> import sim
>>> sim.getCurSimid()  #获取当前卡，当前是卡1
0
>>> sim.switchCard(1)  #切到卡2
0
>>> sim.getCurSimid()  #获取当前卡，成功切到卡2
1
```



## 回调注册功能

### `sim.setCallback`

```python
sim.setCallback(usrFun)
```

热插拔注册监听回调函数：用于注册监听回调函数。在开启SIM卡热插拔功能的情况下，当SIM卡有插拔动作，将调用此方法注册的回调函数。

**参数描述：**

* `usrFun` - 回调函数名，回调函数格式以及回调函数的参数说明如下：

```python
def usrFun(args):
	pass
```

| 参数   | 类型 | 含义                                                      |
| ------ | ---- | --------------------------------------------------------- |
| `args` | 整型 | 当前SIM卡插拔状态：`1`  表示SIM卡插入；`2` 表示 SIM卡拔出 |

**返回值描述：**

返回一个整型值，`0`表示注册成功，`-1`表示注册失败。



> BC25/EG810M系列不支持此方法。
>
> EC600M/EC800M中除了LA/LE/GA系列支持，其它系列均不支持此方法。



**示例：**

```python
import sim

def usrCallback(args):
    simstates = args
    print('sim states:{}'.format(simstates))
    
sim.setCallback(usrCallback)
```



### `sim.setSwitchcardCallback`

```python
sim.setSwitchcardCallback(usrFun)
```

该方法用于注册监听SIM卡切卡状态回调函数：注册监听回调函数,响应SIM卡切卡动作。

**参数描述：**

* `usrFun` - 回调函数名，回调函数格式以及回调函数的参数说明如下：

```python
def usrFun(args):
	pass
```

| 参数 | 类型 | 含义                                                        |
| ---- | ---- | ----------------------------------------------------------- |
| args | 整型 | 切换SIM卡结果：`7` -表示切换SIM成功，`8`- 表示切换SIM卡失败 |

**返回值描述：**

返回一个整型值，`0`表示注册成功，`-1`表示注册失败。



> 支持该方法的模组：EC600M/EC800M/EC600E/EC800E系列。
>
> 注意以下几点：<br>1、目标卡不存在或者目标卡状态异常；<br>2、目标卡是当前卡；<br>以上情况切卡方法`sim.switchCard`直接返回-1，不触发此接口设置的回调函数。



**示例：**

```python
import sim

def usrCallback(args):
    switchcard_state = args
    print('sim switchcard states:{}'.format(switchcard_state))
    
sim.setSwitchcardCallback(usrCallback)
```
