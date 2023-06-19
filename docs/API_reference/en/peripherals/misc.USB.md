# class USB - USB Plug-in/Out Detection

This class provides USB plug-in/out detection.

> Note: EC600S, EC600N, EC800N, EG912N, EC200U, EC600U, EG915U, EC600M, EC800M, EC200A series modules support this feature.

## Constructors

### `misc.USB`

```python
class misc.USB()
```

**Example:**

```python
from misc import USB
usb = USB()
```

## Methods

### `USB.getStatus`

```python
USB.getStatus()
```

This method gets the current USB connection status.

**Return Value:**

`-1` - Failed execution

`0 ` - Currently not connected to USB

`1 ` - USB connected

### `usb.setCallback`

```
usb.setCallback(usrFun)
```

This method registers USB plug-in/out callback function. When USB is inserted or unplugged, a callback function will be triggered to notify you of the current USB status. 

**Parameter:**

- `usrFun` - Callback function whose prototype is usrFun (conn_status). The parameter is conn_status with `0` indicating not connected and `1` indicating connected.

**Return Value:**

`0` - Successful registration

`-1` - Failed registration

> Note: please do not perform blocking operations in this callback function.

**Example:**

```python
from misc import USB

usb = USB()

def usb_callback(conn_status):
	status = conn_status
	if status == 0:
		print('USB is disconnected.')
	elif status == 1:
		print('USB is connected.')
usb.setCallback(usb_callback)
```

