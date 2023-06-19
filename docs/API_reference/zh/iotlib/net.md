# net - 网络相关功能

该模块包含了模组网络相关的功能，提供配置和查询网络模式信息等接口，比如获取注网状态，设置搜网模式等。



>建议用户使用不同运营商的SIM卡时，则配置对应运营商的APN信息；如果不配置或者配置错误，可能会导致模组无法注网。用户具体如何配置APN信息，参考`dataCall.setPDPContext`方法。



## 获取CSQ信号强度

### `net.csqQueryPoll`

```python
net.csqQueryPoll()
```

该方法用于获取csq信号强度。

**返回值描述：**

  成功返回整型的csq信号强度值，失败返回整型值`-1`，返回值为`99`表示异常。



>信号强度值范围0 ~ 31，值越大表示信号强度越好。



**示例：**

```python
>>> import net
>>> net.csqQueryPoll()
31
```



## 获取小区信息

### `net.getCellInfo`

```python
net.getCellInfo()
```

该方法用于获取邻近小区的信息。

**返回值描述：**

  失败返回整型值`-1`，成功返回包含三种网络系统`（GSM、UMTS、LTE）`的信息的list，如果对应网络系统信息为空，则返回空的List。格式和说明如下：

  `([(flag, cid, mcc, mnc, lac, arfcn, bsic, rssi)], [(flag, cid, licd, mcc, mnc, lac, uarfcn, psc, rssi)], [(flag, cid, mcc, mnc, pci, tac, earfcn, rssi, rsrq, sinr),...])`

* `GSM`网络系统返回值说明

| 参数    | 参数意义                                                     |
| ------- | ------------------------------------------------------------ |
| `flag`  | 小区类型，范围0 - 3， 0：当前服务小区，1：邻区，2：同频邻区 ，3：异频邻区 |
| `cid`   | 返回GSM网络下的cell id信息，0则为空，范围0 ~ 65535           |
| `mcc`   | 移动设备国家代码，范围 0 ~ 999<br>注意：EC100Y/EC600S/EC600N/EC600E/EC800E/EC200A/EC600M/EC800M系列的模组，该值是用十六进制来表示，比如下面示例中的十进制数1120，用十六进制表示为0x460，表示移动设备国家代码460，其他型号模组，该值直接用十进制表示，比如移动设备国家代码460，就是用十进制的460来表示。 |
| `mnc`   | 移动设备网络代码，范围 0 ~ 99                                |
| `lac`   | 位置区码，范围 1 ~ 65534                                     |
| `arfcn` | 无线频道编号，范围 0 ~ 65535                                 |
| `bsic`  | 基站识别码，范围 0 ~ 63                                      |
| `rssi`  | GSM网络下，该值表示接收电平，描述接收到信号强度，99表示未知或者无法检测到，该值的计算方式如下：<br/>rssi = RXLEV - 111，单位dBm，RXLEV 的范围是 0 ~ 63，所以rssi范围是 -111 ~ -48 dBm； |

* `UMTS`网络系统返回值说明

| 参数     | 参数意义                                                     |
| -------- | ------------------------------------------------------------ |
| `flag`   | 小区类型，范围0 - 3，0：当前服务小区，1：邻区，2：同频邻区 ，3：异频邻区 |
| `cid`    | 表示UMTS网络下的 Cell identity ，Cell identity = RNC_ID * 65536 + Cell_ID，Cell identity范围 0x0000000 ~ 0xFFFFFFF（注意这里是28bits）；即Cell identity前两个字节是RNC_ID，后两个字节是Cell_ID，Cell_ID的范围是0 ~ 65535 |
| `lcid`   | URA ID，范围 0 ~ 65535，0表示该信息不存在                    |
| `mcc`    | 移动设备国家代码，范围 0 ~ 999                               |
| `mnc`    | 移动设备网络代码，范围 0 ~ 99                                |
| `lac`    | 位置区码，范围 1 ~ 65534                                     |
| `uarfcn` | 无线频道编号，范围 0 ~ 65535                                 |
| `psc`    | 主扰码，该参数确定所扫描的小区的主要扰码，范围 0 ~ 511       |
| `rssi`   | UMTS网络下，该值表示RSCP即CPICH/PCCPCH 接收信号码功率，该值的计算方式如下：<br>rssi = RSCP - 115，单位dBm ，范围 -121 ~ -25 dBm； |

* `LTE`网络系统返回值说明

