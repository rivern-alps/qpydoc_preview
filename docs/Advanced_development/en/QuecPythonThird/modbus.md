

## Application Note of Modbus _V1.0



## About document

**Revision history**

| **Version** | **Date**   | Author       | **Description** |
| ----------- | ---------- | ------------ | --------------- |
| 1.0         | 2021-09-14 | Jeremy.Jiang | Initial Version |

## Basic illustration

This article tells how to used modbus DTU.

## Application case of modbus

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



## Application note of modbus API

### modbus_utils.init (uartN, buadrate, databits, parity, stopbit, flowctl)

Initialize UART port

| **Parameter** | **Type** | Illustration                                                 |
| ------------- | -------- | ------------------------------------------------------------ |
| uartN         | int      | UART0 - DEBUG PORT UART1 – BT PORT UART2 – MAIN PORT UART3 – USB CDC PORT |
| buadrate      | int      | Baud rate, common baud rates are supported. 4800、9600、19200、38400、57600、115200、230400 |
| databits      | int      | Data bits (5~8), the Unisoc just supports 8 bits             |
| parity        | int      | Parity validation（0 – NONE，1 – EVEN，2 - ODD）             |
| stopbits      | int      | Stop bits（1\~2）                                            |
| flowctl       | int      | HW flow control（0 – FC_NONE， 1 – FC_HW）                   |

### modbus_utils.divmod_low_high(addr)

Split the high and low bit of address

| Input parameter | Type | Illustration |
| --------------- | ---- | ------------ |
| addr            | int  | Hex address  |

| Returned value | **Type** | **Illustration**         |
| -------------- | -------- | ------------------------ |
| high           | int      | Hex address of high bits |
| low            | int      | Hex address of low bits  |

### modbus_utils.calc_crc(string_byte)

Calculate the value of bytearray parity bit. 

| Parameter   | Type      | Illustration |
| ----------- | --------- | ------------ |
| string_byte | bytearray | bytearray    |

| **Type of returned value** | Type | Illustration         |
| -------------------------- | ---- | -------------------- |
| crc_high                   | int  | CRC high bit address |
| crc_low                    | int  | CRC low bit address  |

### modbus_utils.split_return_bytes(ret_bytes)

Split the bytes read from UART port and convert as bytearray

| **Parameter** | **Type** | **Illustration** |
| ------------- | -------- | ---------------- |
| ret_bytes     | bytes    | bytes            |

| **Type of returned value** | **Type** | **Illustration**                                             |
| -------------------------- | -------- | ------------------------------------------------------------ |
| bytes_split                | list     | List after splitting bytes, the format is shown as [b’00’, b’1E’, …..] |

### modbus_utils.read_uart()

Read the uart data and return bytes value

| **Type of returned value** | **Type** | **Illustration**         |
| -------------------------- | -------- | ------------------------ |
| bytes_string               | bytes    | Format ： b”01,1E,1F…..” |

### modbus_utils.write_coils(slave, const, start, coil_qty, crc_flag=True)

Write coils

| Parameter | **Type** | **Illustration**             |
| --------- | -------- | ---------------------------- |
| slave     | int      | Device address               |
| const     | int      | Functional code              |
| start     | int      | Starting address             |
| coil_qty  | int      | Read coil quantity           |
| crc_flag  | bool     | Whether the parity is needed |

| **Type of returned value** | Type | **Illustration** |
| -------------------------- | ---- | ---------------- |
| status                     | bool | Return True      |

### modbus_utils.write_coils_any(\*args, crc_flag=True)

 Write any coil address

| Parameter | **Type** | **Illustration**             |
| --------- | -------- | ---------------------------- |
| \*args    | list     | List by any byte             |
| crc_flag  | bool     | Whether the parity is needed |

## Functional code list of uModBusConst 

| Name                          | **Address** |
| ----------------------------- | ----------- |
| READ_DISCRETE_INPUTS          | 0X02        |
| READ_COILS                    | 0X01        |
| WRITE_SINGLE_COIL             | 0X05        |
| WRITE_MULTIPLE_COILS          | 0X0F        |
| READ_INPUT_REGISTER           | 0X04        |
| READ_HOLDING_REGISTERS        | 0X03        |
| WRITE_SINGLE_REGISTER         | 0X06        |
| WRITE_MULTIPLE_REGISTERS      | 0X10        |
| READ_WRITE_MULTIPLE_REGISTERS | 0X17        |
| MASK_WRITE_REGISTER           | 0X16        |
| READ_FIFO_QUEUE               | 0X18        |
| READ_FILE_RECORD              | 0X14        |
| WRITE_FILE_RECORD             | 0X15        |
| READ_EXCEPTION_STATUS         | 0X07        |
| DIAGNOSTICS                   | 0X08        |
| GET_COM_EVENT_COUNTER         | 0X0B        |
| GET_COM_EVENT_LOG             | 0X0C        |
| REPORT_SERVER_ID              | 0X11        |
| READ_DEVICE_IDENTIFICATION    | 0X2B        |
