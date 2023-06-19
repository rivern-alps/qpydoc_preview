# voiceCall - 电话功能

该模块提供电话功能相关接口。



>* 支持voiceCall功能的模组：
>EC100Y系列：EC100YCN_AA
> EC200N系列：EC200NCN_AA/EC200NCN_AC/EC200NCN_LA
> EC600N系列：EC600NCN_AA/EC600NCN_LC/EC600NCN_LD/EC600NCN_LF
> EC600S系列：EC600SCN_LA
> EG912N系列：EG912NEN_AA
> EG915N系列：EG915NEU_AG
> EC200A系列：EC200AAU_HA/EC200ACN_DA/EC200ACN_HA/EC200ACN_LA/EC200AEU_HA
> EC200U系列：EC200UAU_AB/EC200UCN_AA/EC200UEU_AA/EC200UEU_AB
> EC600U系列：EC600CEU_AB/EG912UGL_AA/EG915UEU_AB
> BC25/EC600G/EC800G/BG95/BG77系列模组不支持voiceCall功能。
> * 其他系列模组需要定制版本才能支持voiceCall功能。



## 设置自动应答时间

### `voiceCall.setAutoAnswer`

```python
voiceCall.setAutoAnswer(seconds)
```

该方法用于设置自动应答时间。

**参数描述：** 

* `seconds` - 自动应答时间，整型值，单位/s，范围：0-255。

**返回值描述：**

  成功返回整型`0`，失败返回整型`-1`。

**示例：**

```python
>>> import voiceCall
>>> voiceCall.setAutoAnswer(5)
0
```



## 拨打电话

### `voiceCall.callStart`

```python
voiceCall.callStart(phonenum)
```

该方法用于主动拨打电话。

**参数描述：** 

* `phonenum` - 接收方电话号码，字符串类型。

**返回值描述：**

  成功返回整型`0`，失败返回整型`-1`。

**示例：**

```python
>>> import voiceCall
>>> voiceCall.callStart("13855169092")
0
```



## 接听电话

### `voiceCall.callAnswer`

```python
voiceCall.callAnswer()
```

该方法用于接听电话。

**返回值描述：**

  成功返回整型`0`，失败返回整型`-1`。

**示例：**

```python
>>> voiceCall.callAnswer()
0
```



## 挂断电话

### `voiceCall.callEnd`

```python
voiceCall.callEnd()
```

该方法用于挂断电话。

**返回值描述：**

  成功返回整型`0`，失败返回整型`-1`。

**示例：**

```python
>>> import voiceCall
>>> voiceCall.callEnd()
0
```



## 回调注册功能

### `voiceCall.setCallback`

```python
voiceCall.setCallback(voicecallFun)
```

该方法用于注册回调函数。监听不同的通话状态并通过回调反馈给用户。

**参数描述：**

* `voicecallFun` - 回调函数名，回调函数格式以及回调函数的参数说明如下：
```python
def voicecallFun(args):
	pass
```
`args[0]` - 通话状态，整型值，回调函数的参数个数并不是固定的，而是根据第一个参数`args[0]`来决定，如下表：