| 参数   | 参数意义                                                     |
| ------ | ------------------------------------------------------------ |
| `flag` | 小区类型，范围0 - 3，0：当前服务小区，1：邻区，2：同频邻区 ，3：异频邻区 |
| `cid`  | 表示LTE网络下的小区标识（Cell Identity），也叫ECI（E-UTRAN Cell Identifier），ECI = eNodeB ID *256 + Cell ID组成，范围0x0000000 ~ 0xFFFFFFF（注意是28bits），前20bit表示基站标识（eNodeB ID），后8bit表示LTE小区ID（Cell ID） |
| `mcc`  | 移动设备国家代码，范围 0 ~ 999                               |
| `mnc`  | 移动设备网络代码，范围 0 ~ 99                                |
| `pci`  | 物理层小区标识号，0 ~ 503                                    |
| `tac`  | 跟踪区域码，0 ~ 65535                                        |
| `earfcn` | 无线频道编号，范围 0 ~ 65535 |
| `rssi` | LTE网络下，rssi：表示接收的所有信号强度，单位dBm，范围 -140 ~ -44 dBm<br>注：目前除BC25系列和BG77/BG95系列，其它平台均无法获取rssi，使用RSRP代替:<br>RSRP：表示接收到的有效信号强度，单位dBm，范围 -140 ~ -44 dBm |
| `rsrq` |LTE网络参考信号接收质量，范围 -20 ~ -3 <br>注：理论上rsrq的范围应该是-19.5 ~ -3，但由于计算方法问题，目前能给出的是-20 ~ -3<br>目前仅BC25系列、BG77/BG95系列和EC600E/EC800E系列获取该参数有意义，其它平台该参数无意义|



>该接口搜小区时会一直阻塞，一般是3-5秒，在无信号的地方会更长
>



**示例：**

```python
>>> import net
>>> net.getCellInfo()
([], [], [(0, 232301375, 1120, 17, 378, 26909, 1850, -66, -8), (3, 110110494, 1120, 17, 10, 26909, 2452, -87, -17), (3, 94542859, 1120, 1, 465, 56848, 1650, -75, -10), 
(3, 94472037, 1120, 1, 369, 56848, 3745, -84, -20)])

>>> net.getCellInfo()
([], [], [(0, 17104243, 460, 4, 121, 19472, 3688, -76, -15)])
```



## 网络制式及漫游配置

### `net.getConfig`

```python
net.getConfig()
```

该方法用于获取当前网络模式及漫游配置。

**返回值描述：**

  失败返回整型值`-1`，成功返回一个元组，包含当前首选的网络制式与漫游打开状态，说明如下：

* 网络制式

| 值   | 网络制式                  |      | 值   | 网络制式                        |
| ---- | :------------------------ | ---- | ---- | ------------------------------- |
| 0    | GSM                       |      | 17   | UMTS_LTE（双链路）              |
| 1    | UMTS                      |      | 18   | GSM_UMTS_LTE（双链路）          |
| 2    | GSM_UMTS（自动）          |      | 19   | CATM，BG95/BG77系列支持         |
| 3    | GSM_UMTS（GSM 优先）      |      | 20   | GSM_CATM,  BG95系列支持         |
| 4    | GSM_UMTS（UMTS 优先）     |      | 21   | CATNB,   BG95/BG77系列支持      |
| 5    | LTE                       |      | 22   | GSM_CATNB,  BG95系列支持        |
| 6    | GSM_LTE（自动）           |      | 23   | CATM_CATNB,   BG95/BG77系列支持 |
| 7    | GSM_LTE（GSM 优先）       |      | 24   | GSM_CATM_CATNB, BG95系列支持    |
| 8    | GSM_LTE（LTE 优先）       |      | 25   | CATM_GSM,  BG95系列支持         |
| 9    | UMTS_LTE（自动）          |      | 26   | CATNB_GSM,  BG95系列支持        |
| 10   | UMTS_LTE（UMTS 优先）     |      | 27   | CATNB_CATM, BG95/BG77系列支持   |
| 11   | UMTS_LTE（LTE 优先）      |      | 28   | GSM_CATNB_CATM, BG95系列支持    |
| 12   | GSM_UMTS_LTE（自动）      |      | 29   | CATM_GSM_CATNB,  BG95系列支持   |
| 13   | GSM_UMTS_LTE（GSM 优先）  |      | 30   | CATM_CATNB_GSM,   BG95系列支持  |
| 14   | GSM_UMTS_LTE（UMTS 优先） |      | 31   | CATNB_GSM_CATM,   BG95系列支持  |
| 15   | GSM_UMTS_LTE（LTE 优先）  |      | 32   | CATNB_CATM_GSM,   BG95系列支持  |
| 16   | GSM_LTE（双链路）         |      |      |                                 |



