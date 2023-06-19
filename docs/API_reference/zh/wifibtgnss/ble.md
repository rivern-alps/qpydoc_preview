# ble-低功耗蓝牙相关功能

`ble`模块用于提供BLE GATT Server （从机）与 Client （主机）功能，基于BLE 4.2协议。

**示例**：

见github：https://github.com/QuecPython/example_BLE

> 当前仅EC200U/EC600U/EG915U/EG912U型号支持`ble`功能。



## 初始化相关功能

### `ble.gattStart`

```python
ble.gattStart()
```

开启 BLE GATT 功能。

**返回值描述：**

- 执行成功返回整型0，失败返回整型-1。

### `ble.gattStop`

```python
ble.gattStop()
```

关闭 BLE GATT 功能。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.getStatus`

```python
ble.getStatus()
```

获取 BLE 的状态。

**返回值描述：**

0 - BLE处于停止状态。1 - BLE处于开启状态。-1 - 获取状态失败。

### `ble.getPublicAddr`

```python
ble.getPublicAddr()
```

获取 BLE 协议栈正在使用的公共地址。该接口需要在BLE已经初始化完成并启动成功后才能调用，比如在回调中收到 event_id 为0的事件之后，即 start 成功后，去调用。

**返回值描述：**

执行成功返回bytearray类型的BLE地址，大小6个byte，失败返回整型-1。

**示例**：

```python
>>> addr = ble.getPublicAddr()
>>> print(addr)
b'\xdb3\xf5\x1ek\xac'
>>> mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
>>> print('mac = [{}]'.format(mac))
mac = [ac:6b:1e:f5:33:db]
```



> 如果有出厂设置默认蓝牙MAC地址，那么该接口获取的MAC地址和默认的蓝牙MAC地址是一致的；如果没有设置，那么该接口获取的地址，将是蓝牙启动后随机生成的静态地址，因此在每次重新上电运行蓝牙功能时都不相同。



## BLE Server相关功能

### `ble.serverInit`

```python
ble.serverInit(user_cb)
```

初始化 BLE Server 并注册回调函数。

**参数描述：**

- `user_cb`-回调函数，类型为function。回调函数参数含义：args[0] 固定表示event_id，args[1]固定 表示状态，0表示成功，非0表示失败。回调函数的参数个数并不是固定2个，而是根据第一个参数args[0]来决定的，下表中列出了不同事件ID对应的参数个数及说明。

| event_id | 参数个数 | 参数说明                                                     |
| :------: | :------: | ------------------------------------------------------------ |
|    0     |    2     | args[0] ：event_id，表示 BT/BLE start<br>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    1     |    2     | args[0] ：event_id，表示 BT/BLE stop<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    16    |    4     | args[0] ：event_id，表示 BLE connect<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id<br/>args[3] ：addr，BT/BLE address，bytearray类型数据 |
|    17    |    4     | args[0] ：event_id，表示 BLE disconnect<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id，<br/>args[3] ：addr，BT/BLE address，bytearray类型数据 |
|    18    |    7     | args[0] ：event_id，表示 BLE update connection parameter<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id<br/>args[3] ：max_interval，最大的间隔，间隔：1.25ms，取值范围：6-3200，时间范围：7.5ms\ ~ 4s<br/>args[4] ：min_interval，最小的间隔，间隔：1.25ms，取值范围：6-3200，时间范围：7.5ms\ ~ 4s<br/>args[5] ：latency，从机忽略连接状态事件的时间。需满足：（1+latecy)\*max_interval\*2\*1.25<timeout\*10<br/>args[6] ：timeout，没有交互，超时断开时间，间隔：10ms，取值范围：10-3200ms，时间范围：100ms ~ 32s |
|    20    |    4     | args[0] ：event_id，表示 BLE connection mtu<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：handle<br/>args[3] ：mtu值 |
|    21    |    7     | args[0] ：event_id，表示 client写入特征值或描述符通知<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，获取数据的长度<br/>args[3] ：data，一个数组，存放获取的数据<br/>args[4] ：attr_handle，属性句柄，整型值<br/>args[5] ：short_uuid，整型值<br/>args[6] ：long_uuid，一个16字节数组，存放长UUID |
|    22    |    7     | args[0] ：event_id，表示client读取特征值或描述符通知 <br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，获取数据的长度<br/>args[3] ：data，一个数组，存放获取的数据<br/>args[4] ：attr_handle，属性句柄，整型值<br/>args[5] ：short_uuid，整型值<br/>args[6] ：long_uuid，一个16字节数组，存放长UUID |
|    25    |    2     | args[0] ：event_id，表示 server发送通知并接收到了发送结束通知<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
def ble_callback(args):
    event_id = args[0]
    status = args[1]
    print('[ble_callback]: event_id={}, status={}'.format(event_id, status))

    if event_id == 0:  # ble start
        if status == 0:
            print('[callback] BLE start success.')
        else:
            print('[callback] BLE start failed.')
    elif event_id == 1:  # ble stop
        if status == 0:
            print('[callback] ble stop successful.')
        else:
            print('[callback] ble stop failed.')
    elif event_id == 16:  # ble connect
        if status == 0:
            print('[callback] ble connect successful.')
            connect_id = args[2]
            addr = args[3] # 这是一个bytearray类型
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))
        else:
            print('[callback] ble connect failed.')
    elif event_id == 17:  # ble disconnect
        if status == 0:
            print('[callback] ble disconnect successful.')
            connect_id = args[2]
            addr = args[3] # 这是一个bytearray类型
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))
        else:
            print('[callback] ble disconnect failed.')
            ble.gattStop()
            return
    elif event_id == 18:  # ble update connection parameter
        if status == 0:
            print('[callback] ble update parameter successful.')
            connect_id = args[2]
            max_interval = args[3]
            min_interval = args[4]
            latency = args[5]
            timeout = args[6]
            print('[callback] connect_id={},max_interval={},min_interval={},latency={},timeout={}'.format(connect_id, max_interval, min_interval, latency, timeout))
        else:
            print('[callback] ble update parameter failed.')
            ble.gattStop()
            return
    elif event_id == 20:  # ble connection mtu
        if status == 0:
            print('[callback] ble connect mtu successful.')
            handle = args[2]
            ble_mtu = args[3]
            print('[callback] handle = {:#06x}, ble_mtu = {}'.format(handle, ble_mtu))
        else:
            print('[callback] ble connect mtu failed.')
            ble.gattStop()
            return
    elif event_id == 21:  # server:when ble client write characteristic value or descriptor,server get the notice
        if status == 0:
            print('[callback] ble recv successful.')
            data_len = args[2]
            data = args[3]  # 这是一个bytearray类型
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # 这是一个bytearray类型
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv failed.')
            ble.gattStop()
            return
    elif event_id == 22:  # server:when ble client read characteristic value or descriptor,server get the notice
        if status == 0:
            print('[callback] ble recv read successful.')
            data_len = args[2]
            data = args[3]  # 这是一个bytearray类型
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # 这是一个bytearray类型
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv read failed.')
            ble.gattStop()
            return
    elif event_id == 25:  # server send notification,and recieve send end notice
        if status == 0:
            print('[callback] ble send data successful.')
        else:
            print('[callback] ble send data failed.')
    else:
        print('unknown event id.')

ble.serverInit(ble_callback)
```

