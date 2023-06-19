# misc- Miscellaneous Features

Module feature: shutdown, software restart, PWM and ADC.

## Diversity Antenna Configuration Interface

### `misc.antennaSecRXOffCtrl`

```python
misc.antennaSecRXOffCtrl(*args)
```

Configures and queries the diversity antennas. (EC200A series module supports this interface).

**Parameter:**

It is a variable parameter: 
When the number of parameter is 0, query through: misc.antennaSecRXOffCtrl();
When the number of parameter is 1, set through: misc.antennaSecRXOffCtrl(SecRXOff_set).

- `SecRXOff_set` - Integer type. Range: 0/1. `0`: Do not close diversity antennas `1`: Close diversity antennas.

**Return Value:**

Query: If successful, it returns the diversity antenna configuration. If failed, it returns integer `-1`;

Set: If successful, it returns integer `0`; If failed, it returns integer `-1`.

**Example:**

```python
import misc

misc.antennaSecRXOffCtrl()
0
misc.antennaSecRXOffCtrl(1)
0
misc.antennaSecRXOffCtrl()
1
```

## Classes

- [class PowerKey – PowerKey Callback Registration](./misc.PowerKey.md)
- [class PWM – Pulse Width Modulation](./misc.PWM.md)
- [class ADC - Analog-to-digital Conversion](./misc.ADC.md)
- [class USB– USB Plug-in Detection](./misc.USB.md)

## Submodules

- [module Power – Shutdown and Software Restart](./misc.Power.md)

- [module USBNET – USBnet](./misc.USBNET.md)