>BC25系列不支持此方法;
>
>BG95-M1系列仅支持CATM制式；
>
>BG95-M2/BG77系列仅支持包含CATM和CATNB两种制式；
>
>BG95-M3/M8系列支持CATM，CATNB和GSM全部三种制式；



**示例：**

```python
>>> import net
>>>net.getConfig ()
(8, False)
```



### `net.setConfig`

```python
net.setConfig(mode [, roaming])
```

该方法用于设置网络制式及漫游配置。

**参数描述：**

* `mode` - 网络制式，整型值，详见上述网络制式表格

* `roaming` - 漫游开关，整型值，可选参数（`0`：关闭， `1`：开启）

**返回值描述：**

  设置成功返回整型值`0`，设置失败返回整型值`-1`。



>* roaming为可选参数，不支持的平台，该参数可不写
>* BC25系列不支持此方法
>* EC200U/EC600U/EG915U系列模组不支持漫游参数配置，且仅支持设置网络制式0/5/6/8，<br>其中6/8底层都是都是LTE优先，当设置为8时，查询为6。
>* EC600E/EC800E系列模组仅支持LTE ONLY.



**示例：**

```python
>>> import net
>>>net.setConfig(6)
0

>>>net.getConfig ()
(6, False)
```



## 获取网络配置模式

### `net.getNetMode`

```python
net.getNetMode()
```

该方法用于获取网络配置模式。

**返回值描述：**

失败返回整型值`-1`，成功返回一个元组，格式为：`(selection_mode, mcc, mnc, act)`参数说明如下：

| 参数             | 类型   | 参数说明                 |
| ---------------- | ------ | ------------------------ |
| `selection_mode` | 整型   | 方式，0 - 自动，1 - 手动 |
| `mcc`            | 字符串 | 移动设备国家代码         |
| `mnc`            | 字符串 | 移动设备网络代码         |
| `act`            | 整型   | 首选网络的ACT模式        |

`ACT`模式枚举值参照下表：

| 值   | ACT模式            |
| ---- | ------------------ |
| 0    | GSM                |
| 1    | COMPACT            |
| 2    | UTRAN              |
| 3    | GSM wEGPRS         |
| 4    | UTRAN wHSDPA       |
| 5    | UTRAN wHSUPA       |
| 6    | UTRAN wHSDPA HSUPA |
| 7    | E UTRAN            |
| 8    | UTRAN HSPAP        |
| 9    | E TRAN A           |
| 10   | NONE               |

BG95系列模组`ACT`模式枚举值参照下表：

| 值   | ACT模式             |
| ---- | ------------------ |
| 0    | GSM                |
| 1    | GSM COMPACT        |
| 2    | UTRAN              |
| 3    | GSM wEGPRS         |
| 4    | UTRAN wHSDPA       |
| 5    | UTRAN wHSUPA       |
| 6    | UTRAN wHSDPA HSUPA |
| 7    | E_UTRAN            |
| 8    | UTRAN HSPAP        |
| 9    | E_UTRAN_CA         |
| 10   | E_UTRAN_NBIOT      |
| 11   | E_UTRAN_EMTC       |
| 12   | NONE               |

**示例：**

```python
>>> import net
>>> net.getNetMode()
(0, '460', '46', 7)
```



## 获取详细信号强度

### `net.getSignal`

```python
net.getSignal([sinrEnable])
```

该方法用于获取详细信号强度。

**参数描述：**

* `sinrEnable` - 使能是否获取sinr数值，整型值，可选参数，取值范围见下表：

| 取值 | 含义          |
|-----| ------------- |
| 0   | 不获取sinr数值 |
| 1   | 获取sinr数值   |

**返回值描述：**

  失败返回整型值`-1`，成功返回一个元组，包含两个List`(GW 、LTE)`，返回值格式和说明如下：

  `([rssi, bitErrorRate, rscp, ecno], [rssi, rsrp, rsrq, cqi, sinr])`

* `GSM/WCDMA`返回值参数说明：

| 参数           | 参数意义                                                     |
| -------------- | ------------------------------------------------------------ |
| `rssi`         | GSM和WCDMA网络下，该值表示接收电平，描述接收到信号强度，99表示未知或者无法检测到，该值的计算方式如下<br/>rssi = RXLEV - 111，单位dBm，RXLEV 的范围是 0 ~ 63 |
| `bitErrorRate` | 误码率，范围 0 ~ 7，99表示未知或者无法检测到                 |
| `rscp`         | 接收信号码功率，范围 -121 ~ -25 dBm，255表示未知或者无法检测到 |
| `ecno`         | 导频信道，范围 -24 ~ 0，255表示未知或者无法检测到            |

