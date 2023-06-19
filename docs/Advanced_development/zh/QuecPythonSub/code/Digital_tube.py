"""
@Author: Kayden
@Date: 2021-09-23
@Description: Digital tube experiment
@FilePath: Digital_tube.py
"""
from machine import Pin
import utime

'''
数码管模块和V1.3开发板的排针连接方式为：
DIO接开发板上P60对应的排针
RCLK接开发板上P58对应的排针
SCLK接开发板上P61对应的排针
P60对应EC600S/EC600N模组的GPIO13、对应EC600U模组的GPIO4
P56对应EC600S/EC600N模组的GPIO28、对应EC600U模组的GPIO16
P61对应EC600S/EC600N模组的GPIO14、对应EC600U模组的GPIO1
'''
# 当使用的模组为EC600S/EC600N时
# DIO = Pin(Pin.GPIO13, Pin.OUT, Pin.PULL_PU, 0)
# RCLK = Pin(Pin.GPIO28, Pin.OUT, Pin.PULL_PU, 0)
# SCLK = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_PU, 0)

# 当使用的模组为EC600U时
DIO = Pin(Pin.GPIO4, Pin.OUT, Pin.PULL_PU, 0)
RCLK = Pin(Pin.GPIO16, Pin.OUT, Pin.PULL_PU, 0)
SCLK = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_PU, 0)

# 变量初始化
i = 0
j = 0

# 字模元组     0 	1	  2	   3	   4	5	 6	   7	   8	9	  A	   b	   C    d	  E      F     -
LED_fonts = (0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x92, 0x82, 0xF8, 0x80, 0x90, 0x88, 0x83, 0xC6, 0xA1, 0x86, 0x8E, 0xBF)


# 向74HC595写入数据的函数
def LED_OUT(data):
    for i in range(8):
        if data & 0X80:
            DIO.write(1)
        else:
            DIO.write(0)
        data <<= 1
        SCLK.write(0)
        SCLK.write(1)


# 数码管依次显示17个字模的函数
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
