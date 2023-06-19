# sms - 短信功能

该模块提供短信功能相关方法，包括读取、发送、删除短信等方法。



> BC25/EC600M系列不支持此功能。



## 发送短信

### `sms.sendTextMsg`

```
sms.sendTextMsg(phoneNumber, msg, codeMode)
```

该方法用于发送TEXT类型的消息（不支持发送空短信）。

**参数描述：**

* `phoneNumber` - 接收方手机号码，字符串类型，最大长度不超过20字节。
* `msg` - 待发送消息，字符串类型，单条短信长度不超过140个字节。
* `codeMode` -使用的字符编码方式，字符串类型，取值范围如下：

| 值       | 含义                                           |
| -------- | ---------------------------------------------- |
| `'GSM'`  | GSM编码方式，用于发送英文短信                  |
| `'UCS2'` | UCS2编码方式，可以用于发送中文短信以及英文短信 |

**返回值描述：**

返回一个整型值，`0`表示发送成功，`-1`表示发送失败。



> 仅以下系列支持长短信：
>
> EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC800M/EG810M/EC200A系列支持6条正常短信长度；
>
> EC200U/EC600U/EG912U/EC600G/EC800G系列支持4条正常短信长度。



**示例：**

```python
# -*- coding: UTF-8 -*-
import sms

sms.sendTextMsg('18158626517', '这是一条中文测试短信！', 'UCS2')
sms.sendTextMsg('18158626517', 'Hello, world.', 'GSM')
sms.sendTextMsg('18158626517', '这是一条夹杂中文与英文的测试短信,hello world!', 'UCS2')
```



### `sms.sendPduMsg`

```
sms.sendPduMsg(phoneNumber, msg, codeMode)
```

该方法用于发送PDU类型的消息（不支持发送空短信）。

**参数描述：**

* `phoneNumber` - 接收方手机号码，字符串类型，最大长度不超过20字节。
* `msg` - 待发送消息，字符串类型，单条短信长度不超过140个字节。
* `codeMode` -使用的字符编码方式，字符串类型，取值范围如下：

| 值       | 含义                                           |
| -------- | ---------------------------------------------- |
| `'GSM'`  | GSM编码方式，用于发送英文短信                  |
| `'UCS2'` | UCS2编码方式，可以用于发送中文短信以及英文短信 |

**返回值描述：**

返回一个整型值，`0`表示发送成功，`-1`表示发送失败。



> 仅以下系列支持长短信：
>
> EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A系列支持6条正常短信长度；
>
> EC200U/EC600U/EG912U/EC600G/EC800G系列支持4条正常短信长度。



**示例：**

```python
# -*- coding: UTF-8 -*-
import sms

sms.sendPduMsg('18158626517', 'send pdu msg by GSM mode.', 'GSM')
sms.sendPduMsg('18158626517', 'send pdu msg by UCS2 mode.', 'UCS2')
sms.sendPduMsg('18158626517', '这是一条中文测试短信！通过PDU-UCS2模式', 'UCS2')   
```



## 删除短信

### `sms.deleteMsg`

```
sms.deleteMsg(index [, delmode])
```

该方法用于删除指定索引的消息。

**参数描述：**

* `index` - 索引号，整型值，需要删除短信的索引号。
* `delmode` - 模式，整型值，可选参数，当不写时默认为0，具体如下：

| 值   | 说明                      |
| ---- | ------------------------- |
| 0    | 删除指定`index`索引的短信 |
| 4    | 删除全部短信              |

**返回值描述：**

返回一个整型值，`0`表示删除成功，`-1`表示删除失败。



> BC25/EC800G不支持可选参数的使用



**示例：**

```python
>>> import sms
>>> sms.deleteMsg(2)  #删除索引号为2的那一条短信
0
>>> sms.deleteMsg(1,4)  #删除所有短信
0
```



## 短信存储位置配置

### `sms.setSaveLoc`

```
sms.setSaveLoc(mem1, mem2, mem3)
```

该方法用于设置短信的存储位置。

**参数描述：**

* `mem1` - 读取和删除消息所在的位置，字符串类型，支持如下参数:

| 值     | 含义                  |
| ------ | --------------------- |
| `"SM"` | SIM消息存储<br/>      |
| `"ME"` | 移动设备信息存储<br/> |
| `"MT"` | 暂不支持              |

* `mem2` - 写入和发送消息所在的位置，字符串类型，支持参数同上`mem1`的值。

* `mem3` - 接收消息的存储位置，字符串类型，支持参数同上`mem1`的值。