* `LTE`返回值参数说明：

| 参数   | 参数意义                                                  |
| ------ |-------------------------------------------------------|
| `rssi` | 接收的信号强度，范围 -140 ~ -44 dBm，99表示未知或者无法检测到               |
| `rsrp` | 下行参考信号的接收功率，范围 -140 ~ -44 dBm，99表示未知或者无法检测到           |
| `rsrq` | 下行特定小区参考信号的接收质量，范围 -20 ~ -3 dBm，值越大越好 ,255表示未知或者无法检测到 |
| `cqi`  | 信道质量，255表示未知或者无法检测到                                   |
| `sinr` | 信噪比，范围 -10 ~ 40 dBm，255表示未知或者无法检测到                    |



>* `sinrEnable`为可选参，不支持的平台可不写，不写默认不获取sinr
>* BC25系列不支持获取sinr，其余模组型号均支持



**示例：**

```python
>>> import net
>>>net.getSignal()
([99, 99, 255, 255], [-51, -76, -5, 255])
>>>net.getSignal(0)
([99, 99, 255, 255], [-51, -76, -5, 255])
>>>net.getSignal(1)
([99, 99, 255, 255], [-51, -76, -5, 255, 18])
```



## 获取当前基站时间

### `net.nitzTime`

```python
net.nitzTime()
```

该方法用于获取当前基站时间。这个时间是基站在模块开机注网成功时下发的时间。

**返回值描述：**

  失败返回整型值`-1`，成功返回一个元组，包含基站时间与对应时间戳与闰秒数（0表示不可用），格式为：`(date, abs_time, leap_sec)`，说明如下：

| 参数       | 类型   | 参数意义                                                                                                                                                                          |
| ---------- | ------ |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `date`     | 字符串 | 基站时间，其中关于时区的部分，不同系列有所区别，具体见示例。<br>如果需要设置和获取时区，请使用`utime`模块的`setTimeZone(offset)`和`getTimeZone()`接口，<br>不同平台，这两个接口的单位都是小时，具体参考[`utime`](../QuecPython_classlib/utime.md)模块的说明。 |
| `abs_time` | 整型   | 基站时间的绝对秒数表示                                                                                                                                                                   |
| `leap_sec` | 整型   | 闰秒数                                                                                                                                                                           |

**示例：**

```python
>>> import net
>>> net.nitzTime() 
# EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A系列的返回值，时区单位小时，这里8即表示东八区
('21/10/26 06:08:03 8 0', 1635228483, 0)  
# BC25/EC600E/EC800E/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G系列返回值，时区单位15分钟，这里+32即表示东八区
('20/11/26 02:13:25 +32 0', 1606356805, 0)
# BG77/BG95系列的返回值，无时区部分
('23/02/14 02:25:13', 1676312713, 0)
```



## 获取运营商信息

### `net.operatorName`

```python
net.operatorName()
```

该接口用于获取当前注网的运营商信息。

**返回值描述：**

  失败返回整型值`-1`，成功返回一个元组，包含注网的运营商信息，格式为： `(long_eons, short_eons, mcc, mnc)`，说明如下：

| 参数         | 类型   | 参数说明         |
| ------------ | ------ | ---------------- |
| `long_eons`  | 字符串 | 运营商信息全称   |
| `short_eons` | 字符串 | 运营商信息简称   |
| `mcc`        | 字符串 | 移动设备国家代码 |
| `mnc`        | 字符串 | 移动设备网络代码 |

**示例：**

```python
>>> import net
>>> net.operatorName()
('CHN-UNICOM', 'UNICOM', '460', '01')
```



## 获取网络注册信息

### `net.getState`

```python
net.getState()
```

该接口用于获取当前网络注册信息。

**返回值描述：**

  失败返回整型值`-1`，成功返回一个元组，包含电话和网络注册信息，元组中`voice`开头的表示电话注册信息，`data`开头的表示网络注册信息，格式为：`([voice_state, voice_lac, voice_cid, voice_rat, voice_reject_cause, voice_psc], [data_state, data_lac, data_cid, data_rat, data_reject_cause, data_psc])`

* 返回值参数说明：

