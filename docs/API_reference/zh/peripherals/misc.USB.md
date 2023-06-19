# class USB - USB插拔检测

提供USB插拔检测功能。

> EC600S/EC600N/EC800N/EG912N/EC200U/EC600U/EG915U/EC600M/EC800M/EC200A系列支持该功能。

## 构造函数

### `misc.USB`

```python
class misc.USB()
```

**示例：**

```python
from misc import USB
usb = USB()
```

## 方法

### `USB.getStatus`

```python
USB.getStatus()
```

该方法用于获取当前USB连接状态。

**返回值描述：**

`-1` 表示 获取状态失败，`0 `表示USB当前没有连接，`1 `表示 USB已连接。

### `usb.setCallback`

```
usb.setCallback(usrFun)
```

该方法用于注册USB插拔回调函数，当USB插入或者拔出时，会触发回调来通知用户当前USB状态。

**参数描述：**

- `usrFun` -回调函数，原型usrFun (conn_status)，参数conn_status：`0`表示未连接，`1`表示连接。

**返回值描述：**

`0`表示注册成功，`-1`表示注册失败。

> 回调函数中不要进行阻塞性的操作。

**示例：**

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

