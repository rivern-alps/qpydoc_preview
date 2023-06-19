# CamDecoder - Camera Scan Code

Class feature: Camera code scanning.

> Note: Please initialize the LCD before enabling preview feature.

**Example:**

```python
from machine import LCD
import camera

# Initialize the LCD object based on the contents of the machine.LCD class before enabling preview feature
# lcd = LCD()
# lcd.lcd_init(*args)

# The LCD object can be left uninitialized if there is no need to enable preview feature

# Define a callback function
def scan_callback(para):
    # para[0] Scan result 	0: Success Other: Failure
    print("scan result is ", para[0])		
    # para[1] Decode content
    if para[0] == 0:
        print("decode content is ", para[1]) 

# Create a camScandecode object
scaner = camera.camScandecode(0,1,640,480,1,240,240)

# Enable camera scanning feature
scaner.open()

# Register scanning callback function
scaner.callback(scan_callback)

# Start scanning
scaner.start()

# Stop scanning
scaner.stop()

# Disable camera scanning feature
scaner.close()
```

## Constructor

### `camera.camScandecode`

```python
class camera.camScandecode(model,decode_level,cam_w,cam_h,perview_level,lcd_w,lcd_h)
```

Creates a camScandecode object.

**Parameter：**

- `model` - Integer type. Camera model. It can be set to 0 or 1. <a href="#label_cam_map2">Click here</a> for corresponding camera model.
- `decode_level` - Integer type. Decoding level. Fill with 1 or 2 on EC600N series, EC800N series, EC600M series and EC800M series modules. The higher the level, the smoother the image, and the more resources consumed. Fill with 1 on other modules.
- `cam_w` - Integer type. Camera horizontal resolution. Please fill in according to the specifications of the corresponding camera model.
- `cam_h` - Integer type. Camera vertical resolution. Please fill in according to the specifications of the corresponding camera model.
- `perview_level` - Integer type. Preview level. Fill with 1 or 2 on EC600N series, EC800N series, EC600M series and EC800M series modules. The higher the level, the smoother the image, and the more resources consumed. Fill with 1 on other modules.
- `lcd_w` - Integer type. LCD horizontal resolution. Please fill in according to the specifications of the LCD actually used.
- `lcd_h` - Integer type. LCD vertical resolution. Please fill in according to the specifications of the LCD actually used.

<span id="label_cam_map2">**Corresponding Camera Model:**</span>

| Number | Camera Model | Communication Method |
| ------ | ------------ | -------------------- |
| 0      | GC032A       | SPI                  |
| 1      | BF3901       | SPI                  |

## Method

### camScandecode.open

```python
camScandecode.open()
```

This method enables the camera code scanning feature.

**Parameter：**

None

**Return Value：**

`0` - Successful execution; Other values - Failed execution.

### camScandecode.close

```python
camScandecode.close()
```

This method disables the camera code scanning feature.

**Parameter：**

None

**Return Value：**

`0` - Successful execution; Other values - Failed execution.

### camScandecode.start

```python
camScandecode.start()
```

This method starts the camera code scanning. 

**Parameter：**

None

**Return Value：**

`0` - Successful execution; Other values - Failed execution.

### camScandecode.stop

```python
camScandecode.stop()
```

This method stops the camera code scanning.

**Parameter：**

None

**Return Value：**

`0` - Successful execution; Other values - Failed execution.

### camScandecode.pause

```python
camScandecode.pause()
```

This method pauses the camera code scanning.

**Parameter：**

None

**Return Value：**

`0` - Successful execution; Other values - Failed execution.

### camScandecode.resume

```python
camScandecode.resume()
```

This method resumes the camera code scanning.

**Parameter：**

None

**Return Value：**

`0` - Successful execution; Other values - Failed execution.

### camScandecode.callback

```python
camScandecode.callback(cb)
```

This method sets the scanning callback function.

**Parameter：**

- `cb` - Scanning callback function. The prototype is as follows:

  ```
  cb(result_list)
  ```

  **Parameter of the Callback Function：**

  - `result_list[0]` - Integer type. The scanning result. `0` indicates successful execution and other values indicate failed execution.

  - `result_list[1]` - String type. The scanning content.

**Return Value：**

`0` - Successful execution; Other values - Failed execution.