### `ble.serverRelease`

```python
ble.serverRelease()
```

BLE Server 资源释放。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.setLocalName`

```python
ble.setLocalName(code, name)
```

设置 BLE 名称。

**参数描述：**

- `code`-编码模式，类型为整型。0 - UTF8，1 - GBK。
- `name`-编码模式，类型为string。BLE 名称，名称最长不能超过29个字节。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
>>> ble.setLocalName(0, 'QuecPython-BLE')
0
```



> 对于BLE，设备在广播时，如果希望手机扫描app扫描时，能看到广播设备的名称，是需要在广播数据中包含蓝牙名称的，或者在扫描回复数据中包含设备名称。



### `ble.setAdvParam`

```python
ble.setAdvParam(min_adv,max_adv,adv_type,addr_type,channel,filter_policy,discov_mode,no_br_edr,enable_adv)
```

设置广播参数。

**参数描述：**

- `min_adv`-最小广播间隔，范围0x0020-0x4000。计算方式：时间间隔 = min_adv \* 0.625，单位ms。类型为整型。
- `max_adv`-最大广播间隔，范围0x0020-0x4000。计算方式：时间间隔 = max_adv \* 0.625，单位ms。类型为整型。
- `adv_type`-广播类型，0 - 可连接的非定向广播，默认选择，1 - 可连接高占空比的定向广播，2 - 可扫描的非定向广播，3 - 不可连接的非定向广播，4 - 可连接低占空比的定向广播。类型为整型。
- `addr_type`-本地地址类型，0 - 公共地址，1 - 随机地址。类型为整型。
- `channel`-广播通道，1 - 37信道，2 - 38信道，4 - 39信道，7 - 上述3个通道都选择，默认该选项。类型为整型。
- `filter_policy`-广播过滤策略，0 - 处理所有设备的扫描和连接请求，1 - 处理所有设备的连接请求和只处理白名单设备的扫描请求（暂不支持），2 - 处理所有设备的扫描请求和只处理白名单设备的连接请求（暂不支持），3 - 只处理白名单设备的连接和扫描请求（暂不支持）。类型为整型。
- `discov_mode`-发现模式，GAP协议使用，1 - 有限可发现模式，2 - 一般可发现模式。类型为整型。
- `no_br_edr`-不用BR/EDR，1-不用BR/EDR，默认为该值，0-使用BR/EDR。类型为整型。
- enable_adv-使能广播，1-使能，默认为该值，0-不使能。类型为整型。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
def ble_gatt_set_param():
    min_adv = 0x300
    max_adv = 0x320
    adv_type = 0  # 可连接的非定向广播,默认选择
    addr_type = 0  # 公共地址
    channel = 0x07
    filter_strategy = 0  # 处理所有设备的扫描和连接请求
    discov_mode = 2
    no_br_edr = 1
    enable_adv = 1
    ret = ble.setAdvParam(min_adv, max_adv, adv_type, addr_type, channel, filter_strategy, discov_mode, no_br_edr, enable_adv)
    if ret != 0:
        print('ble_gatt_set_param failed.')
        return -1
    print('ble_gatt_set_param success.')
    return 0
