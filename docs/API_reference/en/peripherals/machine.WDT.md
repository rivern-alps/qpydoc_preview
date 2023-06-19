# class WDT – Watchdog Timer

This class provides system restart operation when application program exception occurs.

## Constructors

### `machine.WDT`

```python
class machine.WDT(period)
```

Creates a software watchdog object.

**Parameter:**

- `period` - Integer type. Set software watchdog detection time. Unit: second.  

**Return Value:**

Returns the software watchdog object.

## Methods

### `wdt.feed`

```python
wdt.feed()
```

This method feeds the watchdog.

**Return Value:**

Returns integer `0` when the execution is successful. 

### `wdt.stop`

```python
wdt.stop()
```

This method disables the software watchdog.

**Return Value:**

Returns integer `0` when the execution is successful.

**Example:**

```python
from machine import WDT
from machine import Timer
import utime


'''
The following two global variables are necessary. You can modify the values of these two global variables based on your actual projects.
'''
PROJECT_NAME = "QuecPython_WDT_example"
PROJECT_VERSION = "1.0.0"

timer1 = Timer(Timer.Timer1)

def feed(t):
    wdt.feed()


if __name__ == '__main__':
    wdt = WDT(20)  # Enables the watchdog and sets the timeout period
    timer1.start(period=15000, mode=timer1.PERIODIC, callback=feed)  # Feeds the watchdog

    # wdt.stop()

```