**返回值描述：**

返回一个整型值，`0`表示设置成功，`-1`表示设置失败。



> 不同系列短信默认存储空间有差异，用户根据自己的需求进行设置。
>
> EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC800M/EG810M/EC200A系列如果要改变接收消息的存储位置，需要同时设定mem2 & mem3；EC200U/EC600U/EG912U/EG915U/EC600G/EC800G系列只需设定mem3即可



**示例：**

```python
>>> import sms
>>> sms.setSaveLoc('SM', 'SM', 'SM')
0
```



### `sms.getSaveLoc`

```
sms.getSaveLoc()
```

该方法用于获取当前模块短信存储位置相关信息。

**返回值描述：**

成功： 返回元组数据,格式`([loc1, current_nums, max_nums],[loc2, current_nums, max_nums],[loc3, current_nums, max_nums])`,如下表：

| 参数           | 类型   | 含义                                                         |
| -------------- | ------ | ------------------------------------------------------------ |
| `loc1`         | 字符串 | 读取和删除消息所在的位置，具体含义同`sms.setSaveLoc`中`mem1`的值 |
| `loc2`         | 字符串 | 写入和发送消息所在的位置，具体含义同`sms.setSaveLoc`中`mem1`的值 |
| `loc3`         | 字符串 | 接收消息的存储位置，具体含义同`sms.setSaveLoc`中`mem1`的值   |
| `current_nums` | 整型   | 当前空间已有短信数量                                         |
| `max_nums`     | 整型   | 当前空间最大短信存储数量                                     |

失败：返回`-1`。

**示例：**

```python
>>> sms.getSaveLoc()
(['SM', 2, 50], ['SM', 2, 50], ['SM', 2, 50])
>>> sms.setSaveLoc('SM','ME','MT')
0
>>> sms.getSaveLoc()
(['SM', 2, 50], ['ME', 14, 180], ['MT', 2, 50])
```



## 获取短信的数量

### `sms.getMsgNums`

```
sms.getMsgNums()
```

该方法用于获取短信的数量。

**返回值描述：**

成功： 返回短信数量值。失败： 返回`-1`。

**示例：**

```python
>>> import sms
>>> sms.getMsgNums() # 执行本行前，先发送一条短信到模块
1
```



## 获取短信内容

### `sms.searchPduMsg`

```
sms.searchPduMsg(index)
```

该方法用于以PDU方式获取短信内容。

**参数描述：**

* `index` - 需要获取短信的索引，整型值，范围`0 ~ MAX-1`，`MAX`为模块存储短信的最大数量。

**返回值描述：**

成功： 返回字符串类型的PDU数据，为短信内容，包含收到短信的时间，所以相同短信内容的PDU数据是不同的。

失败： 返回整型`-1`。

**示例：**

```python
>>> import sms
>>> sms.sendPduMsg('+8618226172342', '123456789aa', 'GSM') # 自己给自己发送一条短信
>>> sms.searchPduMsg(0) # 以PDU方式获取短信内容，下面PDU格式短信需要解码后才能正常显示短信内容
'0891683110305005F0240BA19169256015F70000022141013044230B31D98C56B3DD70B97018'
```



### `sms.searchTextMsg`

```
sms.searchTextMsg(index)
```

该方法用于以TEXT方式获取短信内容。

**参数描述：**

* `index` - 需要获取短信的索引，整型值，范围`0 ~ MAX-1`，`MAX`为模块存储短信的最大数量。

**返回值描述：**

成功： 返回元组数据，格式`(phoneNumber， msg， msgLen)`，具体参数如下：

| 参数          | 类型   | 含义           |
| ------------- | ------ | -------------- |
| `phoneNumber` | 字符串 | 短信来源手机号 |
| `msg`         | 字符串 | 短信内容       |
| `msgLen`      | 整型   | 短信消息长度   |

失败： 返回整型值`-1`。

**示例：**

```python
>>> import sms
>>> sms.sendPduMsg('+8618226172342', '123456789aa', 'GSM') # 自己给自己发送一条短信
>>> sms.searchTextMsg(0) # 以TEXT方式获取短信内容
('+8618226172342', '123456789aa', 22)
```



## PDU短信解码

### `sms.getPduLength`

```python
sms.getPduLength(pduMsg)
```

该方法用于获取指定PDU短信的长度。

**参数描述：**

- `pduMsg` - PDU短信，字符串类型。

**返回值描述：**

成功： 返回PDU短信长度，整型值。

