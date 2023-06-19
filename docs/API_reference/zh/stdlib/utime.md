# utime - 时间相关功能

`utime`模块用于获取当前时间、测量时间间隔和休眠。该模块实现相应CPython模块的子集。更多信息请参阅CPython文档：[time](https://docs.python.org/3.5/library/time.html#module-time)

**示例**：

```python
import utime
import log

# 设置日志输出级别
log.basicConfig(level=log.INFO)
time_log = log.getLogger("LocalTime")

if __name__ == '__main__':
    # 获取本地时间，返回元组
    tupe_t = utime.localtime()
    time_log.info(tupe_t)
    # 返回当前时间戳，参数为元组
    t = utime.mktime(utime.localtime())
    time_log.info(t)
    # 休眠sleep示例
    for i in [0, 1, 2, 3, 4, 5]:
        utime.sleep(1)   # 休眠(单位 m)
        time_log.info(i)

    for i in [0, 1, 2, 3, 4, 5]:
        utime.sleep_ms(1000)   # 休眠(单位 ms)
        time_log.info(i)
```



## 当前时间相关功能

### `utime.localtime`

```python
utime.localtime(secs)
```

将一个以秒为单位的时间转换为一个日期格式的时间并返回，或者返回本地RTC的时间，取决于参数`secs`是否提供。

**参数描述：**

- `secs`-int类型，一个以秒为单位的时间。

**返回值描述：**

`(year, month, day, hour, minute, second, weekday, yearday)`-类型为元组，包含了年、月、日、时、分、秒、星期、一年中第几天。当提供参数`secs`时，返回转换后的时间。当参数`secs`没有提供时，则返回本地RTC的时间。返回值含义如下：

| 元组成员 | 范围及类型             | 含义             |
| -------- | ---------------------- | ---------------- |
| year     | int型                  | 年份             |
| month    | int型，1~12            | 月份             |
| day      | int型，1~31            | 日，当月多少号   |
| hour     | int型，0~23            | 小时             |
| minute   | int型，0~59            | 分钟             |
| second   | int型，0~59            | 秒               |
| weekday  | int型，周一到周日是0~6 | 星期             |
| yearday  | int型                  | 一年中的第多少天 |

**示例**：

```python
>>> import utime
>>> utime.localtime()
(2020, 9, 29, 8, 54, 42, 1, 273)
>>> utime.localtime(646898736)
(1990, 7, 2, 14, 5, 36, 0, 183)
```

### `utime.mktime`

```python
utime.mktime(date)
```

将一个存放在元组中的日期格式的时间转换为以秒为单位的时间并返回。

**参数描述：**

- `date`-日期格式的时间，类型为元组，格式：(year, month, mday, hour, minute, second, weekday, yearday)。

**返回值描述：**

int类型。

**示例**：

```python
>>> import utime
>>> date = (2020, 9, 29, 8, 54, 42, 1, 273)
>>> utime.mktime(date)
1601340882
```

### `utime.time`

```python
utime.time()
```

返回自设备开机以来的秒数。

**返回值描述：**

int类型。

### `utime.getTimeZone`

```python
utime.getTimeZone()
```

获取当前时区。

**返回值描述：**

int类型，单位小时，范围[-12, 12]，负值表示西时区，正值表示东时区，0表示零时区。

### `utime.setTimeZone`

```python
utime.setTimeZone(offset)
```

设置时区。设置时区后，本地时间会随之变化为对应时区的时间。

**参数描述：**

- int类型，单位小时，范围[-12, 12]，负值表示西时区，正值表示东时区，0表示零时区。

**返回值描述：**

int类型，成功返回0，失败抛异常。

### `utime.getTimeZoneEx`

```python
utime.getTimeZoneEx()
```

获取当前时区（增强型），精度更高，可获取非整数时区。

**返回值描述：**

float类型，单位小时，范围[-12.0, 12.0]，负值表示西时区，正值表示东时区，0.0表示零时区。

> 增强型时区读取/设置接口须成对使用，如使用原有的时区接口读取非整数时区，会造成精度丢失。当前仅 EC200A 系列支持该功能。

### `utime.setTimeZoneEx`

```python
utime.setTimeZoneEx(offset)
```

设置时区（增强型），精度更高，可设置非整数时区。设置时区后，本地时间会随之变化为对应时区的时间。

**参数描述：**

- float类型，单位小时，范围[-12.0, 12.0]，最大精度为0.25小时（即参数须为0.25的整数倍）负值表示西时区，正值表示东时区，0.0表示零时区。

**返回值描述：**

int类型，成功返回0，失败抛异常。

> 增强型时区读取/设置接口须成对使用，如使用原有的时区接口读取非整数时区，会造成精度丢失。当前仅 EC200A 系列支持该功能。

## 测量时间间隔相关功能

### `utime.ticks_ms`

```python
utime.ticks_ms()
```

返回不断递增的毫秒计数器，在超过0x3FFFFFFF值后会重新计数。

**返回值描述：**

int类型，毫秒计数值，计数值本身无特定意义，只适合用在 `ticks_diff()`函数中。

### `utime.ticks_us`

```python
utime.ticks_us()
```

返回不断递增的微秒计数器，在超过0x3FFFFFFF值后会重新计数。

**返回值描述：**

int类型，微秒计数值，计数值本身无特定意义，只适合用在 `ticks_diff()`函数中。

### `utime.ticks_cpu`

```python
utime.ticks_cpu()
```

返回不断递增的cpu计数器，单位不确定，取决于硬件平台底层的时钟。

**返回值描述：**

int类型，计数值，计数值本身无特定意义，只适合用在 `ticks_diff()`函数中。

### `utime.ticks_diff`

```python
utime.ticks_diff(ticks1, ticks2)
```

计算两次调用` ticks_ms`， `ticks_us`，或 `ticks_cpu`之间的时间间隔。因为`ticks_xxx`这些函数的计数值可能会回绕，所以不能直接相减，需要使用 `ticks_diff`函数。通常用法是在带超时的轮询事件中调用。

**参数描述：**

- `ticks1`-int类型，第二次调用` ticks_ms`， `ticks_us`，或 `ticks_cpu`获取的tick值。
- `ticks2`-int类型，第一次调用` ticks_ms`， `ticks_us`，或 `ticks_cpu`获取的tick值。

**返回值描述：**

int类型，时间间隔，两次调用` ticks_ms`， `ticks_us`，或 `ticks_cpu`之间的时间间隔。单位和传入的`ticks2`和`ticks1`的单位一致。



> `ticks2`和`ticks1`的顺序不能颠倒，否则结果无法确定。且这个函数不要用在计算很长的时间间隔，具体限制为`ticks2`和`ticks1`的tick差值不能超过0x1FFFFFFF，否则结果无法确定。



**示例**：

```python
import utime
start = utime.ticks_us()
while True:
    if utime.ticks_diff(utime.ticks_us(), start) > 500:
        print('Timeout')
        break
```

## 休眠相关功能

### `utime.sleep`

```python
utime.sleep(seconds)
```

休眠给定秒数的时间。

**参数描述：**

- `seconds`-int类型，休眠的时长，单位秒。

### `utime.sleep_ms`

```python
utime.sleep_ms(ms)
```

休眠给定毫秒数的时间。

**参数描述：**

- `ms`-int类型，休眠的时长，单位毫秒。

### `utime.sleep_us`

```python
utime.sleep_us(us)
```

休眠给定微秒数的时间。

**参数描述：**

- `us`-int类型，休眠的时长，单位微秒。



> `utime.sleep`、`utime.sleep_ms`及`utime.sleep_us`函数的调用会导致程序休眠阻塞。