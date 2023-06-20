# CamCapture - Camera Capture

Class feature: Camera capturing and saving.

> Note: Please initialize the LCD before using this feature.

**Example:**

```python
from machine import LCD
import camera

# Initialize the LCD object based on the contents of the machine.LCD class
# lcd = LCD()
# lcd.lcd_init(*args)

# Define a callback function
def cam_callback(para):
    # para[0] Camera capture result 	0: Success Other: Failure
    print("cam capture result is ", para[0])		
    # para[1] Name of the saved image
    if para[0] == 0:
        print("image {} has been saved".format(para[1])) 

# Create a camCapture object
cam = camera.camCapture(0,640,480,1,240,240)

# Enable camera feature
cam.open()

# Set a callback function
cam.callback(cam_callback)

# Take a picture and save it
cam.start(240, 240, "image_demo")

# Disable camera feature
cam.close()
```

## Constructor

### `camera.camCapture`

```python
class camera.camCapture(model,cam_w,cam_h,perview_level,lcd_w,lcd_h)
```

Creates a camCapture object.

**Parameter:**

- `model` - Integer type. Camera model. It can be set to 0 or 1. <a href="#label_cam_map3">Click here</a> for corresponding camera model.
- `cam_w` - Integer type. Camera horizontal resolution. Please fill in according to the specifications of the corresponding camera model.
- `cam_h` - Integer type. Camera vertical resolution. Please fill in according to the specifications of the corresponding camera model.
- `perview_level` - Integer type. Preview level. Fill with 1 or 2 on EC600N series, EC800N series, EC600M series and EC800M series modules. The higher the level, the smoother the image, and the more resources consumed. Fill with 1 on other modules.
- `lcd_w` - Integer type. LCD horizontal resolution. Please fill in according to the specifications of the LCD actually used.
- `lcd_h` - Integer type. LCD vertical resolution. Please fill in according to the specifications of the LCD actually used.

<span id="label_cam_map3">**Corresponding Camera Model:**</span>

| Number | Camera Model | Communication Method |
| ------ | ------------ | -------------------- |
| 0      | GC032A       | SPI                  |
| 1      | BF3901       | SPI                  |

## Method

### camCapture.open

```python
camCapture.open()
```

This method enables the camera capturing feature.

**Parameter:**

None

**Return Value:**

`0` - Successful execution; Other values - Failed execution.

### camCapture.close

```python
camCapture.close()
```

This method disables the camera capturing feature.

**Parameter：**

None

**Return Value：**

`0` - Successful execution; Other values - Failed execution.

### camCapture.start

```python
camCaputre.start(width,  height, pic_name)
```

This method starts capturing and saving the image.

**Parameter：**

- `width` - Integer type. The horizontal resolution of the saved image.
- `height` - Integer type. The vertical resolution of the saved image.
- `pic_name` - String type. The name of the image. You don't have to add `.jpeg` suffix to the image name as it will be added automatically.

**Return Value：**

`0` - Successful execution; Other values - Failed execution.

> Note: The capture result is based on the callback function parameters.

### camCapture.callback

```python
camCapture.callback(cb)
```

This method sets the callback function of camera capturing.

**Parameter：**

- `cb` - The callback function of camera capture. The prototype is as follows:

  ```
  cb(result_list)
  ```

  **Parameter of the Callback Function：**

  - `result_list[0]` - Integer type. The save result. `0` indicates successful execution and other values indicate failed execution.

  - `result_list[1]` - String type. The name of the saved image.

**Return Value：**

`0` - Successful execution; Other values - Failed execution.