失败： 返回`-1`。

**示例：**

```python
>>> import sms
>>> sms.searchPduMsg(0)
'0891683108501505F0040D91688122162743F200000211529003332318C16030180C0683C16030180C0683E170381C0E87'
>>> sms.getPduLength(sms.searchPduMsg(0)) #注意，是获取PDU短信长度，不是上面字符串的长度
40
```



### `sms.decodePdu`

```python
sms.decodePdu(pduMsg, pduLen)
```

该方法用于PDU解码，解析`sms.searchPduMsg()`接口读取到的PDU数据。

**参数描述：**

- `pduMsg` - PDU短信，字符串类型。

- `pduLen` - PDU短信长度，整型值。

**返回值描述：**

成功： 返回元组数据，格式`(phoneNumber， msg， time， msgLen)`，具体参数如下:

| 参数          | 类型   | 含义           |
| ------------- | ------ | -------------- |
| `phoneNumber` | 字符串 | 短信来源手机号 |
| `msg`         | 字符串 | 短信内容       |
| `time`        | 整型   | 收到短信的时间 |
| `msgLen`      | 整型   | 短信消息长度   |

失败： 返回整型值`-1`。

**示例：**

```python
>>> import sms
>>>sms.decodePdu('0891683110305005F00405A10110F000081270319043442354516C76CA77ED4FE1FF1A00320030003200315E7496328303975E6CD596C68D445BA34F2067086D3B52A863D09192FF1A4E3B52A88FDC79BB975E6CD596C68D44FF0C5171540C5B8862A47F8E597D751F6D3B3002',20)
>>>('10010', '公益短信：2021年防范非法集资宣传月活动提醒：主动远离非法集资，共同守护美好生活。', '2021-07-13 09:34:44', 118)
```



## 短信中心号码配置

### `sms.getCenterAddr`

```python
sms.getCenterAddr()
```

该方法用于获取短信中心号码。


**返回值描述：**

成功： 返回字符串类型的短信中心号码。

失败： 返回整型值`-1`。

**示例：**

```python
>>> import sms
>>> sms.getCenterAddr()
'+8613800551500'
# 有些系列返回值中可能不带+，如EC600U系列：
>>> sms.getCenterAddr()
'8613800551500'
```



### `sms.setCenterAddr`

```python
sms.setCenterAddr(addr)
```

该方法用于设置短信中心号码。若无特殊需求，不建议更改短信中心号码。

**参数描述：**

- `addr` - 需要设置的短信中心号码，字符串类型。


**返回值描述：**

返回一个整型值，`0`表示设置成功，`-1`表示设置失败。



## 回调注册功能

### `sms.setCallback`

```python
sms.setCallback(usrFun)
```

该方法用于注册监听回调函数，当接收到短信时，调用此方法注册的回调函数。

**参数描述：**

* `usrFun` - 回调函数名，回调函数格式以及回调函数的参数说明如下：

```python
def usrFun(args):
	pass
```

| 参数      | 类型   | 参数说明             |
| --------- | ------ | -------------------- |
| `args[0]` | 整型   | 当前SIM卡卡槽的simId |
| `args[1]` | 整型   | 短信索引             |
| `args[2]` | 字符串 | 短信存储位置         |

**返回值描述：**

返回一个整型值，`0`表示设置成功，`-1`表示设置失败。

**示例：**

```python
# 示例一
import sms

def cb(args):
    index = args[1]
    storage = args[2]
    print('New message! storage:{},index:{}'.format(storage, index))
    
sms.setCallback(cb)

# 示例二
# 2021-09-09之前发布的版本使用方法不同，如下所示，参照示例二：
import sms

def cb(args):
    ind_flag = args[0]
	if ind_flag == 4097:
	    mes_buf, mes_len = args[1], args[2]
		print('New message! ind_flag:{},mes_buf:{},mes_len:{}'.format(ind_flag, mes_buf, mes_len))
    elif ind_flag == 4099:
	    mes_type, storage, index = args[1], args[2], args[3]
        print('New message! ind_flag:{},mes_type:{},storage:{},index:{}'.format(ind_flag, mes_type, storage, index))
	elif ind_flag == 4100:
	    mes_buf = args[1]
        print('New message! ind_flag:{},mes_buf:{}'.format(ind_flag, mes_buf))
	elif ind_flag == 4101:
		storage,index = args[1], args[2]
        print('New message! ind_flag:{},storage:{},index:{}'.format(ind_flag, storage, index))
    
sms.setCallback(cb)
```