```

### `ble.setAdvData`

```python
ble.setAdvData(data)
```

设置广播数据内容。

**参数描述：**

- `data`-广播数据，最长不超过31个字节，类型为bytearray。广播数据的内容，采用 length+type+data 的格式。一条广播数据中可以包含多个这种格式数据的组合，如下示例中包含了两个数据组合，第一个是 "0x02, 0x01, 0x05"，0x02表示后面有两个数据，分别是0x01和0x05，0x01即type，0x05表示具体数据；第二个是ble名称数据组合， length为ble名称长度加1、type为0x09，具体数据为name对应的具体编码值。关于type具体值代表的含义，请参考蓝牙协议官方标准文档。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
def ble_gatt_set_data():
    adv_data = [0x02, 0x01, 0x05]
    ble_name = "Quectel_ble"
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvData(data)
    if ret != 0:
        print('ble_gatt_set_data failed.')
        return -1
    print('ble_gatt_set_data success.')
    return 0
```

### `ble.setAdvRspData`

```python
ble.setAdvRspData(data)
```

设置扫描回复数据。

**参数描述：**

- `data`-扫描回复数据，最长不超过31个字节，类型为bytearray。 格式和上面设置广播数据内容接口一致。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
def ble_gatt_set_rsp_data():
    adv_data = []
    ble_name = "Quectel_ble"
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_rsp_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvRspData(data)
    if ret != 0:
        print('ble_gatt_set_rsp_data failed.')
        return -1
    print('ble_gatt_set_rsp_data success.')
    return 0
```



> 当client设备扫描方式为积极扫描时，设置扫描回复数据才有意义。



### `ble.addService`

```python
ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)
```

增加一个服务。

**参数描述：**

- `primary`-服务类型，1表示主要服务，其他值表示次要服务，类型为整型。
- `server_id`-服务ID，用来确定某一个服务，类型为整型。 
- `uuid_type`-uuid类型，0 - 长UUID，128bit；1 - 短UUID，16bit。类型为整型。 
- `uuid_s`-短UUID，2个字节（16bit），类型为整型，当uuid_type为0时，该值给0。
- `uuid_l`-长UUID，16个字节（128bit），类型为bytearray，当uuid_type为1时，该值填 bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])。 

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
def ble_gatt_add_service():
    primary = 1
    server_id = 0x01
    uuid_type = 1  # 短UUID
    uuid_s = 0x180F
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_service failed.')
        return -1
    print('ble_gatt_add_service success.')
    return 0
```