| 参数           | 参数说明                                                     |
| -------------- | ------------------------------------------------------------ |
| `state`        | 网络注册状态，具体见下表                                     |
| `lac`          | 位置区码，范围 1 ~ 65534                                     |
| `cid`          | cell id，范围 0x00000000 ~ 0x0FFFFFFF，具体见上面`net.getCellInfo()`中返回值 |
| ``rat``        | 接入技术，access technology，具体见后面表格                  |
| `reject_cause` | 注册被拒绝的原因，EC200U/EC600U/BC25系列该参数保留，不作为有效参数 |
| `psc`          | 主扰码，Primary Scrambling Code，EC200U/EC600U/BC25系列该参数保留，不作为有效参数 |

* 网络注册状态`state`枚举值见下表：

| 值   | 状态说明                              |
| ---- | ------------------------------------- |
| 0    | 没有注册，MT也没有再搜索              |
| 1    | 注册完成,，本地网络                   |
| 2    | 没有注册，但是MT在尝试搜索            |
| 3    | 拒绝注册                              |
| 4    | 未知状态                              |
| 5    | 注册完成， 漫游网络                   |
| 6    | 注册为“仅限短信”，本地网络 (不适用)   |
| 7    | 注册为“仅限短信”，漫游网络(不适用)    |
| 8    | 紧急attach仅限紧急承载服务            |
| 9    | 注册为“CSFB不优先”，本地网络 (不适用) |
| 10   | 注册为“CSFB不优先”，漫游网络(不适用)  |
| 11   | 仅限紧急承载服务                      |

* 接入技术`access technology`

| 值   | 说明               |
| ---- | ------------------ |
| 0    | GSM                |
| 1    | GSM COMPACT        |
| 2    | UTRAN              |
| 3    | GSM wEGPRS         |
| 4    | UTRAN wHSDPA       |
| 5    | UTRAN wHSUPA       |
| 6    | UTRAN wHSDPA HSUPA |
| 7    | E_UTRAN            |
| 8    | UTRAN HSPAP        |
| 9    | E_UTRAN_CA         |
| 10   | NONE               |



> BG77/BG95系列参照下表

| 值   | 说明               |
| ---- | ------------------ |
| 0    | GSM                |
| 1    | GSM COMPACT        |
| 2    | UTRAN              |
| 3    | GSM wEGPRS         |
| 4    | UTRAN wHSDPA       |
| 5    | UTRAN wHSUPA       |
| 6    | UTRAN wHSDPA HSUPA |
| 7    | E_UTRAN            |
| 8    | UTRAN HSPAP        |
| 9    | E_UTRAN_CA         |
| 10   | E_UTRAN_NBIOT      |
| 11   | E_UTRAN_EMTC       |
| 12   | NONE               |

**示例：**

```python
>>> import net
>>> net.getState()
([11, 26909, 232301323, 7, 0, 466], [0, 26909, 232301323, 7, 0, 0])
```



## 获取小区ID

### `net.getCi`

```python
net.getCi()
```

该方法用于获取附近小区ID。该接口获取结果即为`net.getCellInfo()`接口获取结果中的cid集合。

**返回值描述：**

  成功返回一个list类型的数组，包含小区id，格式为：`[id, ……, id]`。数组成员数量并非固定不变，位置不同、信号强弱不同等都可能导致获取的结果不一样。

  失败返回整型值`-1`。

**示例：**

```python
>>> net.getCi()
[14071232, 0]
```



### `net.getServingCi`

```python
net.getServingCi()
```

该方法用于获取服务小区ID。该接口获取结果即为`net.getCellInfo()`接口获取结果中的cid集合。

**返回值描述：**

  成功返回服务小区ID。失败返回整型值`-1`。

**示例：**

```python
>>> import net
>>> net.getServingCi()
94938399
```



## 获取小区的MNC

### `net.getMnc`

```python
net.getMnc()
```

该方法用于获取附近小区的mnc。该接口获取结果即为`net.getCellInfo()`接口获取结果中的mnc集合。

**返回值描述：**

  成功返回一个list类型的数组，包含小区`mnc`，格式为：`[mnc, ……, mnc]`。数组成员数量并非固定不变，位置不同、信号强弱不同等都可能导致获取的结果不一样。

  失败返回整型值`-1`。

**示例：**

```python
>>> import net
>>> net.getMnc()
[0, 0]
```



### `net.getServingMnc`

```python
net.getServingMnc()
```

该方法用于获取服务小区的mnc。该接口获取结果即为`net.getCellInfo()`接口获取结果中的mnc集合。

