# I2C – Two-wire Serial Protocol

This class is designed for the two-wire serial protocol for communication between devices.

## Constructor

### `machine.I2C`

```python
class machine.I2C(I2Cn, MODE)
```

**Parameter:**

- `I2Cn` - Integer type. I2C channel index number. <br />`I2C0` : `0` - Channel 0 <br />`I2C1` : `1` - Channel 1 <br />`I2C2` : `2` - Channel 2<br />

- `MODE` - Integer type. I2C working mode. <br />`STANDARD_MODE` : `0` - Standard mode<br />`FAST_MODE` ：`1` - Fast mode

**Example:**

```python
>>> from machine import I2C
>>> # Creates an I2C object
>>> i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # Returns an I2C object
```

**I2C Pin Correspondences:**

| Module        | Pin                                                          |
| ------------- | ------------------------------------------------------------ |
| EC600U        | I2C0:<br />SCL: pin11<br />SDA: pin12<br />I2C1:<br />SCL: pin57<br />SDA: pin56 |
| EC200U        | I2C0:<br />SCL: pin41<br />SDA: pin42<br />I2C1:<br />SCL: pin141<br />SDA: pin142 |
| EC200A        | I2C0:<br />SCL: pin41<br />SDA: pin42                        |
| EC600S/EC600N | I2C1:<br />SCL: pin57<br />SDA: pin56                        |
| EC100Y        | I2C0:<br />SCL: pin57<br />SDA: pin56                        |
| BC25          | I2C0:<br />SCL: pin23<br />SDA: pin22<br />I2C1:<br />SCL: pin20<br />SDA: pin21 |
| EC800N        | I2C0:<br />SCL: pin67<br />SDA: pin66                        |
| BG95M3        | I2C0:<br />SCL: pin18<br />SDA: pin19<br />I2C1:<br />SCL: pin40<br />SDA: pin41<br />I2C2:<br />SCL: pin26<br />SDA: pin25 |
| EC600M        | I2C0:<br />SCL: pin9<br />SDA: pin64<br />I2C1:<br />SCL: pin57<br />SDA: pin56<br />I2C2:<br />SCL: pin67<br />SDA: pin65 |
| EG915U        | I2C0:<br />SCL: pin103<br />SDA: pin114<br />I2C1:<br />SCL: pin40<br />SDA: pin41 |
| EC800M        | I2C0:<br />SCL: pin67<br />SDA: pin66<br />I2C2:<br />SCL: pin68<br />SDA: pin69 |
| EG912N        | I2C1:<br />SCL: pin40<br />SDA: pin41                        |

## Methods

### `I2C.read`

```python
I2C.read(slaveaddress, addr,addr_len, r_data, datalen, delay)
```

This method reads data to I2C bus.

**Parameter:**

- `slaveaddress` - Integer type. I2C device address.
- `addr` - Bytearray type. I2C register address.
- `addr_len` - Integer type. Register address length.
- `r_data` - Bytearray type. Byte array for receiving data.
- `datalen` - Integer type. Length of byte array.
- `delay` - Integer type. Delay. Data conversion buffer time (unit: ms).

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `I2C.write`

```python
I2C.write(slaveaddress, addr, addr_len, data, datalen)
```

This method writes data to I2C bus. 

**Parameter:**

- `slaveaddress` - Integer type. I2C device address.
- `addr` - Bytearray type. I2C register address.
- `addr_len` - Integer type. Register address length.
- `data` - Bytearray type. Data to be written.
- `datalen` - Integer type. Length of data to be written.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

**Example:**

> Please connect the device.

```python
import log
from machine import I2C
import utime


'''
The following two global variables are necessary. You can modify the values of these two global variables based on project requirement.
'''
PROJECT_NAME = "QuecPython_I2C_example"
PROJECT_VERSION = "1.0.0"

'''
I2C usage example
'''

# Sets log output level
log.basicConfig(level=log.INFO)
i2c_log = log.getLogger("I2C")


if __name__ == '__main__':
    I2C_SLAVE_ADDR = 0x1B  # I2C device address
    WHO_AM_I = bytearray([0x02, 0])   # I2C register address. It is passed in as a buff. Take the first value and calculate the length of a value  

    data = bytearray([0x12, 0])   # Inputs the corresponding command
    i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # Returns an I2C object
    i2c_obj.write(I2C_SLAVE_ADDR, WHO_AM_I, 1, data, 2) # Writes data

    r_data = bytearray(2)  # Creates a byte array with the length of 2 bytes for receiving
    i2c_obj.read(I2C_SLAVE_ADDR, WHO_AM_I, 1, r_data, 2, 0)   # read
    i2c_log.info(r_data[0])
    i2c_log.info(r_data[1])

```

## Constants

| Constant          | Description                 | Module                                                       |
| ----------------- | --------------------------- | ------------------------------------------------------------ |
| I2C.I2C0          | I2C passage index number: 0 | EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M |
| I2C.I2C1          | I2C passage index number: 1 | EC600S/EC600N/EC600U/EC200U/BC25/BG95M3/EC600M/EG915U/EC800M/EG912N |
| I2C.I2C2          | I2C passage index number: 2 | BG95M3/EC600M                                                |
| I2C.STANDARD_MODE | Standard mode               | All modules                                                  |
| I2C.FAST_MODE     | Fast mode                   | All modules                                                  |