# Timer - Control Hardware Timers

This class provides the method of controlling hardware timer.

> Note: For Timer0 to Timer3, each of them can only execute one task at the same time and multiple objects cannot use the same timer.

## Constructor

### `machine.Timer`

```python
class machine.Timer(Timern)
```

**Parameter:**

- `Timern` - Integer type. Timer number. Timer0 to Timer3 are supported.

**Example:**

```python
>>> # Creates a Timer object
>>> from machine import Timer
>>> timer1 = Timer(Timer.Timer1)
```

## Methods

### `timer.start`

```python
timer.start(period, mode, callback)
```

This method enables the timer.

**Parameter:**

- `period` - Integer type. Interruption period. Unit: millisecond. The period is greater than or equal to 1. 

- `mode` - Integer type. Running mode. <br />`ONE_SHOT` - Single mode indicating the time is executed for only once. <br />`PERIODIC` - Periodic mode indicates periodic execution. 

- `callback` - Function type. Timer execution function. 

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

**Example:**

```python
>>> def fun(args):
        print("###timer callback function###")
>>> timer1.start(period=1000, mode=timer1.PERIODIC, callback=fun)
0
###timer callback function###
###timer callback function###
###timer callback function###
……
```

### `timer.stop`

```python
timer.stop()
```

This method disables the timer.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

**Example:**

```python
import log
import utime
from machine import Timer
import checkNet


'''
The following two global variables are necessary. You can modify the values of these two global variables based on project requirement.
'''
PROJECT_NAME = "QuecPython_Timer_example"
PROJECT_VERSION = "1.0.0"

# Sets the log output level
log.basicConfig(level=log.INFO)
Timer_Log = log.getLogger("Timer")

num = 0
state = 1
# Note: EC100YCN series module supports Timer0 to Timer3. 
t = Timer(Timer.Timer1)

# Creates a execution function and enters an example of timer
def timer_test(t):
	global num
	global state
	Timer_Log.info('num is %d' % num)
	num += 1
	if num > 10:
		Timer_Log.info('num > 10, timer exit')
		state = 0
		t.stop()   # Ends the example of this timer


if __name__ == '__main__':
	t.start(period=1000, mode=t.PERIODIC, callback=timer_test)   # Enables the timer
```

## Constants

| Constant       | Description                                                |
| -------------- | ---------------------------------------------------------- |
| Timer.Timer0   | Timer 0                                                    |
| Timer.Timer1   | Timer 1                                                    |
| Timer.Timer2   | Timer 2                                                    |
| Timer.Timer3   | Timer 3                                                    |
| Timer.ONE_SHOT | Single mode indicating the time is executed for only once. |
| Timer.PERIODIC | Periodic mode indicates periodic execution.                |

