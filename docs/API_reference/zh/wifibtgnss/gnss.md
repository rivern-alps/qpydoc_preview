# gnss - 外置GNSS

对L76K GPS型号（或数据类型与之类似的GPS模组）进行数据获取，可以得到模块定位是否成功，定位的经纬度数据，UTC授时时间，获取GPS模块的定位模式，获取GPS模块定位使用卫星数量，获取GPS模块定位可见卫星数量，获取定位方位角，GPS模块对地速度，模块定位大地高等数据信息。目前，该模块提供的功能接口，所获取的数据都来源于从串口读出的原始GNSS数据包中的GNGGA、GNRMC和GPGSV语句。

> 当前仅EC600S/EC600N/EC800N/200U/600U/600M/800M模块支持该功能
>

## 创建gnss对象

### `gnss.GnssGetData`

```python
gnss.GnssGetData(uartn,baudrate,databits,parity,stopbits,flowctl)
```

创建获取GNSS的对象，参数为挂载GNSS模块的串口以及通信参数

**参数描述**

* `uartn`，int类型
  uartn
  `0`-uart0 - DEBUG PORT
  `1`-uart1 – BT PORT
  `2`-uart2 – MAIN PORT
  `3`-uart3 – USB CDC PORT
* `baudrate`，int类型，常用波特率都支持，如4800、9600、19200、38400、57600、115200、230400等
* `databits`，int类型，数据位（5 ~ 8），ECX00U系列平台当前仅支持8位
* `parity`，int类型，奇偶校验（0 – NONE，1 – EVEN，2 - ODD）
* `stopbits`，int类型，停止位（1 ~ 2）
* `flowctl`，int类型，硬件控制流（0 – FC_NONE， 1 – FC_HW）

**返回值描述**<br />gnss类的对象

**示例**

```python
from gnss import GnssGetData
gnss = GnssGetData(1, 9600, 8, 0, 1, 0)
```

## 读取GNSS数据并解析

### `gnss.read_gnss_data`

```python
gnss.read_gnss_data(max_retry=1, debug=0)
```

从串口读取GNSS数据，返回数据长度

**参数描述**

* `max_retry`，int类型，可选参数，可不填该参数，默认为1；表示当读取的GNSS无效时，自动重新读取的最大尝试次数，如果读取数据长度为0（即没有读取到数据）则直接退出。
* `debug`，int类型， 可选参数，可不填该参数，默认为0；表示在读取解析GNSS数据过程中，是否输出一些调试信息，为0表示不输出详细信息，为1表示输出详细信息。

**返回值描述**

返回从串口读取的GNSS数据长度，int类型，单位字节。

**示例**

```python
#=========================================================================
gnss.read_gnss_data()	# 使用默认设置，仅读取一次，不输出详细调试信息
4224	# 读取数据成功，并解析GNGGA、GNRMC和GPGSV语句都成功，直接返回读取的原始数据长度
#=========================================================================
gnss.read_gnss_data()  # 使用默认设置，仅读取一次，不输出详细调试信息
GNGGA data is invalid. # 读取数据成功，获取的GNGGA定位数据无效
GNRMC data is invalid. # 读取数据成功，获取的GNRMC定位数据无效
648		# 返回读取的原始数据长度
#=========================================================================
gnss.read_gnss_data(max_retry=3)  # 设置最大自动读取次数为3次
Not find GPGSV data or GPGSV data is invalid.  # 第1次读取，GPGSV数据未找到或无效
continue read.        # 继续读取下一包数据
Not find GNGGA data.  # 第2次读取，没有找到GNGGA数据
Not find GNRMC data.  # 第2次读取，没有找到GNRMC数据
continue read.        # 继续尝试读取下一包
Not find GNGGA data.  # 第3次读取，没有找到GNGGA数据
Not find GNRMC data.  # 第3次读取，没有找到GNRMC数据
continue read.        # 第3次依然失败，准备继续读取，判断出已经达到最大尝试次数，退出
128
#=========================================================================
gnss.read_gnss_data(debug=1)  # 设置读取解析过程输出详细信息
GGA data : ['GNGGA', '021224.000', '3149.27680', 'N', '11706.93369', 'E', '1', '19', '0.9', '168.2', 'M', '-5.0', 'M', '', '*52']  # 输出从原始GNSS数据中匹配到并简单处理后的GNGGA数据
RMC data : ['GNRMC', '021224.000', 'A', '3149.27680', 'N', '11706.93369', 'E', '0.00', '153.28', '110122', '', '', 'A', 'V*02']  # 输出从原始GNSS数据中匹配到并简单处理后的GNRMC数据
total_sen_num = 3, total_sat_num = 12  # 输出一组完整GPGSV语句总条数和可视卫星数量
# 下面是具体的匹配到的GPGSV语句信息
[0] : ['$GPGSV', '3', '1', '12', '10', '79', '210', '35', '12', '40', '070', '43', '21', '08', '305', '31', '23', '46', '158', '43', '0*6E']
[1] : ['$GPGSV', '3', '2', '12', '24', '', '', '26', '25', '54', '125', '42', '31', '', '', '21', '32', '50', '324', '34', '0*64']
[2] : ['$GPGSV', '3', '3', '12', '193', '61', '104', '44', '194', '58', '117', '42', '195', '05', '162', '35', '199', '', '', '32', '0*54']
4224
```