### `ble.addChara`

```python
ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)
```

在服务里增加一个特征。

**参数描述：**

- `server_id`-服务ID，用来确定某一个服务，类型为整型。
- `chara_id`-特征ID，类型为整型。 
- `chara_prop`-特征的属性，十六进制数，可通过“或运算”同时指定多个属性，值具体含义如下表，类型为整型。 

| 值   | 含义                          |
| ---- | ----------------------------- |
| 0x01 | 广播                          |
| 0x02 | 可读                          |
| 0x04 | 0x04 - 可写且不需要链路层应答 |
| 0x08 | 可写                          |
| 0x10 | 通知                          |
| 0x20 | 指示                          |
| 0x40 | 认证签名写                    |
| 0x80 | 扩展属性                      |

- `uuid_type`-uuid类型，0 - 长UUID，128bit；1 - 短UUID，16bit。类型为整型。
- `uuid_s`-短UUID，2个字节（16bit），类型为整型，当uuid_type为0时，该值给0。
- `uuid_l`-长UUID，16个字节（128bit），类型为bytearray，当uuid_type为1时，该值填 bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])。 

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
def ble_gatt_add_characteristic():
    server_id = 0x01
    chara_id = 0x01
    chara_prop = 0x02 | 0x10 | 0x20  # 0x02-可读 0x10-通知 0x20-指示
    uuid_type = 1  # 短UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_characteristic failed.')
        return -1
    print('ble_gatt_add_characteristic success.')
    return 0
```

### `ble.addCharaValue`

```python
ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
```

在特征里增加一个特征值。

**参数描述：**

- `server_id`-服务ID，用来确定某一个服务，类型为整型。
- `chara_id`-特征ID，类型为整型。 
- `permission`-特征值的权限，2个字节，十六进制数，可通过“或运算”同时指定多个属性，值具体含义如下表，类型为整型。 

| 值     | 含义           |
| ------ | -------------- |
| 0x0001 | 可读权限       |
| 0x0002 | 可写权限       |
| 0x0004 | 读需要认证     |
| 0x0008 | 读需要授权     |
| 0x0010 | 读需要加密     |
| 0x0020 | 读需要授权认证 |
| 0x0040 | 写需要认证     |
| 0x0080 | 写需要授权     |
| 0x0100 | 写需要加密     |
| 0x0200 | 写需要授权认证 |

- `uuid_type`-uuid类型，0 - 长UUID，128bit；1 - 短UUID，16bit。类型为整型。
- `uuid_s`-短UUID，2个字节（16bit），类型为整型，当uuid_type为0时，该值给0。
- `uuid_l`-长UUID，16个字节（128bit），类型为bytearray，当uuid_type为1时，该值填 bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])。 
- `value`-特征值数据。类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
def ble_gatt_add_characteristic_value():
    data = []
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # 短UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    for i in range(0, 244):
        data.append(0x00)
    value = bytearray(data)
    ret = ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_value failed.')
        return -1
    print('ble_gatt_add_characteristic_value success.')
    return 0
```

### `ble.changeCharaValue`

```python
ble.changeCharaValue(server_id, chara_id, value)
```

修改特征值。

**参数描述：**

- `server_id`-服务ID，用来确定某一个服务，类型为整型。
- `chara_id`-特征ID，类型为整型。  

- `value`-特征值数据。类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.addCharaDesc`

```python
ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
```

在特征里增加一个特征描述，注意特征描述和特征值同属与一个特征。

**参数描述：**

- `server_id`-服务ID，用来确定某一个服务，类型为整型。
- `chara_id`-特征ID，类型为整型。 
- `permission`-特征值的权限，2个字节，十六进制数，可通过“或运算”同时指定多个属性，值具体含义如下表，类型为整型。 

| 值     | 含义           |
| ------ | -------------- |
| 0x0001 | 可读权限       |
| 0x0002 | 可写权限       |
| 0x0004 | 读需要认证     |
| 0x0008 | 读需要授权     |
| 0x0010 | 读需要加密     |
| 0x0020 | 读需要授权认证 |
| 0x0040 | 写需要认证     |
| 0x0080 | 写需要授权     |
| 0x0100 | 写需要加密     |
| 0x0200 | 写需要授权认证 |

- `uuid_type`-uuid类型，0 - 长UUID，128bit；1 - 短UUID，16bit。类型为整型。
- `uuid_s`-短UUID，2个字节（16bit），类型为整型，当uuid_type为0时，该值给0。
- `uuid_l`-长UUID，16个字节（128bit），类型为bytearray，当uuid_type为1时，该值填 bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])。 
- `value`-特征描述数据。类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

**示例**：

```python
def ble_gatt_add_characteristic_desc():
    data = [0x00, 0x00]
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # 短UUID
    uuid_s = 0x2902
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    value = bytearray(data)
    ret = ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_desc failed.')
        return -1
    print('ble_gatt_add_characteristic_desc success.')
    return 0
