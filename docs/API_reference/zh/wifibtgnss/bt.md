# bt - 经典蓝牙相关功能

`bt`模块提供经典蓝牙的相关功能，支持HFP、A2DP、AVRCP、SPP。

**示例**：

见github：https://github.com/QuecPython/example_BT

> 当前仅EC200U/EC600U/EG915U/EG912U型号支持`bt`功能。



## 初始化相关功能

### `bt.init`

```python
bt.init(user_cb)
```

蓝牙初始化并注册回调函数。

**参数描述：**

- `user_cb`-回调函数，类型为function。回调函数参数含义：args[0] 固定表示event_id，args[1] 固定表示状态，0表示成功，非0表示失败。回调函数的参数个数并不是固定2个，而是根据第一个参数args[0]来决定的，下表中列出了不同事件ID对应的参数个数及说明。

| event_id | 参数个数 | 参数说明                                                     |
| :------: | :------: | ------------------------------------------------------------ |
|    0     |    2     | args[0] ：event_id，表示 BT/BLE start 事件<br>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败 |
|    1     |    2     | args[0] ：event_id，表示 BT/BLE stop<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败 |
|    6     |    6     | args[0] ：event_id，表示 BT inquiry 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：rssi，搜索到的设备的信号强度；<br/>args[3] ：device_class <br/>args[4] ：device_name，设备名称，字符串类型<br/>args[5] ：addr，搜到的蓝牙设备的mac地址 |
|    7     |    3     | args[0] ：event_id，表示 BT inquiry end 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：end_status，0 - 正常结束搜索，8 - 强制结束搜索 |
|    14    |    4     | args[0] ：event_id，表示 BT spp recv 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：data_len，收到的数据长度<br/>args[3] ：data，收到的数据，bytearray类型数据 |
|    40    |    4     | args[0] ：event_id，表示 BT HFP connect 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_connect_status，表示hfp的连接状态；<br/>                 0 - 已经断开连接<br/>                 1 - 连接中<br/>                 2 - 已经连接<br/>                 3 - 断开连接中<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    41    |    4     | args[0] ：event_id，表示 BT HFP disconnect 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_connect_status，表示hfp的连接状态；<br/>                 0 - 已经断开连接<br/>                 1 - 连接中<br/>                 2 - 已经连接<br/>                 3 - 断开连接中<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    42    |    4     | args[0] ：event_id，表示 BT HFP call status 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_call_status，表示hfp的通话状态；<br/>                 0 - 当前没有正在进行的通话<br/>                 1 - 当前至少有一个正在进行的通话<br/> args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    43    |    4     | args[0] ：event_id，表示 BT HFP call setup status 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_call_setup_status，表示hfp的call setup状态；<br/>                 0 - 表示没有电话需要接通<br/>                 1 - 表示有一个拨进来的电话还未接通<br/>                 2 - 表示有一个拨出去的电话还没有接通<br/>                 3 - 表示拨出电话的蓝牙连接的另一方正在响铃<br/> args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    44    |    4     | args[0] ：event_id，表示 BT HFP network status 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_network_status，表示AG的网络状态；<br/>                 0 - 表示网络不可用<br/>                 1 - 表示网络正常<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    45    |    4     | args[0] ：event_id，表示 BT HFP network signal 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_network_signal，表示AG的信号，范围 0~5<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    46    |    4     | args[0] ：event_id，表示 BT HFP battery level 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_battery_level，表示AG端的电池电量，范围 0~5<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    47    |    4     | args[0] ：event_id，表示 BT HFP call held status 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_call_held_status，表示hfp的call held状态；<br/>                 0 - 表示没有保持呼叫<br/>                 1 - 表示呼叫被暂停或活动/保持呼叫交换<br/>                 2 - 表示呼叫暂停，没有活动呼叫<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    48    |    4     | args[0] ：event_id，表示 BT HFP audio status 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_audio_status，表示audio连接状态；<br/>                 0 - 表示audio已经断开连接<br/>                 1 - 表示audio正在连接中<br/>                 2 - 表示audio已经连接成功<br/>                 3 - 表示audio正在断开连接<br>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    49    |    4     | args[0] ：event_id，表示 BT HFP volume type 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_volume_type<br/>                 0 - 表示volume type为speaker<br/>                 1 - 表示volume type为microphone<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    50    |    4     | args[0] ：event_id，表示 BT HFP service type 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_service_type，表示当前AG的网络服务模式；<br/>                 0 - 表示AG当前为正常网络模式<br/>                 1 - 表示AG当前处于漫游模式<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    51    |    4     | args[0] ：event_id，表示 BT HFP ring 事件，即来电时响铃事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：当前无实际意义，保留<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    52    |    4     | args[0] ：event_id，表示 BT HFP codec type 事件，即编解码模式<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_codec_type，表示当前使用哪个编解码模式；<br/>                 1 - 表示 CVDS，采用8kHz采样率<br/>                 2 - 表示mSBC，采用16kHz采样率<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    61    |    4     | args[0] ：event_id，表示 BT SPP connect 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：spp_connect_status，表示spp的连接状态；<br/>                 0 - 已经断开连接<br/>                 1 - 连接中<br/>                 2 - 已经连接<br/>                 3 - 断开连接中<br/> args[3] ：addr，对端设备的mac地址，bytearray类型数据 |
|    62    |    4     | args[0] ：event_id，表示 BT SPP disconnect 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：spp_connect_status，表示spp的连接状态；<br/>                 0 - 已经断开连接<br/>                 1 - 连接中<br/>                 2 - 已经连接<br/>                 3 - 断开连接中<br/> args[3] ：addr，对端设备的mac地址，bytearray类型数据 |

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
def bt_callback(args):
	event_id = args[0]  # 第一个参数固定是 event_id
	status = args[1] # 第二个参数固定是状态,表示某个操作的执行结果是成功还是失败
	......
