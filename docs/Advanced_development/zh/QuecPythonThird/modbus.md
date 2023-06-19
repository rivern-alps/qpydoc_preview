

## **Modubus使用说明_V1.0**



## 文档历史

**修订记录**

| **版本** | **日期**   | **作者**     | **变更表述** |
|----------|------------|--------------|--------------|
| 1.0      | 2021-09-14 | Jeremy.Jiang | 初始版本     |

## 基本概述

本文档主要基于modbus DTU使用。

## modbus使用示例

```python
from usr.sensor import ModbusInit
import usr.uModBusConst as Const
from machine import UART
import utime as time

# LightSensor UART info
uart_port = UART.UART0
bardrate = 9600
databits = 8
parity = 0
stopbit = 1
flowctl = 0
# sensor addrinfo
slave = 0x01
const = Const.READ_HOLDING_REGISTERS
start_addr = 0X03
coil_qyt = 0x02
# light data transfer
def light_data_transfer(ret_str):
    str_list = list(map(lambda x: x.decode("utf-8"), ret_str.split(b",")))
    data_bits = int(str_list[2])
    data_list = str_list[3: 3+data_bits]
    one_place = int("0x" + data_list[0] + data_list[1], 16)
    tens_place = int("0x" + data_list[2] + data_list[3], 16)
    return tens_place * 10 + one_place

if __name__ == '__main__':
    modbus = ModbusInit(uart_port, bardrate, databits, parity, stopbit, flowctl)
    while True:
        modbus.write_coils(slave, const, start_addr, coil_qyt)
        ret_str = modbus.read_uart()
        print(ret_str)
        digit_val = light_data_transfer(ret_str)
        print(digit_val)
        time.sleep_ms(1000)
```



## modbus API 使用说明

### modbus_utils.init(uartN, buadrate, databits, parity, stopbit, flowctl)

初始化UART接口

| **参数** | **类型** | **说明**                                                                                  |
|----------|----------|-------------------------------------------------------------------------------------------|
| uartN    | int      | UARTn作用如下： UART0 - DEBUG PORT UART1 – BT PORT UART2 – MAIN PORT UART3 – USB CDC PORT |
| buadrate | int      | 波特率，常用波特率都支持，如4800、9600、19200、38400、57600、115200、230400等             |
| databits | int      | 数据位（5\~8），展锐平台当前仅支持8位                                                     |
| parity   | int      | 奇偶校验（0 – NONE，1 – EVEN，2 - ODD）                                                   |
| stopbits | int      | 停止位（1\~2）                                                                            |
| flowctl  | int      | 硬件控制流（0 – FC_NONE， 1 – FC_HW）                                                     |

### modbus_utils.divmod_low_high(addr)

分割地址高低位

| **输入参数** | **类型** | **说明**     |
|--------------|----------|--------------|
| addr         | int      | 十六进制地址 |

| **返回值** | **类型** | **说明**         |
|------------|----------|------------------|
| high       | int      | 高位十六进制地址 |
| low        | int      | 低位十六进制地址 |

### modbus_utils.calc_crc(string_byte)

计算bytearray校验位值

| **参数**    | **类型**  | **说明**  |
|-------------|-----------|-----------|
| string_byte | bytearray | bytearray |

| **返回值类型** | **类型** | **说明**    |
|----------------|----------|-------------|
| crc_high       | int      | CRC高位地址 |
| crc_low        | int      | CRC低位地址 |

### modbus_utils.split_return_bytes(ret_bytes)

切分从UART口读取的bytes并转换为bytesarray

| **参数**  | **类型** | **说明** |
|-----------|----------|----------|
| ret_bytes | bytes    | bytes    |

| **返回值类型** | **类型** | **说明**                                     |
|----------------|----------|----------------------------------------------|
| bytes_split    | list     | bytes切分后的列表，格式：[b’00’, b’1E’, …..] |

### modbus_utils.read_uart()

读取uart的数据,并返回bytes值

| **返回值类型** | **类型** | **说明**             |
|----------------|----------|----------------------|
| bytes_string   | bytes    | 格式：b”01,1E,1F…..” |

### modbus_utils.write_coils(slave, const, start, coil_qty, crc_flag=True)

写线圈操作

| **参数** | **类型** | **说明**     |
|----------|----------|--------------|
| slave    | int      | 设备地址     |
| const    | int      | 功能码       |
| start    | int      | 起始地址     |
| coil_qty | int      | 读取线圈数   |
| crc_flag | bool     | 是否需要校验 |

| **返回值类型** | **类型** | **说明** |
|----------------|----------|----------|
| status         | bool     | 返回True |

### modbus_utils.write_coils_any(\*args, crc_flag=True)

任意写入线圈地址操作

| **参数** | **类型** | **说明**             |
|----------|----------|----------------------|
| args   | list     | 任意的byte组成的list |
| crc_flag | bool     | 是否需要校验         |

## uModBusConst功能码清单

| **名称**                      | **地址** |
|-------------------------------|----------|
| READ_DISCRETE_INPUTS          | 0X02     |
| READ_COILS                    | 0X01     |
| WRITE_SINGLE_COIL             | 0X05     |
| WRITE_MULTIPLE_COILS          | 0X0F     |
| READ_INPUT_REGISTER           | 0X04     |
| READ_HOLDING_REGISTERS        | 0X03     |
| WRITE_SINGLE_REGISTER         | 0X06     |
| WRITE_MULTIPLE_REGISTERS      | 0X10     |
| READ_WRITE_MULTIPLE_REGISTERS | 0X17     |
| MASK_WRITE_REGISTER           | 0X16     |
| READ_FIFO_QUEUE               | 0X18     |
| READ_FILE_RECORD              | 0X14     |
| WRITE_FILE_RECORD             | 0X15     |
| READ_EXCEPTION_STATUS         | 0X07     |
| DIAGNOSTICS                   | 0X08     |
| GET_COM_EVENT_COUNTER         | 0X0B     |
| GET_COM_EVENT_LOG             | 0X0C     |
| REPORT_SERVER_ID              | 0X11     |
| READ_DEVICE_IDENTIFICATION    | 0X2B     |

## 下载代码
  <a href="code/modbus.zip" target="_blank">下载代码</a>