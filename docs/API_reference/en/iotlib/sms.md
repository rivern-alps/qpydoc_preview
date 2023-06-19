# sms - SMS Related Feature

This feature provides methods of reading, sending and deleting SMS.



> BC25/EC600M series module does not support this feature.



## Send SMS

### `sms.sendTextMsg`

```
sms.sendTextMsg(phoneNumber, msg, codeMode)
```

Sends a text message (Empty messages are not supported). 

**Parameter**

* `phoneNumber` - String type. Phone number of the recipient. Length: up to 20 bytes.
* `msg` - String type. The message to be sent. Length of a single message: up to 140 bytes.
* `codeMode` - String type. SMS encoding mode.

| Value    | Description                              |
| -------- | ---------------------------------------- |
| `'GSM'`  | GSM 7-bit, used for English SMS.         |
| `'UCS2'` | UCS-2, used for Chinese and English SMS. |

**Return Value**

`0` - Successful execution

`-1` - Failed execution



> Only the following series modules support long messages.
>
> EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC800M/EG810M/EC200A series module supports six normal messages.
>
> EC200U/EC600U/EG912U/EC600G/EC800G series module supports four normal messages.



**Example**

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

Sends an SMS message in PDU mode (Empty messages are not supported). 

**Parameter**

* `phoneNumber` - String type. Phone number of the recipient. Length: up to 20 bytes.
* `msg` - String type. The message to be sent. Length of a single message: up to 140 bytes.
* `codeMode` - String type. SMS encoding mode.

| Value    | Description                              |
| -------- | ---------------------------------------- |
| `'GSM'`  | GSM 7-bit, used for English SMS.         |
| `'UCS2'` | UCS-2, used for Chinese and English SMS. |

**Return Value**

`0` - Successful execution

`-1` - Failed execution



> Only the following series modules support long messages.
>
> EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A series module supports six normal messages.
>
> EC200U/EC600U/EG912U/EC600G/EC800G series module supports four normal messages.



**Example**

```python
# -*- coding: UTF-8 -*-
import sms

sms.sendPduMsg('18158626517', 'send pdu msg by GSM mode.', 'GSM')
sms.sendPduMsg('18158626517', 'send pdu msg by UCS2 mode.', 'UCS2')
sms.sendPduMsg('18158626517', '这是一条中文测试短信！通过PDU-UCS2模式', 'UCS2')   
```



## Delete SMS

### `sms.deleteMsg`

```
sms.deleteMsg(index [, delmode])
```

Deletes the message for the specified index.

**Parameter**

* `index` - Integer type. The index number of the SMS message to be deleted.
* `delmode` - Integer type. Deletion mode. It is an optional parameter. Default value: 0.

| Value | Description                                      |
| ----- | ------------------------------------------------ |
| 0     | Delete the SMS message of the specified `index`. |
| 4     | Delete all SMS messages.                         |

**Return Value**

`0` - Successful execution

`-1` - Failed execution



> BC25/EC800G series module does not support `delmode`.



**Example**

```python
>>> import sms
>>> sms.deleteMsg(2)  # Delete the SMS message whose index number is 2.
0
>>> sms.deleteMsg(1,4)  #Delete all SMS messages.
0
```



## Set SMS Message Storage Location

### `sms.setSaveLoc`

```
sms.setSaveLoc(mem1, mem2, mem3)
```

Sets SMS message storage location.

**Parameter**

* `mem1` - String type. The storage location of messages to be read and deleted.

| Value  | Description        |
| ------ | ------------------ |
| `"SM"` | SIM card<br/>      |
| `"ME"` | Mobile device<br/> |
| `"MT"` | Not supported      |

* `mem2` - String type. The storage location of messages to be written and sent. See the detailed parameters in `mem1`.

* `mem3` - String type. The storage location of new messages. See the detailed parameters in `mem1`.

**Return Value**

`0` - Successful execution

`-1` - Failed execution



> The default SMS storage location of different modules varies. You can set the default SMS storage location based on your requirements.
>
> EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC800M/EG810M/EC200A series module must set mem2 and mem3 at the same time when changing the storage location of the received message.
>
> EC200U/EC600U/EG912U/EG915U/EC600G/EC800G series module only needs to set mem3.



**Example**

```python
>>> import sms
>>> sms.setSaveLoc('SM', 'SM', 'SM')
0
```



### `sms.getSaveLoc`

```
sms.getSaveLoc()
```

Gets SMS message storage location.

**Return Value**

A tuple`([loc1, current_nums, max_nums],[loc2, current_nums, max_nums],[loc3, current_nums, max_nums])` - Successful execution

| Parameter      | Type    | Description                                                  |
| -------------- | ------- | ------------------------------------------------------------ |
| `loc1`         | String  | The storage location of messages to be read and deleted, as the same as `mem1` in `sms.setSaveLoc`. |
| `loc2`         | String  | The storage location of messages to be written and sent, as the same as `mem2` in `sms.setSaveLoc`. |
| `loc3`         | String  | The storage location of new messages, as the same as `mem3` in `sms.setSaveLoc`. |
| `current_nums` | Integer | Current number of SMS messages.                              |
| `max_nums`     | Integer | The maximum number of SMS message storages.                  |

`-1` - Failed execution

**Example**

```python
>>> sms.getSaveLoc()
(['SM', 2, 50], ['SM', 2, 50], ['SM', 2, 50])
>>> sms.setSaveLoc('SM','ME','MT')
0
>>> sms.getSaveLoc()
(['SM', 2, 50], ['ME', 14, 180], ['MT', 2, 50])
```



## Get the Number of SMS Messages

### `sms.getMsgNums`

```
sms.getMsgNums()
```

Gets the number of SMS messages.

**Return Value**

