'''
File: EBF_SMD4805.py
Project: others
File Created: Wednesday, 6th January 2021 2:16:52 pm
Author: chengzhu.zhou
-----
Last Modified: Wednesday, 6th January 2021 2:56:42 pm
Modified By: chengzhu.zhou
-----
Copyright 2021 - 2021 quectel
'''

"""
reference material
1. API
https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=pwm
https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=pin
2. Module data
https://item.taobao.com/item.htm?ft=t&id=543053172983
https://ebf-products.readthedocs.io/zh_CN/latest/module/motor/ebf-msd4805.html
"""

"""
Pin connection
| electrical machinery | development board | The corresponding function label |
| -------------------- | ----------------- | -------------------------------- |
| ENA- （GPIO）        | GPIO81 (pin 16)   | GPIO7                            |
| DIR- (GPIO)          | GPIO77 (pin15)    | GPIO6                            |
| PUL- （PWM）         | GPIO2_1V8 (pin70) | PWM2                             |
| ENA+   DIR+  PUL+    | 1V8(power supply) | 无                               |
"""




from misc import PWM
from machine import Pin
import utime as time
import urandom as random
import log
def delay_500us():
    for i in range(600):
        pass


def delay_250us():
    for i in range(310):
        pass


ENABLE_MOTOR = 0x1
DISABLE_MOTOR = 0x0

DIR_CLOCKWISE = 0x1
DIR_ANTI_CLOCKWISE = 0x0


class ebf_smd4805():

    dev_log = None

    # Parameters of stepping motor
    sm_para_step = None  # Step angle
    # Parameters of controller
    env_pin = None  # Enable pin
    dir_pin = None  # Direction pin
    pul_pwm = None  # Pulse output pin
    ctrl_divstep = None  # For subdivision parameters, please refer to the controller manual

    def init(self, step, divstep):
        self.dev_log = log.getLogger("ebf_smd4805")
        self.env_pin = Pin(Pin.GPIO7, Pin.OUT, Pin.PULL_DISABLE, 0)
        self.dir_pin = Pin(Pin.GPIO6, Pin.OUT, Pin.PULL_DISABLE, 0)
        # Configure the parameters of the motor
        self.sm_para_step = step
        # Configure the parameters of the controller
        self.ctrl_divstep = divstep

    def reset(self):
        self.env_pin.write(DISABLE_MOTOR)
        self.dir_pin.write(DIR_ANTI_CLOCKWISE)
        if self.pul_pwm is not None:
            self.pul_pwm.close()

    # Initialize PWM according to frequency
    def outputpwm(self, HZ, duty_cycle):
        # Convert Hz to us level
        cycleTime = int(1000000/HZ)
        highTime = int(cycleTime * duty_cycle)
        return highTime, cycleTime

    # Set the output of PWM according to the speed
    def enable_pwm(self, speed):
        # 1. First, calculate the number of pulses required for one revolution according to the stepping angle of the stepping
        Count_pulse = int(360/self.sm_para_step)
        self.dev_log.debug("sm motor step as {0}".format(Count_pulse))
        # 2. According to the subdivision parameters of the controller, calculate the number of pulses required for the controller to control the stepper motor to rotate for one turn
        Count_pulse = int(Count_pulse * self.ctrl_divstep)
        # 3. Finally, calculate how many pulses are needed to rotate the speed cycle in one second, in other words, the frequency
        Count_pulse = int(Count_pulse * speed)
        # 4. Initialize PWM, default duty cycle% 50
        highTime, cycleTime = self.outputpwm(Count_pulse, 0.1)
        self.dev_log.debug(
            """config  frequency  is {0}HZ,cycleTime {1}us, hightime {2}us"""
            .format(Count_pulse, cycleTime, highTime))
        self.pul_pwm = PWM(PWM.PWM2, PWM.ABOVE_10US,
                           int(highTime), int(cycleTime))
        self.pul_pwm.open()
        pass

    def disable_pwm(self):
        self.pul_pwm.close()
        pass

    # Speed is the speed, how many laps per second
    # Duration is the duration, Ms
    # Dir indicates direction
    def run(self, speed, Duration, dir=DIR_CLOCKWISE):
        self.dir_pin.write(dir)
        self.dev_log.info(
            "Configure the motor to rotate {0} revolutions per second".format(speed))
        self.enable_pwm(speed)
        self.env_pin.write(1)
        # delay
        for i in range(int(Duration * 4)):
            delay_250us()
        self.env_pin.write(0)

        self.reset()
        pass


def test_ebf_smd4805():
    log.basicConfig(level=log.DEBUG)
    # log.basicConfig(level=log.INFO)
    ebf_smd4805_dev = ebf_smd4805()
    ebf_smd4805_dev.init(step=1.8, divstep=2)
    for i in range(2, 10):
        ebf_smd4805_dev.run(i, Duration=1000, dir=DIR_CLOCKWISE)
    print("test_ebf_smd4805  Function exit,!!!")
    pass


if __name__ == "__main__":
    # creat a thread Check key status
    test_ebf_smd4805()
