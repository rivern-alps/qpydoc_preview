# voiceCall - Voice Call

This feature provides voice call APIs.



>* The modules supporting voice call are listed below.
>EC100Y series: EC100YCN_AA
> EC200N series: EC200NCN_AA/EC200NCN_AC/EC200NCN_LA
> EC600N series: EC600NCN_AA/EC600NCN_LC/EC600NCN_LD/EC600NCN_LF
> EC600S series: EC600SCN_LA
> EG912N series: EG912NEN_AA
> EG915N series: EG915NEU_AG
> EC200A series: EC200AAU_HA/EC200ACN_DA/EC200ACN_HA/EC200ACN_LA/EC200AEU_HA
> EC200U series: EC200UAU_AB/EC200UCN_AA/EC200UEU_AA/EC200UEU_AB
> EC600U series: EC600CEU_AB/EG912UGL_AA/EG915UEU_AB
> * BC25/EC600G/EC800G/BG95/BG77 series module does not support voice call.
> * For other modules,  a custom version is required to support voice call.



## Set Automatic Answering Time

### `voiceCall.setAutoAnswer`

```python
voiceCall.setAutoAnswer(seconds)
```

Sets automatic answering time of a voice call.

**Parameter** 

* `seconds` - Integer type. Automatic answering time of a voice call. Range: 0–255. Unit: s.

**Return Value**

  `0` - Successful execution

`-1` - Failed execution

**Example**

```python
>>> import voiceCall
>>> voiceCall.setAutoAnswer(5)
0
```



## Dial Voice Call

### `voiceCall.callStart`

```python
voiceCall.callStart(phonenum)
```

Dials a voice call.

**Parameter** 

* `phonenum` - String type. Phone number of the recipient. 

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution

**Example**

```python
>>> import voiceCall
>>> voiceCall.callStart("13855169092")
0
```



## Answer Voice Call

### `voiceCall.callAnswer`

```python
voiceCall.callAnswer()
```

Answers a voice call.

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution

**Example**

```python
>>> voiceCall.callAnswer()
0
```



## End Voice Call

### `voiceCall.callEnd`

```python
voiceCall.callEnd()
```

Ends a voice call.

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution

**Example**

```python
>>> import voiceCall
>>> voiceCall.callEnd()
0
```



## Register Callback Function

### `voiceCall.setCallback`

```python
voiceCall.setCallback(voicecallFun)
```

Registers the callback function of different voice call statuses.

**Parameter**

* `voicecallFun` - Callback function name. The callback function format and parameters are described below.
```python
def voicecallFun(args):
	pass
```
`args[0]` - Integer type. Voice call status. The number of parameters to the callback function is not fixed but is determined by the first parameter `args[0]`, as shown in the following table.

