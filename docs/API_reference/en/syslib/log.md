# log - Output Log

A log is a tool used to record the runtime state of an application in program development, as well as help developers diagnose and troubleshoot problems. Developers can quickly identify the root causes of problems and better understand the behaviors and performance of applications by viewing logs. `log` feature can output different log levels, including the DEBUG level, WARNING level, and ERROR level.



## Log Level

### `log.DEBUG`

Constant of log level. The most detailed information is recorded at the DEBUG level and this level is usually used in development and debugging.

### `log.INFO`

Constant of log level.  The information recorded at the INFO level indicates that everything is running normally.

### `log.WARNING`

Constant of log level.  The information recorded at the WARNING level indicates that something unexpected has occurred or potentially harmful events, but the application can continue to function normally.

### `log.ERROR`

Constant of log level. The information recorded at the ERROR level indicates that an application is no longer able to execute certain functions due to some serious problems.

### `log.CRITICAL`

Constant of log level. The information recorded at the CRITICAL level indicates a critical error in the application that may stop the application from running. 

## Set Log

### `log.basicConfig`

Sets the log output level. Default level: log.INFO. The system will only output logs whose levels are greater than or equal to that level.

```python
log.basicConfig(level)
```

**Parameter**

* `level` - Log level.

**Return Value**

None

**Example**

```python
import log
log.basicConfig(level=log.INFO)
```

### `log.set_output`

Destination where the logs are output. Currently only uart and usys.stdout are supported.

```python
log.set_output(out)
```

**Parameter**

* `out` - The destination where the logs are output. Set the parameter to a specified serial port or the interaction port. Default value: the interaction port. 

**Return Value**

None

**Example**

```python
import log
log.basicConfig(level=log.INFO)
Testlog = log.getLogger("TestLog")

# Output the log through the debug UART
from machine import UART
uart = UART(UART.UART0, 115200, 8, 0, 1, 0)

log.set_output(uart)

Testlog.info("this is a Test log") # The logs will be output through the specified UART.

# Output the log through the interaction port
import usys
log.set_output(usys.stdout)

Testlog.info("this is a Test log") # The logs will be output through the interaction port.
```

## Output Log

### `log.getLogger`

Gets the log object which supports logs of different levels.

```python
Testlog = log.getLogger(name)
```

**Parameter**

* `name` - String type. The topic of the current log object

**Return Value**

*  A log handle (log object) with the method of outputting logs.

### `log.debug`

Outputs the DEBUG-level logs. 

```python
Testlog.debug(msg)
```

**Parameter**

* `msg` - String type. The content of logs.

### `log.info`

Outputs the INFO-level logs.

```python
Testlog.info(msg)
```

**Parameter**

* `msg` - String type. The content of logs.

### `log.warning`

Outputs the WARNING-level logs.

```python
Testlog.warning(msg)
```

**Parameter**

* `msg` - String type. The content of logs.

### `log.error`

Outputs the ERROR-level logs.

```python
Testlog.error(msg)
```

**Parameter**

* `msg` - String type. The content of logs.

### `log.critical`

Outputs the CRITICAL-level logs.

```python
Testlog.critical(msg)
```

**Parameter**

* `msg` - String type. The content of logs.

**Example**

```python
import log

# Set the log output level.
log.basicConfig(level=log.INFO)
# Get the logger object. If "name" is not specified, the default value "root" will be configured. If the "name" is set to the same value multiple times, the same logger object will be returned.
Testlog = log.getLogger("Quec")

Testlog.error("Test error message!!")
Testlog.debug("Test debug message!!")
Testlog.critical("Test critical message!!")
Testlog.info("Test info message!!")
Testlog.warning("Test warning message!!")
```



