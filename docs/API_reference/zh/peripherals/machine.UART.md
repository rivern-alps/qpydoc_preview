# class UART - 串口通信

该类提供uart串口数据传输功能。

## 构造函数

### `machine.UART`

```python
class machine.UART(UART.UARTn, baudrate, databits, parity, stopbits, flowctl)
```

**参数描述：**

- `UARTn` - UART编号，int类型，UARTn说明如下：<br />`UART0` - DEBUG PORT<br />`UART1` - BT PORT<br />`UART2` - MAIN PORT<br />`UART3` - USB CDC PORT (不支持BG95M3)<br />`UART4` - STDOUT PORT (仅支持EC200U/EC600U/EG915U)

- `baudrate` - 波特率，int类型，支持常用波特率，如`4800`、`9600`、`19200`、`38400`、`57600`、`115200`、`230400`等。
- `databits` - 数据位[5 ~ 8]，int类型，EC600U/EC200U/EG915U仅支持8位。
- `parity` - 奇偶校验(`0` – NONE，`1` – EVEN，`2` – ODD)，int类型。
- `stopbits` - 停止位[1 ~ 2]，int类型。
- `flowctl` - 硬件控制流(`0` – FC_NONE， `1` – FC_HW)，int类型。

**UART引脚对应关系 ：**

| 平台          | 引脚                                                         |
| ------------- | ------------------------------------------------------------ |
| EC600U        | uart1:<br />TX: 引脚号124<br />RX: 引脚号123<br />uart2:<br />TX:引脚号32<br />RX:引脚号31<br />uart4:<BR />TX:引脚号103<BR />RX:引脚号104 |
| EC200U        | uart1:<br />TX: 引脚号138<br />RX: 引脚号137<br />uart2:<br />TX:引脚号67<br />RX:引脚号68<br />uart4:<BR />TX:引脚号82<BR />RX:引脚号81 |
| EC200A        | uart1:<br />TX: 引脚号63(EC200ACN_LA: 引脚号26)<br />RX: 引脚号66(EC200ACN_LA: 引脚号27)<br />uart2:<br />TX:引脚号67<br />RX:引脚号68<br />注意:EC200ACN_LA模组uart1引脚号与其他型号不同 |
| EC600S/EC600N | uart0:<br />TX: 引脚号71<br />RX: 引脚号72<br />uart1:<br />TX: 引脚号3<br />RX: 引脚号2<br />uart2:<br />TX:引脚号32<br />RX:引脚号31 |
| EC100Y        | uart0:<br />TX: 引脚号21<br />RX: 引脚号20<br />uart1:<br />TX: 引脚号27<br />RX: 引脚号28<br />uart2:<br />TX:引脚号50<br />RX:引脚号49 |
| EC800N        | uart0:<br />TX: 引脚号39<br />RX: 引脚号38<br />uart1:<br />TX: 引脚号50<br />RX: 引脚号51<br />uart2:<br />TX:引脚号18<br />RX:引脚号17 |
| BC25PA        | uart1:<br />TX: 引脚号29<br />RX: 引脚号28                   |
| BG95M3        | uart0:<br />TX: 引脚号23<br />RX: 引脚号22<br />uart1:<br />TX:引脚号27<br />RX:引脚号28<br />uart2:<br />TX: 引脚号64<br />RX: 引脚号65 |
| EC600M        | uart0:<br />TX: 引脚号71<br />RX: 引脚号72<br />uart1(flowctl = 0):<br />TX: 引脚号3<br />RX: 引脚号2<br />uart1(flowctl = 1):<br />TX: 引脚号33<br />RX: 引脚号34<br />uart2:<br />TX:引脚号32<br />RX:引脚号31 |
| EG915U        | uart1:<br />TX: 引脚号27<br />RX: 引脚号28<br />uart2:<br />TX:引脚号35<br />RX:引脚号34<br/>uart4:<br/>TX:引脚号19<br/>RX:引脚号18 |
| EC800M/EG810M | uart0:<br />TX: 引脚号39<br />RX: 引脚号38<br />uart1(flowctl = 0):<br />TX: 引脚号50<br />RX: 引脚号51<br />uart1(flowctl = 1):<br />TX: 引脚号22<br />RX: 引脚号23<br />注意:EC800M/EG810MCN_GA uart1不可用<br />uart2:<br />TX:引脚号18<br />RX:引脚号17 |
| EG912N        | uart0:<br />TX: 引脚号23<br />RX: 引脚号22<br />uart1(flowctl = 0):<br />TX: 引脚号27<br />RX: 引脚号28<br/>uart1(flowctl = 1):<br />TX: 引脚号36<br />RX: 引脚号37<br />uart2:<br />TX:引脚号34<br />RX:引脚号35 |
| EC600E        | uart0:<br />TX: 引脚号71<br />RX: 引脚号72<br />uart1:<br />TX:引脚号70<br />RX:引脚号69<br />uart2:<br />TX:引脚号32<br />RX:引脚号31 |
| EC800E        | uart0:<br />TX: 引脚号39<br />RX: 引脚号38<br />uart1:<br />TX:引脚号29<br />RX:引脚号28<br />uart2:<br />TX:引脚号18<br />RX:引脚号17 |