**返回值描述：**

  成功返回服务小区`mnc`。失败返回整型值`-1`。

**示例：**

```python
>>> import net
>>> net.getServingMnc()
1
```



## 获取小区的MCC

### `net.getMcc`

```python
net.getMcc()
```

该方法用于获取附近小区的mcc。该接口获取结果即为`net.getCellInfo()`接口获取结果中的mcc集合。

**返回值描述：**

  成功返回一个list类型的数组，包含小区`mcc`，格式为：`[mcc, ……, mcc]`。数组成员数量并非固定不变，位置不同、信号强弱不同等都可能导致获取的结果不一样。

  失败返回整型值`-1`。



> EC100Y/EC600S/EC600N/EC600E/EC800E/EC200A/EC600M/EC800M系列的模组，该值是用十六进制来表示，比如下面示例中的十进制数1120，十六进制即0x460，表示移动设备国家代码460，其他型号模组，该值直接用十进制表示，比如移动设备国家代码460，就是用十进制的460来表示。



**示例：**

```python
>>> import net
>>> net.getMcc()
[1120, 0]
```



### `net.getServingMcc`

```python
net.getServingMcc()
```

该方法用于获取服务小区的mcc。该接口获取结果即为`net.getCellInfo()`接口获取结果中的mcc集合。

**返回值描述：**

  成功返回服务小区的`mcc`，失败返回整型值`-1`。



> EC100Y/EC600S/EC600N系列的模组，该值是用十六进制来表示，比如下面示例中的十进制数1120，十六进制即0x460，表示移动设备国家代码460，其他型号模组，该值直接用十进制表示，比如移动设备国家代码460，就是用十进制的460来表示。



**示例：**

```python
>>> import net
>>> net.getServingMcc()
1120
```



## 获取小区的Lac

### `net.getLac`

```python
net.getLac()
```

该方法用于获取附近小区的Lac。该接口获取结果即为`net.getCellInfo()`接口获取结果中的lac集合。

**返回值描述：**

  成功返回一个list类型的数组，包含小区lac，格式为：`[lac, ……, lac]`。数组成员数量并非固定不变，位置不同、信号强弱不同等都可能导致获取的结果不一样。

  失败返回整型值`-1`。

**示例：**

```python
>>> import net
>>> net.getLac()
[21771, 0]
```



### `net.getServingLac`

```python
net.getServingLac()
```

该方法用于获取服务小区的Lac。该接口获取结果即为`net.getCellInfo()`接口获取结果中的lac集合。

**返回值描述：**

  成功返回服务小区`lac`，失败返回整型值`-1`。

**示例：**

```python
>>> import net
>>> net.getServingLac()
56848
```



## 工作模式配置

### `net.getModemFun`

```python
net.getModemFun()
```

该方法用于获取当前工作模式。

**返回值描述：**

  成功返回当前模组工作模式，失败返回整型值`-1`；模组工作模式详细如下：

| 模式 | 说明       |
| --- | ---------- |
| 0   | 全功能关闭  |
| 1   | 全功能开启（默认）|
| 4   | 飞行模式    |

**示例：**

```python
>>> import net
>>> net.getModemFun()
1
```



### `net.setModemFun`

```python
net.setModemFun(fun [, rst])
```

该方法用于设置当前模组工作模式。

**参数描述：**

* `fun` - 模组工作模式，整型值
| 模式 | 说明       |
| --- | ---------- |
| 0   | 全功能关闭  |
| 1   | 全功能开启（默认）|
| 4   | 飞行模式    |

* `rst` - 重启标志，整型值，可选参数
| 值   | 说明       |
| --- | ---------- |
| 0   | 设置完不重启（默认）  |
| 1   | 设置完重启  |

**返回值描述：**

  设置成功返回整型值`0`，设置失败返回整型值`-1`。

**示例：**

```python
>>> import net
>>> net.setModemFun(4)
0
```



## band设置与获取

### `net.setBand`

```python
net.setBand(netRat, gsmBand, bandTuple)
```
该方法用于设置需要的band，即在模组支持的前提下，锁定用户指定的band。

* `band`值对照表

