# class LCD - LCD显示屏

该类提供对LCD显示屏的控制。

> 支持的平台和模块型号：
>
> EC200U系列、EC600U系列、EC600N系列、EC800N系列
>
> EC600M-CNLA、EC600M-CNLE
>
> EC800M-CNLA、EC800M-CNLE、EC800M-CNGA、EC800G-CNGA、EC810M-CNGA
>
> EG912N-ENAA、EG912U-GLAA
>
> EG915N-EUAG、EG915U-EUAB

## 构造函数

### `machine.LCD`

```python
class machine.lcd = LCD()
```

**示例：**

```python
>>> from machine import LCD 
>>> lcd = LCD()    # 创建lcd对象
```

## 方法

### `lcd.lcd_init`

该方法用于初始化LCD。

#### **接口1：设备接模块LCM接口**

```python
lcd.lcd_init(lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid, lcd_display_on, lcd_display_off, lcd_set_brightness)
```

**参数描述：**

| 参数               | 类型      | 说明                                                         |
| ------------------ | --------- | ------------------------------------------------------------ |
| lcd_init_data      | bytearray | LCD 初始化的配置命令                                         |
| lcd_width          | int       | LCD 屏幕的宽度，宽度不超过 500像素                           |
| lcd_hight          | int       | LCD 屏幕的高度，高度不超过 500像素                           |
| lcd_clk            | int       | LCD SPI 时钟频率：<br />6500: 6.5MHz<br />13000:13MHz<br />26000:26MHz<br />52000:52MHz |
| data_line          | int       | 数据线数，参数值为 1 和 2                                    |
| line_num           | int       | 线的数量，参数值为 3 和 4                                    |
| lcd_type           | int       | 屏幕类型，0 - rgb；1 - fstn                                  |
| lcd_invalid        | bytearray | LCD 区域设置的配置命令                                       |
| lcd_display_on     | bytearray | LCD 屏亮的配置命令                                           |
| lcd_display_off    | bytearray | LCD 屏灭的配置命令                                           |
| lcd_set_brightness | bytearray | LCD屏亮度的配置命令：<br />设置为 None表示由 LCD_BL_K 控制亮度 |

**返回值描述：**

`0` 表示成功。

`-1` 表示已经初始化。

`-2` 表示参数错误，为空或过大(大于 1000 像素点)。

`-3` 表示缓存申请失败。

`-5` 表示配置参数错误。

#### **接口2：设备接模块SPI接口**

```python
lcd.lcd_init(lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid, lcd_display_on, lcd_display_off, lcd_set_brightness, lcd_interface, spi_port, spi_mode, cs_pin, dc_pin, rst_pin)
```

**参数描述：**

| 参数               | 类型      | 说明                                                         |
| ------------------ | --------- | ------------------------------------------------------------ |
| lcd_init_data      | bytearray | LCD 初始化的配置命令                                         |
| lcd_width          | int       | LCD 屏幕的宽度，宽度不超过 500像素                           |
| lcd_hight          | int       | LCD 屏幕的高度，高度不超过 500像素                           |
| lcd_clk            | int       | SPI 时钟，见machine.SPI 创建SPI对象参数说明clk               |
| data_line          | int       | 数据线数，参数值为 1 和 2                                    |
| line_num           | int       | 线的数量，参数值为 3 和 4                                    |
| lcd_type           | int       | 屏幕类型，0 - rgb；1 - fstn                                  |
| lcd_invalid        | bytearray | LCD 区域设置的配置命令                                       |
| lcd_display_on     | bytearray | LCD 屏亮的配置命令                                           |
| lcd_display_off    | bytearray | LCD 屏灭的配置命令                                           |
| lcd_set_brightness | bytearray | LCD屏亮度的配置命令：<br />设置为 None表示由 LCD_BL_K 控制亮度 |
| lcd_interface      | int       | LCD接口类型，0 - LCM接口；1 - SPI接口                        |
| spi_port           | int       | 通道选择[0,1]，参照SPI部分                                   |
| spi_mode           | int       | SPI 的工作模式(通常使用工作模式0)：<br />时钟极性CPOL：即SPI空闲时，时钟信号SCLK的电平(0:空闲时低电平; 1:空闲时高电平)<br />0 : CPOL=0, CPHA=0<br />1 : CPOL=0, CPHA=1<br />2 : CPOL=1, CPHA=0<br />3 : CPOL=1, CPHA=1 |
| cs_pin             | int       | CS引脚，见[machine.Pin](machine.Pin.md)中GPIO引脚编号说明    |
| dc_pin             | int       | DC引脚，见[machine.Pin](machine.Pin.md)中GPIO引脚编号说明    |
| rst_pin            | int       | RST引脚，见[machine.Pin](machine.Pin.md)中GPIO引脚编号说明   |

