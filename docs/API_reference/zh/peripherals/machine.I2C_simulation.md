# class I2C_simulation - 模拟I2C通信

该类用于gpio模拟标准I2C协议，除了创建对象外，其它的操作(读写)均与I2C通信一致。

## 构造函数

### `machine.I2C_simulation`

```python
class machin.I2C_simulation(GPIO_clk, GPIO_sda, CLK)
```

**参数描述：**

- `GPIO_clk` - I2C 的CLK引脚(需要控制的GPIO引脚号，参照[Pin模块](machine.Pin.md)的定义)，int类型。
- `GPIO_sda` - I2C 的SDA引脚(需要控制的GPIO引脚号，参照[Pin模块](machine.Pin.md)的定义)，int类型。
- `CLK` - I2C 的频率，范围：(0,1000000Hz]，int类型。

**示例：**

```python
>>> from machine import I2C_simulation
>>> # 创建I2C_simulation对象
>>> i2c_obj = I2C_simulation(I2C_simulation.GPIO10, I2C_simulation.GPIO11, 300)  # 返回I2C对象
```

## 方法

### `I2C_simulation.read`

```python
I2C_simulation.read(slaveaddress, addr,addr_len, r_data, datalen, delay)
```

该方法用于从 I2C 总线中读取数据。

**参数描述：**

- `slaveaddress` - I2C 设备地址，int类型。
- `addr` - I2C 寄存器地址，bytearray类型。
- `addr_len` - 寄存器地址长度，int类型。
- `r_data` - 接收数据的字节数组，bytearray类型。
- `datalen` - 字节数组的长度，int类型。
- `delay` - 延时，数据转换缓冲时间(单位ms)，int类型。

**返回值描述：**

成功返回整型值`0`，失败返回整型值`-1`。

### `I2C_simulation.write`

```python
I2C_simulation.write(slaveaddress, addr, addr_len, data, datalen)
```

该方法用于从 I2C 总线中写入数据。

**参数描述：**

- `slaveaddress` - I2C 设备地址，int类型。
- `addr` - I2C 寄存器地址，bytearray类型。
- `addr_len` - 寄存器地址长度，int类型。
- `data` - 写入的数据，bytearray类型。
- `datalen` - 写入数据的长度，int类型。

**返回值描述：**

成功返回整型值`0`，失败返回整型值`-1`。

**使用示例：**

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

# AHT10 说明书
# https://server4.eca.ir/eshop/AHT10/Aosong_AHT10_en_draft_0c.pdf
# 该示例是驱动AHT10获取温湿度数据

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
        #　根据数据手册的描述来转化温度
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
        time.sleep_ms(300)  # at last 300ms
        pass


    def ath10_reset(self):
        self.write_data([self.AHT10_RESET_CMD])
        time.sleep_ms(20)  # at last 20ms

    def Trigger_measurement(self):
        # Trigger data conversion
        self.write_data([self.AHT10_START_MEASURMENT_CMD, 0x33, 0x00])
        time.sleep_ms(200)  # at last delay 75ms
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

    # 测试十次
    for i in range(5):
        ath_dev.Trigger_measurement()
        time.sleep(1)


if __name__ == "__main__":
    print('start')
    i2c_aht10_test()


```
