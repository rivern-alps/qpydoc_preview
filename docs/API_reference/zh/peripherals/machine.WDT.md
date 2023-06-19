# class WDT – 看门狗定时器

该类提供APP应用程序发生异常不执行时进行系统重启操作。

## 构造函数

### `machine.WDT`

```python
class machine.WDT(period)
```

创建软狗对象。

**参数描述：**

- `period` - 设置软狗检测时间，单位(s），int类型。

**返回值描述：**

返回软狗对象。

## 方法

### `wdt.feed`

```python
wdt.feed()
```

该方法用于喂狗。

**返回值描述：**

成功返回整型值`0`。

### `wdt.stop`

```python
wdt.stop()
```

该方法用于关闭软狗功能。

**返回值描述：**

成功返回整型值`0`。

**使用示例：**

```python
from machine import WDT
from machine import Timer


timer1 = Timer(Timer.Timer1)

def feed(t):
    wdt.feed()


if __name__ == '__main__':
    wdt = WDT(20)  # 启动看门狗，设置超时时间
    timer1.start(period=15000, mode=timer1.PERIODIC, callback=feed)  # 使用定时器喂狗

    # wdt.stop()

```