**返回值描述：**

`0` 表示成功。

`-1` 表示屏幕已经初始化。

`-2` 表示参数错误，为空或过大(大于 1000 像素点)。

`-3` 表示缓存申请失败。

`-5` 表示配置参数错误。


### `lcd.mipi_init`

```python
lcd.mipi_init(initbuf, **kwargs)
```

该方法用于初始化MIPI，按键值对传参，请根据屏厂提供的初始化参数填写。

> 1.仅支持EC200U系列和EC600U系列。
>
> 2.参数列表中，initbuf为必传参数；后面参数与缺省值不同时传入。

**参数描述：**

| 参数        | 类型      | 说明                                                         |
| ----------- | --------- | ------------------------------------------------------------ |
| initbuf     | bytearray | 必传，传入 MIPI 的配置命令                                   |
| width       | int       | 缺省值：480，屏幕的宽度，单位像素，示例：width=400           |
| hight       | int       | 缺省值：854，屏幕的高度，单位像素，示例：hight=800           |
| bpp         | int       | 缺省值：16，像素深度                                         |
| DataLane    | int       | 缺省值：2，数据通道                                          |
| MipiMode    | int       | 缺省值：0<br />模式：<br />0：DSI_VIDEO_MODE<br />1：DSI_CMD_MODE |
| PixelFormat | int       | 缺省值：0<br />像素格式：<br />0：RGB_PIX_FMT_RGB565<br />16：RGB_PIX_FMT_RGB888<br />32：RGB_PIX_FMT_XRGB888<br />48：RGB_PIX_FMT_RGBX888 |
| DsiFormat   | int       | 缺省值：0<br />DSI格式：<br />0：DSI_FMT_RGB565<br />1：DSI_FMT_RGB666<br />2：DSI_FMT_RGB666L<br />3：DSI_FMT_RGB888 |
| TransMode   | int       | 缺省值：3<br />转换模式：<br />0：DSI_CMD<br />1：DSI_PULSE<br />2：DSI_EVENT<br />3：DSI_BURST |
| RgbOrder    | int       | 缺省值：8<br />RGB顺序：<br />0：RGB<br />8：BGR             |
| BllpEnable  | bool      | 缺省值：true，blank low power 模式使能                       |
| HSync       | int       | 缺省值：10，水平同步                                         |
| HBP         | int       | 缺省值：10，水平后肩                                         |
| HFP         | int       | 缺省值：10，水平前肩                                         |
| VSync       | int       | 缺省值：4，垂直同步                                          |
| VBP         | int       | 缺省值：10，垂直后肩                                         |
| VFP         | int       | 缺省值：14，垂直前肩                                         |
| FrameRate   | int       | 缺省值：60，帧率                                             |
| TESel       | bool      | 缺省值：false，TE选择                                        |
| RstPolarity | int       | 缺省值：1，reset极性                                         |

**返回值描述：**


成功则返回`0`， 失败则报错。

**mipi屏引脚说明：**

