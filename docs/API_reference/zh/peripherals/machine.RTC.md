# class RTC – 实时时钟

该类提供获取设置rtc时间方法，对于BC25PA平台起到从深休眠或者软件关机状态唤醒模组的功能。

## 构造函数

### `machine.RTC`

```python
class machine.RTC()
```

**示例：**

```python
>>> # 创建RTC对象
>>> from machine import RTC
>>> rtc = RTC()
```

## 方法

### `rtc.datetime`

```python
rtc.datetime([year, month, day, week, hour, minute, second, microsecond])
```

该方法用于设置或获取RTC时间。不带参数时，用于获取时间，带参数则是设置时间；设置时间时，参数week不参与设置，microsecond参数保留，暂未使用，默认是0。

**参数描述：**

- `year` -  年，int类型。
- `month` - 月，int类型，范围[1 ~ 12]。
- `day` - 日，int类型，范围[1 ~ 31]。
- `week` - 星期，int类型，范围[0 ~ 6]，其中0表示周日，[1 ~ 6]分别表示周一到周六；设置时间时，该参数不起作用，保留；获取时间时该参数有效。
- `hour` - 时，int类型，范围[0 ~ 23]。
- `minute` - 分，int类型，范围[0 ~ 59]。
- `second` - 秒，int类型，范围[0 ~ 59]。
- `microsecond` - 微秒，int类型，保留参数，暂未使用，设置时间时该参数写0即可。

**返回值描述：**

获取时间时，返回一个元组，包含日期时间，格式如下：<br />`[year, month, day, week, hour, minute, second, microsecond]`

设置时间时，设置成功返回整型值`0`，设置失败返回整型值`-1` 。

**示例：**

```python
>>> from machine import RTC
>>> rtc = RTC()
>>> rtc.datetime()
(2020, 9, 11, 5, 15, 43, 23, 0)
>>> rtc.datetime([2020, 3, 12, 1, 12, 12, 12, 0])
0
>>> rtc.datetime()
(2020, 3, 12, 4, 12, 12, 14, 0)

```

### `rtc.set_alarm`

```python
rtc.set_alarm(data_e)
```

该方法用于设置RTC到期时间,时间到期就会调用注册的回调函数。

**参数描述：**

- `year` -  年，int类型。
- `month` - 月，int类型，范围[1 ~ 12]。
- `day` - 日，int类型，范围[1 ~ 31]。
- `week` - 星期，int类型，范围[0 ~ 6]，其中0表示周日，[1 ~ 6]分别表示周一到周六；设置时间时，该参数不起作用，保留；获取时间时该参数有效。
- `hour` - 时，int类型，范围[0 ~ 23]。
- `minute` - 分，int类型，范围[0 ~ 59]。
- `second` - 秒，int类型，范围[0 ~ 59]。
- `microsecond` - 微秒，int类型，保留参数，暂未使用，设置时间时该参数写0即可。

**返回值描述：**

设置成功返回整型值`0`，设置失败返回整型值`-1` 。

> 该方法支持平台EC600U/EC200U/EC600N/EC800N/BC25。

**示例：**

```python
>>> data_e=rtc.datetime()
>>> data_l=list(data_e)
>>> data_l[6] +=30				
>>> data_e=tuple(data_l)
>>> rtc.set_alarm(data_e)
0
```

### `rtc.register_callback`

```python
rtc.register_callback(callback)
```

该方法用于注册RTC alarm回调处理函数。

**参数描述：**

- `callback` - RTC alarm回调处理函数，function类型，原型为callback(arg)，`arg`未实际使用，可直接传入`None`。

**返回值描述：**

注册成功返回整型值`0`，注册失败返回整型值`-1` 。

> 该方法支持平台EC600U/EC200U/EC600N/EC800N/BC25。

### `rtc.enable_alarm`

```python
rtc.enable_alarm(on_off)
```

该方法用于打开/关闭RTC alarm功能。

**参数描述：**

- `on_off` - `1`表示打开RTC alarm功能，`0`表示关闭RTC alarm功能，int类型。

**返回值描述：**

打开/关闭成功返回整型值`0`，打开/关闭失败返回整型值`-1` 。

> 该方法支持平台EC600U/EC200U/EC600N/EC800N/BC25，BC25PA平台只有设置回调函数，才能启动定时器。

**示例：**

```python
from machine import RTC
rtc = RTC()
def callback(args):
   print('RTC alarm')

rtc.register_callback(callback)
rtc.set_alarm([2021, 7, 9, 5, 12, 30, 0, 0])
rtc.enable_alarm(1)
```

> EC600U/EC200U平台支持自动开机，即设置alarm功能之后将模块关机，alarm时间到了之后可以自动开机。其他平台不支持该特性。
