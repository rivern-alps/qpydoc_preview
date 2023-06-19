

# CamPreview - Camera Preview

Class feature: Camera previewing.

> Note: Please initialize the LCD before using this feature.

**Example:**

```python
from machine import LCD
import camera

# Initialize the LCD object based on the contents of the machine.LCD class
# lcd = LCD()
# lcd.lcd_init(*args)

# Create a camPreview object
preview = camera.camPreview(0,640,480,240,240,1)

# Enable camera preview feature
preview.open()

# Disable camera preview feature
preview.close()
```

## Constructor

### `camera.camPreview`

```python
class camera.camPreview(model,cam_w,cam_h,lcd_w,lcd_h,perview_level)
```

Creates a camPreview object.

**Parameter:**

- `model` - Integer type. Camera model. <a href="#label_cam_map1">Click here</a> for corresponding camera model.
- `cam_w` - Integer type. Camera horizontal resolution. Please fill in according to the specifications of the corresponding camera model.
- `cam_h` - Integer type. Camera vertical resolution. Please fill in according to the specifications of the corresponding camera model.
- `lcd_w` - Integer type. LCD horizontal resolution. Please fill in according to the specifications of the LCD actually used.
- `lcd_h` - Integer type. LCD vertical resolution. Please fill in according to the specifications of the LCD actually used.
- `perview_level` - Integer type. Preview level. Fill with 1 or 2 on EC600N series, EC800N series, EC600M series and EC800M series modules. The higher the level, the smoother the image, and the more resources consumed. Fill with 1 on other modules.

<span id="label_cam_map1">**Corresponding Camera Model:**</span>

| Number | Camera Model | Communication Method |
| ------ | ------------ | -------------------- |
| 0      | GC032A       | SPI                  |
| 1      | BF3901       | SPI                  |

## Method

### camPreview.open

```python
camPreview.open()
```

This method enables the camera preview feature.

**Parameter：**

None

**Return Value：**

`0` - Successful execution; Other values - Failed execution.

### camPreview.close

```
camPreview.close()
```

This method disables the camera preview feature.

**Parameter：**

None

**Return Value：**

`0` - Successful execution; Other values - Failed execution.