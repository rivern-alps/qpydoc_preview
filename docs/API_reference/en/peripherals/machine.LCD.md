# LCD - LCD Driver

This class controls LCD.

> Supported module models are as follows:
>
> EC200U series module, EC600U series module, EC600N series module, EC800N series module,
>
> EC600M-CNLA, EC600M-CNLE
>
> EC800M-CNLA, EC800M-CNLE, EC800M-CNGA, EC800G-CNGA
>
> EG912N-ENAA, EG912U-GLAA
>
> EG915N-EUAG, EG915U-EUAB

## Constructor

### `machine.LCD`

```python
class machine.lcd = LCD()
```

**Example:**

```python
>>> from machine import LCD 
>>> lcd = LCD()    # Creates a LCD object
```

## Methods

### `lcd.lcd_init`

This method initializes LCD.

#### Interface 1: The device connects to LCM interfaces of modules

```python
lcd.lcd_init(lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid, lcd_display_on, lcd_display_off, lcd_set_brightness)
```

**Parameter:**

| Parameter          | Type      | Description                                                  |
| ------------------ | --------- | ------------------------------------------------------------ |
| lcd_init_data      | bytearray | Write command for LCD initialization.                        |
| lcd_width          | int       | Width of LCD screen. The width cannot exceed 500 pixels.     |
| lcd_hight          | int       | Height of LCD screen. The height cannot exceed 500 pixels.   |
| lcd_clk            | int       | LCD SPI clock frequency:<br />6500: 6.5 MHz<br />13000: 13 MHz<br />26000: 26 MHz<br />52000: 52 MHz |
| data_line          | int       | Number of data lines. Parameter values are 1 and 2.          |
| line_num           | int       | Number of lines. Parameter values are 3 and 4.               |
| lcd_type           | int       | Screen type. 0-rgb; 1-fstn.                                  |
| lcd_invalid        | bytearray | Write command for LCD region settings.                       |
| lcd_display_on     | bytearray | Write command for turning on the LCD screen.                 |
| lcd_display_off    | bytearray | Write command for turning off the LCD screen.                |
| lcd_set_brightness | bytearray | Write command for LCD screen brightness:<br />None indicates that LCD_BL_K controls brightness. |

**Return Value:**

`0` - Successful execution.

`-1` - LCD initialized.

`-2` - Parameter error. Parameter is empty or too large (more than 1000 pixels).

`-3` - Failed cache request.

`-5` - Parameter configuration error.

#### Interface 2: The device connects to module SPI

```python
lcd.lcd_init(lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid, lcd_display_on, lcd_display_off, lcd_set_brightness, lcd_interface, spi_port, spi_mode, cs_pin, dc_pin, rst_pin)
```

**Parameter:**

| Parameter          | Type      | Description                                                  |
| ------------------ | --------- | ------------------------------------------------------------ |
| lcd_init_data      | bytearray | Write command for LCD initialization.                        |
| lcd_width          | int       | Width of LCD screen. The width cannot exceed 500 pixels.     |
| lcd_hight          | int       | Height of LCD screen. The height cannot exceed 500 pixels.   |
| lcd_clk            | int       | See machine.SPI <font color="red"> 漏了超链接 </font>for creating SPI objects parameter descriptions. |
| data_line          | int       | Number of data lines. Parameter values are 1 and 2.          |
| line_num           | int       | Number of lines. Parameter values are 3 and 4.               |
| lcd_type           | int       | Screen type. 0-rgb; 1-fstn.                                  |
| lcd_invalid        | bytearray | Write command for LCD region settings.                       |
| lcd_display_on     | bytearray | Write command for turning on LCD screen.                     |
| lcd_display_off    | bytearray | Write command for turning off LCD screen.                    |
| lcd_set_brightness | bytearray | Write command for LCD screen brightness:<br />None indicates that LCD_BL_K controls the brightness. |
| lcd_interface      | int       | LCD interface type. 0 - LCM; 1 - SPI                         |
| spi_port           | int       | Channel selection [0,1]. See machine.SPI <font color="red"> 漏了超链接 </font>for port description. |
| spi_mode           | int       | SPI work mode (Work mode 0 is commonly used):<br />CPOL: The level of clock signal of SCLK when SPI is idle (0: low level; 1: high level)<br />0 : CPOL=0, CPHA=0<br />1 : CPOL=0, CPHA=1<br />2 : CPOL=1, CPHA=0<br />3 : CPOL=1, CPHA=1 |
| cs_pin             | int       | CS pin. See [machine.Pin](machine.Pin.md) for descriptions of GPIO pin number. |
| dc_pin             | int       | DC pin. See [machine.Pin](machine.Pin.md) for descriptions of GPIO pin number. |
| rst_pin            | int       | RST pin. See [machine.Pin](machine.Pin.md) for descriptions of GPIO pin number. |

