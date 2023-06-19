# class PowerKey - power key按键回调注册功能

提供power key事件回调注册功能。

## 构造函数

### `misc.PowerKey`

```python
class misc.PowerKey()
```

**返回值描述：**

返回创建的对象。

**示例：**

```python
from misc import PowerKey
pk = PowerKey()
```

## 方法

### `PowerKey.powerKeyEventRegister`

```python
PowerKey.powerKeyEventRegister(usrFun)
```

该方法用于注册powerkey按键的回调函数。

**参数描述：**

- `usrfun`-回调函数，原型usrfun(status)，参数status，int类型：`0`表示松开，`1`表示按下；按下或松开powerkey按键时触发回调。

**返回值描述：**

`0`表示注册成功，`-1`表示注册失败。

> ECX00S/ECX00N/ECX00M/ECX00E系列，对于powerkey，按下和松开时，都会触发用户注册的回调函数；
>
> ECX00U/ECX00G系列，对于powerkey，只在按键松开时才会触发回调函数，并且按键按下的时间需要维持500ms以上；
>
> 上述所有平台在注册用户的回调函数后，powerkey长按不再触发关机。

**示例：**

EC600S/EC600N系列：

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

EC200U/EC600U系列：

```python
from misc import PowerKey

pk = PowerKey()

def pwk_callback(status):
	if status == 0: # 只有按键释放时才会触发回调
		print('powerkey release.')

pk.powerKeyEventRegister(pwk_callback)
```
