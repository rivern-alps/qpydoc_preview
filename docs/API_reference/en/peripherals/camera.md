# camera  - Camera Driver

Module feature: Camera preview, camera decoder, and camera capture.

> Currently supported modules: EC600N Series, EC800N Series, EC600M Series, EC800M Series, EC600U-CN and EC200U-CN.
>
> Note: If the preview feature is needed, please initialize the LCD object first by referring to [the content of lcd class in the machine module](machine.LCD.md) before initializing the camera object.

**Example:**

```python
# -*- coding: UTF-8 -*-
from machine import LCD
import camera

# If the preview feature is needed, please initialize the LCD object first by referring to the content of the lcd class in the machine module.
# lcd = LCD()
# lcd.lcd_init(*args)

# Camera preview feature
preview = camera.camPreview(0,640,480,240,240,1)
preview.open()
preview.close()

# Camera decoder feature
def scan_callback(para):
    # para[0] Scan result 	0: Success Other: Failure
    print("scan result is ", para[0])		
    # para[1] Decode content
    if para[0] == 0:
        print("decode content is ", para[1]) 

scaner = camera.camScandecode(0,1,640,480,1,240,240)
scaner.open()
scaner.callback(scan_callback)
scaner.start()
scaner.stop()
scaner.close()

# Camera capture feature
def cam_callback(para):
    # para[0] Camera capture result 	0: Success Other: Failure
    print("cam capture result is ", para[0])		
    # para[1] Name of the saved image
    if para[0] == 0:
        print("image {} has been saved".format(para[1])) 

cam = camera.camCapture(0,640,480,1,240,240)
cam.open()
cam.callback(cam_callback)
cam.start(240, 240, "image_demo")
cam.close()
```



## Classes

- [class CamPreview - Camera Preview](./camera.CamPreview.md)

- [class CamDecoder - Camera Decoder](camera.CamDecoder.md)

- [class CamCapture - Camera Capture](camera.CamCapture.md)