> EC600M/EC800M/EG810M/EG912N 的uart1在flowctl = 1时，仅将uart1映射到不同的引脚，未开启流控功能。

**示例：**

```python
>>> # 创建uart对象
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
```

## 方法

### `uart.any`

```python
uart.any()
```

该方法用于获取接收缓存未读数据大小。

**返回值描述：**

返回接收缓存器中有多少字节的数据未读。

**示例：**

```python
>>> uart1.any()
20 #表示接收缓冲区中有20字节数据未读
```

### `uart.read`

```python
uart.read(nbytes)
```

该方法用于从串口读取数据。

**参数描述：**

- `nbytes` - 要读取的字节数，int类型。

**返回值描述：**

返回读取的数据。

### `uart.write`

```python
uart.write(data)
```

该方法用于发送数据到串口。

**参数描述：**

- `data` - 发送的数据，bytes类型。

**返回值描述：**

返回发送的字节数。

### `uart.close`

```python
uart.close()
```

该方法用于关闭串口。

**返回值描述：**

成功返回整型值`0`，失败返回整型值`-1`。

### `uart.control_485`

```python
uart.control_485(UART.GPIOn, direction)
```

该方法用于控制485通信方向，串口发送数据之前和之后进行拉高拉低指定GPIO，用来指示485通信的方向。

**参数描述：**

- `GPIOn` - 需要控制的GPIO引脚号，参照[Pin模块](machine.Pin.md)的引脚定义，int类型。

- `direction` - 引脚电平变化，int类型，说明如下：<br />`1`表示引脚电平变化为：串口发送数据之前由低拉高、发送数据之后再由高拉低<br />`0`表示引脚电平变化为：串口发送数据之前由高拉低、发送数据之后再由低拉高

**返回值描述：**

成功返回整型值`0`，失败返回整型值`-1`。

> BC25PA/BG95M3平台不支持此方法。

**示例：**

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
>>> uart1.control_485(UART.GPIO24, 1)
```

### `uart.set_callback`

```python
uart.set_callback(fun)
```

该方法用于设置串口数据回调，串口收到数据后，会执行该回调。

**参数描述：**

- `fun` - 串口回调函数，回调函数原型：

  ```
  fun(result_list)
  ```

  回调函数参数描述：

  - `result_list[0]`：接收是否成功(0：成功，其它：失败)

  - `result_list[1]`：接收端口

  - `result_list[2]`：返回有多少数据

**返回值描述：**

成功返回整型值`0`，失败返回整型值`-1`。

**示例：**

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
>>> 
>>> def uart_call(para):
>>>		print(para)
>>> uart1.set_callback(uart_call)
```

**使用示例：**

```python
"""
运行本例程，需要通过串口线连接开发板的 MAIN 口和PC，在PC上通过串口工具
打开 MAIN 口，并向该端口发送数据，即可看到 PC 发送过来的消息。
"""
import _thread
import utime
import log
from machine import UART

'''
 * 参数1：端口
        注：EC100YCN平台与EC600SCN平台，UARTn作用如下
        UART0 - DEBUG PORT
        UART1 – BT PORT
        UART2 – MAIN PORT
        UART3 – USB CDC PORT
 * 参数2：波特率
 * 参数3：data bits  （5~8）
 * 参数4：Parity  （0：NONE  1：EVEN  2：ODD）
 * 参数5：stop bits （1~2）
 * 参数6：flow control （0: FC_NONE  1：FC_HW）
'''


# 设置日志输出级别
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
    

# 运行结果示例
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

## 常量

| 常量       | 说明  |
| ---------- | ----- |
| UART.UART0 | UART0 |
| UART.UART1 | UART1 |
| UART.UART2 | UART2 |
| UART.UART3 | UART3 |
| UART.UART4 | UART4 |

