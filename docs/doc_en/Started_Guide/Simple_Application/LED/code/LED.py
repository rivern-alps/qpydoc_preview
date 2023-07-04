import utime  # import utime module
from machine import Pin  # import Pin module


gpio_x = Pin(Pin.GPIO4, Pin.OUT, Pin.PULL_PU, 0)  # GPIO is configured in output mode with 0 output by default

count = 30
state = 1
while count:
    gpio_x.write(state)
    print('LED state: {}'.format(state))
    if state == 1:
        state = 0
    else:
        state = 1
    utime.sleep_ms(500)
    count -= 1
