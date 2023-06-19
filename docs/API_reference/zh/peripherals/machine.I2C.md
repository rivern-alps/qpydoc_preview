# class I2C – I2C通信

该类用于设备之间通信的双线协议。

## 构造函数

### `machine.I2C`

```python
class machine.I2C(I2Cn, MODE)
```

**参数描述：**

- `I2Cn` - I2C 通路索引号，int类型，说明如下：<br />`I2C0` : `0` - 通道0 <br />`I2C1` : `1` - 通道1 <br />`I2C2` : `2` - 通道2<br />

- `MODE` - I2C 的工作模式，int类型，说明如下：<br />`STANDARD_MODE` : `0` - 标准模式<br />`FAST_MODE` ：`1` - 快速模式

**示例：**

```python
>>> from machine import I2C
>>> # 创建I2C对象
>>> i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # 返回I2C对象
```

**I2C引脚对应关系：**

| 平台          | 引脚                                                         |
| ------------- | ------------------------------------------------------------ |
| EC600U        | I2C0:<br />SCL: 引脚号11<br />SDA: 引脚号12<br />I2C1:<br />SCL:引脚号57<br />SDA:引脚号56 |
| EC200U        | I2C0:<br />SCL: 引脚号41<br />SDA: 引脚号42<br />I2C1:<br />SCL:引脚号141<br />SDA:引脚号142 |
| EC200A        | I2C0:<br />SCL: 引脚号41<br />SDA: 引脚号42                  |
| EC600S/EC600N | I2C1:<br />SCL:引脚号57<br />SDA:引脚号56                    |
| EC100Y        | I2C0:<br />SCL:引脚号57<br />SDA:引脚号56                    |
| BC25PA        | I2C0:<br />SCL: 引脚号23<br />SDA: 引脚号22<br />I2C1:<br />SCL:引脚号20<br />SDA:引脚号21 |
| EC800N        | I2C0:<br />SCL:引脚号67<br />SDA:引脚号66                    |
| BG95M3        | I2C0:<br />SCL: 引脚号18<br />SDA: 引脚号19<br />I2C1:<br />SCL:引脚号40<br />SDA:引脚号41<br />I2C2:<br />SCL:引脚号26<br />SDA:引脚号25 |
| EC600M        | I2C0:<br />SCL: 引脚号9<br />SDA: 引脚号64<br />I2C1:<br />SCL:引脚号57<br />SDA:引脚号56<br />I2C2:<br />SCL:引脚号67<br />SDA:引脚号65 |
| EG915U        | I2C0:<br />SCL: 引脚号103<br />SDA: 引脚号114<br />I2C1:<br />SCL:引脚号40<br />SDA:引脚号41 |
| EC800M/EG810M | I2C0:<br />SCL: 引脚号67<br />SDA: 引脚号66<br />I2C2:<br />SCL:引脚号68<br />SDA:引脚号69 |
| EG912N        | I2C1:<br />SCL: 引脚号40<br />SDA: 引脚号41                  |
| EC600E        | I2C1:<br />SCL: 引脚号57(11)<br />SDA: 引脚号56(12)<br />注：模块的Pin57、Pin56 和Pin11、Pin12 共用内部同一路 I2C 接口。 |
| EC800E        | I2C0:<br />SCL: 引脚号67(57)<br />SDA: 引脚号66(58)<br />注：<br />1.模块的Pin67、Pin66 和Pin57、Pin58 共用内部同一路 I2C 接口。<br />2.EC800ECN_LE&LQ 的57/58引脚不可用 |

## 方法

### `I2C.read`

```python
I2C.read(slaveaddress, addr,addr_len, r_data, datalen, delay)
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

### `I2C.write`

```python
I2C.write(slaveaddress, addr, addr_len, data, datalen)
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

> 需要连接设备使用。

```python
import log
from machine import I2C
import utime

'''
I2C使用示例
'''

# 设置日志输出级别
log.basicConfig(level=log.INFO)
i2c_log = log.getLogger("I2C")


if __name__ == '__main__':
    I2C_SLAVE_ADDR = 0x1B  # I2C  设备地址
    WHO_AM_I = bytearray([0x02, 0])   # I2C  寄存器地址，以buff的方式传入，取第一个值，计算一个值的长度

    data = bytearray([0x12, 0])   # 输入对应指令
    i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # 返回I2C对象
    i2c_obj.write(I2C_SLAVE_ADDR, WHO_AM_I, 1, data, 2) # 写入data

    r_data = bytearray(2)  # 创建长度为2的字节数组接收
    i2c_obj.read(I2C_SLAVE_ADDR, WHO_AM_I, 1, r_data, 2, 0)   # read
    i2c_log.info(r_data[0])
    i2c_log.info(r_data[1])

```

## 常量

| 常量              | 说明             | 适用平台                                                     |
| ----------------- | ---------------- | ------------------------------------------------------------ |
| I2C.I2C0          | I2C通路索引号: 0 | EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EC800E |
| I2C.I2C1          | I2C通路索引号: 1 | EC600S/EC600N/EC600U/EC200U/BC25PA/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E |
| I2C.I2C2          | I2C通路索引号: 2 | BG95M3/EC600M                                                |
| I2C.STANDARD_MODE | 标准模式         | --                                                           |
| I2C.FAST_MODE     | 快速模式         | --                                                           |