**Return Value:**

`0` - Successful execution.

`-1` - LCD Initialized.

`-2` - Parameter error. Parameter is empty or too large (more than 1000 pixels).

`-3` - Failed cache request.

`-5` - Parameter configuration error.


### `lcd.mipi_init`

```python
lcd.mipi_init(initbuf, **kwargs)
```

This method initializes MIPI and passes parameters according to key-value pairs. Please set parameters according to initialization parameters provided by the screen manufacturer.  

> 1. Only EC200U and EC600U series modules support this function.
> 2. In the parameter list below, *initbuf* is a required parameter. Other parameters are optional parameters. If values are consistent with default values, you needn’t pass this parameter. 

**Parameter:**

| Parameter   | Type      | Description                                                  |
| ----------- | --------- | ------------------------------------------------------------ |
| initbuf     | bytearray | Required. Write command for passing MIPI.                    |
| width       | int       | Width of LCD screen. Default value: 480.  Example: width = 400. |
| hight       | int       | Height of LCD screen. Default value: 854. Example: height = 800. |
| bpp         | int       | Bits per pixel. Default value: 16.                           |
| DataLane    | int       | Data channel. Default value: 2.                              |
| MipiMode    | int       | Mode:<br />0: DSI_VIDEO_MODE<br />1: DSI_CMD_MODE<br />Default value: 0 |
| PixelFormat | int       | Pixel format: <br />0: RGB_PIX_FMT_RGB565<br />16: RGB_PIX_FMT_RGB888<br />32: RGB_PIX_FMT_XRGB888<br />48: RGB_PIX_FMT_RGBX888<br />Default value: 0 |
| DsiFormat   | int       | DSI format:<br />0: DSI_FMT_RGB565<br />1: DSI_FMT_RGB666<br />2: DSI_FMT_RGB666L<br />3: DSI_FMT_RGB888<br />Default value: 0 |
| TransMode   | int       | Transform mode:<br />0: DSI_CMD<br />1: DSI_PULSE<br />2: DSI_EVENT<br />3: DSI_BURST<br />Default value: 3 |
| RgbOrder    | int       | RGB order: <br />0: RGB<br />8: BGR<br />Default value: 8    |
| BllpEnable  | bool      | Enable blank low power. Default value: true.                 |
| HSync       | int       | Horizontal synchronization. Default value: 10.               |
| HBP         | int       | Horizontal back porch. Default value: 10.                    |
| HFP         | int       | Horizontal front porch. Default value: 10.                   |
| VSync       | int       | Vertical Synchronization. Default value: 4.                  |
| VBP         | int       | Vertical back porch. Default value: 10.                      |
| VFP         | int       | Vertical front porch. Default value: 14.                     |
| FrameRate   | int       | Frame rate. Default value: 60.                               |
| TESel       | bool      | TE selection. Default value: false.                          |
| RstPolarity | int       | Reset polarity. Default value: 1.                            |

**Return Value:**

`0` - Successful execution

Error codes - Failed execution

**Pin Description of MIPI Screen：**

| Pin Name | EC600U Series Module | EC200U Series Module |
| -------- | -------------------- | -------------------- |
| CKN      | PIN61                | PIN27                |
| CKP      | PIN58                | PIN26                |
| D1N      | PIN59                | PIN24                |
| D1P      | PIN60                | PIN25                |
| D0N      | PIN69                | PIN13                |
| D0P      | PIN70                | PIN135               |
| FMARK    | PIN62                | PIN119               |
| RESET    | PIN64                | PIN120               |

**Example:**

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

This method clears LCD screen. 

**Parameter:**

- `color` - String type in hexadecimal. The color used to clear the LCD screen.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `lcd.lcd_write`

```
lcd.lcd_write(color_buffer,start_x,start_y,end_x,end_y)
```

This method writes LCD screen in a specified area.

**Parameter:**

