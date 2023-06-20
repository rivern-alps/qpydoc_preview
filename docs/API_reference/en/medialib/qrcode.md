# qrcode- QR Code Display 

Feature introduction: generate a corresponding QR code according to the input content.

## Display QR Code

### `qrcode.show`

```python
qrcode.show(qrcode_str,magnification,start_x,start_y,Background_color,Foreground_color)
```

Displays QR codes to LCD.

**Parameter：**

- `qrcode_str` - String type. QR code content. 
- `magnification` - Integer type. Magnification. Range: 1–6. 
- `start_x` - Integer type. The start x coordinate of the displayed QR code.
- `start_y` - Integer type. The start y coordinate of the displayed QR code.
- `Background_color` - Integer type. Background color. Default value: 0xffff.
- `Foreground_color` - Integer type. Foreground color. Default value: 0x0000.

**Return Value**

`0` - Successful execution

`-1` - QR code generation failed

`-2` - Magnification failed

`-3` - Display failed