# class camCapture - 摄像头拍照

该类提供摄像头的拍照及保存功能。

> 使用该功能前，需要初始化LCD。

## 构造函数

### `camera.camCapture`

```python
class camera.camCapture(model,cam_w,cam_h,perview_level,lcd_w,lcd_h)
```

创建camCapture对象。

**参数描述：**

- `model` - camera型号，int类型，0或1，<a href="#label_cam_map3">点此查看</a>摄像头型号对应表。
- `cam_w` - camera水平分辨率，int类型，请按照对应摄像头型号的规格填写。
- `cam_h` - camera垂直分辨率，int类型，请按照对应摄像头型号的规格填写。
- `perview_level` - 预览等级，int类型，型号EC600N系列、EC800N系列、EC600M系列、EC800M系列、EG810M系列可填写1或2，等级越高，图像越流畅,消耗资源越大；其他型号只可填写1。
- `lcd_w` - LCD水平分辨率，int类型，请按照所使用的LCD的规格填写。
- `lcd_h` - LCD垂直分辨率，int类型，请按照所使用的LCD的规格填写。

<span id="label_cam_map3">**摄像头型号对应表：**</span>

| 编号 | 摄像头型号 | 通信方式 |
| ---- | ---------- | -------- |
| 0    | gc032a     | spi      |
| 1    | bf3901     | spi      |

## 方法

### `camCapture.open`

```python
camCapture.open()
```

该方法用于使能摄像头的拍照功能。

**参数描述：**

无。

**返回值描述：**

`0` 表示打开使能成功，其他表示打开使能失败。

### `camCapture.close`

```python
camCapture.close()
```

该方法用于关闭使能摄像头的拍照功能。

**参数描述：**

无。

**返回值描述：**

`0` 表示关闭使能成功，其他表示关闭使能失败。

### `camCapture.start`

```python
camCaputre.start(width,  height, pic_name)
```

该方法用于拍照保存。

**参数描述：**

- `width` - 保存图片水平分辨率，int类型。
- `height` - 保存图片垂直分辨率，int类型。
- `pic_name` - 图片名，string类型。图片无需加后缀.jpeg，会自动添加。

**返回值描述：**

`0` 表示拍照保存成功，其他表示开始拍照保存失败。

> 拍照结果还是以回调函数参数为主。

### `camCapture.callback`

```python
camCapture.callback(cb)
```

该方法用于设置拍照回调函数。

**参数描述：**

`cb` - 拍照回调函数，回调函数原型：

```python
def cb(result_list):
    pass
```

**回调函数参数描述：**

- `result_list[0]` - 拍照保存结果，int类型，`0`表示成功， 其它表示失败
- `result_list[1]` - 保存的照片名称，string类型。

**返回值描述：**

`0` 表示设置拍照回调函数成功，其他表示设置拍照回调函数失败。