| 引脚名 | EC600U系列 | EC200U系列 |
| ------ | ---------- | ---------- |
| CKN    | PIN61      | PIN27      |
| CKP    | PIN58      | PIN26      |
| D1N    | PIN59      | PIN24      |
| D1P    | PIN60      | PIN25      |
| D0N    | PIN69      | PIN13      |
| D0P    | PIN70      | PIN135     |
| FMARK  | PIN62      | PIN119     |
| RESET  | PIN64      | PIN120     |

**使用示例：**

```python
init_480X854 = (
0x11,0,0,
0xFF,120,5,0x77,0x01,0x00,0x00,0x10,
0xC0,0,2,0xE9,0x03,
0xC1,0,2,0x11,0x02,
0xC2,0,2,0x31,0x08,
0xCC,0,1,0x10,
0xB0,0,16,0x00,0x0D,0x14,0x0D,0x10,0x05,0x02,0x08,0x08,0x1E,0x05,0x13,0x11,0xA3,0x29,0x18,
0xB1,0,16,0x00,0x0C,0x14,0x0C,0x10,0x05,0x03,0x08,0x07,0x20,0x05,0x13,0x11,0xA4,0x29,0x18,
0xFF,0,5,0x77,0x01,0x00,0x00,0x11,
0xB0,0,1,0x6C,
0xB1,0,1,0x43,
0xB2,0,1,0x07,
0xB3,0,1,0x80,
0xB5,0,1,0x47,
0xB7,0,1,0x85,
0xB8,0,1,0x20,
0xB9,0,1,0x10,
0xC1,0,1,0x78,
0xC2,0,1,0x78,
0xD0,0,1,0x88,
0xE0,100,3,0x00,0x00,0x02,
0xE1,0,11,0x08,0x00,0x0A,0x00,0x07,0x00,0x09,0x00,0x00,0x33,0x33,
0xE2,0,13,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0xE3,0,4,0x00,0x00,0x33,0x33,
0xE4,0,2,0x44,0x44,
0xE5,0,16,0x0E,0x60,0xA0,0xA0,0x10,0x60,0xA0,0xA0,0x0A,0x60,0xA0,0xA0,0x0C,0x60,0xA0,0xA0,
0xE6,0,4,0x00,0x00,0x33,0x33,
0xE7,0,2,0x44,0x44,
0xE8,0,16,0x0D,0x60,0xA0,0xA0,0x0F,0x60,0xA0,0xA0,0x09,0x60,0xA0,0xA0,0x0B,0x60,0xA0,0xA0,
0xEB,0,7,0x02,0x01,0xE4,0xE4,0x44,0x00,0x40,
0xEC,0,2,0x02,0x01,
0xED,0,16,0xAB,0x89,0x76,0x54,0x01,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x10,0x45,0x67,0x98,0xBA,
0xFF,0,5,0x77,0x01,0x00,0x00,0x00,
0x3A,0,1,0x77,
0x36,0,1,0x00,
0x35,0,1,0x00,
0x29,0,0
)
from machine import LCD
mipilcd = LCD()
mipilcd.mipi_init(initbuf=bytearray(init_480X854), TransMode=1)
```

### `lcd.lcd_clear`

```
lcd.lcd_clear(color)
```

该方法用于清除屏幕。

**参数描述：**

- `color` - 需要刷屏的颜色值，16进制。

**返回值描述：**

成功返回`0`，失败返回`-1`。

### `lcd.lcd_write`

```
lcd.lcd_write(color_buffer,start_x,start_y,end_x,end_y)
```

该方法用于区域写屏。 

**参数描述：**

- `color_buffer` - 屏幕的颜色值缓存，bytearray类型。
- `start_x` - 起始 x 坐标，int类型。
- `start_y` - 起始 y 坐标，int类型。
- `end_x` - 结束 x 坐标，int类型。
- `end_y` - 结束 y 坐标，int类型。

**返回值描述：**

`0` 表示成功。

`-1` 表示屏幕未初始化。

`-2` 表示宽度和高度设置错误。