The number of SMS messages - Successful execution

`-1` - Failed execution

**Example**

```python
>>> import sms
>>> sms.getMsgNums() # Please send an SMS message to the module before calling this method.
1
```



## Get SMS Content

### `sms.searchPduMsg`

```
sms.searchPduMsg(index)
```

Gets an SMS message content in PDU mode.

**Parameter**

* `index` - Integer type. The index number of the SMS message to be gotten. Range: `0 – MAX-1`. `MAX` is the maximum number of SMS messages stored by the module.

**Return Value**

Message content in PDU mode - Successful execution

The SMS message content includes the time when the SMS message is received. Therefore, the PDU data of the same SMS message content is different.

`-1` - Failed execution

**Example**

```python
>>> import sms
>>> sms.sendPduMsg('+8618226172342', '123456789aa', 'GSM') # Send an SMS message to yourself.
>>> sms.searchPduMsg(0) # Get the SMS message content in PDU mode. The text message content can be displayed normally only after it is decoded.
'0891683110305005F0240BA19169256015F70000022141013044230B31D98C56B3DD70B97018'
```



### `sms.searchTextMsg`

```
sms.searchTextMsg(index)
```

Gets a message content in text mode.

**Parameter**

* `index` - Integer type. The index number of the SMS message to be obtained. Range: `0 – MAX-1`. `MAX` is the maximum number of SMS messages stored by the module.

**Return Value**

A tuple`(phoneNumber， msg， msgLen)` - Successful execution 

| Parameter     | Type    | Description                                |
| ------------- | ------- | ------------------------------------------ |
| `phoneNumber` | String  | Phone number of the sender.                |
| `msg`         | String  | Message content.                           |
| `msgLen`      | Integer | Length of the message content. Unit: byte. |

`-1` - Failed execution

**Example**

```python
>>> import sms
>>> sms.sendPduMsg('+8618226172342', '123456789aa', 'GSM') # Send an SMS message to yourself.
>>> sms.searchTextMsg(0) # Get a message content in text mode.
('+8618226172342', '123456789aa', 22)
```



## Encode SMS Message in PDU Mode

### `sms.getPduLength`

```python
sms.getPduLength(pduMsg)
```

Gets the length of the specified SMS message in PDU mode.

**Parameter**

- `pduMsg` - String type. SMS message in PDU mode.

**Return Value**

Length of an SMS message in PDU mode - Successful execution

`-1` - Failed execution

**Example**

```python
>>> import sms
>>> sms.searchPduMsg(0)
'0891683108501505F0040D91688122162743F200000211529003332318C16030180C0683C16030180C0683E170381C0E87'
>>> sms.getPduLength(sms.searchPduMsg(0)) # Please note that the length of the message in PDU mode is obtained, not the length of the string above.
40
```



### `sms.decodePdu`

```python
sms.decodePdu(pduMsg, pduLen)
```

Encodes the SMS message in PDU mode read in `sms.searchPduMsg()`.

**Parameter**

- `pduMsg` - String type. The SMS message in PDU mode.

- `pduLen` - Integer type. Length of the SMS message in PDU mode.

**Return Value**

A tuple `(phoneNumber， msg， time， msgLen)` - Successful execution

| Parameter     | Type    | Description                        |
| ------------- | ------- | ---------------------------------- |
| `phoneNumber` | String  | Phone number of the sender         |
| `msg`         | String  | SMS message content                |
| `time`        | Integer | Time for receiving the SMS message |
| `msgLen`      | Integer | Length of the SMS message          |

`-1` - Failed execution

**Example**

```python
>>> import sms
>>>sms.decodePdu('0891683110305005F00405A10110F000081270319043442354516C76CA77ED4FE1FF1A00320030003200315E7496328303975E6CD596C68D445BA34F2067086D3B52A863D09192FF1A4E3B52A88FDC79BB975E6CD596C68D44FF0C5171540C5B8862A47F8E597D751F6D3B3002',20)
>>>('10010', '公益短信：2021年防范非法集资宣传月活动提醒：主动远离非法集资，共同守护美好生活。', '2021-07-13 09:34:44', 118)
```



## Set SMS Center Number

### `sms.getCenterAddr`

```python
sms.getCenterAddr()
```

Gets the SMS center number.


**Return Value**

SMS center number - Successful execution

`-1` - Failed execution

**Example**

```python
>>> import sms
>>> sms.getCenterAddr()
'+8613800551500'
# Some series modules may return values without +, such as EC600U series module.
>>> sms.getCenterAddr()
'8613800551500'
```



### `sms.setCenterAddr`

```python
sms.setCenterAddr(addr)
```

Sets the SMS center number (It is not recommended to change the SMS center number unless otherwise requested).

**Parameter**

- `addr` - String type. SMS center number to be set.


**Return Value**

`0` - Successful execution

`-1` - Failed execution



## Register Callback Function

### `sms.setCallback`

```python
sms.setCallback(usrFun)
```

Registers the callback function of receiving an SMS message.

**Parameter**

* `usrFun` - Callback function name. The callback function format and parameters are described below.

```python
def usrFun(args):
	pass
```

| Parameter | Type    | Description                  |
| --------- | ------- | ---------------------------- |
| `args[0]` | Integer | SIM card slot ID             |
| `args[1]` | Integer | SMS message index            |
| `args[2]` | String  | SMS message storage location |

**Return Value**

`0` - Successful execution

`-1` - Failed execution

**Example**

```python
# Example 1
import sms

def cb(args):
    index = args[1]
    storage = args[2]
    print('New message! storage:{},index:{}'.format(storage, index))
    
sms.setCallback(cb)

# Example 2
# Versions released before 2021-09-09 adopt different methods, as shown in the example 2.
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