```

### `ble.addOrClearService`

```python
ble.addOrClearService(option, mode)
```

增加已添加的所有服务信息到模块，或者删除模块中已增加的所有服务信息。

**参数描述：**

- `option`-操作类型，类型为整型。0 - 删除服务，1 - 增加服务。
- `mode`-是否保留系统默认服务，类型为整型。 0 - 删除系统默认的GAP和GATT服务，1 - 保留系统默认的GAP和GATT服务。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.sendNotification`

```python
ble.sendNotification(connect_id, attr_handle, value)
```

发送通知。

**参数描述：**

- `connect_id`-连接ID，类型为整型。
- `attr_handle`-属性句柄，类型为整型。 
- `value`-要发送的数据，发送数据长度不要超过MTU，类型为bytearray。 

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.sendIndication`

```python
ble.sendIndication(connect_id, attr_handle, value)
```

发送指示。

**参数描述：**

- `connect_id`-连接ID，类型为整型。
- `attr_handle`-属性句柄，类型为整型。 
- `value`-要发送的数据，发送数据长度不要超过MTU，类型为bytearray。 

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.advStart`

```python
ble.advStart()
```

开启广播。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.advStop`

```python
ble.advStop()
```

停止广播。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

## BLE Client相关功能

### `ble.clientInit`

```python
ble.clientInit(user_cb)
```

初始化 BLE Client 并注册回调函数。

**参数描述：**

- `user_cb`-回调函数，类型为function。回调函数参数含义：args[0] 固定表示event_id，args[1] 固定表示状态，0表示成功，非0表示失败。回调函数的参数个数并不是固定2个，而是根据第一个参数args[0]来决定的，下表中列出了不同事件ID对应的参数个数及说明。

| event_id | 参数个数 | 参数说明                                                     |
| :------: | :------: | ------------------------------------------------------------ |
|    0     |    2     | args[0] ：event_id，表示 BT/BLE start<br>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    1     |    2     | args[0] ：event_id，表示 BT/BLE stop<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    16    |    4     | args[0] ：event_id，表示 BLE connect<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id<br/>args[3] ：addr，BT/BLE address，bytearray类型数据 |
|    17    |    4     | args[0] ：event_id，表示 BLE disconnect<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id，<br/>args[3] ：addr，BT/BLE address，bytearray类型数据 |
|    18    |    7     | args[0] ：event_id，表示 BLE update connection parameter<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id<br/>args[3] ：max_interval，最大的间隔，间隔：1.25ms，取值范围：6-3200，时间范围：7.5ms ~ 4s<br/>args[4] ：min_interval，最小的间隔，间隔：1.25ms，取值范围：6-3200，时间范围：7.5ms ~ 4s<br/>args[5] ：latency，从机忽略连接状态事件的时间。需满足：（1+latecy)\*max_interval\*2\*1.25<timeout\*10<br/>args[6] ：timeout，没有交互，超时断开时间，间隔：10ms，取值范围：10-3200，时间范围：100ms ~ 32s |
|    19    |    9     | args[0] ：event_id，表示 BLE scan report<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：event_type<br/>args[3] ：扫描到的设备名称<br/>args[4] ：设备地址类型<br/>args[5] ：设备地址，bytearray类型数据<br/>args[6] ：rssi，信号强度<br/>args[7] ：data_len，扫描的原始数据长度<br/>args[8] ：data，扫描的原始数据 |
|    20    |    4     | args[0] ：event_id，表示 BLE connection mtu<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：handle<br/>args[3] ：mtu值 |
|    23    |    4     | args[0] ：event_id，表示 client接收到通知<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，包含句柄等数据的原始数据，数据格式及解析见最后的综合示例程序 |
|    24    |    4     | args[0] ：event_id，表示 client recieve indication，即接收指示<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，包含indication的原始数据，数据格式及解析见最后的综合示例程序 |
|    26    |    2     | args[0] ：event_id，表示 开始查找服务<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    27    |    5     | args[0] ：event_id，表示查找到服务<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：start_handle，表示service的开始句柄<br/>args[3] ：end_handle，表示service的结束句柄<br/>args[4] ：UUID，表示service的UUID（短UUID） |
|    28    |    4     | args[0] ：event_id，表示查找到服务特征<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，包含句柄、属性、UUID等数据的原始数据，数据格式及解析见最后的综合示例程序 |
|    29    |    4     | args[0] ：event_id，表示 查找到特征描述<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，包含句柄、UUID等数据的原始数据，数据格式及解析见最后的综合示例程序 |
|    30    |    2     | args[0] ：event_id，表示写入特征值并需要server端确认<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    31    |    2     | args[0] ：event_id，表示写入特征值，无需server端确认<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    32    |    4     | args[0] ：event_id，表示通过句柄来读取特征值<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，原始数据 |
|    33    |    4     | args[0] ：event_id，表示通过UUID来读取特征值<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，原始数据 |
|    34    |    4     | args[0] ：event_id，表示读取多个特征值<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，原始数据 |
|    35    |    2     | args[0] ：event_id，表示 写入特征描述，需server端确认<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    36    |    4     | args[0] ：event_id，表示读特征描述<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，原始数据 |
|    37    |    3     | args[0] ：event_id，表示属性错误<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：errcode，错误码 |

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.clientRelease`

