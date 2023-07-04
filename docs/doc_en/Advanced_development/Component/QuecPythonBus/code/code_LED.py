# Name of experiment：	horse race lamp
# API connection：  https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=pin


from machine import Pin
import utime


IOdictRead = {}  # Record the GPIO ports that have been initialized
IOdictWrite = {}  # Record the GPIO ports that have been initialized


def GPIO_Read(gpioX, Pull=Pin.PULL_DISABLE, level=1):
    if IOdictWrite.get(gpioX, None):
        del IOdictWrite[gpioX]
    gpioIO = IOdictRead.get(gpioX, None)
    if gpioIO:
        return gpioIO.read()
    else:
        IOdictRead[gpioX] = (Pin(gpioX, Pin.IN, Pull, level))
        gpioIO = IOdictRead.get(gpioX, None)
        return gpioIO.read()


def GPIO_Write(gpioX, level, Pull=Pin.PULL_DISABLE):
    if IOdictRead.get(gpioX, None):
        del IOdictRead[gpioX]
    gpioIO = IOdictWrite.get(gpioX, None)
    if gpioIO:
        gpioIO.write(level)
    else:
        IOdictWrite[gpioX] = (Pin(gpioX, Pin.OUT, Pull, level))
        gpioIO = IOdictWrite.get(gpioX, None)
        gpioIO.write(level)


LED1 = Pin.GPIO1  # Define LED pin
LED2 = Pin.GPIO2  # Define LED pin
LED3 = Pin.GPIO3  # Define LED pin
LED4 = Pin.GPIO4  # Define LED pin
LED5 = Pin.GPIO5  # Define LED pin


def IO_On(gpioX):  # Set the pin as 0
    GPIO_Write(gpioX, 0)  # Call write function


def IO_Off(gpioX):  # Set the pin as 1
    GPIO_Write(gpioX, 1)  # Call write function


def IO_All_Off():  # Set all pins as 1
    IO_Off(LED1)
    IO_Off(LED2)
    IO_Off(LED3)
    IO_Off(LED4)
    IO_Off(LED5)


def main():
    while True:
        IO_All_Off()	# Off 
        IO_On(LED1)	# On
        utime.sleep_ms(200)	# Latency
        IO_All_Off()	# Off 
        IO_On(LED2)	# On
        utime.sleep_ms(200)	# Latency
        IO_All_Off()	# Off 
        IO_On(LED3)	# On
        utime.sleep_ms(200)	# Latency
        IO_All_Off()	# Off 
        IO_On(LED4)	# On
        utime.sleep_ms(200)	# Latency
        IO_All_Off()	# Off 
        IO_On(LED5)	# On
        utime.sleep_ms(200)	# Latency


if __name__ == "__main__":
    main()