## 获取读取的原始GNSS数据

### `gnss.getOriginalData`

```python
gnss.getOriginalData()
```

该接口用于返回从串口读取的原始GNSS数据，如果用户希望拿到原始GNSS数据，自己进行处理或者进行一些数据确认，可以通过该接口来获取。该接口在每次调用 `gnss.read_gnss_data(max_retry=1, debug=0)`接口后，返回的即本次读取的原始数据。

**返回值描述**

返回从串口读取的原始GNSS数据，string类型。

**示例**

```python
data = gnss.getOriginalData()
print(data)
# 数据量较大，仅列出部分结果
00,A,3149.28094,N,11706.93869,E,0.00,153.28,110122,,,A,V*04
$GNVTG,153.28,T,,M,0.00,N,0.00,K,A*2E
$GNZDA,021555.000,11,01,2022,00,00*4D
$GPTXT,01,01,01,ANTENNA OK*35
$GNGGA,021556.000,3149.28095,N,11706.93869,E,1,24,0.6,166.5,M,-5.0,M,,*5E
$GNGLL,3149.28095,N,11706.93869,E,021556.000,A,A*47
$GNGSA,A,3,10,12,21,23,24,25,32,193,194,195,199,,1.0,0.6,0.8,1*35
$GNGSA,A,3,01,04,07,09,14,21,22,24,38,39,42,45,1.0,0.6,0.8,4*36
... 
$GNGGA,021600.000,3149.28096,N,11706.93877,E,1,25,0.6,166.4,M,-5.0,M,,*52
$GNGLL,3149.28096,N,11706.93877,E,021600.000,A,A*4B
$GNGSA,A,3,10,12,21,23,24,25,31,32,193,194,195,199,1.0,0.6,0.8,1*37
$GNGSA,A,3,01,04,07,09,$GNGGA,021601.000,3149.28096,N,11706.93878,E,1,25,0.6,166.4,M,-5.0,M,,*5C
$GNGLL,3149.2809
```

## 检查本次读取解析结果有效性

### `gnss.checkDataValidity`

```python
gnss.checkDataValidity()
```

GNSS模块提供的功能接口，所获取的数据都来源于从串口读出的原始GNSS数据包中的GNGGA、GNRMC和GPGSV语句，该接口用于检查读取的一包GNSS数据中，GNGGA、GNRMC和GPGSV语句的有效性。

**返回值描述**

返回一个列表，形式为 ` (gga_valid, rmc_valid, gsv_valid)`

`gga_valid` - 表示本次读取解析，是否匹配到GNGGA数据并解析成功，0表示没有匹配到GNGGA数据或数据无效，1表示有效；

`rmc_valid` - 表示本次读取解析，是否匹配到GNRMC数据并解析成功，0表述没有匹配到GNRMC数据或数据无效，1表示有效；

`gsv_valid` - 表示本地读取解析，是否匹配到GPGSV数据并解析成功，0表示没有匹配到GPGSV数据或数据无效，1表示有效。

如果用户只关心定位结果，即GNGGA数据是否有效，只要gga_valid参数为1即可（或者通过gnss.isFix()接口来判断定位是否成功），不一定要三个参数都为1；解析GNRMC数据是为了获取对地速度，解析GPGSV数据是为了获取可视卫星数量以及这些卫星对应的方位角，所以用户如果不关心这些参数，可忽略rmc_valid和gsv_valid。

**示例**

