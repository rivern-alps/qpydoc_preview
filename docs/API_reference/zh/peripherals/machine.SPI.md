# class SPI – SPI通信

该类提供串行外设接口总线协议功能。

## 构造函数

### `machine.SPI`

```python
class machine.SPI(port, mode, clk)
```

**参数描述：**

- `port` - 通道选择[0,1]，int类型。

- `mode` - SPI 的工作模式，说明如下：<br />时钟极性CPOL：即SPI空闲时，时钟信号SCLK的电平(0:空闲时低电平; 1:空闲时高电平)<br />`0` : CPOL=0, CPHA=0<br />`1` : CPOL=0, CPHA=1<br />`2`:  CPOL=1, CPHA=0<br />`3`:  CPOL=1, CPHA=1

- `clk` - 时钟频率，说明如下：<br />EC600N/EC600S/EC800N/BG95M3/EC600M/EC800M/EG810M/EG912N/EC200A/EC600E/EC800E:<br />`0` : 812.5kHz<br />`1` : 1.625MHz<br />`2` : 3.25MHz<br />`3` : 6.5MHz<br />`4` : 13MHz<br />`5` :  26MHz(EC600E/EC800E不支持)<br />`6`：52MHz(EC600E/EC800E不支持)<br />EC600U/EC200U/EG915U:<br />`0` : 781.25KHz<br />`1` : 1.5625MHz<br />`2` : 3.125MHz<br />`3` : 5MHz<br />`4` : 6.25MHz<br />`5` : 10MHz<br />`6` : 12.5MHz<br />`7` : 20MHz<br />`8` : 25MHz<br />`9` : 33.33MHz<br />BC25PA：<br />`0` ：5MHz<br />`X` : XMHz  (X in [1,39])


> BC25PA平台不支持1、2模式。

**示例：**

```python
>>> from machine import SPI
>>> # 创建SPI对象
>>> spi_obj = SPI(1, 0, 1)
```

**SPI引脚对应关系：**

| 平台          | 引脚                                                         |
| ------------- | ------------------------------------------------------------ |
| EC600U        | port0:<br />CS:引脚号4<br />CLK:引脚号1<br />MOSI:引脚号3<br />MISO:引脚号2<br />port1:<br />CS:引脚号58<br />CLK:引脚号61<br />MOSI:引脚号59<br />MISO:引脚号60 |
| EC200U        | port0:<br />CS:引脚号134<br />CLK:引脚号133<br />MOSI:引脚号132<br />MISO:引脚号131<br />port1:<br />CS:引脚号26<br />CLK:引脚号27<br />MOSI:引脚号24<br />MISO:引脚号25 |
| EC600S/EC600N | port0:<br />CS:引脚号58<br />CLK:引脚号61<br />MOSI:引脚号59<br />MISO:引脚号60<br />port1:<br />CS:引脚号4<br />CLK:引脚号1<br />MOSI:引脚号3<br />MISO:引脚号2 |
| EC100Y        | port0:<br />CS:引脚号25<br />CLK:引脚号26<br />MOSI:引脚号27<br />MISO:引脚号28<br />port1:<br />CS:引脚号105<br />CLK:引脚号104<br />MOSI:引脚号107<br />MISO:引脚号106 |
| EC800N        | port0:<br />CS:引脚号31<br />CLK:引脚号30<br />MOSI:引脚号32<br />MISO:引脚号33<br />port1:<br />CS:引脚号52<br />CLK:引脚号53<br />MOSI:引脚号50<br />MISO:引脚号51 |
| BC25PA        | port0:<br />CS:引脚号6<br />CLK:引脚号5<br />MOSI:引脚号4<br />MISO:引脚号3 |
| BG95M3        | port0:<br />CS:引脚号25<br />CLK:引脚号26<br />MOSI:引脚号27<br />MISO:引脚号28<br />port1:<br />CS:引脚号41<br />CLK:引脚号40<br />MOSI:引脚号64<br />MISO:引脚号65 |
| EC600M        | port0:<br />CS:引脚号58<br />CLK:引脚号61<br />MOSI:引脚号59<br />MISO:引脚号60<br />port1:<br />CS:引脚号4<br />CLK:引脚号1<br />MOSI:引脚号3<br />MISO:引脚号2 |
| EG915U        | port0:<br />CS:引脚号25<br />CLK:引脚号26<br />MOSI:引脚号64<br />MISO:引脚号88 |
| EC800M/EG810M | port0:<br />CS:引脚号31<br />CLK:引脚号30<br />MOSI:引脚号32<br />MISO:引脚号33</u><br />port1:<br />CS:引脚号52<br />CLK:引脚号53<br />MOSI:引脚号50<br />MISO:引脚号51 |
| EG912N        | port0:<br />CS:引脚号25<br />CLK:引脚号26<br />MOSI:引脚号27<br />MISO:引脚号28<br/>port1:<br />CS:引脚号5<br />CLK:引脚号4<br />MOSI:引脚号6<br />MISO:引脚号7 |
| EC200A        | port0:<br />CS:引脚号37<br />CLK:引脚号40<br />MOSI:引脚号38<br />MISO:引脚号39<br />port1:<br />CS:引脚号26<br />CLK:引脚号27<br />MOSI:引脚号25<br />MISO:引脚号24 |
| EC600E        | port0:<br />CS:引脚号65<br />CLK:引脚号67<br />MOSI:引脚号66<br />MISO:引脚号64<br />port1:<br />CS:引脚号69<br />CLK:引脚号71<br />MOSI:引脚号70<br />MISO:引脚号72 |
| EC800E        | port0:<br />CS:引脚号28<br />CLK:引脚号39<br />MOSI:引脚号29<br />MISO:引脚号38<br />port1:<br />CS:引脚号52<br />CLK:引脚号53<br />MOSI:引脚号50<br />MISO:引脚号51<br />注：EC800ECN_LE&LQ port1 不可用 |

## 方法

### `SPI.read`

```python
SPI.read(recv_data, datalen)
```

该方法用于读取数据。

**参数描述：**

- `recv_data` - 接收读取数据的数组，bytearray类型。
- `datalen` - 读取数据的长度，int类型。

**返回值描述：**

成功返回整型值`0`，失败返回整型值`-1`。

### `SPI.write`

```python
SPI.write(data, datalen)
```

该方法用于写入数据。

**参数描述：**

- `data` - 写入的数据，bytes类型。
- `datalen` - 写入的数据长度，int类型。

**返回值描述：**

成功返回整型值`0`，失败返回整型值`-1`。

### `SPI.write_read`

```python
SPI.write_read(r_data, data, datalen)
```

该方法用于写入和读取数据。

**参数描述：**

- `r_data  ` - 接收读取数据的数组，bytearray类型。
- `data` - 发送的数据，bytes类型。
- `datalen` - 读取数据的长度，int类型。

**返回值描述：**

成功返回整型值`0`，失败返回整型值`-1`。

**使用示例：**

> 需要配合外设使用！

```python
import log
from machine import SPI
import utime

spi_obj = SPI(0, 0, 1)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
spi_log = log.getLogger("SPI")

if __name__ == '__main__':
    r_data = bytearray(5)  # 创建接收数据的buff
    data = b"world"  # 测试数据

    ret = spi_obj.write_read(r_data, data, 5)  # 写入数据并接收
    spi_log.info(r_data)

```
