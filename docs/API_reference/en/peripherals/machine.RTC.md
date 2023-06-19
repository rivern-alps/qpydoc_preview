# RTC – Real Time Clock

This class provides methods of getting and setting RTC. For BC25PA series module, it provides the feature of waking up modules from deep sleep and software power-off state.

## Constructor

### `machine.RTC`

```python
class machine.RTC()
```

**Example:**

```python
>>> # Creates a RTC object
>>> from machine import RTC
>>> rtc = RTC()
```

## Methods

### `rtc.datetime`

```python
rtc.datetime([year, month, day, week, hour, minute, second, microsecond])
```

This method sets or gets RTC time. If this function contains parameters, this method sets the time otherwise this methods gets the time. When setting the time, you need not to set `week`.  `microsecond` is reserved and it is not currently used and its default value is 0.

**Parameter:**

- `year` - Integer type. Year.
- `month` - Integer type. Month. Range: [1–12].
- `day` - Integer type. Day. Range: [1–31].
- `week` - Integer type. Week. Range: [0–6]. 0 indicates Sunday. 1 to 6 indicates Monday to Saturday respectively. This parameter is reserved when setting time and it only takes effect when getting the time.   
- `hour` - Integer type. Hour. Range: [0–23].
- `minute` - Integer type. Minute. Range: [0–59].
- `second` - Integer type. Second. Range: [0–59].
- `microsecond` - Integer type. Microsecond. This parameter is reserved and it is not currently used. Set to 0 when you set the time.

**Return Value:**

A tuple containing a date and time.  <br />

`[year, month, day, week, hour, minute, second, microsecond]`

Set RTC time:

`0` - Successful execution

`-1` - Failed execution

**Example:**

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

This method sets RTC expiration time. The registered callback function will be called when the time expires.

**Parameter:**

- `year` - Integer type. Year.
- `month` - Integer type. Month. Range: [1–12].
- `day` - Integer type. Day. Range: [1–31].
- `week` - Integer type. Week. Range: [0–6]. 0 indicates Sunday. 1 to 6 indicates Monday to Saturday respectively. This parameter is reserved when setting time and it only takes effect when getting the time.   
- `hour` - Integer type. Hour. Range: [0-23].
- `minute` - Integer type. Minute. Range: [0-59].
- `second` - Integer type. Second. Range: [0-59].
- `microsecond` - Integer type. Microsecond. This parameter is reserved and it is not currently used. Set to 0 when you set the time.

**Return Value:**

 `0` - Successful execution

 `-1` - Failed execution

> Note: This method supports EC600U, EC200U, EC600N, EC800N and BC25 series modules.

**Example:**

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
rtc.register_callback(fun)
```

This method registers callback function of RTC alarm.

**Parameter:**

- `fun` - Function type. Callback function of RTC alarm.

**Return Value:**

 `0` - Successful execution

 `-1` - Failed execution

> Note: This method supports EC600U, EC200U, EC600N, EC800N and BC25 series modules.

### `rtc.enable_alarm`

```python
rtc.enable_alarm(on_off)
```

This method enables and disables RTC alarm.

**Parameter:**

- `on_off` - Integer type. `1` means to enable RTC alarm and `0` means to disable RTC alarm.

**Return Value:**

 `0` - Successful execution

 `-1` - Failed execution

> This method supports EC600U, EC200U, EC600N, EC800N and BC25 series modules. For BC25 series module, only when the callback function is set can RTC alarm be enabled.

**Example:**

```python
from machine import RTC
rtc = RTC()
def callback(args):
   print('RTC alarm')

rtc.register_callback(callback)
rtc.set_alarm([2021, 7, 9, 5, 12, 30, 0, 0])
rtc.enable_alarm(1)
```

> Only EC600U and EC200U series modules support automatic power-on. It means that if you power off the module after RTC alarm is set, the module will power on automatically when the alarm time expires.
