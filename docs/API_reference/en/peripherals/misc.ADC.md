# ADC - Voltage Collection

This class collects voltage signals.

## Constructor

### `misc.ADC`

```python
class misc.ADC()
```

**Example:**

```python
from misc import ADC
adc = ADC()
```

## Methods

### `ADC.open`

```python
ADC.open()
```

This method initializes ADC.

**Return Value:**

 `0` - Successful execution

 `-1` - Failed execution

### `ADC.read`

```python
ADC.read(ADCn)
```

This method reads voltage values of a specified channel. Unit: `mV`.

**Parameter:**

- `ADCn` - Integer type. ADC channel. <a href="#label_pinmap">Click here to learn more</a> for supported channels and corresponding pins.

**Return Value:**

If successful, a specified channel voltage value is returned.

 `-1` - Failed execution.

**Example:**

```python
>>>adc.read(ADC.ADC0)  # Reads voltage value of ADC0
613
>>>adc.read(ADC.ADC1)  # Reads voltage value of ADC1
605
```

<span id="label_pinmap">**Mapping Relationship Between ADC Passages and Pysical Pins:**</span>

The corresponding pins of EC100Y series module are as follows:<br/>ADC0 – pin39<br/>ADC1 – pin81<br/>The corresponding pin of EC600S/EC600N series module is as follows: <br/>ADC0 – pin19<br/>The corresponding pins of EC600M series module is as follows: <br/>ADC0 – pin19<br/>ADC1 – pin20<br/>The corresponding pin of EC800N series module is as follows:<br/>ADC0 – pin9<br/>The corresponding pins of EC600U series module is as follows:<br />ADC0 – pin19<br/>ADC1 – pin20<br />ADC2 – pin113<br />ADC3 – pin114<br />The corresponding pins of EC200U series module is as follows: <br />ADC0 – pin45<br/>ADC1 – pin44<br />ADC2 – pin43<br />The corresponding pins of EC200A series module is as follows: <br/>ADC0 – pin45<br/>ADC1 – pin44<br/>The corresponding pin of BG95 series module is as follows:<br/>ADC0 – pin24<br/>The corresponding pins of EG915U series module is as follows:<br/>ADC0 – pin24<br/>ADC1 – pin2<br/>The corresponding pins of EC800M series module is as follows:<br/>ADC0 – pin9<br/>ADC1 – pin96<br/>The corresponding pins of EG912N series module is as follows:<br/>ADC0 – pin24<br/>ADC1 – pin2

### ADC.close

```python
ADC.close()
```

**Return Value:**

 `0` - Successful execution

 `-1` - Failed execution

## Constants

| Constant | Description   | Module                                                       |
| -------- | ------------- | ------------------------------------------------------------ |
| ADC.ADC0 | ADC channel 0 | EC600S/EC600N/EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC200A/EC600M/EG915U/EC800M/EG912N |
| ADC.ADC1 | ADC channel 1 | EC600U/EC200U/EC200A/EC600M/EG915U/EC800M/EG912N             |
| ADC.ADC2 | ADC channel 2 | EC600U/EC200U                                                |
| ADC.ADC3 | ADC channel 3 | EC600U                                                       |