# class camScandecode - 摄像头扫码

该类提供摄像头的扫码功能。

> 如果开启预览，需要先初始化LCD。

## 构造函数

### `camera.camScandecode`

```python
class camera.camScandecode(model,decode_level,cam_w,cam_h,perview_level,lcd_w,lcd_h)
```

创建camScandecode对象。

**参数描述：**

- `model` - camera型号，int类型，0或1，<a href="#label_cam_map2">点此查看</a>摄像头型号对应表。
- `decode_level` - 解码等级，int类型，型号EC600N系列、EC800N系列、EC600M系列、EC800M系列、EG810M系列可填写1或2，等级越高，图像越流畅，消耗资源越大；其他型号只可填写1。
- `cam_w` - camera水平分辨率，int类型，请按照对应摄像头型号的规格填写。
- `cam_h` - camera垂直分辨率，int类型，请按照对应摄像头型号的规格填写。
- `perview_level` - 预览等级，int类型，型号EC600N系列、EC800N系列、EC600M系列、EC800M系列、EG810M系列可填写1或2，等级越高，图像越流畅，消耗资源越大；其他型号只可填写1。
- `lcd_w` - LCD水平分辨率，int类型，请按照所使用的LCD的规格填写。
- `lcd_h` - LCD垂直分辨率，int类型，请按照所使用的LCD的规格填写。

<span id="label_cam_map2">**摄像头型号对应表：**</span>

| 编号 | 摄像头型号 | 通信方式 |
| ---- | ---------- | -------- |
| 0    | gc032a     | spi      |
| 1    | bf3901     | spi      |

## 方法

### `camScandecode.open`

```python
camScandecode.open()
```

该方法用于使能摄像头的扫码功能。

**参数描述：**

无。

**返回值描述：**

`0` 表示打开使能成功，其他表示打开使能失败。

### `camScandecode.close`

```python
camScandecode.close()
```

该方法用于关闭使能摄像头的扫码功能。

**参数描述：**

无。

**返回值描述：**

`0` 表示关闭使能成功，其他表示关闭使能失败。

### `camScandecode.start`

```python
camScandecode.start()
```

该方法用于开始摄影头扫码。

**参数描述：**

无。

**返回值描述：**

`0` 表示开始扫码，其他表示开始扫码失败。

### `camScandecode.stop`

```python
camScandecode.stop()
```

该方法用于结束摄像头扫码。

**参数描述：**

无。

**返回值描述：**

`0` 表示结束扫码扫码，其他表示结束扫码失败。

### `camScandecode.pause`

```python
camScandecode.pause()
```

该方法用于暂停摄像头扫码。

**参数描述：**

无。

**返回值描述：**

`0` 表示暂停扫码成功，其他表示暂停扫码失败。

### `camScandecode.resume`

```python
camScandecode.resume()
```

该方法用于继续摄像头扫码。

**参数描述：**

无。

**返回值描述：**

`0` 表示继续扫码成功，其他表示继续扫码失败。

### `camScandecode.callback`

```python
camScandecode.callback(cb)
```

该方法用于设置识别回调函数。

**参数描述：**

`cb` - 识别回调函数，回调函数原型：

```python
def cb(result_list):
    pass
```

**回调函数参数描述：**

- `result_list[0]` - 扫码结果，int类型，`0`表示成功， 其它表示失败
- `result_list[1]` - 扫码内容，string类型。

**返回值描述：**

`0` 表示设置识别回调函数成功，其他表示设置识别回调函数失败。