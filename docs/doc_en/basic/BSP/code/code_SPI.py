# -*- coding: UTF-8 -*-
import utime
from machine import SPI
from machine import Pin

# Shield the data inteference of GNSS module. As the SPI_MISO and SPI_MOSI are multiplexed as UART1, A GNSS module (L76K)is also connected to EVB. In order to disconnect the inteference to SPI communition by data from L76K, followiing two lines of codes should be added.  
gpio11 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 0)   # Used in EC600S/EC600N
gpio11.write(0)                                     # Used in EC600S/EC600N

w_data = "Grey"
r_data = bytearray(len(w_data))
count = 10  # Running count
spi_obj = SPI(1, 0, 1)      # Running count
# spi_obj = SPI(0, 0, 1)    # Running count

while count:
    count -= 1
    utime.sleep(1)
    ret = spi_obj.write_read(r_data, w_data, 100)
    if ret == -1:
        SPI_msg = "SPIReadError"
    else:
        SPI_msg = "SPIRead:{}  running:{:0>2d}".format(r_data, count)
    print(SPI_msg)