```

### `bt.release`

```python
bt.release()
```

蓝牙资源释放。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.start`

```python
bt.start()
```

开启蓝牙功能。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.stop`

```python
bt.stop()
```

关闭蓝牙功能。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.getStatus`

```python
bt.getStatus()
```

获取蓝牙的状态。

**返回值描述：**

蓝牙状态：类型为整型，0-蓝牙处于停止状态，1-蓝牙正常运行中，-1-获取状态失败。

### `bt.getLocalAddr`

```python
bt.getLocalAddr()
```

获取蓝牙地址。

**返回值描述：**

蓝牙地址：执行成功返回类型为bytearray的蓝牙地址，大小6字节，失败返回整型-1。

**示例**：

```python
>>> addr = bt.getLocalAddr()
>>> print(addr)
b'\xc7\xa13\xf8\xbf\x1a'
>>> mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
>>> print('mac = [{}]'.format(mac))
mac = [1a:bf:f8:33:a1:c7]
```



> 该接口需要在蓝牙已经初始化完成并启动成功后才能调用，比如在回调中收到 event_id 为0的事件之后，即 start 成功后，去调用。



### `bt.setLocalName`

```python
bt.setLocalName(code, name)
```

设置蓝牙名称。

**参数描述：**

- `code`-编码模式，类型为整型，0 - UTF8，1 - GBK。
- `name`-蓝牙名称，类型为string，最大长度22字节。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
>>> bt.setLocalName(0, 'QuecPython-BT')
0
```

### `bt.getLocalName`

```python
bt.getLocalName()
```

获取蓝牙名称。

**返回值描述：**

执行成功返回一个元组`(code, name)`，包含编码模式和蓝牙名称，失败返回整型-1。

**示例**：

```python
>>> bt.getLocalName()
(0, 'QuecPython-BT')
```

### `bt.setVisibleMode`

```python
bt.setVisibleMode(mode)
```

设置蓝牙可见模式，即做从机被扫描时，是否可被发现以及可被连接。

**参数描述：**

- `mode`-可见模式，类型为整型，具体含义如下表。

| 值   | 含义                     |
| ---- | ------------------------ |
| 0    | 不可被发现，不可被连接   |
| 1    | 可以被发现，但不可被连接 |
| 2    | 不可被发现，但可被连接   |
| 3    | 可以被发现，可被连接     |

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
>>> bt.setVisibleMode(3)
0
```

