# class ExtInt - 外部中断

该类用于配置I/O引脚在发生外部事件时中断。

## 构造函数

### `machine.ExtInt`

```python
class machine.ExtInt(GPIOn, mode, pull, callback)
```

**参数描述：**

- `GPIOn` - 需要控制的GPIO引脚号，int类型，参照[Pin模块](./machine.Pin.md)的引脚定义(除BG95M3外)，<a href="#BG95M3_label_pinmap">点此查看</a>BG95M3平台引脚对应关系

- `mode` - 触发方式，int类型，说明如下：<br />`IRQ_RISING` – 上升沿触发<br />`IRQ_FALLING` – 下降沿触发<br />`IRQ_RISING_FALLING` – 上升和下降沿触发(EC600E/EC800E不支持)

- `pull` - 上下拉模式，int类型，说明如下：<br />`PULL_PU` – 上拉模式 <br />`PULL_PD`  – 下拉模式<br />`PULL_DISABLE` – 浮空模式

- `callback` - 中断触发回调函数，int类型，说明如下：<br />返回参数为长度为2的元组<br />args[0]: gpio号<br />args[1]: 触发沿（0：上升沿 1：下降沿）

<details>
  <summary><span id="BG95M3_label_pinmap"></span>BG95M3平台引脚对应关系<br /></summary>
GPIO2 – 引脚号5<br />GPIO3 – 引脚号6<br />GPIO6 – 引脚号19<br />GPIO7 – 引脚号22<br />GPIO8 – 引脚号23<br />GPIO9 – 引脚号25<br />GPIO11 – 引脚号27<br />GPIO12 – 引脚号28<br />GPIO14 – 引脚号41<br />GPIO16 – 引脚号65<br/>GPIO17 – 引脚号66<br />GPIO18 – 引脚号85<br />GPIO19 – 引脚号86<br />GPIO20 – 引脚号87<br />GPIO21 – 引脚号88
</details>

**示例：**

```python
>>> # 创建ExtInt对象
>>> from machine import ExtInt
>>> def fun(args):
        print('### interrupt  {} ###'.format(args)) # args[0]:gpio号 args[1]:上升沿或下降沿
>>> extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun)
```

## 方法

### `extint.enable`

```
extint.enable()
```

该方法用于使能中断，使能extint对象外部中断，当中断引脚收到上升沿或者下降沿信号时，会调用callback执行。

**返回值描述：**

使能成功返回整型值`0`，使能失败返回整型值`-1`。

### `extint.disable`

```
extint.disable()
```

该方法用于关闭中断，禁用与extint对象关联的中断 。

**返回值描述：**

使能成功返回整型值`0`，使能失败返回整型值`-1`。

### `extint.line`

```
extint.line()
```

该方法用于读取引脚映射行号。

**返回值描述：**

返回引脚映射的行号。

**示例：**

```python
>>> extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun)
>>> extint.line()
1
```

### `extint.read_count`

```
extint.read_count(is_reset)
```

该方法用于返回触发中断的次数。

**参数描述：**

- `is_reset` - 读取后是否重置计数，int类型，`0`表示不重置，`1`表示重置。

**返回值描述：**

返回列表 `[rising_count, falling_count]`<br />`rising_count`：上升沿触发中断的次数<br />`falling_count`：下降沿触发中断的次数

### `extint.count_reset`

```
extint.count_reset()
```

该方法用于清空触发中断的次数。

**返回值描述：**

返回`0`表示成功，返回其他表示失败。

### `extint.read_level`

```
extint.read_level()
```

该方法用于读取当前引脚电平。

**返回值描述：**

返回引脚电平，`0`表示获取到的引脚电平为低电平，`1` 表示获取到的引脚电平为高电平。