```python
ble.clientRelease()
```

BLE Client 资源释放。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.setScanParam`

```python
ble.setScanParam(scan_mode, interval, scan_window, filter_policy, addr_type)
```

设置扫描参数。

**参数描述：**

- `scan_mode`-扫描模式，类型为整型。扫描模式，默认为积极扫描。0 - 消极扫描，1 - 积极扫描。
- `interval`-扫描间隔，类型为整型。范围0x0004-0x4000，时间间隔 = interval \* 0.625，单位ms。
- `scan_window`-一次扫描的时间，类型为整型。范围0x0004-0x4000，扫描时间 = scan_window\* 0.625，单位ms。
- `filter_policy`-扫描过滤策略，类型为整型。默认为0。0 - 过滤目标地址不是本设备的定向广播包，1 - 过滤目标地址不是本设备的定向广播包及白名单之外的广播包，2 -过滤目标地址不是本设备且没使用Resolvable private address的定向广播包，3 - 过滤目标地址不是本设备且没使用Resolvable private address的定向广播包及白名单之外的广播包。
- `addr_type`-本地地址类型，类型为整型。0 - 公共地址，1 - 随机地址。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。



> 扫描时间 `scan_window` 不能大于扫描间隔 `interval` 。如果两者相等，则表示连续不停的扫描。此时 BLE 的 Controller 会连续运行扫描，占满系统资源而导致无法执行其他任务。所以不允许设置连续扫描。并且不建议将时间设置的太短，扫描越频繁则功耗越高。



### `ble.scanStart`

```python
ble.scanStart()
```

开始扫描。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.scanStop`

```python
ble.scanStop()
```

停止扫描。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.setScanFilter`

```python
ble.setScanFilter(act)
```

打开或者关闭扫描过滤。如果打开，那么扫描设备的广播数据时，同一个设备的广播数据只会上报一次；如果关闭，则同一个设备的所有的广播数据都会上报。

**参数描述：**

- `act`-扫描过滤开关，类型为整型。0 - 关闭扫描过滤功能，1 - 打开扫描过滤功能。默认打开过滤功能。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.connect`

```python
ble.connect(addr_type, addr)
```

根据指定的设备地址去连接设备。

**参数描述：**

- `addr_type`-地址类型，类型为整型。0 - 公共地址，1 - 随机地址。
- `addr`-BLE地址，类型为bytearray，大小为6字节。  

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.cancelConnect`

```python
ble.cancelConnect(addr)
```

取消正在建立的连接。

**参数描述：**

- `addr`-BLE地址，类型为bytearray，大小为6字节。  

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.disconnect`

