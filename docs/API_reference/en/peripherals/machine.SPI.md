# SPI – Serial Peripheral Interface Bus Protocol

This class provides bus protocol of serial peripheral interface (SPI) .

## Constructor

### `machine.SPI`

```python
class machine.SPI(port, mode, clk)
```

**Parameter:**

- `port` - Integer type. Channel selection: [0,1].
- `mode` - SPI working mode.<br />Clock polarity CPOL: The pin level of clock signal SCLK when SPI is idle (0: low level; 1: high level)<br />`0` : CPOL=0, CPHA=0<br />`1` : CPOL=0, CPHA=1<br />`2`:  CPOL=1, CPHA=0<br />`3`:  CPOL=1, CPHA=1

- `clk` - Clock frequency.<br />EC600N/EC600S/EC800N/BG95M3/EC600M/EC800M/EG912N:<br />`0` : 812.5 kHz<br />`1` : 1.625 MHz<br />`2` : 3.25 MHz<br />`3` : 6.5 MHz<br />`4` : 13 MHz<br />`5` :  26 MHz<br />`6`：52 MHz<br />EC600U/EC200U/EG915U:<br />`0` : 781.25 kHz<br />`1` : 1.5625 MHz<br />`2` : 3.125 MHz<br />`3` : 5 MHz<br />`4` : 6.25 MHz<br />`5` : 10 MHz<br />`6` : 12.5 MHz<br />`7` : 20 MHz<br />`8` : 25 MHz<br />`9` : 33.33 MHz<br />BC25：<br />`0` : 5 MHz<br />`X` : X MHz  (X in [1,39])


> BC25 series module does not support SPI working mode of value 1 or 2. 

**Example:**

```python
>>> from machine import SPI
>>> # Creates a SPI object
>>> spi_obj = SPI(1, 0, 1)
```

**SPI Pin Correspondences:**

| Module        | Pin                                                          |
| ------------- | ------------------------------------------------------------ |
| EC600U        | port0:<br />CS: pin4<br />CLK: pin1<br />MOSI: pin3<br />MISO: pin 2<br />port1:<br />CS: pin58<br />CLK: pin61<br />MOSI: pin59<br />MISO: pin60 |
| EC200U        | port0:<br />CS: pin134<br />CLK: pin133<br />MOSI: pin132<br />MISO: pin131<br />port1:<br />CS: pin26<br />CLK: pin27<br />MOSI: pin24<br />MISO: pin25 |
| EC600S/EC600N | port0:<br />CS: pin58<br />CLK: pin61<br />MOSI: pin59<br />MISO: pin60<br />port1:<br />CS: pin4<br />CLK: pin1<br />MOSI: pin3<br />MISO: pin2 |
| EC100Y        | port0:<br />CS: pin25<br />CLK: pin26<br />MOSI: pin27<br />MISO: pin28<br />port1:<br />CS: pin105<br />CLK: pin104<br />MOSI: pin107<br />MISO: pin106 |
| EC800N        | port0:<br />CS: pin31<br />CLK: pin30<br />MOSI: pin32<br />MISO: pin33<br />port1:<br />CS: pin52<br />CLK: pin53<br />MOSI: pin50<br />MISO: pin51 |
| BC25          | port0:<br />CS: pin6<br />CLK: pin5<br />MOSI: pin4<br />MISO: pin3 |
| BG95M3        | port0:<br />CS: pin25<br />CLK: pin26<br />MOSI: pin27<br />MISO: pin28<br />port1:<br />CS: pin41<br />CLK: pin40<br />MOSI: pin64<br />MISO: pin65 |
| EC600M        | port0:<br />CS: pin58<br />CLK: pin61<br />MOSI: pin59<br />MISO: pin60<br />port1:<br />CS: pin4<br />CLK: pin1<br />MOSI: pin3<br />MISO: pin2 |
| EG915U        | port0:<br />CS: pin25<br />CLK: pin26<br />MOSI: pin64<br />MISO: pin88 |
| EC800M        | port0:<br />CS: pin31<br />CLK: pin30<br />MOSI: pin32<br />MISO: pin33</u><br />port1:<br />CS: pin52<br />CLK: pin53<br />MOSI: pin50<br />MISO: pin51 |
| EG912N        | port0:<br />CS: pin25<br />CLK: pin26<br />MOSI: pin27<br />MISO: pin28<br/>port1:<br />CS: pin5<br />CLK: pin4<br />MOSI: pin6<br />MISO: pin7 |

## Methods

### `SPI.read`

```python
SPI.read(recv_data, datalen)
```

This method reads data.

**Parameter:**

- `recv_data` - Bytearray type. An array used to receive data.
- `datalen` - Integer type. Length of the data to be read.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `SPI.write`

```python
SPI.write(data, datalen)
```

This method writes data.

**Parameter:**

- `data` - Bytearray type. Data to be written.
- `datalen` - Integer type. Length of data to be written.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `SPI.write_read`

```python
SPI.write_read(r_data, data, datalen)
```

This method writes and reads data.

**Parameter:**

- `r_data  ` - Bytearray type. An array used to receive data.
- `data` - Bytearray type. Data to be sent.
- `datalen` - Integer type. Length of data to be read.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

**Example:**

> Please use this function with the peripherals.

```python
import log
from machine import SPI
import utime



spi_obj = SPI(0, 0, 1)

# Sets the log output level 
log.basicConfig(level=log.INFO)
spi_log = log.getLogger("SPI")


if __name__ == '__main__':
    r_data = bytearray(5)  # Creates a buff for receiving data
    data = b"world"  # Tests data

    ret = spi_obj.write_read(r_data, data, 5)  # Writes data and receives data to r_data
    spi_log.info(r_data)

```
