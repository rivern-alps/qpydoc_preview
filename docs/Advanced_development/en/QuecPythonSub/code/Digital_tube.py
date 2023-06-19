"""
@Author: Kayden
@Date: 2021-09-23
@Description: Digital tube experiment
@FilePath: Digital_tube.py
"""
from machine import Pin
import utime

'''
The pin arrangement connection mode of nixie tube module and v1.3 development board is:
Dio is connected to the row pin corresponding to P60 on the development board
RCLK is connected to the row pin corresponding to P58 on the development board
SCLK is connected to the row pin corresponding to p61 on the development board
P60 corresponds to gpio13 of ec600s / ec600n module and gpio4 of ec600u module
P56 corresponds to gpio28 of ec600s / ec600n module and gpio16 of ec600u module
P61 corresponds to gpio14 of ec600s / ec600n module and gpio1 of ec600u module
'''
# When the module used is ec600s / ec600n
# DIO = Pin(Pin.GPIO13, Pin.OUT, Pin.PULL_PU, 0)
# RCLK = Pin(Pin.GPIO28, Pin.OUT, Pin.PULL_PU, 0)
# SCLK = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_PU, 0)

# When the module used is ec600u
DIO = Pin(Pin.GPIO4, Pin.OUT, Pin.PULL_PU, 0)
RCLK = Pin(Pin.GPIO16, Pin.OUT, Pin.PULL_PU, 0)
SCLK = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_PU, 0)

# Font tuple 0 	    1	   2     3     4    5       6    7     8     9     A 	 b 	   C    d 	   E     F     -
LED_fonts = (0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x92, 0x82, 0xF8, 0x80, 0x90, 0x88, 0x83, 0xC6, 0xA1, 0x86, 0x8E, 0xBF)


# Function to write data to 74HC595
def LED_OUT(data):
    for i in range(8):
        if data & 0X80:
            DIO.write(1)
        else:
            DIO.write(0)
        data <<= 1
        SCLK.write(0)
        SCLK.write(1)


# The nixie tube displays 17 font functions in turn
def LED_Display():
    for j in range(17):
        LED_OUT(LED_fonts[j])
        LED_OUT(0x0f)
        RCLK.write(0)
        RCLK.write(1)
        utime.sleep(1)


if __name__ == "__main__":
    while True:
        LED_Display()