```python
gnss.checkDataValidity()
(1, 1, 1)  # 说明本次读取解析，GNGGA、GNRMC和GPGSV这三种数据都匹配成功并解析成功
```

## 检查是否定位成功

### `gnss.isFix`

```python
gnss.isFix()
```

检查指定串口是否读取到有效GNSS信息

**返回值描述**

`1`：定位成功

`0`：定位失败

**示例**

```
gnss.isFix()
1
```

## 获取定位的UTC时间

### `gnss.getUtcTime`

```python
gnss.getUtcTime()
```

获取GNSS信息中携带的时间

**返回值描述**

成功返回UTC时间，字符串类型，失败返回整型`-1`。

**示例**

```python
gnss.getUtcTime()
'06:22:05.000'  # hh:mm:ss.sss
```

## 获取GPS模块定位模式

### `gnss.getLocationMode`

```python
gnss.getLocationMode()
```

获取GNSS信息中携带的定位模式

**返回值描述**

| 返回值 | 描述                                     |
| ------ | ---------------------------------------- |
| -1     | 获取失败，串口未读到数据或未读到有效数据 |
| 0      | 定位不可用或者无效                       |
| 1      | 定位有效,定位模式：GPS、SPS 模式         |
| 2      | 定位有效,定位模式： DGPS、DSPS 模式      |
| 6      | 估算（航位推算）模式                     |

**示例**

```python
gnss.getLocationMode()
1
```

## 获取GPS模块定位使用卫星数量

### `gnss.getUsedSateCnt`

```python
gnss.getUsedSateCnt()
```

获取GNSS信息中携带的使用卫星数量

**返回值描述**

成功返回GPS模块定位使用卫星数量，返回值类型为整型，失败返回整型`-1`。

**示例**

```
gnss.getUsedSateCnt()
24
```

## 获取GPS模块定位的经纬度信息

### `gnss.getLocation`

```python
gnss.getLocation()
```

获取GNSS信息中携带的经纬度信息

**返回值描述**

成功返回GPS模块定位的经纬度信息，失败返回整型`-1`；成功时返回值格式如下：

`(longitude, lon_direction, latitude, lat_direction)`

`longitude` - 经度，float型

`lon_direction` - 经度方向，字符串类型，E表示东经，W表示西经

`latitude` - 纬度，float型

`lat_direction` - 纬度方向，字符串类型，N表示北纬，S表示南纬

**示例**

```python
gnss.getLocation()
(117.1156448333333, 'E', 31.82134916666667, 'N')
```

## 获取GPS模块定位可见卫星数量

### **`gnss.getViewedSateCnt`**

```python
gnss.getViewedSateCnt()
```

获取GNSS信息中携带的可见卫星数量

**返回值描述**

成功返回GPS模块定位可见卫星数量，整型值，失败返回整型-1。

**示例**

```python
gnss.getViewedSateCnt()
12
```

## 获取可视的GNSS卫星方位角

### **`gnss.getCourse`**

```python
gnss.getCourse()
```

获取GNSS信息中携带的卫星方位角

**返回值描述**

返回所有可视的GNSS卫星方位角，范围：`0 ~ 359`，以正北为参考平面。返回形式为字典，其中key表示卫星编号，value表示方位角。要注意，value的值可能是一个整型值，也可能是空，这取决于原始的GNSS数据中GPGSV语句中方位角是否有值，如获取失败返回-1。返回值形式如下：

`{key:value, ...,  key:value}`

**示例**

```python
 gnss.getCourse()
{'10': 204, '195': 162, '12': 68, '193': 105, '32': 326, '199': 162, '25': 122, '31': 247, '24': 52, '194': 116, '21': 304, '23': 159}
```

## 获取GPS模块定位海拔高度

### **`gnss.getGeodeticHeight`**

```python
gnss.getGeodeticHeight()
```

获取GNSS信息中携带的海拔高度

**返回值描述**

成功返回浮点类型海拔高度(单位:米)，失败返回整型`-1`。

**示例**

```python
gnss.getGeodeticHeight()
166.5
```

## 获取GPS模块对地速度

### `gnss.getSpeed`

```python
gnss.getSpeed()
```

获取GNSS信息中携带的对地速度

**返回值描述**

成功返回GPS模块对地速度(单位:KM/h)，浮点类型，失败返回整型`-1`

**示例**

```python
gnss.getSpeed()
0.0
```
