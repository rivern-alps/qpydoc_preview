# I2C_simulation - Software Implementation of I2C Protocol

This class is designed for GPIO simulating standard I2C protocol. Except for creating the object, all other operations (read and write) are consistent with I2C communication.   

## Constructor

### `machine.I2C_simulation`

```python
class machin.I2C_simulation(GPIO_clk, GPIO_sda, CLK)
```

**Parameter:**

- `GPIO_clk` - Integer type. CLK pin of I2C (See definitions in [machine.Pin](machine.Pin.md) for GPIO pin numbers that need to be controlled).    
- `GPIO_sda` - Integer type. SDA pin of I2C (See definitions in [machine.Pin](machine.Pin.md) for GPIO pin numbers that need to be controlled). 
- `CLK` - Integer type. Frequency of I2C. Range: [1, 1000000 Hz].

**Example:**

```python
>>> from machine import I2C_simulation
>>> # Creates an I2C_simulation object
>>> i2c_obj = I2C_simulation(I2C_simulation.GPIO10, I2C_simulation.GPIO11, 300)  # Returns an I2C object
```

## Methods

### `I2C_simulation.read`

```python
I2C_simulation.read(slaveaddress, addr,addr_len, r_data, datalen, delay)
```

This method reads data to I2C bus.

**Parameter:**

- `slaveaddress` - Integer type. I2C device address.
- `addr` - Bytearray type. I2C register address.
- `addr_len` - Integer type. Register address length.
- `r_data` - Bytearray type. Byte array used to receive data.
- `datalen` - Integer type. Length of byte array.
- `delay` - Integer type. Delay. Data conversion buffer time (unit: ms).

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `I2C_simulation.write`

```python
I2C_simulation.write(slaveaddress, addr, addr_len, data, datalen)
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

```python
import log
#from machine import I2C
from machine import I2C_simulation
import utime as time
"""
1. calibration
2. Trigger measurement
3. read data
"""

# API  manual http://qpy.quectel.com/wiki/#/zh-cn/api/?id=i2c
# AHT10 instructions
# https://server4.eca.ir/eshop/AHT10/Aosong_AHT10_en_draft_0c.pdf
# This example shows that driver AHT10 obtains temperature and humidity data.

class aht10class():
    i2c_log = None
    i2c_dev = None
    i2c_addre = None

    # Initialization command
    AHT10_CALIBRATION_CMD = 0xE1
    # Trigger measurement
    AHT10_START_MEASURMENT_CMD = 0xAC
    # reset
    AHT10_RESET_CMD = 0xBA

    def write_data(self, data):
        self.i2c_dev.write(self.i2c_addre,
                           bytearray(0x00), 0,
                           bytearray(data), len(data))
        pass

    def read_data(self, length):
        print("read_data start")
        r_data = [0x00 for i in range(length)]
        r_data = bytearray(r_data)
        print("read_data start1")
        ret = self.i2c_dev.read(self.i2c_addre,
                          bytearray(0x00), 0,
                          r_data, length,
                          0)
        print("read_data start2")
        print('ret',ret)
        print('r_data:',r_data)
        return list(r_data)

    def aht10_init(self, addre=0x38, Alise="Ath10"):
        self.i2c_log = log.getLogger(Alise)
        self.i2c_dev = I2C_simulation(I2C_simulation.GPIO10, I2C_simulation.GPIO11, 300)
        self.i2c_addre = addre
        self.sensor_init()
        pass

    def aht10_transformation_temperature(self, data):
        r_data = data
        #　Convert the temperature according to descriptions in the data manual 
        humidity = (r_data[0] << 12) | (
            r_data[1] << 4) | ((r_data[2] & 0xF0) >> 4)
        humidity = (humidity/(1 << 20)) * 100.0
        print("current humidity is {0}%".format(humidity))
        temperature = ((r_data[2] & 0xf) << 16) | (
            r_data[3] << 8) | r_data[4]
        temperature = (temperature * 200.0 / (1 << 20)) - 50
        print("current temperature is {0}°C".format(temperature))
        

    def sensor_init(self):
        # calibration
        self.write_data([self.AHT10_CALIBRATION_CMD, 0x08, 0x00])
        time.sleep_ms(300)  # At least 300 ms
        pass


    def ath10_reset(self):
        self.write_data([self.AHT10_RESET_CMD])
        time.sleep_ms(20)  # At least 20 ms

    def Trigger_measurement(self):
        # Trigger data conversion
        self.write_data([self.AHT10_START_MEASURMENT_CMD, 0x33, 0x00])
        time.sleep_ms(200)  # At least delay 75 ms
        # check has success
        r_data = self.read_data(6)
        # check bit7
        if (r_data[0] >> 7) != 0x0:
            print("Conversion has error")
        else:
            self.aht10_transformation_temperature(r_data[1:6])

ath_dev = None

def i2c_aht10_test():
    global ath_dev
    ath_dev = aht10class()
    ath_dev.aht10_init()

    # Test ten times
    for i in range(5):
        ath_dev.Trigger_measurement()
        time.sleep(1)


if __name__ == "__main__":
    print('start')
    i2c_aht10_test()


```