```python
ble.disconnect(connect_id)
```

断开已建立的连接。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.discoverAllService`

```python
ble.discoverAllService(connect_id)
```

扫描所有的服务。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.discoverByUUID`

```python
ble.discoverByUUID(connect_id, uuid_type, uuid_s, uuid_l)
```

扫描指定UUID的服务。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。
- `uuid_type`-uuid类型，0 - 长UUID，128bit；1 - 短UUID，16bit。类型为整型。
- `uuid_s`-短UUID，2个字节（16bit），类型为整型，当uuid_type为0时，该值给0。
- `uuid_l`-长UUID，16个字节（128bit），类型为bytearray，当uuid_type为1时，该值填 bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.discoverAllIncludes`

```python
ble.discoverAllIncludes(connect_id, start_handle, end_handle)
```

扫描所有的引用，start_handle和end_handle要属于同一个服务。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。
- `start_handle`-开始句柄，从这个句柄开始寻找引用，类型为整型。
- `end_handle`-结束句柄，从这个句柄结束寻找引用，类型为整型。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.discoverAllChara`

```python
ble.discoverAllChara(connect_id, start_handle, end_handle)
```

扫描所有的特征，start_handle和end_handle要属于同一个服务。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。
- `start_handle`-开始句柄，从这个句柄开始寻找特征，类型为整型。
- `end_handle`-结束句柄，从这个句柄结束寻找特征，类型为整型。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.discoverAllCharaDesc`

```python
ble.discoverAllCharaDesc(connect_id, start_handle, end_handle)
```

扫描所有特征的描述，start_handle和end_handle要属于同一个服务。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。
- `start_handle`-开始句柄，从这个句柄开始寻找特征描述，类型为整型。
- `end_handle`-结束句柄，从这个句柄结束寻找特征描述，类型为整型。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.readCharaByUUID`

```python
ble.readCharaByUUID(connect_id, start_handle, end_handle, uuid_type, uuid_s, uuid_l)
```

读取指定UUID的特征值，start_handle和end_handle必须要包含一个特征值句柄。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。
- `start_handle`-开始句柄，一定要属于同一个服务的句柄，类型为整型。
- `end_handle`-结束句柄，一定要属于同一个服务的句柄，类型为整型。
- `uuid_type`-uuid类型，0 - 长UUID，128bit；1 - 短UUID，16bit。类型为整型。
- `uuid_s`-短UUID，2个字节（16bit），类型为整型，当uuid_type为0时，该值给0。
- `uuid_l`-长UUID，16个字节（128bit），类型为bytearray，当uuid_type为1时，该值填 bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.readCharaByHandle`

```python
ble.readCharaByHandle(connect_id, handle, offset, is_long)
```

读取指定句柄的特征值。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。
- `handle`-特征值句柄，类型为整型。
- `offset`-偏移位置，类型为整型。
- `is_long`-长特征值标志，0-短特征值，一次可以读取完；1-长特征值，分多次读取。类型为整型。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.readCharaDesc`

```python
ble.readCharaDesc(connect_id, handle, is_long)
```

读取特征描述。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。
- `handle`-特征值句柄，类型为整型。
- `is_long`-长特征值标志，0-短特征值，一次可以读取完；1-长特征值，分多次读取。类型为整型。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.writeChara`

```python
ble.writeChara(connect_id, handle, offset, is_long, data)
```

写入特征值，需要对端应答。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。
- `handle`-特征值句柄，类型为整型。
- `offset`-偏移位置，类型为整型。
- `is_long`-长特征值标志，0-短特征值，一次可以读取完；1-长特征值，分多次读取。类型为整型。
- `data`-特征值数据，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.writeCharaNoRsp`

```python
ble.writeCharaNoRsp(connect_id, handle, data)
```

写入特征值，不需要对端应答。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。
- `handle`-特征值句柄，类型为整型。
- `data`-特征值数据，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。

### `ble.writeCharaDesc`

```python
ble.writeCharaDesc(connect_id, handle, data)
```

写入特征描述。

**参数描述：**

- `connect_id`-连接ID，建立连接时得到的连接ID，类型为整型。
- `handle`-特征描述句柄，类型为整型。
- `data`-特征描述数据，类型为bytearray。

**返回值描述：**

执行成功返回整型0，失败返回整型-1。