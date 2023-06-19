# class SoftSPI – Software Implementation of SPI Bus Protocol 

This class provides bus protocol of Serial Peripheral Interface (SPI).

> EC600E/EC800E module supports this feature.

## Constructor

### `machine.SoftSPI`

```python
class machine.SoftSPI(gpio_clk, gpio_cs, gpio_mosi, [gpio_miso],[wire_type],[speed],[mode],[cs_active_lvl])
```

**Parameter**

- `gpio_clk` - Integer type. The GPIO corresponding to the CLK.
- `gpio_cs` - Integer type. The GPIO corresponding to the CS.
- `gpio_mosi` - Integer type. The GPIO corresponding to the MOSI.
- `[gpio_miso]` - Integer type. The GPIO corresponding to the MISO. For 3-wire SPI, this parameter can be omitted and the MOSI can be used for receiving and sending data.
- `[wire_type]` - Integer type. Set SPI to 3-wire SPI or 4-wire SPI. `WIRE_3`: 3-wire SPI. `WIRE_4`: 4-wire SPI. Default value: 4-wire SPI.
- `[speed]` - Integer type. Transmission speed.  `0`: 50 kHz.  `1`: 100 kHz. Default value: 100 kHz.
- `[mode]` - Integer type. SPI mode. Range:  `0`–`3`.  Default value: `0`. <br />`0` : CPOL=0, CPHA=0<br />`1` : CPOL=0, CPHA=1<br />`2`:  CPOL=1, CPHA=0<br />`3`:  CPOL=1, CPHA=1
- `[cs_active_lvl]` - Integer type. CS active level.  `LOW`: low level. `HIGH`: high level. Default value: low level. 

**Return Value**

The object created - Successful execution

Error - Failed execution

**Example**

```python
from machine import SoftSPI
# Create a 4-wire SPI object. CLK: GPIO14. CS: GPIO11. MOSI: GPIO12. MISO: GPIO13. SPI mode: 0. Transmission speed: 100 kHz. CS: low level. 
spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi= SoftSPI.GPIO12,gpio_miso= SoftSPI.GPIO13)
# Create a 4-wire SPI object. CLK: GPIO14. CS: GPIO11. MOSI: GPIO12. MISO: GPIO13. SPI mode: 1. Transmission speed: 50 kHz. CS: high level. 
spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi=SoftSPI.GPIO12,gpio_miso=SoftSPI.GPIO13,
            speed=0,mode=1,cs_active_lvl=SoftSPI.HIGH)
# Create a 3-wire SPI object. CLK: GPIO14. CS: GPIO11. MOSI: GPIO12. SPI mode: 0. Transmission speed: 100 kHz. CS: low level. 
spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi= SoftSPI.GPIO12,wire_type= SoftSPI.WIRE_3)
# Create a 3-wire SPI object. CLK: GPIO14. CS: GPIO11. MOSI: GPIO12. SPI mode: 2. Transmission speed: 50 kHz. CS: high level.
spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi=SoftSPI.GPIO12,wire_type=SoftSPI.WIRE_3,
            speed=0,mode=2,cs_active_lvl=SoftSPI.HIGH)
```

## Methods

### `SoftSPI.read`

```python
SoftSPI.read(recv_data, datalen)
```

This method reads data.

**Parameter**

- `recv_data` - Bytearray type. An array used to receive data.
- `datalen` - Integer type. Length of the data to be read.

**Return Value**

`0`

### `SoftSPI.write`

```python
SoftSPI.write(data, datalen)
```

This method writes data.

**Parameter**

- `data` - Bytes type. Data to be written.
- `datalen` - Integer type. Length of data to be written.

**Return Value**

`0`

### `SoftSPI.write_read`

```python
SoftSPI.write_read(r_data, data, datalen)
```

This method writes and reads data.

**Parameter**

- `r_data  ` - Bytearray type. An array used to receive data.
- `data` - Bytes type. Data to be sent.
- `datalen` - Integer type. Length of data to be read.

**Return Value**

`0`

> For 3-wire SPI, in the communicating process, MOSI is set to the output mode first and data will be sent. And then MOSI is set to the input mode and the *datalen* bytes of data will be read.

**Example**

> Please use this method with the peripherals.

Example for 4-wire SPI

```python
from machine import SoftSPI

spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi= SoftSPI.GPIO12,gpio_miso= SoftSPI.GPIO13)

if __name__ == '__main__':
    r_data = bytearray(5)  # Create a buffer for receiving data
    data = b"world"  # Test data
    spi.write_read(r_data, data, 5)  # Write and receive data
	spi.read(r_data,5) # Receive data to r_data
    spi.write(data,5)# Send data
```

Example for 3-wire SPI

```python
from machine import SoftSPI

spi=SoftSPI(gpio_clk=SoftSPI.GPIO14,gpio_cs=SoftSPI.GPIO11,gpio_mosi= SoftSPI.GPIO12,wire_type= SoftSPI.WIRE_3)

if __name__ == '__main__':
    r_data = bytearray(5)  # Create a buffer for receiving data
    data = b"world"  # Test data
    spi.write_read(r_data, data, 5)  # Write and receive data
	spi.read(r_data,5) # Receive data to r_data
    spi.write(data,5)# Send data
```

