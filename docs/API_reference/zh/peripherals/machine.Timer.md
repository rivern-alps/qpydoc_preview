# class Timer - 硬件定时器

该类提供硬件定时器功能。

> 使用该定时器时需注意定时器0-3，每个在同一时间内只能执行一件任务，且多个对象不可使用同一个定时器。

## 构造函数

### `machine.Timer`

```python
class machine.Timer(Timern)
```

**参数描述：**

- `Timern` - 定时器号，int类型，支持定时器Timer0 ~ Timer3。

**示例：**

```python
>>> # 创建Timer对象
>>> from machine import Timer
>>> timer1 = Timer(Timer.Timer1)
```

## 方法

### `timer.start`

```python
timer.start(period, mode, callback)
```

该方法用于启动定时器。

**参数描述：**

- `period` - 中断周期，int类型，单位毫秒，大于等于1。

- `mode` - 运行模式，int类型，说明如下：<br />`ONE_SHOT` - 单次模式，定时器只执行一次<br />`PERIODIC` - 周期模式，循环执行

- `callback` - 定时器执行函数，function类型，原型为callback(arg)，`arg`未实际使用，可直接传入`None`。callback函数触发后，必须调用stop接口停止该定时器，否则下次调用start接口后，callback不会被执行。

**返回值描述：**

启动成功返回整型值`0`，失败返回整型值`-1`。

**示例：**

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

该方法用于关闭定时器。

**返回值描述：**

成功返回整型值`0`，失败返回整型值`-1`。

**使用示例**：

```python
import log
import utime
from machine import Timer
import checkNet

# 设置日志输出级别
log.basicConfig(level=log.INFO)
Timer_Log = log.getLogger("Timer")

num = 0
state = 1
# 注：EC100YCN支持定时器Timer0 ~ Timer3
t = Timer(Timer.Timer1)

# 创建一个执行函数，并将timer实例传入
def timer_test(t):
	global num
	global state
	Timer_Log.info('num is %d' % num)
	num += 1
	if num > 10:
		Timer_Log.info('num > 10, timer exit')
		state = 0
		t.stop()   # 结束该定时器实例


if __name__ == '__main__':
	t.start(period=1000, mode=t.PERIODIC, callback=timer_test)   # 启动定时器
```

## 常量

| 常量           | 说明                       |
| -------------- | -------------------------- |
| Timer.Timer0   | 定时器0                    |
| Timer.Timer1   | 定时器1                    |
| Timer.Timer2   | 定时器2                    |
| Timer.Timer3   | 定时器3                    |
| Timer.ONE_SHOT | 单次模式，定时器只执行一次 |
| Timer.PERIODIC | 周期模式，定时器循环执行   |

