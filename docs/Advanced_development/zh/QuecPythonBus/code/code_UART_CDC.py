# import log
import utime
import _thread
import ubinascii
from machine import UART

state = 1
uart_x = None
usbcdc = None


def uart_x_read():
    global state
    global uart_x
    global usbcdc

    while state:
        msglen = uart_x.any()  # Returns whether there is a readable length of data
        if msglen:  # Read when data is available
            msg = uart_x.read(msglen)  # Read Data
            utf8_msg = msg.decode()  # The initial data is byte type (bytes), which encodes byte type data
            if "Grey" in utf8_msg:
                break
            else:
                usbcdc.write("{}".format(utf8_msg))  # send data
        utime.sleep_ms(1)
    state = 0


def usbcdc_read():
    global state
    global uart_x
    global usbcdc

    while state:
        msglen = usbcdc.any()  # Returns whether there is a readable length of data
        if msglen:  # Read when data is available
            msg = usbcdc.read(msglen)  # Read Data
            utf8_msg = msg.decode()  # The initial data is byte type (bytes), which encodes byte type data
            if "Grey" in utf8_msg:
                break
            else:
                uart_x.write("{}".format(utf8_msg))  # send data
        utime.sleep_ms(1)
    state = 0


if __name__ == "__main__":
    uart_x = UART(UART.UART2, 115200, 8, 0, 1, 0)
    usbcdc = UART(UART.UART3, 115200, 8, 0, 1, 0)  # It is unvalid to set the baudrate, while in communication, any baudrate is available

    uart_x.write("Grey_test")
    usbcdc.write("Grey_test") 

    _thread.start_new_thread(uart_x_read, ())  # Create a thread to listen for receiving UART messages
    _thread.start_new_thread(usbcdc_read, ())  # Create a thread to listen for receiving CDC messages

    while state:
        utime.sleep_ms(1)