`-3 ` 表示数据缓存为空。

### `lcd.lcd_brightness`

```
lcd.lcd_brightness(level)
```

该方法用于设置屏幕亮度等级。

**参数描述：**

- `level` - 亮度等级，int类型 ，说明如下：<br />此处会调用 lcd.lcd_init()中的 lcd_set_brightness回调。若该参数为 None，亮度调节则由背光亮度调节引脚来控制，范围[0,5]。

**返回值描述：**

成功返回`0`， 失败返回`-1`。

### `lcd.lcd_display_on`

```
lcd.lcd_display_on()
```

此接口用于向LCD发送lcd_display_on指令来打开屏幕显示，请确保lcd初始化的时候传入了正确的lcd_display_on指令。 

**返回值描述：**

成功返回`0`， 失败返回`-1`。

### `lcd.lcd_display_off`

```python
lcd.lcd_display_off()
```

此接口用于向LCD发送lcd_display_off 指令来关闭屏幕显示，请确保lcd初始化的时候传入了正确的lcd_display_off 指令。 

**返回值描述：**

成功返回`0`， 失败返回`-1`。

### `lcd.lcd_write_cmd`

```
lcd.lcd_write_cmd(cmd_value, cmd_value_len)
```

该方法用于写入命令。

**参数描述：**

- `cmd_value` - 命令值 ，16进制 。
- `cmd_value_len` - 命令值长度，int类型。

**返回值描述：**

成功返回`0`， 失败返回其他值。

### `lcd.lcd_write_data`

```python
lcd.lcd_write_data(data_value, data_value_len)
```

该方法用于写入数据。

**参数描述：**

- `data_value` - 数据值，16进制。
- `data_value_len` - 数据值长度，int类型。

**返回值描述：**

成功返回`0`， 失败返回其他值。

### `lcd.lcd_show`

```
lcd.lcd_show(file_name, start_x,start_y,width,hight)
```

该方法采用读文件方式，显示图片。

> 该文件是由Image2Lcd工具生成的bin文件，若勾选包含图像头文件，则width和hight无需填写。

**参数描述：**

- `file_name ` - 需要显示的图片名，str类型。
- `start_x` - 起始x坐标，int类型。
- `start_y` - 起始y坐标，int类型。
- `width` - 图片宽度(若图片文件包含头信息，则该处不填)，int类型。
- `hight` - 图片高度(若图片文件包含头信息，则该处不填)，int类型。

**返回值描述：**

成功返回`0`， 失败返回其他值。

### `lcd.lcd_show_jpg`

```python
lcd.lcd_show_jpg( file_name, start_x,start_y)
```

该方法采用读文件方式，显示jpeg图片。

**参数描述：**

- `file_name ` - 需要显示的图片名，str类型。
- `start_x` - 起始x坐标，int类型。
- `start_y` - 起始y坐标，int类型。

**返回值描述：**

成功返回`0`， 失败返回其他值。

**使用示例：**

> 需要配合LCD屏使用，如下代码以st7789为例。

