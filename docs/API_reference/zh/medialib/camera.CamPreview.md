

# class camPreview - 摄像头预览

该类提供摄像头的预览功能。

> 使用该功能前，需要初始化LCD。

## 构造函数

### `camera.camPreview`

```python
class camera.camPreview(model,cam_w,cam_h,lcd_w,lcd_h,perview_level)
```

创建camPreview对象。

**参数描述：**

- `model` - camera型号，int类型，<a href="#label_cam_map1">点此查看</a>摄像头型号对应表。
- `cam_w` - camera水平分辨率，int类型，请按照对应摄像头型号的规格填写。
- `cam_h` - camera垂直分辨率，int类型，请按照对应摄像头型号的规格填写。
- `lcd_w` - LCD水平分辨率，int类型，请按照所使用的LCD的规格填写。
- `lcd_h` - LCD垂直分辨率，int类型，请按照所使用的LCD的规格填写。
- `perview_level` - 预览等级，int类型，型号EC600N系列、EC800N系列、EC600M系列、EC800M系列、EG810M系列可填写1或2，等级越高，图像越流畅,消耗资源越大；其他型号只可填写1。

<span id="label_cam_map1">**摄像头型号对应表：**</span>

| 编号 | 摄像头型号 | 通信方式 |
| ---- | ---------- | -------- |
| 0    | gc032a     | spi      |
| 1    | bf3901     | spi      |

## 方法

### `camPreview.open`

```python
camPreview.open()
```

该方法用于打开摄像头的预览功能。

**参数描述：**

无。

**返回值描述：**

`0` 表示打开预览成功，其他表示打开预览失败。

### `camPreview.close`

```
camPreview.close()
```

该方法用于关闭摄像头的预览功能。

**参数描述：**

无。

**返回值描述：**

`0` 表示打开预览成功，其他表示打开预览失败。