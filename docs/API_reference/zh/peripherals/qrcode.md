# qrcode- 二维码显示

根据输入的内容，生成对应的二维码。

> 当前支持的型号：EC600N/EC800N系列。

## 二维码显示功能

### `qrcode.show`

```python
qrcode.show(qrcode_str,magnification,start_x,start_y,Background_color,Foreground_color)
```

显示二维码到LCD。

**参数描述：**

- `qrcode_str`-string类型，二维码内容;
- `magnification`-int类型，放大倍数[1,6];
- `start_x`-int类型，二维码显示起始x坐标;
- `start_y`-int类型，二维码显示起始y坐标;
- `Background_color`-int类型,前景色（不设置即默认为0xffff）;
- `Foreground_color`-int类型,背景色（不设置即默认为0x0000）。

**返回值描述：**

`0`表示成功，`-1`表示生成二维码失败，`-2`表示放大失败，`-3`表示显示失败。