```python
from machine import LCD 

# 根据LCD商家给出的相应的初始化示例来填写
# 第一行：2, 0, 120,		2表示sleep命令,中间恒为0,120表示sleep的毫秒数。收到此行数据,LCD将sleep 120ms
# 第二行：0, 0, 0x11,		0表示写入寄存器地址命令,中间数字表示后续需要写入的DATA长度，0表示没有要写入的数据,0x11是寄存器地址
# 第三行：0, 1, 0x36,		0表示写入寄存器地址命令,中间数字表示后续需要写入的DATA长度，1表示要写入一字节数据,0x36是寄存器地址
# 第四行：1, 1, 0x00,		1表示写入数据命令,中间数字表示写入的数据长度,0x00是数据
# 后面按照前四行的格式将初始化示例填入即可
init_data = (2, 0, 120,	
            0, 0, 0x11,	
            0, 1, 0x36,	
            1, 1, 0x00,	
            0, 1, 0x3A,
            1, 1, 0x05,
            0, 0, 0x21,
            0, 5, 0xB2,
            1, 1, 0x05,
            1, 1, 0x05,
            1, 1, 0x00,
            1, 1, 0x33,
            1, 1, 0x33,
            0, 1, 0xB7,
            1, 1, 0x23,
            0, 1, 0xBB,
            1, 1, 0x22,
            0, 1, 0xC0,
            1, 1, 0x2C,
            0, 1, 0xC2,
            1, 1, 0x01,
            0, 1, 0xC3,
            1, 1, 0x13,
            0, 1, 0xC4,
            1, 1, 0x20,
            0, 1, 0xC6,
            1, 1, 0x0F,
            0, 2, 0xD0,
            1, 1, 0xA4,
            1, 1, 0xA1,
            0, 1, 0xD6,
            1, 1, 0xA1,
            0, 14, 0xE0,
            1, 1, 0x70,
            1, 1, 0x06,
            1, 1, 0x0C,
            1, 1, 0x08,
            1, 1, 0x09,
            1, 1, 0x27,
            1, 1, 0x2E,
            1, 1, 0x34,
            1, 1, 0x46,
            1, 1, 0x37,
            1, 1, 0x13,
            1, 1, 0x13,
            1, 1, 0x25,
            1, 1, 0x2A,
            0, 14, 0xE1,
            1, 1, 0x70,
            1, 1, 0x04,
            1, 1, 0x08,
            1, 1, 0x09,
            1, 1, 0x07,
            1, 1, 0x03,
            1, 1, 0x2C,
            1, 1, 0x42,
            1, 1, 0x42,
            1, 1, 0x38,
            1, 1, 0x14,
            1, 1, 0x14,
            1, 1, 0x27,
            1, 1, 0x2C,
            0, 0, 0x29,
            0, 1, 0x36,
            1, 1, 0x00,
            0, 4, 0x2a,
            1, 1, 0x00,
            1, 1, 0x00,
            1, 1, 0x00,
            1, 1, 0xef,
            0, 4, 0x2b,
            1, 1, 0x00,
            1, 1, 0x00,
            1, 1, 0x00,
            1, 1, 0xef,
            0, 0, 0x2c,)

display_on_data = (
    0, 0, 0x11,
    2, 0, 20,
    0, 0, 0x29,
)
display_off_data = (
    0, 0, 0x28,
    2, 0, 120,
    0, 0, 0x10,
)
# 设置区域参数
XSTART_H = 0xf0
XSTART_L = 0xf1
YSTART_H = 0xf2
YSTART_L = 0xf3
XEND_H = 0xE0
XEND_L = 0xE1
YEND_H = 0xE2
YEND_L = 0xE3
invalid_data = (
    0, 4, 0x2a,
    1, 1, XSTART_H,
    1, 1, XSTART_L,
    1, 1, XEND_H,
    1, 1, XEND_L,
    0, 4, 0x2b,
    1, 1, YSTART_H,
    1, 1, YSTART_L,
    1, 1, YEND_H,
    1, 1, YEND_L,
    0, 0, 0x2c,
)

lcd = LCD()
init_list = bytearray(init_data)
display_on_list = bytearray(display_on_data)
display_off_list = bytearray(display_off_data)
invalid_list = bytearray(invalid_data)

    
lcd.lcd_init(init_list, 240,240,13000,1,4,0,invalid_list,display_on_list,display_off_list,None)

Color_buffer =(0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f) 

Color_buffer = bytearray(Color_buffer) 

lcd.lcd_write(Color_buffer,10,10,20,20)
lcd.lcd_clear(0xf800) # 红色

lcd.lcd_show("lcd_test.bin",0,0)	#该lcd_test.bin 中包含图像头数据
lcd.lcd_show("lcd_test1.bin",0,0,126,220) #该lcd_test1.bin 中没有包含图像头数据
```
