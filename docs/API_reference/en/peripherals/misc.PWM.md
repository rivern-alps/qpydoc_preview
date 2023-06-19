# PWM - Pulse Width Modulation

This class provides the feature of PWM output. 

> Note: BC25 series module does not support this feature.

## Constructor

### `misc.PWM`

```python
class misc.PWM(PWM.PWMn,PWM.ABOVE_xx, highTime, cycleTime)
```

**Parameter:**

- `PWM.PWMn` - Integer type. PWM channel. <a href="#label_pwmmap">Click here to learn more</a> for supported channels and corresponding pins.

- `PWM.ABOVE_xx` - Integer type. Time range. 

  For EC200U, EC600U and EG915U series modules:<br />PWM.ABOVE_MS				          ms-level time range: (0,10]<br/>PWM.ABOVE_1US				        us-level time range: (0,10000]<br/>PWM.ABOVE_10US				      us-level time range: (1,10000]<br/>PWM.ABOVE_BELOW_US			ns-level time range: [100,65535]

- `highTime` - Integer type. High level time. 

  For ms-level time, unit: ms.<br/>For us-level time, unit: us.<br/>For ns-level: it needs to be calculated by users.<br/>               Frequency = 13Mhz / cycleTime<br/>               Duty cycle = highTime/ cycleTime

- `cycleTime` - Integer type. Cycle time.

  For ms-level time, unit: ms.<br/>For us-level time, unit: us.<br/>For ns-level: it needs to be calculated by users. <br/>              Frequency = 13Mhz / cycleTime<br/>              Duty cycle = highTime/ cycleTime

**Example:**

```python
 from misc import PWM
 pwm1 = PWM(PWM.PWM1, PWM.ABOVE_MS, 1, 2)
```

<span id="label_pwmmap">**Mapping Relationship Between PWM Channels and Pysical Pins:**</span>

The corresponding pins of EC100Y series module for PWM0-PWM3 are as follows:<br/>PWM0 – pin19<br/>PWM1 – pin18<br/>PWM2 – pin23<br/>PWM3 – pin22<br/>The corresponding pins of EC600S-CN and EC600N modules for PWM0-PWM3 are as follows:<br/>PWM0 – pin52<br/>PWM1 – pin53<br/>PWM2 – pin70<br/>PWM3 – pin69<br />The corresponding pins of EC800N module for PWM0-PWM3 are as follows:<br/>PWM0 – pin79<br/>PWM1 – pin78<br/>PWM2 – pin16<br/>PWM3 – pin49<br />The corresponding pin of EC200U series module for PWM0 is as follows:<br />PWM0 – pin135<br />The corresponding pin of EC600U series module for PWM0 is as follows:<br />PWM0 – pin70<br />The corresponding pins of EC600M module for PWM0-PWM3 are as follows:<br/>PWM0 – pin57<br/>PWM1 – pin56<br/>PWM2 – pin70<br/>PWM3 – pin69<br/>The corresponding pin of EG915U series module for PWM0 is as follows:<br/>PWM0 – pin20<br/>The corresponding pins of EC800M module for PWM0-PWM3 are as follows:<br/>PWM0 – pin83<br/>PWM1 – pin78<br/>PWM2 – pin16<br/>PWM3 – pin49<br/>The corresponding pins of EG912N module for PWM0-PWM3 are as follows:<br/>PWM0 – pin21<br/>PWM1 – pin116<br/>PWM2 – pin107<br/>PWM3 – pin92

## Methods

### `PWM.open`

```python
PWM.open()
```

This methods enables PWM output.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `PWM.close`

```
PWM.close()
```

This methods disables PWM output.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

**Example:**

```python
from misc import PWM
import utime
if __name__ == '__main__':
    pwm = PWM(PWM.PWM0, PWM.ABOVE_MS, 1, 2)  # Initializes a PWM object
    pwm.open()  # Enables PWM output
    utime.sleep(10)
    pwm.close()  # Disables PWM output
```

## Constants

| Constant | Description | Module                                                       |
| -------- | ----------- | ------------------------------------------------------------ |
| PWM.PWM0 | PWM0        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N |
| PWM.PWM1 | PWM1        | EC600S / EC600N / EC100Y/EC800N/EC600M/EC800M/EG912N         |
| PWM.PWM2 | PWM2        | EC600S / EC600N / EC100Y/EC800N/EC600M/EC800M/EG912N         |
| PWM.PWM3 | PWM3        | EC600S / EC600N / EC100Y/EC800N/EC600M/EC800M/EG912N         |