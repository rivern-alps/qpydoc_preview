from machine import ExtInt


def callback(args):
    print('interrupt: {}'.format(args))


extint = ExtInt(ExtInt.GPIO4, ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, callback)  # Create object
extint.enable()  # Enable interrupt
print('Start GPIO: {} Interrupt. \r\n'.format(extint.line()))

# extint.disable()  # Disable interrupt 