| 值   | 参数个数 | args[0]值说明                                 | 其他参数说明                                                 |
| ---- | -------- | --------------------------------------------- | ------------------------------------------------------------ |
| 1    | 1        | voicecall初始化成功（底层完成，无需用户干预） |                                                              |
| 2    | 3        | 来电通知，响铃                                | `args[1]`：呼叫识别号码<br>`args[2]`：电话号码               |
| 3    | 3        | 通话接通                                      | `args[1]`：呼叫识别号<br>`args[2]`：电话号码                 |
| 4    | 3        | 通话挂断                                      | `args[1]`：呼叫识别号码<br/>`args[2]`：通话挂断原因          |
| 5    | 1        | 未知错误                                      |                                                              |
| 6    | 5        | 呼叫等待                                      | `args[1]`：呼叫识别号码<br/>`args[2]`：电话号码<br/>`args[3]`：号码类型[129/145],129:非国际号码,145:国际号码<br/>`args[4]`：CLI状态 |
| 7    | 1        | 呼出中                                        |                                                              |
| 8    | 4        | 呼出失败                                      | `args[1]`：呼叫识别号码<br/>`args[2]`：呼叫失败原因<br/>`args[3]`：指示是否可以从网络端获得in-band tones |
| 9    | 3        | 等待                                          | `args[1]`：呼叫识别号码<br>`args[2]`：电话号码               |
| 10   | 8        | 来电通知，响铃（volte通话）                   | `args[1]`：呼叫识别号码<br/>`args[2]`：呼叫方向(MO/MT)<br/>`args[3]`：通话状态<br/>`args[4]`：业务类型(这里一般都是0，表示voice call，语音通话业务)<br/>`args[5]`：多方通话标志，0：非多方通话，1：多方通话<br/>`args[6]`：电话号码<br/>`args[7]`：号码类型[129/145],129:非国际号码,145:国际号码 |
| 11   | 8        | 通话接通（volte通话）                         | `args[1] ~ args[7]`：具体说明同上                            |
| 12   | 8        | 通话挂断（volte通话）                         | `args[1] ~ args[7]`：具体说明同上                            |
| 13   | 8        | 呼叫等待（volte通话）                         | `args[1] ~ args[7]`：具体说明同上                            |
| 14   | 8        | 呼出中（volte通话）                           | `args[1] ~ args[7]`：具体说明同上                            |
| 15   | 8        | 呼出中，对方未响铃（volte通话）               | `args[1] ~ args[7]`：具体说明同上                            |
| 16   | 8        | 等待（volte通话）                             | `args[1] ~ args[7]`：具体说明同上                            |

**返回值描述：**

注册成功返回整型`0`，失败返回整型`-1`。

**示例：**

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



>* 1、以上仅适用2021-09-09之后发布的支持语音通话的版本
>* 2、QPY_V0004_EC600N_CNLC_FW_VOLTE(2021-09-09发布)之前发布的版本都按照以下规则使用voiceCall



`args[0]` - 通话状态，整型值，参数个数及其他参数含义如下表：

| 值   | 参数个数 | args[0]值说明               | 其他参数说明                                                 |
| ---- | -------- | --------------------------- | ------------------------------------------------------------ |
| 4103 | 8        | 来电通知，响铃（volte通话） | `args[1]`：呼叫识别号码<br/>`args[2]`：呼叫方向(MO/MT)<br/>`args[3]`：通话状态<br/>`args[4]`：业务类型(这里一般都是0，表示voice call，语音通话业务)<br/>`args[5]`：多方通话标志，0：非多方通话 1：多方通话<br/>`args[6]`：电话号码<br/>`args[7]`：号码类型[129/145],129:非国际号码,145:国际号码 |
| 4104 | 8        | 通话接通（volte通话）       | `args[1] ~ args[7]`：具体说明同上                            |
| 4105 | 8        | 通话挂断（volte通话）       | `args[1] ~ args[7]`：具体说明同上                            |
| 4106 | 8        | 呼叫等待（volte通话）       | `args[1] ~ args[7]`：具体说明同上                            |

**示例：**

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



## 来电自动挂断功能

### `voiceCall.setAutoCancel`

```python
voiceCall.setAutoCancel(enable)
```

该方法用于使能来电自动挂断功能。

**参数描述：** 

* `enable` - 开启或者关闭来电自动挂断功能，`1`：开启，`0`：关闭 (默认不开启)。

**返回值描述：**

  成功返回整型`0`，失败返回整型`-1`。



>EC200AAU_HA/EC200ACN_DA/EC200ACN_HA/EC200ACN_LA/EC200AEU_HA系列模组支持该功能



**示例：**

```python
>>> import voiceCall
#手机呼叫模块，默认不会自动挂断
>>> voiceCall.getAutoCancelStatus()
0

#设置自动挂断功能，手机呼叫模块，默认自动挂断
>>> voiceCall.setAutoCancel(1)
0
>>> voiceCall.getAutoCancelStatus()
1
```



### `voiceCall.getAutoCancelStatus`

```python
voiceCall.getAutoCancelStatus()
```

该方法用于获取来电自动挂断使能状态。

**返回值描述：**

`0`：来电自动挂断使能关闭，来电不会被模组自动挂断。

`1`：来电自动挂断使能开启，来电会被模组自动挂断。

**示例：**

```python
>>> import voiceCall
#手机呼叫模块，默认不会自动挂断
>>> voiceCall.getAutoCancelStatus()
0

#设置自动挂断功能，手机呼叫模块，默认自动挂断
>>> voiceCall.setAutoCancel(1)
0
>>> voiceCall.getAutoCancelStatus()
1
```