### `bt.getVisibleMode`

```python
bt.getVisibleMode()
```

获取蓝牙可见模式。

**返回值描述：**

执行成功返回蓝牙当前的可见模式值，失败返回整型-1。

**示例**：

```python
>>> bt.getVisibleMode()
3
```

### `bt.startInquiry`

```python
bt.startInquiry(mode)
```

开始搜索周边的蓝牙设备。

**参数描述：**

- `mode`-搜索类型。目前固定为15，表示搜索所有类型的设备。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
bt.startInquiry(15)
```

### `bt.cancelInquiry`

```python
bt.cancelInquiry()
```

取消搜索操作。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.setChannel`

```python
bt.setChannel(channel)
```

设置音频输出通道，使用场景为蓝牙接听电话或者播放音频时。

**参数描述：**

- `channel`-音频通道，类型为整型。0 - 听筒，1 - 耳机，2 - 喇叭。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.reconnect_set`

```python
bt.reconnect_set(max_count, period)
```

配置尝试重连的最大次数和相邻2次尝试重连的时间间隔，使用场景为模块和蓝牙设备距离拉远后断开连接时。

**参数描述：**

- `max_count`-尝试重连的最大次数，类型为整型，设置0则关闭自动重连功能。
- `period`-相邻2次尝试重连的时间间隔，单位秒，类型为整型。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
bt.reconnect_set(25, 2)#配置尝试重连的最大次数为25,每次尝试重连的间隔为2秒
```

### `bt.reconnect`

```python
bt.reconnect()
```

模组主动重连上次配对过的设备，如手机。使用场景为模组重启后重新初始化打开蓝牙、或者模组不重启仅关闭蓝牙再重新打开蓝牙。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

参考A2DP示例程序。见github：https://github.com/QuecPython/example_BT/blob/master/bt_a2dp_avrcp_demo.py

## HFP协议相关功能

提供蓝牙通话相关功能。

### `bt.hfpInit`

```python
bt.hfpInit()
```

HFP 功能初始化 。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.hfpRelease`

```python
bt.hfpRelease()
```

HFP 资源释放。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.hfpConnect`

```python
bt.hfpConnect(addr)
```

连接AG，建立HFP连接。

**参数描述：**

- `addr`-AG端蓝牙地址，6个字节，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.hfpDisonnect`

```python
bt.hfpDisonnect(addr)
```

断开HFP连接。

**参数描述：**

- `addr`-AG端蓝牙地址，6个字节，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.hfpSetVolume`

```python
bt.hfpSetVolume(addr, vol)
```

设置蓝牙通话时的音量。

**参数描述：**

- `addr`-AG端蓝牙地址，6个字节，类型为bytearray。
- `vol`-通话音量，类型为整型，范围 1-15。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.hfpRejectAfterAnswer`

```python
bt.hfpRejectAfterAnswer(addr)
```

挂断接通的电话。

**参数描述：**

- `addr`-AG端蓝牙地址，6个字节，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.hfpRejectCall`

```python
bt.hfpRejectCall(addr)
```

拒接电话。

**参数描述：**

- `addr`-AG端蓝牙地址，6个字节，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.hfpAnswerCall`

```python
bt.hfpAnswerCall(addr)
```

接听电话。

**参数描述：**

- `addr`-AG端蓝牙地址，6个字节，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.hfpEnableVR`

```python
bt.hfpEnableVR(addr)
```

开启语音助手。

**参数描述：**

- `addr`-AG端蓝牙地址，6个字节，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.hfpDisableVR`

```python
bt.hfpDisableVR(addr)
```

关闭语音助手。

**参数描述：**

- `addr`-AG端蓝牙地址，6个字节，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.hfpDisableVR`

