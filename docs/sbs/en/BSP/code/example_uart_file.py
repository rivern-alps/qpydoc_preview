import _thread  # 导入线程模块
import utime  # 导入定时模块
import log  # 导入log模块
from machine import UART  # 导入UART模块

# 设置日志输出级别
log.basicConfig(level=log.INFO)
uart_log = log.getLogger("UART")
uart = UART(UART.UART1, 115200, 8, 0, 1, 0)

def uartWrite():
    global uart
    count = 10
    while count:
        write_msg = "Hello count={}".format(count)
        uart.write(write_msg)
        uart_log.info("Write msg :{}".format(write_msg))
        utime.sleep(1)
        count -= 1
    uart_log.info("uartWrite end!")


def UartRead():
    global uart
    while 1:
        msgLen = uart.any()
        utime.sleep(0.1)
        # 当有数据时进行读取
        if msgLen:
            msg = uart.read(msgLen)
            utf8_msg = msg.decode()
            uart_log.info("UartRead msg: {}".format(utf8_msg))
        else:
            continue


def run():
    _thread.start_new_thread(UartRead, ())
    _thread.start_new_thread(uartWrite, ())

if __name__ == "__main__":
    run()
    while True:
        utime.sleep(0.5)
