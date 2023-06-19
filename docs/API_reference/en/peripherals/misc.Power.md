# power - Power Off and Reboot

Module features: power off, reboot software, get the power-on reason, get the last power-off reason and get battery voltage.

## Power Off

### `Power.powerDown`

```python
Power.powerDown()
```

This method powers off the module.

**Example:**

```python
from misc import Power

Power.powerDown()
```

## Reboot

### `Power.powerRestart`

```python
Power.powerRestart()
```

This method reboots the module.

## Get the Power-on Reason

### `Power.powerOnReason`

```python
Power.powerOnReason()
```

This method gets the power-on reason.

**Return Value:**

| Value | Description                                                  |
| ----- | ------------------------------------------------------------ |
| 0     | Failed to get the power-on reason or unknown power-on reason |
| 1     | Press PWRKEY to power on                                     |
| 2     | Press RESET to reboot                                        |
| 3     | Power-on triggered by VBAT                                   |
| 4     | Power-on triggered by RTC                                    |
| 5     | Reboot triggered by watchdog or power-on error               |
| 6     | Power-on triggered by VBUS                                   |
| 7     | Power-on triggered by charging                               |
| 8     | Wake up from PSM                                             |
| 9     | Reboot after dump occurs                                     |

## Get the Last Power-off Reason

### `Power.powerDownReason`

```
Power.powerDownReason()
```

This method gets the power-off reason.

**Return Value:**

| Value | Description                                |
| ----- | ------------------------------------------ |
| 0     | Unknown reason                             |
| 1     | Power off normally                         |
| 2     | Power off due to high power supply voltage |
| 3     | Power off due to low power supply voltage  |
| 4     | Power off due to high temperature          |
| 5     | Power-off triggered by watchdog            |
| 6     | Power-off triggered by low VRTC voltage    |

> Note: BC25PA, EC200U and EC600U series modules do not support this method.

## Get Battery Voltage

### `Power.getVbatt`

```python
Power.getVbatt()
```

This method gets the battery voltage. Unit: mV.

**Return Value:**

Integer type. Voltage value.

**Example:**

```python
>>> Power.getVbatt()
3590
```

