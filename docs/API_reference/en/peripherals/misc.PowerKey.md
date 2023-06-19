# class PowerKey - PowerKey Callback and Registration

This class provides the feature of triggering the callback function when registering the powerkey event. 

## Constructors

### `misc.PowerKey`

```python
class misc.PowerKey()
```

**Return Value:**

Returns the created object. 

**Example：**

```python
from misc import PowerKey
pk = PowerKey()
```

## Methods

### `PowerKey.powerKeyEventRegister`

```python
PowerKey.powerKeyEventRegister(usrFun)
```

This method registers the callback function for the powerkey event.

**Parameter:**

- `usrfun` - Callback function whose prototype is usrfun (status). The parameter is status with `0` indicating to release and `1` indicating to press. The callback will be triggered when pressing or releasing the powerkey.

**Return Value:**

`0` - Successful registration

`-1 ` - Failed registration



> Note: For EC600S and EC600N series modules: The callback function will be triggered when pressing and releasing the powerkey. For EC200U and EC600U series modules: The callback function will be triggered only when releasing the powerkey and the key have been pressed for at least 500 ms.
>
> 

**Example:**

For EC600S and EC600N series modules:

```python
from misc import PowerKey

pk = PowerKey()

def pwk_callback(status):
	if status == 0:
		print('powerkey release.')
	elif status == 1:
		print('powerkey press.')
        
pk.powerKeyEventRegister(pwk_callback)
```

For EC200U and EC600U series modules:

```python
from misc import PowerKey

pk = PowerKey()

def pwk_callback(status):
	if status == 0: # The callback will be triggered only when the power key is released
		print('powerkey release.')

pk.powerKeyEventRegister(pwk_callback)
```
