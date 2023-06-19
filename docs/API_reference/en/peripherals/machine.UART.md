# UART - Duplex Serial Communication Bus

This class transmits data through the UART.

## Constructor

### `machine.UART`

```python
class machine.UART(UART.UARTn, buadrate, databits, parity, stopbits, flowctl)
```

**Parameter:**

- `UARTn` - Integer type. UART number. <br />`UART0` - DEBUG PORT<br />`UART1` - BT PORT<br />`UART2` - MAIN PORT<br />`UART3` - USB CDC PORT (BG95M3 series module does not support it.)<br />`UART4` - STDOUT PORT (Only EC200U/EC600U/EG915U series module supports it.  )

- `buadrate` - Integer type. Baud rate. Some common baud rates are supported, like `4800`, `9600`, `19200`, `38400`, `57600`, `115200` and `230400`. 
- `databits` - Integer type. Data bit. Range: [5–8]. EC600U/EC200U/EG915U series module only supports 8 data bits. 
- `parity` - Integer type. Parity check.  `0` – NONE, `1` – EVEN, `2` – ODD. 
- `stopbits` - Integer type. Stop bit. Range: [1–2].
- `flowctl` - Integer type. Hardware control flow.  `0` – FC_NONE,  `1` – FC_HW.

**UART Pin Correspondences:**

| Module        | Pin                                                          |
| ------------- | ------------------------------------------------------------ |
| EC600U        | UART1:<br />TX: pin124<br />RX: pin123<br />UART2:<br />TX: pin32<br />RX: pin31<br />UART4:<BR />TX: pin103<BR />RX: pin104 |
| EC200U        | UART1:<br />TX: pin138<br />RX: pin137<br />UART2:<br />TX: pin67<br />RX: pin68<br />UART4:<BR />TX: pin82<BR />RX: pin81 |
| EC200A        | UART1:<br />TX: pin63<br />RX: pin66<br />UART2:<br />TX: pin67<br />RX: pin68 |
| EC600S/EC600N | UART0:<br />TX: pin71<br />RX: pin72<br />UART1:<br />TX: pin3<br />RX: pin2<br />UART2:<br />TX: pin32<br />RX: pin31 |
| EC100Y        | UART0:<br />TX: pin21<br />RX: pin20<br />UART1:<br />TX: pin27<br />RX: pin28<br />UART2:<br />TX: pin50<br />RX: pin49 |
| EC800N        | UART0:<br />TX: pin39<br />RX: pin38<br />UART1:<br />TX: pin50<br />RX: pin51<br />UART2:<br />TX: pin18<br />RX: pin17 |
| BC25          | UART1:<br />TX: pin29<br />RX: pin28                         |
| BG95M3        | UART0:<br />TX: pin23<br />RX: pin22<br />UART1:<br />TX: pin27<br />RX: pin28<br />UART2:<br />TX: pin64<br />RX: pin65 |
| EC600M        | UART0:<br />TX: pin71<br />RX: pin72<br />UART1 (flowctl = 0):<br />TX: pin3<br />RX: pin2<br />UART1 (flowctl = 1):<br />TX: pin33<br />RX: pin34<br />UART2:<br />TX: pin32<br />RX: pin31 |
| EG915U        | UART1:<br />TX: pin27<br />RX: pin28<br />UART2:<br />TX: pin35<br />RX: pin34<br/>UART4:<br/>TX: pin19<br/>RX: pin18 |
| EC800M        | UART0:<br />TX: pin39<br />RX: pin38<br />UART1(flowctl = 0):<br />TX: pin50<br />RX: pin51<br />UART1(flowctl = 1):<br />TX: pin22<br />RX: pin23<br />Note: UART1 is unavailable for EC800M-CN_GA module. <br />UART2:<br />TX: pin18<br />RX: pin17 |
| EG912N        | UART0:<br />TX: pin23<br />RX: pin22<br />UART1 (flowctl = 0):<br />TX: pin27<br />RX: pin28<br/>UART1 (flowctl = 1):<br />TX: pin36<br />RX: pin37<br />UART2:<br />TX: pin34<br />RX: pin35 |

> When UART1 of EC600M/EC800M/EG912N series module is in flowctl = 1 state, modules only map UART1 to different pins but flow control is not enabled.

**Example:**

```python
>>> # Creates a UART object
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
```

## Methods

### `uart.any`

```python
uart.any()
```

This method gets the size of the unread data in the receiving cache.

**Return Value:**

Size of data that is unread in the receiving cache.

**Example:**

```python
>>> uart.any()
20 # It indicates that there is 20 bytes of unread data in the receiving cache.
```

### `uart.read`

```python
uart.read(nbytes)
```

This method reads data from the UART.

**Parameter:**

- `nbytes` - Integer type. Size of data to be read.  

**Return Value:**

