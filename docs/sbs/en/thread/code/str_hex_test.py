from machine import UART
uart2 = UART(UART.UART2, 115200, 8, 0, 1, 0)
str_test = 'Quectel build a smarter world'
def str_to_hex(s):
    list_hex = ' '.join([hex(ord(c)) for c in s]).split()
    list = [int(i,16) for i in list_hex]
    bytearr = bytearray(list)
    return bytearr
hex_test = str_to_hex(str_test)
uart2.write(hex_test)