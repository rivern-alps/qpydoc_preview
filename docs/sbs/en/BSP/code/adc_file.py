from misc import ADC  # Import ADC module
import utime    # Import timing module
read_time = 5   # Set read count
adc = ADC()
while read_time:
    adc.open()
    read_data = adc.read(ADC.ADC0)
    print(read_data)
    adc.close()
    read_time -= 1
    utime.sleep(1)  # Postpone 1S