Size of data that has been read.

### `uart.write`

```python
uart.write(data)
```

This method sends data to the UART.

**Parameter:**

- `data` - Bytes type. Data to be sent.  

**Return Value:**

Size of data that has been sent. 

### `uart.close`

```python
uart.close()
```

This method disables the UART.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `uart.control_485`

```python
uart.control_485(UART.GPIOn, direction)
```

This method controls the direction of RS-485 communication. Before and after sending data through the UART, the specified GPIO is pulled up and down to indicate the direction of RS-485 communication. 

**Parameter:**

- `GPIOn` - Integer type. GPIO numbers to be controlled. See [class Pin - Control I/O Pins](machine.Pin.md) for pin definitions. 

- `direction` - Integer type. Pin level change. <br />`1`  - The pin is pulled high before the data is sent through the UART, and pulled low after the data is sent.<br />

  `0` - The pin is pulled low before the data is sent through the UART, and pulled high after the data is sent.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

> Note: BC25 series/BG95-M3 series module does not support this method.

**Example:**

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
>>> uart1.control_485(UART.GPIO24, 1)
```

### `uart.set_callback`

```python
uart.set_callback(fun)
```

This method sets the callback function of the UART. This callback function will be triggered when data is received on the UART.

**Parameter:**

- `fun` - Callback function of the UART. Prototype:

  ```
  fun(result_list)
  ```

  Parameter of the callback function:

  - `result_list[0]`：Whether the data is received successfully. 

    0 - Received successfully

    Others - Receiving failed
  
  - `result_list[1]`：Port for receiving data.
  
  - `result_list[2]`：How much data is returned. 

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

**Example:**

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
>>> 
>>> def uart_call(para):
>>>		print(para)
>>> uart1.set_callback(uart_call)
```

**Example:**

```python
"""
Runnnig this routine, you need to connect the main port on the EVB to a PC by a USB-to-Serial Port Adapter, enable the main port by a UART tool on the PC and send data to this port. Then you can see the messages sent by PC.
"""
import _thread
import utime
import log
from machine import UART


'''
The following two global variables are necessary. You can modify the values of these two global variables based on your project requirements.
'''
PROJECT_NAME = "QuecPython_UART_example"
PROJECT_VERSION = "1.0.1"

'''
 * Parameter1: Port
        Note: For EC100Y-CN and EC600S-CN modules, descriptions of UARTn are as follows:
        UART0 - DEBUG PORT
        UART1 – BT PORT
        UART2 – MAIN PORT
        UART3 – USB CDC PORT
 * Parameter2：Baud rate
 * Parameter3：Data bits  (5—8)
 * Parameter4：Parity  （0：NONE  1：EVEN  2：ODD）
 * Parameter5：Stop bits (1–2)
 * Parameter6：Flow control (0: FC_NONE  1: FC_HW)
'''


# Sets the log output level
log.basicConfig(level=log.INFO)
uart_log = log.getLogger("UART")

class Example_uart(object):
    def __init__(self, no=UART.UART2, bate=115200, data_bits=8, parity=0, stop_bits=1, flow_control=0):
        self.uart = UART(no, bate, data_bits, parity, stop_bits, flow_control)
        self.uart.set_callback(self.callback)


    def callback(self, para):
        uart_log.info("call para:{}".format(para))
        if(0 == para[0]):
            self.uartRead(para[2])

    
    def uartWrite(self, msg):
        uart_log.info("write msg:{}".format(msg))
        self.uart.write(msg)

    def uartRead(self, len):
        msg = self.uart.read(len)
        utf8_msg = msg.decode()
        uart_log.info("UartRead msg: {}".format(utf8_msg))
        return utf8_msg

    def uartWrite_test(self):
        for i in range(10):
            write_msg = "Hello count={}".format(i)
            self.uartWrite(write_msg)
            utime.sleep(1)

if __name__ == "__main__":
    uart_test = Example_uart()
    uart_test.uartWrite_test()
    

# Examples of running results
'''
INFO:UART:write msg:Hello count=0
INFO:UART:write msg:Hello count=1
INFO:UART:write msg:Hello count=2
INFO:UART:write msg:Hello count=3
INFO:UART:write msg:Hello count=4
INFO:UART:write msg:Hello count=5
INFO:UART:write msg:Hello count=6
INFO:UART:write msg:Hello count=7
INFO:UART:write msg:Hello count=8
INFO:UART:write msg:Hello count=9

INFO:UART:call para:[0, 2, 15]
INFO:UART:UartRead msg: my name is XXX


'''

```

## Constants

| Constant   | Description |
| ---------- | ----------- |
| UART.UART0 | UART0       |
| UART.UART1 | UART1       |
| UART.UART2 | UART2       |
| UART.UART3 | UART3       |
| UART.UART4 | UART4       |

