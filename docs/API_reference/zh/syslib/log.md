# log -日志输出

在程序开发中，日志（log）是一种用于记录应用程序在运行时状态的工具。它可以记录应用程序的运行情况，以及帮助开发人员诊断和解决问题。通过记录日志，开发人员可以更快地找到问题的根本原因，也可以更好地了解应用程序的行为和性能。`log` 模块可以输出不同级别的日志，包括调试信息、警告信息、错误信息等。



## 日志级别

### `log.DEBUG`

常量，用来标识LOG等级，最详细的日志信息，通常只在开发和调试时使用。

### `log.INFO`

常量，用来标识LOG等级，确认一切按预期运行。

### `log.WARNING`

常量，用来标识LOG等级，表明发生了一些意外，或者指示可能出现问题的情况，但仍然可以继续执行。

### `log.ERROR`

常量，用来标识LOG等级，由于更严重的问题，应用程序已不能执行某些功能。

### `log.CRITICAL`

常量，用来标识LOG等级，指出应用程序中的严重错误，可能导致应用程序停止运行。

## 日志设置

### `log.basicConfig`

设置日志输出级别，默认为log.INFO，系统只会输出 level 数值大于或等于该 level 的的日志结果。

```python
log.basicConfig(level)
```

**参数描述：**

* `level`-日志等级

**返回值描述：**

无

**示例：**

```python
import log
log.basicConfig(level=log.INFO)
```

### `log.set_output`

设置日志输出的位置，目前只支持uart和usys.stdout

```python
log.set_output(out)
```

**参数描述：**

* `out` - 日志输出位置，输出到指定串口或者交互口，默认不设置为交互口输出，类型参考示例

**返回值描述：**

无

**示例：**

```python
import log
log.basicConfig(level=log.INFO)
Testlog = log.getLogger("TestLog")

# 设置输出到debug口
from machine import UART
uart = UART(UART.UART0, 115200, 8, 0, 1, 0)

log.set_output(uart)

Testlog.info("this is a Test log") # 会输出带对应的uart口

# 从uart口切换成交互口输出
import usys
log.set_output(usys.stdout)

Testlog.info("this is a Test log") # 会输出到交互口
```

## 日志输出

### `log.getLogger`

获取log对象，对象支持输出不同等级的log信息。

```python
Testlog = log.getLogger(name)
```

**参数描述：**

* `name` - 当前log对象的主题信息，字符串类型

**返回值描述：**

*  log操作句柄，也可理解成log对象，拥有log输出的方法。

### `log.debug`

输出DEBUG级别的日志。

```python
Testlog.debug(msg)
```

**参数描述：**

* `msg` - 日志内容，字符串类型

### `log.info`

输出INFO级别的日志。

```python
Testlog.info(msg)
```

**参数描述：**

* `msg` - 日志内容，字符串类型

### `log.warning`

输出WARNING级别的日志。

```python
Testlog.warning(msg)
```

**参数描述：**

* `msg` - 日志内容，字符串类型

### `log.error`

输出ERROR级别的日志。

```python
Testlog.error(msg)
```

**参数描述：**

* `msg` - 日志内容，字符串类型

### `log.critical`

输出CRITICAL级别的日志。

```python
Testlog.critical(msg)
```

**参数描述：**

* `msg` - 日志内容，字符串类型


**示例：**

```python
import log

# 设置日志输出级别
log.basicConfig(level=log.INFO)
# 获取logger对象，如果不指定name则返回root对象，多次使用相同的name调用getLogger方法返回同一个logger对象
Testlog = log.getLogger("Quec")

Testlog.error("Test error message!!")
Testlog.debug("Test debug message!!")
Testlog.critical("Test critical message!!")
Testlog.info("Test info message!!")
Testlog.warning("Test warning message!!")
```



