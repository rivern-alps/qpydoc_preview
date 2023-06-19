# sim - SIM Card Related Features

This feature provides you with the SIM Card APIs, such as the methods of getting SIM card status, ICCID, IMSI and the phone number.

> The IMSI, ICCID, and phone number can be gotten only when the SIM card status is 1. You can call *sim.getstatus()* to get the current SIM card status.



## Access Generic SIM Features

### `sim.genericAccess`

```
sim.genericAccess(simId, cmd)
```

Accesses generic SIM features to send CSIM commands and interact with SIM cards.

**Parameter**

* `simId` - Integer type. SIM card slot ID. 0 - SIM card 0. 1- SIM card 1. Only 0 is supported now.
* `cmd` - String type. The command passed by the mobile terminal to the SIM in the format described in GSM 51.011.

**Return Value**

A tuple `(len，data)` - Successful execution

`len` - Integer type. Length of `data`.

`data` - String type. The data content returned.

`-1` - Failed execution



> Only EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N series module supports this method.



**Example**

```python
>>> import sim
>>> sim.genericAccess(0,'80F2000016')
(48, '623E8202782183027FF08410A0000000871002FF86FF9000')
```



## Get SIM Card Information

### `sim.getImsi`

```python
sim.getImsi()
```

Gets the IMSI number of the SIM card.

**Return Value**

`IMSI` - Successful execution

`-1` - Failed execution

**Example**

```python
>>> import sim
>>> sim.getImsi()
'460105466870381'
```



### `sim.getIccid`

```python
sim.getIccid()
```

Gets the ICCID number of the SIM card.

**Return Value**

`ICCID` - Successful execution

`-1` - Failed execution

**Example**

```python
>>> import sim
>>> sim.getIccid()
'89860390845513443049'
```



### `sim.getPhoneNumber`

```python
sim.getPhoneNumber()
```

Gets the phone number of the SIM card. The phone number of the SIM card must be written into the module first.

**Return Value**

`Phone number` - Successful execution

`-1` - Failed execution

>BC25 series module does not support this method.



**Example**

```python
>>> import sim
>>> sim.getPhoneNumber()
'+8618166328752'
```



## Get SIM Card Status

### `sim.getStatus`

```python
sim.getStatus()
```

Gets the current SIM card status.

**Return Value**

String type. SIM card status codes, as described in details below.

| Code | Description                                                  |
| ---- | ------------------------------------------------------------ |
| 0    | The SIM card does not exist/has been removed.                |
| 1    | The SIM card is ready.                                       |
| 2    | The SIM card has been blocked and waiting for CHV1 password. |
| 3    | The SIM card has been blocked and needs to be unblocked with CHV1 password. |
| 4    | The SIM card has been blocked due to failed SIM/USIM personalized check. |
| 5    | The SIM card is blocked due to an incorrect PCK. An MEP unblocking password is required. |
| 6    | Expecting key for hidden phone book entries                  |
| 7    | Expecting code to unblock the hidden key                     |
| 8    | The SIM card has been blocked and waiting for CHV2 password. |
| 9    | The SIM card has been blocked and needs to be unblocked with CHV2 password. |
| 10   | The SIM card has been blocked due to failed network personalization check. |
| 11   | The SIM card is blocked due to an incorrect NCK. An MEP unblocking password is required. |
| 12   | The SIM card has been blocked due to failed personalization check of network lock. |
| 13   | The SIM card is blocked due to an incorrect NSCK. An MEP unblocking password is required. |
| 14   | The SIM card has been blocked due to failed personalization check of the service provider. |
| 15   | The SIM card is blocked due to an incorrect SPCK. An MEP unblocking password is required. |
| 16   | The SIM card has been blocked due to failed enterprise personalization check. |
| 17   | The SIM card is blocked due to an incorrect CCK. An MEP unblocking password is required. |
| 18   | The SIM card is being initialized and waiting for completion. |
| 19   | The SIM card is blocked for the following six reasons. <br />1) Use of CHV1 is blocked. <br />2) Use of CHV2 is blocked. <br />3) Use of the universal PIN is blocked. <br/>4) Use of code to unblock the CHV1 is blocked.<br/>5) Use of code to unblock the CHV2 is blocked. <br/>6) Use of code to unblock the universal PIN is blocked. |
| 20   | The SIM card is invalid.                                     |
| 21   | Unknown status.                                              |



## PIN Code Verification

### `sim.enablePin`

```python
sim.enablePin(pin)
```

Enables PIN verification. Once this method is called to enable the PIN verification, you need to enter the correct PIN code for verification. Only when the PIN code is verified successfully will the SIM card can be used normally. Please note that you have at most 3 attempts. The SIM card will be locked and must be unblocked with the PUK code after three consecutive failures. 

**Parameter**

- `pin` - String type. PIN code. Default value: ‘1234’. The value contains a maximum of 15 digits.

**Return Value**

`0` -  Successful execution

`-1` - Failed execution

**Example**