| 网络制式        | band值                                                       |
| --------------- | ------------------------------------------------------------ |
| EGPRS(GSM)      | EGSM900 - 0x1<br/>DCS1800 - 0x2<br/>GSM850 - 0x4<br/>PCS1900 - 0x8 |
| LTE/eMTC/NB-IoT | BAND1 - 0x1<br/>BAND2 - 0x2<br/>BAND3 - 0x4<br/>BAND4 - 0x8<br/>BAND5 - 0x10<br/>BAND8 - 0x80<br/>BAND12 - 0x800<br/>BAND13 - 0x1000<br/>BAND18 - 0x20000<br/>BAND19 - 0x40000<br/>BAND20 - 0x80000<br/>BAND25 - 0x1000000<br/>BAND26 - 0x2000000<br/>BAND27 - 0x4000000<br/>BAND28 - 0x8000000<br/>BAND31 - 0x40000000<br/>BAND66 - 0x20000000000000000<br/>BAND71 - 0x400000000000000000<br/>BAND72 - 0x800000000000000000<br/>BAND73 - 0x1000000000000000000<br/>BAND85 - 0x1000000000000000000000<br/> |

* BG95M3模组`band`支持表

| 网络制式 | 支持的BAND                                                   |
| -------- | ------------------------------------------------------------ |
| Cat M    | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B26/B27/B28/B66/B85 |
| NB-IoT   | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B28/B66/B71/B85    |
| EGPRS    | GSM850/EGSM900/DCS1800/PCS1900                               |

* BG95M1模组`band`支持表

| 网络制式 | 支持的BAND                                                   |
| -------- | ------------------------------------------------------------ |
| Cat M    | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B26/B27/B28/B66/B85 |
| EGPRS    | GSM850/EGSM900/DCS1800/PCS1900                               |

* BG95M8模组`band`支持表

| 网络制式 | 支持的BAND                                                   |
| -------- | ------------------------------------------------------------ |
| Cat M    | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B26/B27/B28/B31/B66/B72/B73/B85 |
| NB-IoT   | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B28/B31/B66/B71/B72/B73/B85 |
| EGPRS    | GSM850/EGSM900/DCS1800/PCS1900                               |

* EG912NENAA模组`band`支持表

| 网络制式 | 支持的BAND                           |
| -------- | ------------------------------------ |
| LTE      | B1/B3/B5/B7/B8/B20/B28/B31/B72       |
| EGPRS    | EGSM900/DCS1800                      |

**参数描述：**

* `netRat` - 网络模式，整型值，表示制定要设置的是哪种网络模式下的`band`
| rat值 | 说明                                      |
| ----- | ----------------------------------------- |
| 0     | 设置GSM网络的band                          |
| 1     | 设置LTE网络的band                          |
| 2     | 设置CATM网络的band                         |
| 3     | 设置NB网络的band                           |

* `gsmBand` - `GSM`网络的`band`值，整型值，参照上述`band`值对照表

* `bandtuple` - 设置`GSM`网络之外的其他网络模式的`band`值，是一个包含4个元素的元组，每个成员最大不能超过4字节，具体形式：`(band_hh, band_hl, band_lh, band_ll)`，每个元素说明如下：
`band_hh` - band值的高8字节的高4字节
`band_hl` - band值的高8字节的低4字节
`band_lh` - band值的低8字节的高4字节
`band_ll` - band值的低8字节的低4字节
如果用户最终要设置的`band`值为`band_value`，那么计算方式如下：
`band_hh = (band_value & 0xFFFFFFFF000000000000000000000000) >> 96`
`band_hl = (band_value & 0x00000000FFFFFFFF0000000000000000) >> 64`
`band_lh = (band_value & 0x0000000000000000FFFFFFFF00000000) >> 32`
`band_ll = (band_value & 0x000000000000000000000000FFFFFFFF)`

**返回值描述：**

  设置成功返回整型值`0`，失败返回整型值`-1`。



>* 当前可支持模组型号：BG95系列/EG912NENAA
>* BG95不支持设置上述模式1(LTE)下的`band`
>* EG912NENAA仅支持上述模式0(GSM)和模式1(LTE)



**示例：**

