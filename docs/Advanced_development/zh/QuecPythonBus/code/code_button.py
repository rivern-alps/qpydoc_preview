import utime
from machine import Pin


if __name__ == '__main__':
    gpio = Pin(Pin.GPIO4, Pin.IN, Pin.PULL_PU, 1)
    while True:
        if gpio.read() == 0:
            utime.sleep_ms(10)
            if gpio.read() == 0:
                while gpio.read() == 0:
                    pass
                print("Button press")
        pass