| Value | Number of Parameters | args[0] Description                                          | Description of Other Parameters                              |
| ----- | -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1     | 1                    | Voice call is initialized (The process is completed in the bottom layer with no user intervention. |                                                              |
| 2     | 3                    | Incoming call alert, ringing                                 | `args[1]`: Caller ID<br>`args[2]`: Phone number              |
| 3     | 3                    | Connected                                                    | `args[1]`: Caller ID<br>`args[2]`: Phone number              |
| 4     | 3                    | Disconnected                                                 | `args[1]`: Caller ID<br/>`args[2]`: Call disconnection reason |
| 5     | 1                    | Unknown error                                                |                                                              |
| 6     | 5                    | Call waiting                                                 | `args[1]`: Caller ID<br/>`args[2]`: Phone number<br/>`args[3]`: Phone number type [129/145].<br />129 - Unknown type<br />145 - International type<br/>`args[4]`: CLI status |
| 7     | 1                    | Dialing                                                      |                                                              |
| 8     | 4                    | Dialing failed                                               | `args[1]`: Caller ID<br/>`args[2]`: Dialing failure reason<br/>`args[3]`: Indicator that whether in-band tones can be obtained from the network side |
| 9     | 3                    | Waiting                                                      | `args[1]`: Caller ID<br>`args[2]`: Phone number              |
| 10    | 8                    | Incoming call alert, ringing  (VoLTE call)                   | `args[1]`: Caller ID<br/>`args[2]`: Call direction (MO/MT)<br/>`args[3]`: Call status<br/>`args[4]`: Business type (Generally, this value is 0, indicating voice call)<br/>`args[5]`: Flag of MTPY<br />0 - Non-MTPY<br />1 - MTPY<br/>`args[6]`: Phone number<br/>`args[7]`: Phone number type [129/145].<br />129 - Unknown type<br />145 - International type |
| 11    | 8                    | Connected (VoLTE call)                                       | `args[1] – args[7]`: Same as above for specific description  |
| 12    | 8                    | Disconnected (VoLTE call)                                    | `args[1] – args[7]`: Same as above for specific description  |
| 13    | 8                    | Call waiting (VoLTE call)                                    | `args[1] – args[7]`: Same as above for specific description  |
| 14    | 8                    | Dialing (VoLTE call)                                         | `args[1] – args[7]`: Same as above for specific description  |
| 15    | 8                    | Dialing with no ring on the other party (VoLTE call)         | `args[1] – args[7]`: Same as above for specific description  |
| 16    | 8                    | Waiting (VoLTE call)                                         | `args[1] – args[7]`: Same as above for specific description  |

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution

**Example**

```python
>>> import voiceCall
def voice_callback(args):
     if args[0] == 10:
         print('voicecall incoming call, PhoneNO: ', args[6])
     elif args[0] == 11:
	     print('voicecall connected, PhoneNO: ', args[6])
     elif args[0] == 12:
	     print('voicecall disconnect')
	 elif args[0] == 13:
	     print('voicecall is waiting, PhoneNO: ', args[6])
     elif args[0] == 14:
         print('voicecall dialing, PhoneNO: ', args[6])
     elif args[0] == 15:
	     print('voicecall alerting, PhoneNO: ', args[6])
     elif args[0] == 16:
	     print('voicecall holding, PhoneNO: ', args[6])
     
>>> voiceCall.setCallback(voice_callback)
0
>>> voiceCall.callStart('10086')
0
```



>* 1. The above information only applies to versions released after 2021-09-09 that support voice call.
>* 2. Versions released before QPY_V0004_EC600N_CNLC_FW_VOLTE (released on 2021-09-09) use voice calls according to the following rules.



`args[0]` - Integer type. Voice call status. The number of parameters and the meanings of other parameters are described below.

| Value | Number of Parameters | args[0] Description                        | Description of Other Parameters                              |
| ----- | -------------------- | ------------------------------------------ | ------------------------------------------------------------ |
| 4103  | 8                    | Incoming call alert, ringing  (VoLTE call) | `args[1]`: Caller ID<br/>`args[2]`: Call direction (MO/MT)<br/>`args[3]`: Call status<br/>`args[4]`: Business type (Generally, this value is 0, indicating voice call)<br/>`args[5]`: Flag of MTPT<br />0 - Non-MTPT<br />1 - MTPT<br/>`args[6]`: Phone number<br/>`args[7]`: Phone number type [129/145].<br />129 - Unknown type<br />145 - International type |
| 4104  | 8                    | Connected (VoLTE call)                     | `args[1] – args[7]`: Same as above for specific description  |
| 4105  | 8                    | Disconnected (VoLTE call)                  | `args[1] – args[7]`: Same as above for specific description  |
| 4106  | 8                    | Call waiting (VoLTE call)                  | `args[1] – args[7]`: Same as above for specific description  |

**Example**

```python
>>> import voiceCall
def voice_callback(args):
	if args[0] == 4106:
		print('voicecall is waiting')
	elif args[0] == 4105:
		print('voicecall disconnect')
	elif args[0] == 4104:
		print('voicecall connected, CallNO: ', args[6])
	elif args[0] == 4103:
		print('voicecall incoming call, PhoneNO: ', args[6])
```



## Auto Hang-up

### `voiceCall.setAutoCancel`

```python
voiceCall.setAutoCancel(enable)
```

Enables auto hang-up when receiving calls.

**Parameter** 

* `enable` - Enable or disable auto hang-up when receiving calls.

  `0` -Disable (default)

  `1` - Enable

  

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution



>EC200AAU_HA/EC200ACN_DA/EC200ACN_HA/EC200ACN_LA/EC200AEU_HA series module supports this method.



**Example**

```python
>>> import voiceCall
# When you call the module on your phone, the module will not hang up by default.
>>> voiceCall.getAutoCancelStatus()
0

# Enable auto hang-up. When you call the module on your phone, the module will hang up by default.
>>> voiceCall.setAutoCancel(1)
0
>>> voiceCall.getAutoCancelStatus()
1
```



### `voiceCall.getAutoCancelStatus`

```python
voiceCall.getAutoCancelStatus()
```

Gets the enablement status of auto hang-up.

**Return Value**

`0`: Auto hang-up is disabled

`1`: Auto hang-up is enabled

**Example**

```python
>>> import voiceCall
# When you call the module on your phone, the module will not hang up by default.
>>> voiceCall.getAutoCancelStatus()
0

# Enable auto hang-up. When you call the module on your phone, the module will hang up by default.
>>> voiceCall.setAutoCancel(1)
0
>>> voiceCall.getAutoCancelStatus()
1
```



## Detect DTMF

### `voiceCall.startDtmf`

```python
voiceCall.startDtmf(dtmf, duration)
```

Sets DTMF tone.

**Parameter**

* `dtmf` - String type. DTMF symbols. Valid symbols:`0-9, A, B, C, D, * and #`. Maximum number of characters: 32.
* `duration` - Integer type. Duration. Range: 100–1000. Unit: ms.

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution



>This method takes effect only during a voice call.



**Example**

```python
>>> import voiceCall
>>> voiceCall.startDtmf('A',100)
0
```



### `voiceCall.dtmfDetEnable`

```python
voiceCall.dtmfDetEnable(enable)
```

Enables the feature of DTMF detection. DTMF detection is disabled by default.

**Parameter**

* `enable` - Integer type. Enable or disable DTMF detection. 

  `0` - Disable DTMF detection

  `1` - Enable DTMF detection

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution



>EC600N/EC600S/EC800N/EG912N/EG915N series module supports this method.



### `voiceCall.dtmfSetCb`

```python
voiceCall.dtmfSetCb(dtmfFun)
```

Registers the callback function of DTMF detection.

**Parameter**

* `dtmfFun` - Callback function name. The callback function format and parameters are described below.

```Python
def dtmfFun(args):
	pass
```

| Parameter | Type | Description                            |
| ------- | ---- | ------------------------------------------ |
| `args` | String | DTMF characters entered by the peer end. |

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution



>EC600N/EC600S/EC800N/EG912N/EG915N series module supports this method.



**Example**

```python
>>> import voiceCall
>>> def cb(args):
... print(args)

>>> voiceCall.dtmfSetCb(cb)
0
>>> voiceCall.dtmfDetEnable(1)
0
>>> voiceCall.callStart('13855169092')
0
>>>
1   # If you press 1 on your phone, the pressed character "1" will be received by the callback function.

8   # If you press 8 on your phone, the pressed character "8" will be received by the callback function.

9   # If you press 9 on your phone, the pressed character "9" will be received by the callback function.
```



## Set Up Call Forwarding

### `voiceCall.setFw`

```python
voiceCall.setFw(reason, fwmode, phonenum)
```

Sets up call forwarding.

**Parameter**

* `reason` - Integer type. Call forwarding conditions, as described below.

| Value | Description |
| -- | ------------- |
| 0  | Unconditional |
| 1  | Busy |
| 2  | No reply |
| 3  | Not reachable |

* `fwMode` - Integer type. Call forwarding operations, as described below.

| Value | Description |
| -- | ------------- |
| 0  | Deactivate call forwarding. |
| 1  | Activate call forwarding. |
| 2  | Query call forwarding status. |
| 3  | Register call forwarding. |
| 4  | Erase call forwarding. |

* `phonenum` - String type. The number to which calls are forwarded.

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution



## Switch Voice Channel

### `voiceCall.setChannel`

```python
voiceCall.setChannel(device)
```

Sets the voice output channel during a call. Default value: 0 (handset).

**Parameter**

* `device` - Integer type. Output channel, as described below.

| Value | Description |
| -- | ------------- |
| 0  | Handset |
| 1  | Headset    |
| 2  | Loudspeaker |

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution

**Example**

```python
>>> voiceCall.setChannel(2) # Switch to loudspeaker channel.
0
```



## Set Call Volume

### `voiceCall.getVolume`

```python
voiceCall.getVolume()
```

Gets the current call volume.

**Return Value**

Integer type. Volume.



### `voiceCall.setVolume`

```python
voiceCall.setVolume(volume)
```

Sets call volume.

**Parameter**

* `volume` - Integer type. Volume. Range: `0–11`. The higher the value, the higher the volume.

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution



## Automatic Recording


### `voiceCall.setAutoRecord`

```python
voiceCall.setAutoRecord(enable, recordType, recordMode, filename)
```

Enables automatic recording. Automatic recording is disabled by default. The automatic recording must be enabled before the call.

**Parameter**

* `enable` - Integer type. Enable or disable automatic recording.

  `0` - Disable

  `1` - Enable

* `recordType` - Integer type. Recording file type, as described below.

| Value | Description |
| -------------- | ---- |
| 0              | AMR  |
| 1              | WAV  |

* `recordMode` - Integer type. Mode, as described below.

| Value |Description    |
|-----|--------|
| 0   | RX |
| 1   | TX    |
| 2   | MIX    |

* `filename` - String type. The desired file name, which must contain the full path.

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution

`"NOT SUPPORT"` - The interface is not supported.

**Example**

```python
>>> voiceCall.setAutoRecord(1,0,2,'U:/test.amr')
0
```



### `voiceCall.startRecord`

```python
voiceCall.startRecord(recordType, recordMode, filename)
```

Starts recording the call.

**Parameter**

* `recordType` - Integer type. Recording file type, as described below.

| Value | Description |
| ----- | ----------- |
| 0     | AMR         |
| 1     | WAV         |

* `recordMode` - Integer type. Mode, as described below.

| Value |Description    |
|------|--------|
| 0    | RX |
| 1    | TX    |
| 2    | MIX    |

* `filename` - String type. The desired file name, which must contain the full path.

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution

`"NOT SUPPORT"` - The interface is not supported.

**Example**

```python
>>> import voiceCall
>>> voiceCall.startRecord(0,2,'U:/test.amr')
0
```



### `voiceCall.stopRecord`

```python
voiceCall.stopRecord()
```

Stops recording the call.

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution

`"NOT SUPPORT"` - The interface is not supported.

**Example**

```python
>>> voiceCall.stopRecord()
0
```



### `voiceCall.readRecordStream`

```python
voiceCall.readRecordStream(readBuf, bufLen)
```

Reads recording data stream. 

**Parameter**

* `readBuf` - Buffer used to save the data read.

* `bufLen` - Length of the string to be read, which cannot be longer than the data length requested by  `readBuf`.

**Return Value**

Length of the data read - Successful execution

`-1` - Failed execution

`"NOT SUPPORT"` - The interface is not supported.



>* The first packet of data in the recording stream is the header of the file in the corresponding format.
>* The first packet of recording streams in WAV format does not contain the file size. You need to calculate the file size after the recording is complete.



### `voiceCall.startRecordStream`

```python
voiceCall.startRecordStream(recordType, recordMode, callbackFun)
```

Starts recording the call in stream format.

**Parameter**

* `recordType` - Integer type. Recording file type, as described below.

| Value | Description |
| ----- | ----------- |
| 0     | AMR         |
| 1     | WAV         |

* `recordMode` - Integer type. Mode, as described below.

| Value |Description    |
|------|--------|
| 0    | RX |
| 1    | TX    |
| 2    | MIX    |

* `callbackFun` - Callback function name. The callback function format and parameters are described below.
```python
def recordStreamCallback(args):
	pass
```
| Parameter | Type | Description       |
| ------- | ---- | -------------------- |
| `args[0]` | String | Recording data stream |
| `args[1]` | Integer | Length of the recording data stream. |
| `args[2]` | Integer | Recording status<br/>-1: Recording error<br/>0: Start recording<br/>1: Return recording data<br/>2: Stop recording<br/>3: Recording ends<br/>4: No remaining space. |

**Return Value**

  `0` - Successful execution  

`-1` - Failed execution

`"NOT SUPPORT"` - The interface is not supported.



>* The first packet of data in the recording stream is the header of the file in the corresponding format.
>* The first packet of recording streams in WAV format does not contain the file size. You need to calculate the file size after the recording is completed.



**Example**

```python
>>> import voiceCall
>>> import audio

>>> f=open('usr/mia.amr','w')

>>> def cb(para):
...     if(para[2] == 1):
...         read_buf = bytearray(para[1])
...         voiceCall.readRecordStream(read_buf,para[1])
...         f.write(read_buf,para[1])
...         del read_buf
...     elif(para[2] == 3):
...         f.close()
...         
>>> voiceCall.callStart('13855169092')
0
>>> voiceCall.startRecordStream(0,2,cb)
0
# Hang up. Either MO or MT hangs up.
>>> uos.listdir('usr')
['system_config.json', 'mia.amr']
>>> aud=audio.Audio(0)
>>> aud.setVolume(11)
0
>>> aud.play(2,1,'U:/mia.amr')
0
```