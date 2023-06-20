# quecgnss - Internal GNSS Resolver

This feature provides the APIs of the built-in GNSS feature.

> Only EC200UCNAA/EC200UCNLA/EC200UEUAA/EC800MCNGA/EC800GCNGA series module supports this feature.

**Example**

```python
import quecgnss


def main():
    ret = quecgnss.init()
    if ret == 0:
        print('GNSS init ok.')
    else:
        print('GNSS init failed.')
        return -1
    data = quecgnss.read(4096)
    print(data[1].decode())

    quecgnss.gnssEnable(0)


if __name__ == '__main__':
    main()


#===================================================================================================
#Execution Result
167,169,170,,,,,,,,1.773,1.013,1.455*15
$GPGSV,2,1,8,3,23,303,34,16,32,219,28,22,74,98,26,25,16,43,25*77
$GPGSV,2,2,8,26,70,236,28,31,59,12,38,32,55,127,34,4,5,,21*49
$BDGSV,2,1,8,163,51,192,32,166,70,11,31,167,52,197,32,169,59,334,31*61
$BDGSV,2,2,8,170,40,205,31,161,5,,31,164,5,,27,165,5,,29*59
$GNRMC,022326.000,A,3149.324624,N,11706.921702,E,0.000,261.541,180222,,E,A*38
$GNGGA,022326.000,3149.324624,N,11706.921702,E,1,12,1.013,-8.580,M,0,M,,*47
$GNGLL,3149.324624,N,11706.921702,E,022326.000,A,A*44
$GNGSA,A,3,31,32,3,16,22,25,26,,,,,,1.773,1.013,1.455*1C
$GNGSA,A,3,163,166,167,169,170,,,,,,,,1.773,1.013,1.455*15
$GPGSV,2,1,8,3,23,303,34,16,32,219,27,22,74,98,26,25,16,43,25*78
$GPGSV,2,2,8,26,70,236,28,31,59,12,37,32,55,127,34,4,5,,20*47
$BDGSV,2,1,8,163,51,192,32,166,70,11,31,167,52,197,32,169,59,334,31*61
$BDGSV,2,2,8,170,40,205,31,161,5,,31,164,5,,27,165,5,,29*59
$GNRMC,022327.000,A,3149.324611,N,11706.921713,E,0.000,261.541,180222,,E,A*3F
$GNGGA,022327.000,3149.324611,N,11706.921713,E,1,12,1.013,-8.577,M,0,M,,*48
$GNGLL,3149.324611,N,11706.921713,E,022327.000,A,A*43
...... # Omit some data due to large data quantity.
$GNGSA,A,3,31,32,3,16,22,25,26,,,,,,1.837,1.120,1.456*11
$GNGSA,A,3,163,166,167,169,170,,,,,,,,1.837,1.120,1.456*18
$GPGSV,2,1,8,3,23,302,27,16,32,220,26,22,73,101,27,25,16,43,27*45
$GPGSV,2,2,8,26,70,237,28,31,59,13,33,32,54,128,28,4,5,,24*44
$BDGSV,2,1,8,163,51,192,33,166,71,11,35,167,52,198,33,169,59,334,34*6E
$BDGSV,2,2,8,170,40,205,32,161,5,,33,164,5,,28,165,5,,30*5F
$GNRMC,022507.000,A,3149.324768,N,11706.922344,E,0.000,261.541,180222,,E,A*31
$GNGGA,022507.000,3149.324768,N,11706.922344,E,1,12,1.120,-8.794,M,0,M,,*48
$GNGLL,3149.324768,N,11706.922344,E,022507.000,A,A*4D
$GNGSA,A,3,31,32,3,16,22,25,26,,,,,,1.837,1.120,1.455*12
$GNGSA,A,3,163,166,167,169,170,,,,,,,,1.837,1.120,1.455*1B
$GPGSV,2,1,8,3,23,302,26,16,32,220,26,22,73,101,27,25,16,43,26*45
$GPGSV,2,2,8,26,70,237,28,31,59,13,32,32,54,128,28,4,5,,24*45
$BDGSV,2,1,8,163,51,192,24,166,71,11,35,167,52,198,33,169,59,334,34*68
$BDGSV,2,2,8,170,40,205,31,161,5,,33,164,5,,28,165,5,,30*5C
$GNRMC,022508.000,A,3149.324754,N,11706.922338,E,0.002,261.541,180222,,E,A*38
$GNGGA,022508.000,3149.324754,N,11706.922338,E,1,12,1.120,-8.750,M,0,M,,*4B
$GNGLL,3149.324754,N,11706.922338,E,022508.000,A,A*46
$GNGSA,A,3,31,3
```


## Initialize GNSS 

### **`quecgnss.init`**

```python
quecgnss.init()
```

Initializes the built-in GNSS feature.

**Return Value**
`0` - Successful execution

`-1` - Failed execution

## Get GNSS Working Status

### **`quecgnss.get_state`**

```python
quecgnss.get_state()
```

Gets the current working status of the built-in GNSS feature.

**Return Value**

| Value | Type | Description                                                  |
| ----- | ---- | ------------------------------------------------------------ |
| 0     | int  | GNSS feature is disabled.                                    |
| 1     | int  | GNSS firmware is being updated.                              |
| 2     | int  | GNSS is positioning. In this mode, the module can read the GNSS location data. After obtaining the location data, the user needs to analyze the corresponding sentence to determine whether the location data is effective. For example, if the status of GNRMC sentences is A or V, A indicates valid positioning and V indicates invalid positioning. |

## Enable or Disable GNSS

### `quecgnss.gnssEnable`

```python
quecgnss.gnssEnable(opt)
```

Enables or disables GNSS feature. If you use the built-in GNSS feature for the first time after powering the module on, you need not call this function to enable GNSS feature, but call *quecgnss.init()* directly. *quecgnss.init()* will automatically enable the GNSS feature when GNSS feature is initialized.

**Parameter**

`opt` - Integer type. Enable or disable GNSS.

 `0` - Disable the GNSS feature.

 `1` - Enable the GNSS feature.

**Return Value**

 `0` - Successful execution

 `-1` - Failed execution

## Get GNSS Location Data

### `quecgnss.read`

```python
quecgnss.read(size)
```

Gets GNSS location data.

**Parameter**

`size` - Integer type. Size of the data to be read. Unit: byte.

**Return Value**

A tuple `(size, data)`  - Successful execution

`size` - Size of the data read.
`data` - GNSS location data.

-1 - Failed execution