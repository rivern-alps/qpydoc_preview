# class SoftSPI – 模拟SPI通信

该类提供模拟串行外设接口总线协议功能。

> EC600E/EC800E系列支持该功能。

## 构造函数

### `machine.SoftSPI`

```python
class machine.SoftSPI(gpio_clk, gpio_cs, gpio_mosi, [gpio_miso],[wire_type],[speed],[mode],[cs_active_lvl])
```

**参数描述：**

- `gpio_clk` - int类型，clk管脚对应的gpio；
- `gpio_cs` - int类型，cs管脚对应的gpio；
- `gpio_mosi` - int类型，mosi管脚对应的gpio；
- `[gpio_miso]` - int类型，miso管脚对应的gpio，三线spi无需传入该参数，收发共用mosi管脚；
- `[wire_type]` - int类型，三线、四线spi设置，`WIRE_3`:三线spi，`WIRE_4`:四线spi，缺省为四线spi；
- `[speed]` - int类型，传输速度，`0`:50kHz，`1`:100kHz，缺省为100kHz；
- `[mode]` - int类型，spi模式，范围：`0`~`3`，缺省为模式`0`，说明如下：<br />`0` : CPOL=0, CPHA=0<br />`1` : CPOL=0, CPHA=1<br />`2`:  CPOL=1, CPHA=0<br />`3`:  CPOL=1, CPHA=1
- `[cs_active_lvl]` - int类型，cs有效电平，`LOW`:低电平有效，`HIGH`:高电平有效，缺省为低电平有效。

**返回值描述：**

成功返回创建的对象，失败直接报错。

**示例：**

```python
from machine import SoftSPI
# 创建四线SPI对象，clk为gpio14，cs为gpio11，mosi为gpio12，miso为gpio13，模式0，速度为100kHz,cs低电平有效
spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi= SoftSPI.GPIO12,gpio_miso= SoftSPI.GPIO13)
# 创建四线SPI对象，clk为gpio14，cs为gpio11，mosi为gpio12，miso为gpio13，模式1，速度为50kHz，cs高电平有效
spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi=SoftSPI.GPIO12,gpio_miso=SoftSPI.GPIO13,
            speed=0,mode=1,cs_active_lvl=SoftSPI.HIGH)
# 创建三线SPI对象，clk为gpio14，cs为gpio11，数据线为gpio12，模式0，速度100kHz，cs低电平有效
spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi= SoftSPI.GPIO12,wire_type= SoftSPI.WIRE_3)
# 创建三线SPI对象，clk为gpio14，cs为gpio11，数据线为gpio12，模式2，速度50kHz，cs高电平有效
spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi=SoftSPI.GPIO12,wire_type=SoftSPI.WIRE_3,
            speed=0,mode=2,cs_active_lvl=SoftSPI.HIGH)
```

## 方法

### `SoftSPI.read`

```python
SoftSPI.read(recv_data, datalen)
```

该方法用于读取数据。

**参数描述：**

- `recv_data` - 接收读取数据的数组，bytearray类型。
- `datalen` - 读取数据的长度，int类型。

**返回值描述：**

返回整型值`0`。

### `SoftSPI.write`

```python
SoftSPI.write(data, datalen)
```

该方法用于写入数据。

**参数描述：**

- `data` - 写入的数据，bytes类型。
- `datalen` - 写入的数据长度，int类型。

**返回值描述：**

返回整型值`0`。

### `SoftSPI.write_read`

```python
SoftSPI.write_read(r_data, data, datalen)
```

该方法用于写入和读取数据。

**参数描述：**

- `r_data  ` - 接收读取数据的数组，bytearray类型。
- `data` - 发送的数据，bytes类型。
- `datalen` - 读取数据的长度，int类型。

**返回值描述：**

返回整型值`0`。

> 对于三线spi，通信过程：mosi设置为输出，发送data，mosi设置为输入，读取datalen长度的数据。

**使用示例：**

> 需要配合外设使用！

四线spi示例

```python
from machine import SoftSPI

spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi= SoftSPI.GPIO12,gpio_miso= SoftSPI.GPIO13)

if __name__ == '__main__':
    r_data = bytearray(5)  # 创建接收数据的buff
    data = b"world"  # 测试数据
    spi.write_read(r_data, data, 5)  # 写入数据并接收
	spi.read(r_data,5) #接收数据到r_data
    spi.write(data,5)#发送数据
```

三线spi示例

```python
from machine import SoftSPI

spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi= SoftSPI.GPIO12,wire_type= SoftSPI.WIRE_3)

if __name__ == '__main__':
    r_data = bytearray(5)  # 创建接收数据的buff
    data = b"world"  # 测试数据
    spi.write_read(r_data, data, 5)  # 写入数据并接收
	spi.read(r_data,5) #接收数据到r_data
    spi.write(data,5)#发送数据
```

