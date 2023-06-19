# utime - Time Related Features

`utime ` module gets the current time, measures the time interval and provides the feature of sleep, and realizes subsets of the corresponding CPython module. See CPython file [time](https://docs.python.org/3.5/library/time.html#module-time) for more detailed information.

**Example**

```python
'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module utime
@FilePath: example_utime_loacltime_file.py
'''
import utime
import log


'''
The following two global variables are necessary. You can modify the values of these two global variables based on your actual project
'''
PROJECT_NAME = "QuecPython_localtime_example"
PROJECT_VERSION = "1.0.0"


# Set the log output level
log.basicConfig(level=log.INFO)
time_log = log.getLogger("LocalTime")

if __name__ == '__main__':
    # Gets the local time and returns the tuple
    tupe_t = utime.localtime()
    time_log.info(tupe_t)
    # Returns the current timestamp. The parameter is tuple
    t = utime.mktime(utime.localtime())
    time_log.info(t)
    # Sleep example
    for i in [0, 1, 2, 3, 4, 5]:
        utime.sleep(1)   # Sleep(unit: m)
        time_log.info(i)

    for i in [0, 1, 2, 3, 4, 5]:
        utime.sleep_ms(1000)   # Sleep(unit: ms)
        time_log.info(i)
```



## The Current Time

### `utime.localtime`

```python
utime.localtime(secs)
```

Converts a time in seconds to a time in date format and returns it, or returns the local RTC time when `secs` is provided. 

**Parameter**

- `secs` - Integer type. The time in seconds.

**Return Value**

- `(year, month, mday, hour, minute, second, weekday, yearday)` - Tuple type. Contains year,  month, day, hour, minute, second, week, the day of the year. Returns the converted time when `secs` is provided. Returns the local RTC time when `secs` is not provided. The meaning of return values is below：

| Tuple Members | Range              | Meaning                    |
| ------------- | ------------------ | -------------------------- |
| year          | Integer type       | Year                       |
| month         | Integer type, 1–12 | Month                      |
| mday          | Integer type, 1–31 | Day, the date of the month |
| hour          | Integer type, 0–23 | Hour                       |
| minute        | Integer type, 0–59 | Minute                     |
| second        | Integer type, 0–59 | Second                     |
| weekday       | Integer type, 0–6  | Week                       |
| yearday       | Integer type       | The day of the year        |

**Example**

```python
>>> import utime
>>> utime.localtime()
(2020, 9, 29, 8, 54, 42, 1, 273)
>>> utime.localtime(646898736)
(2020, 7, 1, 6, 5, 36, 2, 183)
```

### `utime.mktime`

```python
utime.mktime(date)
```

Converts a time in date format stored in the tuple to a time in seconds and returns it.

**Parameter**

- `date `- Tuple type. The time in date format. Format: (year, month, mday, hour, minute, second, weekday, yearday).

**Return Value**

- Integer type. The time in seconds.

**Example**

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

Returns seconds since the device was enabled.

**Return Value**

- Integer type. The time in seconds.

### `utime.getTimeZone`

```python
utime.getTimeZone()
```

Gets the current time zone.

**Return Value**

- Unit: hour. Range: [-12, 12]. Negative values indicate the western time zone, positive values indicate the eastern time zone, and 0 indicates the zero time zone.

### `utime.setTimeZone`

```python
utime.setTimeZone(offset)
```

Sets the time zone. After the time zone is set, the local time will change to the time in the corresponding time zone.

**Parameter**

- Unite: hour. Range: [-12, 12]. Negative values indicate the western time zone, positive values indicate the eastern time zone, and 0 indicates the zero time zone.

## Measuring the Time Interval

### `utime.ticks_ms`

```python
utime.ticks_ms()
```

Returns an ascending millisecond counter. It will recount when the value exceeds 0x3FFFFFFF.

**Return Value**

- Millisecond count value. The count value itself has no specific meaning and is only suitable for `ticks_diff()`.

### `utime.ticks_us`

```python
utime.ticks_us()
```

Returns an ascending microsecond counter. It will recount when the value exceeds 0x3FFFFFFF.

**Return Value**

- Microsecond count value. The count value itself has no specific meaning and is only suitable for  `ticks_diff()`.

### `utime.ticks_cpu`

```python
utime.ticks_cpu()
```

Returns an ascending CPU counter. The unit depends on the underlying clock of the hardware platform.

**Return Value**

- Count value. The count value itself has no specific meaning and is only suitable for `ticks_diff()`.

### `utime.ticks_diff`

```python
utime.ticks_diff(ticks1, ticks2)
```

Calculates the time interval between calling ` ticks_ms` , `ticks_us`, or `ticks_cpu`  for the first time and the second time. Because the count value of `ticks_xxx` may be looped, it cannot be directly subtracted so `ticks_diff` should be called. Generally,`ticks_diff` should be called in the event loop with a timeout.

**Parameter**

- `ticks1`- Tick value obtained by calling ` ticks_ms`,  `ticks_us`, or  `ticks_cpu` for the second time.
- `ticks2`- Tick value obtained by calling ` ticks_ms`,  `ticks_us`, or  `ticks_cpu` for the first time.

**Return Value**

- Time interval. The time interval between calling ` ticks_ms`,  `ticks_us`, or `ticks_cpu` for the first time and the second time. The unit is the same as that of the passed `ticks2` and `ticks1`.

**Note**

The order of `ticks2` and `ticks1` cannot be reversed, otherwise the result cannot be determined. This function should not be used to calculate long intervals, that is, the tick difference between `ticks2` and `ticks1` cannot cannot exceeds 0x1FFFFFFF, otherwise the result cannot be determined.

**Example**

```python
import utime
start = utime.ticks_us()
while pin.value() == 0:
    if utime.ticks_diff(utime.ticks_us(), start) > 500:
        raise TimeoutError
```

## Sleep

### `utime.sleep`

```python
utime.sleep(seconds)
```

The given seconds of sleep.

**Parameter**

- `seconds`- The duration of sleep. Unit: second.

### `utime.sleep_ms`

```python
utime.sleep_ms(ms)
```

The given millisecond of sleep.

**Parameter**

`ms` - The duration of sleep. Unit: millisecond.

### `utime.sleep_us`

```python
utime.sleep_us(us)
```

The given microsecond of sleep.

**Parameter**

`us`- The duration of sleep. Unit: microsecond.

**Note**

Calling `utime.sleep`, `utime.sleep_ms` and `utime.sleep_us` will cause the program to block.

