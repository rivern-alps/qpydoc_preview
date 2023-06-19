from misc import PWM
import utime as time
import urandom as random
import log


# Creating log object
buzzer_log = log.getLogger("buzzer_test")

# Duration: ms
def outputpwm(HZ, duty_cycle, Duration):
    cycleTime = int((10000000/HZ)/10)
    highTime = int(cycleTime * duty_cycle)
    buzzer_log.debug(
	    """out put pin70 cycleTime {0} * 10us,
	    highTime {1} * 10us, Duration of {2}"""
	    .format(cycleTime, highTime, Duration))
    pwm1 = PWM(PWM.PWM0, PWM.ABOVE_10US, highTime, cycleTime)       
    pwm1.open()
    time.sleep_ms(Duration)
    pwm1.close()
    pass


def test_Buzzer():
	# Set the log output level
	log.basicConfig(level=log.DEBUG)
	# Loop 10 times
	for i in range(10):
		# Random generation of floating point numbers in the start to end range, optionally， 0~1
		duty_cycle = random.uniform(0.1, 0.8)
		# Suggested that the output2000~5000HZ_PWM waveform
		# Generate a random start ~ end Integer between
		HZ = random.randint(2000, 5000)
		outputpwm(HZ, duty_cycle, 500)
		time.sleep_ms(1500)
	pass


if __name__ == "__main__":
	test_Buzzer()