```python
import net
import utime

'''
用户可直接使用下面两个接口来设置band和获取band
'''
def set_band(net_rat, band_value):
    if net_rat == 0:
        retval = net.setBand(0, band_value, (0, 0, 0, 0))
    else:
        band_hh = (band_value & 0xFFFFFFFF000000000000000000000000) >> 96
        band_hl = (band_value & 0x00000000FFFFFFFF0000000000000000) >> 64
        band_lh = (band_value & 0x0000000000000000FFFFFFFF00000000) >> 32
        band_ll = (band_value & 0x000000000000000000000000FFFFFFFF)
        retval = net.setBand(net_rat, 0, (band_hh, band_hl, band_lh, band_ll))
    return retval


def get_band(net_rat):
    return net.getBand(net_rat)

#======================================================================================================

'''
设置GSM网络band为0xa，即 DCS1800 + PCS1900
0xa = 0x2(DCS1800) + 0x8(PCS1900)
'''
def set_gsm_band_example():
    print('Set GSM band to 0xa example:')
    gsm_band = get_band(0)
    print('GSM band value before setting:{}'.format(gsm_band))
    ret = set_band(0, 0xa)
    if ret == 0:
        print('Set GSM band successfully.')
    else:
        print('Set GSM band failed.')
    utime.sleep(1) # 设置band需要一定时间，延时一段时间再获取新的结果
    gsm_band = get_band(0)
    print('GSM band value after setting:{}'.format(gsm_band))
    return ret


'''
设置eMTC网络band为0x15，即设置 BAND1+BAND3+BAND5
0x15 = 0x1(BAND1) + 0x4(BAND3) + 0x10(BAND5)
'''
def set_camt_band_example():
    print('Set CATM band to 0x15 example:')
    catm_band = get_band(2)
    print('CATM band value before setting:{}'.format(catm_band))
    ret = set_band(2, 0x15)
    if ret == 0:
        print('Set CATM band successfully.')
    else:
        print('Set CATM band failed.')
    utime.sleep(1) # 设置band需要一定时间，延时一段时间再获取新的结果
    catm_band = get_band(2)
    print('CATM band value after setting:{}'.format(catm_band))
    return ret


'''
设置NB-IoT网络band为0x1000800000000000020011，即设置 BAND1+BAND5+BAND18+BAND71+BAND85
0x1000400000000000020011 = 0x1 + 0x10 + 0x20000 + 0x400000000000000000 + 0x1000000000000000000000
'''
def set_nb_band_example():
    print('Set NB band to 0x1000400000000000020011 example:')
    nb_band = get_band(3)
    print('NB band value before setting:{}'.format(nb_band))
    ret = set_band(3, 0x1000400000000000020011)
    if ret == 0:
        print('Set NB band successfully.')
    else:
        print('Set NB band failed.')
    utime.sleep(1) # 设置band需要一定时间，延时一段时间再获取新的结果
    nb_band = get_band(3)
    print('NB band value after setting:{}'.format(nb_band))
    return ret


def main():
    set_gsm_band_example()
    utime.sleep(1)
    set_camt_band_example()
    utime.sleep(1)
    set_nb_band_example()


if __name__ == '__main__':
    main()
    

#===================================================================================================
#运行结果
Set GSM band to 0xa example:
GSM band value before setting:0xf
Set GSM band successfully.
GSM band value after setting:0xa

Set CATM band to 0x15 example:
CATM band value before setting:0x10000200000000090e189f
Set CATM band successfully.
CATM band value after setting:0x15

Set NB band to 0x1000400000000000020011 example:
NB band value before setting:0x10004200000000090e189f
Set NB band successfully.
NB band value after setting:0x1000400000000000020011

```



### `net.getBand`

```python
net.getBand(netRat)
```

该方法用于获取当前某个网络制式下的band设置值。

**参数描述：**

* `netRat` - 网络模式，整型值，表示制定要设置的是哪种网络模式下的`band`
| rat值 | 说明                                      |
| ----- | ----------------------------------------- |
| 0     | 设置GSM网络的band                          |
| 1     | 设置LTE网络的band                          |
| 2     | 设置CATM网络的band                         |
| 3     | 设置NB网络的band                           |

**返回值描述：**

返回十六进制字符串形式的band值。



>* 当前可支持模组型号：BG95系列/EG912NENAA
>* BG95不支持设置上述模式1(LTE)下的`band`
>* EG912NENAA仅支持上述模式0(GSM)和模式1(LTE)



**示例：**

```python
>>> import net
>>> net.getBand(2)
'0x10000200000000090e189f'  # 这是字符串，用户如果需要int型，可通过int(data)来自行转换
```



### `net.bandRst`

```python
net.bandRst()
```

该方法用于恢复band初始设定值。

**返回值描述：**

成功返回整型值`0`，失败返回整型值`-1`。



>当前可支持模组型号：EG912NENAA



**示例：**

```python
'''
先设置成其他band，调用该接口，看是否成功恢复成初始值
EG912NENAA平台初始值：gsm_band:0x3(EGSM900/DCS1800 )  lte_band:0x8000000000480800D5(B1/B3/B5/B7/B8/B20/B28/B31/B72 )
'''
>>> import net
>>> net.bandRst()
0
```