```python
bt.hfpDisableVR(addr, cmd)
```

三方通话控制。

**参数描述：**

- `addr`-AG端蓝牙地址，6个字节，类型为bytearray。
- `cmd`-控制命令，类型为整型。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

## A2DP/AVRCP协议相关功能

提供蓝牙音乐相关功能。

### `bt.a2dpavrcpInit`

```python
bt.a2dpavrcpInit()
```

A2DP和AVRCP功能初始化。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.a2dpavrcpRelease`

```python
bt.a2dpavrcpRelease()
```

A2DP和AVRCP 资源释放。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.a2dpDisconnect`

```python
bt.a2dpDisconnect(addr)
```

断开A2DP连接。

**参数描述：**

- `addr`-A2DP主机蓝牙地址，6个字节，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.a2dpGetAddr`

```python
bt.a2dpGetAddr()
```

获取A2DP主机蓝牙地址。

**返回值描述：**

执行成功返回bytearray类型的A2DP主机蓝牙地址，6字节，失败返回整型-1。

### `bt.a2dpGetConnStatus`

```python
bt.a2dpGetConnStatus()
```

获取A2DP连接状态。

**返回值描述：**

A2DP连接状态，具体含义如下表。

| 值   | 类型 | 含义         |
| ---- | ---- | ------------ |
| -1   | int  | 获取失败     |
| 0    | int  | 连接已断开   |
| 1    | int  | 正在连接中   |
| 2    | int  | 已连接       |
| 3    | int  | 正在断开连接 |

### `bt.avrcpStart`

```python
bt.avrcpStart()
```

控制主机开始播放。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.avrcpPause`

```python
bt.avrcpPause()
```

控制主机停止播放。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.avrcpPrev`

```python
bt.avrcpPrev()
```

控制主机播放上一首。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.avrcpNext`

```python
bt.avrcpNext()
```

控制主机播放下一首。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.avrcpSetVolume`

```python
bt.avrcpSetVolume(vol)
```

设置主机播放音量。

**参数描述：**

- `vol`-播放音量，类型为整型，范围 0 - 11。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.avrcpGetVolume`

```python
bt.avrcpGetVolume()
```

获取主机播放音量。

**返回值描述：**

执行成功返回整形音量值，失败返回整型-1。

### `bt.avrcpGetPlayStatus`

```python
bt.avrcpGetPlayStatus()
```

获取主机播放状态。

**返回值描述：**

播放状态，具体含义如下表。

| 值   | 类型 | 说明           |
| ---- | ---- | -------------- |
| -1   | int  | 获取失败       |
| 0    | int  | 没有播放       |
| 1    | int  | 正在播放       |
| 2    | int  | 暂停播放       |
| 3    | int  | 正在切换下一首 |
| 4    | int  | 正在切换下一首 |

### `bt.avrcpGetConnStatus`

```python
bt.avrcpGetConnStatus()
```

通过AVRCP协议获取主机连接状态。

**返回值描述：**

连接状态，具体含义如下表。

| 值   | 类型 | 说明         |
| ---- | ---- | ------------ |
| -1   | int  | 获取失败     |
| 0    | int  | 连接已断开   |
| 1    | int  | 正在连接中   |
| 2    | int  | 已连接       |
| 3    | int  | 正在断开连接 |

## SPP协议相关功能

提供蓝牙传输相关功能。

### `bt.sppInit`

```python
bt.sppInit()
```

SPP 功能初始化。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.sppRelease`

```python
bt.sppRelease()
```

SPP 资源释放。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.sppConnect`

```python
bt.sppConnect(addr)
```

建立SPP连接。

**参数描述：**

- `addr`-蓝牙地址，类型为bytearray，6个字节。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.sppDisconnect`

```python
bt.sppDisconnect()
```

断开SPP连接。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `bt.sppSend`

```python
bt.sppSend(data)
```

通过SPP发送数据。

**参数描述：**

- `data`-待发送的数据，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

