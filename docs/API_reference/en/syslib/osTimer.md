# osTimer - OS Timer

The module provides a timer interface for the underlying OS. The OS timer timeout will trigger the bound callback function.

**Example**

```python
import osTimer

def test_cb(arg):
    print("osTimer Expired!!")
# Create an OS timer
timer = osTimer()
# Start the timer. The parameters are time, loop or not, and callback function.
timer.start(10000,1,test_cb)
# Stop the timer
timer.stop()
```


## Create Timer

### `osTimer`

```python
osTimer()
```

Creates an OS timer object.

> Compared with [machine.Timer](./machine.Timer.md), there is no limit on the number of created timers.

## Start Timer

### `osTimer.start`

```python
osTimer.start(initialTime, cyclialEn, callback)
```

**Parameter**                              

* `initialTime` - Integer type. The timeout for the timer. Unit: ms.
* `cyclialEn` - Integer type. Loop or not. 0 - Once. 1 - Loop. 
* `callback` - Function type. Callback function triggered when the timer expires. Prototype: *callback(arg)*. `arg` is not actually used and `None` can be configured directly.  

**Return Value**

Integer type.

0 - Successful execution

Other values - Failed execution

## Stop Timer

### `osTimer.stop`

```python
osTimer.stop()
```
Stops the timer. 

**Return Value**

Integer type.

0 - Successful execution

Other values - Failed execution