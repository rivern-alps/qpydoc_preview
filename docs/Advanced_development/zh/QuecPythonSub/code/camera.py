# -*- coding: UTF-8 -*-
import log
from machine import LCD
import camera



class ST7789V(object):
    XSTART_H = 0xf0
    XSTART_L = 0xf1
    YSTART_H = 0xf2
    YSTART_L = 0xf3
    XEND_H = 0xE0
    XEND_L = 0xE1
    YEND_H = 0xE2
    YEND_L = 0xE3

    XSTART = 0xD0
    XEND = 0xD1
    YSTART = 0xD2
    YEND = 0xD3

    def __init__(self, width, hight):
        self._lcdlog = log.basicConfig()
        self._lcdlog = log.getLogger("LCD")
        self._lcdlog.setLevel(log.DEBUG)
        self._lcd = LCD()
        self._lcd_w = width
        self._lcd_h = hight

        self._st7789v_init_data = (
            2, 1, 120,
            0, 0, 0x11,
            2, 1, 120,
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

            0, 0, 0x2c,
        )

        self._st7789v_invalid_data = (
            0, 4, 0x2a,
            1, 1, self.XSTART_H,
            1, 1, self.XSTART_L,
            1, 1, self.XEND_H,
            1, 1, self.XEND_L,
            0, 4, 0x2b,
            1, 1, self.YSTART_H,
            1, 1, self.YSTART_L,
            1, 1, self.YEND_H,
            1, 1, self.YEND_L,
            0, 0, 0x2c,
        )
        try:
            ret = self._lcd.lcd_init(bytearray(self._st7789v_init_data), self._lcd_w, self._lcd_h, 6500, 1, 4, 0, bytearray(self._st7789v_invalid_data), None, None, None)
            self._lcdlog.info('lcd.lcd_init ret = {}'.format(ret))
            if ret != 0:
                raise CustomError("lcd init fail")
        except CustomError as e:
            self._lcdlog.info("error:",repr(e))
            

class CustomError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo=ErrorInfo

    def __str__(self):
        return self.errorinfo


class camera_preview(ST7789V):
    RETURN_OK = 0
    def __init__(self,model=0,pre_level=2,lcd_w=240,lcd_h=240):
        super().__init__(lcd_w,lcd_h)
        self._preview = None

        if model == 0:
            self._preview=camera.camPreview(0,640,480,self._lcd_w,self._lcd_h,pre_level)

        if model == 1:
            self._preview=camera.camPreview(1,320,240,self._lcd_w,self._lcd_h,pre_level)

        if self._preview is None:
            raise CustomError("This type of camera is not supported")

    def _error_put(self, value, str):
        if value != self.RETURN_OK:
            raise CustomError(str)


    def open(self):
        ret = self._preview.open()
        self._error_put(ret, "Failed to open the camera. Please check whether the camera type matches")
        
    def close(self):
        ret = self._preview.close()
        self._error_put(ret, "Failed to close the camera. Please check whether the camera is not turned on")
        
class camera_Scan(ST7789V):
    RETURN_OK = 0
    def __init__(self,model=0, decode_level=1, pre_level=1, callback=None,lcd_w=240,lcd_h=240):
        if pre_level != 0:
            super().__init__(lcd_w,lcd_h)
        self._scan = None

        if model == 0:
            self._scan=camera.camScandecode(0,decode_level, 640,480,pre_level, lcd_w,lcd_h)

        if model == 1:
            self._scan=camera.camScandecode(1,decode_level, 320,240,pre_level, lcd_w,lcd_h)

        if self._scan is None:
            raise CustomError("This type of camera is not supported")


        if callback is None:
            self._callback = self._callback_l
        else:
            self._callback = None

        self._scan.callback(self._callback)

    def _error_put(self, value, str):
        if value != self.RETURN_OK:
            raise CustomError(str)

    def open(self):
        ret = self._scan.open()
        self._error_put(ret, "Failed to open the camera. Please check whether the camera type matches")
        

    def close(self):
        ret = self._scan.close()
        self._error_put(ret, "Failed to close the camera. Please check whether the camera is not turned on")
        

    
    def start(self):
        ret = self._scan.start()
        self._error_put(ret, "Code scanning function failed to open")


    def stop(self):
        ret = self._scan.stop()
        self._error_put(ret, "Code scanning function failed to close")

    def pause(self):
        ret = self._scan.pause()
        self._error_put(ret, "Code scanning function pause failed")

    def resume(self):
        ret = self._scan.resume()
        self._error_put(ret, "Code scanning function recovery failed")

    def callback_set(self, callback):
        self._callback = callback
        ret = self._scan.callback(self._callback)
        self._error_put(ret, "Code scanning function recovery failed")

    def _callback_l(self,para):
        print("scan success:",para)

class camera_Capture(ST7789V):
    RETURN_OK = 0

    def __init__(self,model=0, pre_level=1, callback=None,lcd_w=240,lcd_h=240):
        self._lcd_w = 0
        self._lcd_h = 0
        if pre_level != 0:
            super().__init__(lcd_w,lcd_h)
        self._Cap = None

        if model == 0:
            self._Cap=camera.camCapture(0, 640,480,pre_level, lcd_w,lcd_h)

        if model == 1:
            self._Cap=camera.camCapture(1, 320,240,pre_level, lcd_w,lcd_h)

        if self._Cap is None:
            raise CustomError("This type of camera is not supported")
            return None
        if callback is None:
            self._callback = self._callback_l
        else:
            self._callback = None

        self._Cap.callback(self._callback)

    def _error_put(self, value, str):
        if value != self.RETURN_OK:
            raise CustomError(str)

    def open(self):
        ret = self._Cap.open()
        self._error_put(ret, "Failed to open the camera. Please check whether the camera type matches")

    def close(self):
        ret = self._Cap.close()
        self._error_put(ret, "Failed to close the camera. Please check whether the camera is not turned on")
    
    def start(self, name=None,img_w=240, img_h=240):
        if name is None:
            self._error_put(-1, "Please confirm the picture file name")

        ret = self._Cap.start(img_w, img_h, name)
        self._error_put(ret, "Failed to take photos")


    def _callback_l(self,para):
        print("Photo taken successfully:",para)


if __name__ == '__main__':

    pre_text = camera_preview()

    pre_text.open()