```python
>>> sim.enablePin("1234")
0
```



### `sim.disablePin`

```python
sim.disablePin(pin)
```

Disables PIN code verification.

**Parameter**

- `pin` - String type. PIN code. Default value: ‘1234’. The value contains a maximum of 15 digits.

**Return Value**

`0` -  Successful execution

`-1` - Failed execution

**Example**

```python
>>> import sim
>>> sim.disablePin("1234")
0
```



### `sim.verifyPin`

```python
sim.verifyPin(pin)
```

Verifies PIN code. After the PIN code verification is enabled, if you need to use the SIM card, you can call this method to temporarily make the SIM card work normally, and this method needs to be called again for verification next time when the module is powered on (Or you can call *sim.disablePin(pin)* to disable the PIN verification, then the PIN verification will not be required when the module is powered on again).

**Parameter**

- `pin` - String type. PIN code. Default value: ‘1234’. Length: up to 15 digits.

**Return Value**

`0` -  Successful execution

`-1` - Failed execution

**Example**

```python
>>> import sim
>>> sim.verifyPin("1234")
0
```



### `sim.changePin`

```python
sim.changePin(oldPin, newPin)
```

Changes the PIN code

**Parameter**

- `oldPin` - String type. The old PIN code, with a maximum length of 15 digits. 
- `newPin` - String type. The new PIN code, with a maximum length of 15 digits. 

**Return Value**

`0` -  Successful execution

`-1` - Failed execution

**Example**

```python
>>> import sim
>>> sim.changePin("1234", "4321")
0
```



## Unblock SIM Card

### `sim.unblockPin`

```python
sim.unblockPin(puk, newPin)
```

Unblocks the SIM card. When you enter incorrect PIN codes three times, you need to enter the PUK code to unblock the SIM card. If incorrect PUK codes are entered ten times, the SIM card will be permanently locked and automatically scrapped. 

**Parameter**

- `puk` - String type. PUK code. Length: 8 to 15 digits.
- `newPin` - String type. New PIN code. Length: up to 15 digits.

**Return Value**

`0` -  Successful execution

`-1` - Failed execution

**Example**

```python
>>> import sim
>>> sim.unblockPin("12345678", "0000")
0
```



## Phone Book

### `sim.readPhonebook`

```python
sim.readPhonebook(storage, start, end, username)
```

Reads the phone book to get one or more phone number records from the phone book at the specified storage location.

**Parameter**

- `storage` - Integer type. Storage location of the phone numbers, as described below.

| Value | Description |
| ----- | ----------- |
| 0     | DC          |
| 1     | EN          |
| 2     | FD          |
| 3     | LD          |
| 4     | MC          |
| 5     | ME          |
| 6     | MT          |
| 7     | ON          |
| 8     | RC          |
| 9     | SM          |
| 10    | AP          |
| 11    | MBDN        |
| 12    | MN          |
| 13    | SDN         |
| 14    | ICI         |
| 15    | OCI         |

- `start` - Integer type. The start number of the phone number record to be read. `start` equaling 0 indicates that no number is used to obtain the phone number. `start` must be less than or equal to `end`.
- `end` - Integer type. The end number of the phone number record to be read.  The condition that must be met:  `end - start <= 20`.
- `username` - String type. The username of a phone number. This parameter is valid when `start` equals  0. Chinese characters are not supported currently. Length: up to 30 bytes.

**Return Value**

A tuple `(record_number, [(index, username, phone_number), ... , (index, username, phone_number)])` - Successful execution

The parameters are described below.

| Parameter       | Type    | Description                              |
| --------------- | ------- | ---------------------------------------- |
| `record_number` | Integer | The number of phone number records read. |
| `index`         | Integer | Index of the number in the phone book.   |
| `username`      | String  | Username of the phone number.            |
| `phone_number`  | String  | Phone number.                            |

`-1` - Failed execution



>- EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600MCNLE/EC600MCNLA/EC800MCNLA/EC800MCNLE/EC800MCNGA/EG810M/EC200A series module supports this method.
>
>- When you match a phone number record by username, you do not need to enter a full word. As long as there is an existing record in the phone book whose name starts with the username, the name will be matched with the phone number.



**Example**

```python
>>> import sim
>>> sim.readPhonebook(9, 1, 4, "")
(4,[(1,'Tom','15544272539'),(2,'Pony','15544272539'),(3,'Jay','18144786859'),(4,'Pondy','15544282538')])
>>> sim.readPhonebook(9, 0, 0, "Tom")
(1, [(1, 'Tom', '18144786859')])
>>> sim.readPhonebook(9, 0, 0, "Pony")
(1, [(2, 'Pony', '17744444444')])
>>> sim.readPhonebook(9, 0, 0, "Pon") #Note: Any name that contains'pon' will be matched.
(2, [(2, 'Pony', '17744444444'),(4,'Pondy','15544282538')])
```



### `sim.writePhonebook`

```python
sim.writePhonebook(storage, index, username, number)
```