## DTMF识别功能

### `voiceCall.startDtmf`

```python
voiceCall.startDtmf(dtmf, duration)
```

该方法用于设置DTMF音。

**参数描述：**

* `dtmf` - DTMF字符串，字符串类型，最大字符数：32个，有效字符数有：`0-9、A、B、C、D、*、#`。
* `duration` - 持续时间，整型值，范围：100-1000，单位：毫秒。

**返回值描述：**

  设置成功返回整型`0`，设置失败返回整型`-1`。



>该方法仅在语音通话过程中使用生效



**示例：**

```python
>>> import voiceCall
>>> voiceCall.startDtmf('A',100)
0
```



### `voiceCall.dtmfDetEnable`

```python
voiceCall.dtmfDetEnable(enable)
```

该方法用于使能DTMF识别功能，默认不开启DTMF识别。

**参数描述：**

* `enable` - 使能开关，整型值，取值`0/1`，`0`：不开启DTMF识别，`1`：开启DTMF识别。

**返回值描述：**

设置成功返回整型`0`，设置失败返回整型`-1`。



>支持voiceCall功能的模组型号中，EC600N/EC600S/EC800N/EG912N/EG915N系列支持该方法。



### `voiceCall.dtmfSetCb`

```python
voiceCall.dtmfSetCb(dtmfFun)
```

该方法用于注册DTMF识别功能的回调接口。

**参数描述：**

* `dtmfFun` - 回调函数名，回调函数格式以及回调函数的参数说明如下：

```Python
def dtmfFun(args):
	pass
```

| 参数    | 类型  | 含义                                       |
| ------- | ---- | ------------------------------------------ |
| `args` | 字符串 | 对端输入的DTMF字符                           |

**返回值描述：**

设置成功返回整型`0`，设置失败返回整型`-1`。



>支持voiceCall功能的模组型号中，EC600N/EC600S/EC800N/EG912N/EG915N系列支持该方法。



**示例：**

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
1   #手机端按下1，callback中会收到按下的字符“1”

8   #手机端按下8