- `color_buffer` - Bytearray type. Cache of screen color value.
- `start_x` - Integer type. The start x coordinate. 
- `start_y` - Integer type. The start y coordinate. 
- `end_x` - Integer type. The end x coordinate. 
- `end_y` - Integer type. The end y coordinate. 

**Return Value:**

`0` - Successful execution.

`-1` - LCD screen is not initialized.

`-2` - Width and height setting errors.

`-3 ` - Empty data cache.

### `lcd.lcd_brightness`

```
lcd.lcd_brightness(level)
```

This method sets the screen brightness level.

**Parameter:**

- `level` - Integer type. Brightness level. The description is as follows: <br />*lcd_set_brightness* in *lcd.lcd_init()* will be called. If the parameter is None, the brightness is controlled by LCD_BL_K. Range: [0,5].

**Return Value:**

`0 `- Successful execution

`-1` - Failed execution

### `lcd.lcd_display_on`

```
lcd.lcd_display_on()
```

This method turns on the screen display. *lcd_display_on* in *lcd.lcd_init()* will be called after you call this interface.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `lcd.lcd_display_off`

```python
lcd.lcd_display_off()
```

This method turns off the screen display. *lcd_display_off* in *lcd.lcd_init()* will be called after you call this interface. 

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `lcd.lcd_write_cmd`

```
lcd.lcd_write_cmd(cmd_value, cmd_value_len)
```

This method writes commands.

**Parameter:**

- `cmd_value` - String type in hexadecimal. Command value.
- `cmd_value_len` - Integer type. Command value length.

**Return Value:**

`0` - Successful execution

`Other Values` - Failed execution

### `lcd.lcd_write_data`

```python
lcd.lcd_write_data(data_value, data_value_len)
```

This method writes commands.

**Parameter:**

- `data_value` - String type in hexadecimal. Data value.
- `data_value_len` - Integer type. Data value length.

**Return Value:**

`0` - Successful execution

`Other Values` - Failed execution

### `lcd.lcd_show`

```
lcd.lcd_show(file_name, start_x,start_y,width,hight)
```

This method displays images by reading files.

> This file is a bin file generated by *Image2Lcd*. If the image header file is checked, you needn’t to enter width and height.

**Parameter:**

- `file_name ` - String type. Image name to be displayed.
- `start_x` - Integer type. The start x coordinate. 
- `start_y` - Integer type. The start y coordinate. 
- `width` - Integer type. Image width (If the image file contains header information, you can leave image width blank).
- `hight` - Integer type. Image height (If the image file contains header information, you can leave image height blank).

**Return Value:**

`0` - Successful execution

`Other Values` - Failed execution

### `lcd.lcd_show_jpg`

```python
lcd.lcd_show_jpg( file_name, start_x,start_y)
```

This method displays JPEG images by reading files.

**Parameter:**

- `file_name ` - String type. Image name needs to be displayed.
- `start_x` - Integer type. The start x coordinate. 
- `start_y` - Integer type. The start y coordinate. 

**Return Value:**

`0` - Successful execution

`Other Values` - Failed execution

**Example:**

> An LCD screen is required. The following code takes st7789 as an example.

```python
from machine import LCD 

# Follows the corresponding initialization example given by the LCD manufacturer
# First row: 2, 0, 120,		2 indicates the command of sleep. The middle digit is fixed as 0. 120 indicates the number of milliseconds of sleep. LCD will sleep for 120 ms after receiving this row of data.
# Second row: 0, 0, 0x11,		0 indicates the command of writing data to the register address. The middle digit indicates the length of data to be written later. 0 indicates no data is to be written. 0x11 indicates the register address.
# Third row: 0, 1, 0x36,		0 indicates the command of writing data to the register address. The middle digit indicates the length of data to be written later. 1 indicates one byte of data is to be written. 0x36 indicates the register address.
# Fourth row: 1, 1, 0x00,		1 indicates the command of writing data. The middle digit indicates the length of data to be written. 0x00 indicates the data.
# Then follow the format of the first four rows to enter initialization examples. 
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
# Sets the parameters of LCD screen area
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
lcd.lcd_clear(0xf800) # Red

lcd.lcd_show("lcd_test.bin",0,0)	#This lcd_test.bin file contains image header data. 
lcd.lcd_show("lcd_test1.bin",0,0,126,220) #This lcd_test1.bin file does not contain image header data. 
```