Writes phone book, that is, write a phone record to the specified storage location.

**Parameter**

- `storage` - Integer type. Storage location of the phone numbers. For details, see `storage` of `sim.readPhonebook`.

- `index` - Integer type. Index of the number in the phone book. Range: `1 – 500`.
- `username` - String type. The username of a phone number. Chinese characters are not supported currently. Length: up to 30 bytes.
- `number` - String type. Phone number. Length: up to 20 bytes.

**Return Value**

`0` - Successful execution

`-1`-  Failed execution



> EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600MCNLE/EC600MCNLA/EC800MCNLA/EC800MCNLE/EC800MCNGA/EG810M/EC200A series module supports this method.



**Example**

```python
>>> import sim
>>> sim.writePhonebook(9, 1, 'Tom', '18144786859')
0
```



## Hot Swap

### `sim.setSimDet`

```python
sim.setSimDet(switch, triggerLevel)
```

Sets the hot-swap-related features of the SIM card.

**Parameter**

- `switch` - Integer type. Enable or disable the hot swap feature of the SIM card. 

  `0` - Disable

   `1` - Enable

- `triggerLevel` - Integer type. This parameter is set according to the actual level of the SIM card. If the present level is high when the SIM card is inserted, this parameter should be set to 1. If the present level is low, this parameter should be set to 0.

**Return Value**

`0` - Successful execution

`-1` - Failed execution



> BC25 series module does not support this method.



**Example**

```python
>>> import sim
>>> sim.setSimDet(1, 0)
0
```



### `sim.getSimDet`

```python
sim.getSimDet()
```

Gets the hot-swap-related settings of the SIM card.

**Return Value**

A tuple `(detenable, insertlevel)` - Successful execution

The parameters are described below.

| Parameter     | Type    | Description                                                  |
| ------------- | ------- | ------------------------------------------------------------ |
| `detenable`   | Integer | Enable or disable the hot swap feature of the SIM card. 0 - Disable; 1 - Enable. |
| `insertlevel` | Integer | High level or low level (0/1).                               |

`-1` - Failed execution



>BC25 series module does not support this method.



**Example**

```python
>>> import sim
>>> sim.getSimDet()
(1, 0)
```



## Switch SIM Card

### `sim.getCurSimid`

```python
sim.getCurSimid()
```

Gets the SIM card slot ID of the current SIM card.

**Return Value**

`simId` - Successful execution

`0` - `SIM1`

`1` - `SIM2`

`-1` - Failed execution



>EC600M/EC800M series module supports this method.



**Example**

```python
>>> import sim
>>> sim.getCurSimid()   #Gets the current SIM card ID. 0 indicates SIM card 1.
0
```



### `sim.switchCard`

```python
sim.switchCard(simId)
```

Switches the SIM card.

**Parameter**

- `simId` - Integer type. SIM card slot ID. 

  `0` - `SIM1`

  `1` - `SIM2`

**Return Value**

`0` - Successful execution

`-1` - Failed execution



>EC600M/EC800M series module supports this method.



**Example**

```python
>>> import sim
>>> sim.getCurSimid()  #Gets the current SIM card ID. 0 indicates the current SIM card is SIM 1.
0
>>> sim.switchCard(1)  #Switches to SIM 2.
0
>>> sim.getCurSimid()  #Gets the current SIM card ID. 1 indicates the current SIM card is SIM 2.
1
```



## Register Callback Function

### `sim.setCallback`

```python
sim.setCallback(usrFun)
```

Registers the callback function of hot swap features. When the hot-swap feature is enabled, the callback function registered by this method will be called when the SIM card is inserted or removed.

**Parameter**

* `usrFun` - Callback function name. The callback function format and parameters are described below.

```python
def usrFun(args):
	pass
```

| Parameter | Type    | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ |
| `args`    | Integer | Current status of The SIM card.<br />`1` - The SIM card is inserted. <br />`2` - The SIM card is removed. |

**Return Value**

`0` - Successful execution

`-1` - Failed execution

> BC25 series module does not support this method.



**Example**

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

Registers the callback function of SIM card switch status to respond to the SIM card switch operation.

**Parameter**

* `usrFun` - Callback function name. The callback function format and parameters are described below.

```python
def usrFun(args):
	pass
```

| Parameter | Type    | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ |
| args      | Integer | The result of SIM switch.<br />`7` - Successful switch<br />`8` -  Failed switch |

**Return Value**

`0` - Successful execution
`-1` - Failed execution

> EC600M/EC800M series module supports this method.
>
> Note<br>1. The target SIM card does not exist or is in an abnormal status.<br>2. The target SIM card is the current SIM card.<br>When the two situations mentioned above occur, -1 will be returned when `sim.switchCard` is called, and the callback function registered by this method will not be called. 



**Example**

```python
import sim

def usrCallback(args):
    switchcard_state = args
    print('sim switchcard states:{}'.format(switchcard_state))
    
sim.setSwitchcardCallback(usrCallback)
```