9   #手机端按下9
```



## 设置呼叫转移

### `voiceCall.setFw`

```python
voiceCall.setFw(reason, fwmode, phonenum)
```

该方法用于控制呼叫转移补充业务。

**参数描述：**

* `reason` - 呼叫转移的条件，整型值，具体如下说明：

| 值 | 参数说明       |
| -- | ------------- |
| 0  | 无条件的 |
| 1  | 用户忙 |
| 2  | 用户无响应   |
| 3  | 用户不可达 |

* `fwMode` - 对呼叫转移的控制，整型值，具体如下说明：

| 值 | 参数说明       |
| -- | ------------- |
| 0  | 禁用 |
| 1  | 启用          |
| 2  | 查询状态       |
| 3  | 注册          |
| 4  | 擦除          |

* `phonenum` - 呼叫转移的目标电话，字符串类型

**返回值描述：**

设置成功返回整型`0`，设置失败返回整型`-1`。



## 切换语音通道

### `voiceCall.setChannel`

```python
voiceCall.setChannel(device)
```

该方法用于设置通话时的声音输出通道，默认是通道0，即听筒。

**参数描述：**

* `device` - 输出通道，整型值，具体如下说明：

| 值 | 参数说明       |
| -- | ------------- |
| 0  | 听筒 |
| 1  | 耳机          |
| 2  | 喇叭          |

**返回值描述：**

设置成功返回整型`0`，设置失败返回整型`-1`。

**示例：**

```python
>>> voiceCall.setChannel(2) #切换到喇叭通道
0
```



## 音量大小配置

### `voiceCall.getVolume`

```python
voiceCall.getVolume()
```

该方法用于获取电话当前音量大小。

**返回值描述：**

返回整型音量值。



### `voiceCall.setVolume`

```python
voiceCall.setVolume(volume)
```

该方法用于设置电话音量大小。

**参数描述:**

* `volume` - 音量等级，整型值，范围`（0 ~ 11）`，数值越大，音量越大。

**返回值描述：**

设置成功返回整型`0`，失败返回整型`-1`。



## 自动录音功能


### `voiceCall.setAutoRecord`

```python
voiceCall.setAutoRecord(enable, recordType, recordMode, filename)
```

该接口用于使能自动录音功能。默认关闭自动录音，自动录音使能需要在通话前设置完毕。

**参数描述：**

* `enable` - 使能开关，整型值，取值0或1，`0`：关闭自动录音功能 ，`1`：开启自动录音功能。
* `recordType` - 录音文件类型，整型值，具体如下：

| 值 | 说明 |
| -------------- | ---- |
| 0              | AMR  |
| 1              | WAV  |

* `recordMode` - 模式，整型值，具体如下：

| 值   |说明    |
|-----|--------|
| 0   | RX |
| 1   | TX    |
| 2   | MIX    |

* `filename` - 期望存储的文件名，字符串类型，需包含完整路径。

**返回值描述：**

设置成功返回整型`0`，设置失败返回整型`-1`， 不支持该接口返回字符串`"NOT SUPPORT"`。

**示例：**

```python
>>> voiceCall.setAutoRecord(1,0,2,'U:/test.amr')
0
```



### `voiceCall.startRecord`

```python
voiceCall.startRecord(recordType, recordMode, filename)
```

该方法用于开始通话录音。

**参数描述：**

* `recordType` - 录音文件类型，整型值，具体如下：

| 值   | 说明 |
|-----| ---- |
| 0   | AMR  |
| 1   | WAV  |

* `recordMode` - 模式，整型值，具体如下：

| 值    |说明    |
|------|--------|
| 0    | RX |
| 1    | TX    |
| 2    | MIX    |

* `filename` - 期望存储的文件名，字符串类型，需包含完整路径。

**返回值描述：**

设置成功返回整型`0`，设置失败返回整型`-1`，不支持该接口返回字符串`"NOT SUPPORT"`。

**示例：**

```python
>>> import voiceCall
>>> voiceCall.startRecord(0,2,'U:/test.amr')
0
```



### `voiceCall.stopRecord`

```python
voiceCall.stopRecord()
```

该方法用于停止通话录音。

**返回值描述：**

设置成功返回整型`0`，设置失败返回整型`-1`， 不支持该接口返回字符串`"NOT SUPPORT"`。

**示例：**

```python
>>> voiceCall.stopRecord()
0
```



### `voiceCall.readRecordStream`

```python
voiceCall.readRecordStream(readBuf, bufLen)
```

该方法用于读取录音流数据。

**参数描述：**

* `readBuf` - 存储读取到的数据，用于保存读取到的数据。

* `bufLen` - 期望读取的字符串长度（不能超过readBuf申请的字节长度）。

**返回值描述：**

读取成功返回读取到的数据长度，读取失败返回整型`-1`，不支持该接口返回字符串`"NOT SUPPORT"`。



>* 录音流第一包数据均是对应格式文件的文件头
>* wav格式录音流第一包数据不包含文件大小，需结束录音后自行计算



### `voiceCall.startRecordStream`

```python
voiceCall.startRecordStream(recordType, recordMode, callbackFun)
```

该方法用于开始通话录音（流形式）。

**参数描述：**

* `recordType` - 录音文件类型，整型值，具体如下：

| 值     | 说明 |
|-------| ---- |
| 0     | AMR  |
| 1     | WAV  |

* `recordMode` - 模式，整型值，具体如下：

| 值    |说明    |
|------|--------|
| 0    | RX |
| 1    | TX    |
| 2    | MIX    |

* `callbackFun` - 回调函数名，回调函数格式以及回调函数的参数说明如下：
```python
def recordStreamCallback(args):
	pass
```
| 参数    | 类型  | 含义                  |
| ------- | ---- | -------------------- |
| `args[0]` | 字符串  | 录音流数据       |
| `args[1]` | 整型 | 录音流数据长度 |
| `args[2]` | 整型 | 录音状态<br/>-1：录音出错<br/>0：开始录音<br/>1：返回录音数据<br/>2：录音暂停<br/>3：录音结束<br/>4：空间满 |

**返回值描述：**

设置成功返回整型`0`，设置失败返回整型`-1`，不支持该接口返回字符串`"NOT SUPPORT"`。



>* 录音流第一包数据均是对应格式文件的文件头
>* wav格式录音流第一包数据不包含文件大小，需结束录音后自行计算



**示例：**

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
# 此处挂断电话(MO/MT侧挂断都可以)
>>> uos.listdir('usr')
['system_config.json', 'mia.amr']
>>> aud=audio.Audio(0)
>>> aud.setVolume(11)
0
>>> aud.play(2,1,'U:/mia.amr')
0
```