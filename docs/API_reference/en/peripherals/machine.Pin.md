# Pin - Control I/O Pins

This class provides methods of reading and writing GPIO. A pin object is used to control I/O pins (also known as GPIO - general-purpose input/output). The pin class has methods to set the mode of the pin (IN, OUT, etc) and methods to get and set the digital logic level.

**Example:**

```python
from machine import Pin

# Creates a GPIO object
gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 1)

# Gets the pin level
gpio1.read()

# Sets the pin level
gpio1.write(0)
gpio1.write(1)

# Sets input and output modes
gpio1.set_dir(Pin.IN)
gpio1.set_dir(Pin.OUT)

# Gets input and output modes
gpio1.get_dir()
```

## Constructor

### `machine.Pin`

```python
class machine.Pin(GPIOn, direction, pullMode, level)
```

**Parameter:**

- `GPIOn` - Integer type. GPIO number. <a href="#label_pinmap">Click here to view</a> the mapping relationship between GPIO pin numbers and physical pins.  
- `direction` - Integer type. I/O mode. `IN` - Input mode. `OUT` - Output mode. 
- `pullMode` - Integer type. Pull selection mode. Descriptions are as follows:<br />`PULL_DISABLE` - Floating mode<br />`PULL_PU` - Pull-up mode<br />`PULL_PD` - Pull-down mode

- `level` - Integer type. Pin level. `0` - Set pin to low level.  `1`- Set pin to high level. 

**Example:**

```python
>>> # Creates a GPIO object
>>> from machine import Pin
>>> gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
```

<span id="label_pinmap">**Mapping Relationship Between GPIO Pin Numbers and Physical Pins:**</span>

> Description of GPIO corresponding pin numbers: GPIO pin numbers provided in the document correspond to external pin numbers of the module. For example, for EC100Y-CN module, GPIO1 corresponds to pin22, which is an external pin number of the module. See the provided hardware documents for external pin numbers of the module.

<details>
  <summary>Pin Correspondences of EC100Y Series Module<br /></summary>
GPIO1 – Pin22<br />GPIO2 – Pin23<br />GPIO3 – Pin38<br />GPIO4 – Pin53<br />GPIO5 – Pin54<br />GPIO6 – Pin104<br />GPIO7 – Pin105<br />GPIO8 – Pin106<br />GPIO9 – Pin107<br />GPIO10 – Pin178<br />GPIO11 – Pin195<br />GPIO12 – Pin196<br />GPIO13 – Pin197<br />GPIO14 – Pin198<br />GPIO15 – Pin199<br />GPIO16 – Pin203<br />GPIO17 – Pin204<br />GPIO18 – Pin214<br />GPIO19 – Pin215<br />
</details>

<details>
  <summary>Pin Correspondences of EC600S/EC600N Series Module</summary>
GPIO1 – Pin10<br />GPIO2 – Pin11<br />GPIO3 – Pin12<br />GPIO4 – Pin13<br />GPIO5 – Pin14<br />GPIO6 – Pin15<br />GPIO7 – Pin16<br />GPIO8 – Pin39<br />GPIO9 – Pin40<br />GPIO10 – Pin48<br />GPIO11 – Pin58<br />GPIO12 – Pin59<br />GPIO13 – Pin60<br />GPIO14 – Pin61<br />GPIO15 – Pin62<br/>GPIO16 – Pin63<br/>GPIO17 – Pin69<br/>GPIO18 – Pin70<br/>GPIO19 – Pin1<br/>GPIO20 – Pin3<br/>GPIO21 – Pin49<br/>GPIO22 – Pin50<br/>GPIO23 – Pin51<br/>GPIO24 – Pin52<br/>GPIO25 – Pin53<br/>GPIO26 – Pin54<br/>GPIO27 – Pin55<br/>GPIO28 – Pin56<br/>GPIO29 – Pin57<br />GPIO30 – Pin2<br />GPIO31 – Pin66<br />GPIO32 – Pin65<br />GPIO33 – Pin67<br />GPIO34 – Pin64<br />GPIO35 – Pin4<br />GPIO36 – Pin31<br />GPIO37 – Pin32<br />GPIO38 – Pin33<br />GPIO39 – Pin34<br />GPIO40 – Pin71<br />GPIO41 – Pin72<br />
</details>

<details>
  <summary>Pin Correspondences of EC600M Series Module</summary>
GPIO1 – Pin10<br />GPIO2 – Pin11<br />GPIO3 – Pin12<br />GPIO4 – Pin13<br />GPIO5 – Pin14<br />GPIO6 – Pin15<br />GPIO7 – Pin16<br />GPIO8 – Pin39<br />GPIO9 – Pin40<br />GPIO10 – Pin48<br />GPIO11 – Pin58<br />GPIO12 – Pin59<br />GPIO13 – Pin60<br />GPIO14 – Pin61<br />GPIO15 – Pin62<br/>GPIO16 – Pin63<br/>GPIO17 – Pin69<br/>GPIO18 – Pin70<br/>GPIO19 – Pin1<br/>GPIO20 – Pin3<br/>GPIO21 – Pin49<br/>GPIO22 – Pin50<br/>GPIO23 – Pin51<br/>GPIO24 – Pin52<br/>GPIO25 – Pin53<br/>GPIO26 – Pin54<br/>GPIO27 – Pin55<br/>GPIO28 – Pin56<br/>GPIO29 – Pin57<br />GPIO30 – Pin2<br />GPIO31 – Pin66<br />GPIO32 – Pin65<br />GPIO33 – Pin67<br />GPIO34 – Pin64<br />GPIO35 – Pin4<br />GPIO36 – Pin31<br />GPIO37 – Pin32<br />GPIO38 – Pin33<br />GPIO39 – Pin34<br />GPIO40 – Pin71<br />GPIO41 – Pin72<br />GPIO42 – Pin109<br />GPIO43 – Pin110<br />GPIO44 – Pin112<br />GPIO45 – Pin111<br/>
</details>

<details>
  <summary>Pin Correspondences of EC600U Series Module</summary>
GPIO1 – Pin61 (It cannot be used together with GPIO31.)<br />GPIO2 – Pin58 (It cannot be used together with GPIO32.)<br />GPIO3 – Pin34 (It cannot be used together with GPIO41.)<br />GPIO4 – Pin60 (It cannot be used together with GPIO34.)<br />GPIO5 – Pin69 (It cannot be used together with GPIO35.)<br />GPIO6 – Pin70 (It cannot be used together with GPIO36.)<br />GPIO7 – Pin123 (It cannot be used together with GPIO43.)<br />GPIO8 – Pin118<br />GPIO9 – Pin9 (It cannot be used together with GPIO47.)<br />GPIO10 – Pin1 (It cannot be used together with GPIO37.)<br />GPIO11 – Pin4 (It cannot be used together with GPIO38.)<br />GPIO12 – Pin3 (It cannot be used together with GPIO39.)<br />GPIO13 – Pin2 (It cannot be used together with GPIO40.)<br />GPIO14 – Pin54<br />GPIO15 – Pin57<br/>GPIO16 – Pin56<br/>GPIO17 – Pin12<br/>GPIO18 – Pin33 (It cannot be used together with GPIO42.)<br/>GPIO19 – Pin124 (It cannot be used together with GPIO44.)<br/>GPIO20 – Pin122 (It cannot be used together with GPIO45.)<br/>GPIO21 – Pin121 (It cannot be used together with GPIO46.)<br/>GPIO22 – Pin48<br/>GPIO23 – Pin39<br/>GPIO24 – Pin40<br/>GPIO25 – Pin49<br/>GPIO26 – Pin50<br/>GPIO27 – Pin53<br/>GPIO28 – Pin52<br/>GPIO29 – Pin51<br/>GPIO30 – Pin59 (It cannot be used together with GPIO33.)<br/>GPIO31 – Pin66 (It cannot be used together with GPIO1.)<br/>GPIO32 – Pin63 (It cannot be used together with GPIO2.)<br/>GPIO33 – Pin67 (It cannot be used together with GPIO30.)<br/>GPIO34 – Pin65 (It cannot be used together with GPIO4.)<br/>GPIO35 – Pin137 (It cannot be used together with GPIO5.)<br/>GPIO36 – Pin62 (It cannot be used together with GPIO6.)<br/>GPIO37 – Pin98 (It cannot be used together with GPIO10.)<br/>GPIO38 – Pin95 (It cannot be used together with GPIO11.)<br/>GPIO39 – Pin119 (It cannot be used together with GPIO12.)<br/>GPIO40 – Pin100 (It cannot be used together with GPIO13.)<br/>GPIO41 – Pin120 (It cannot be used together with GPIO3.)<br/>GPIO42 – Pin16 (It cannot be used together with GPIO18.)<br/>GPIO43 – Pin10 (It cannot be used together with GPIO7.)<br/>GPIO44 – Pin14 (It cannot be used together with GPIO19.)<br/>GPIO45 – Pin15 (It cannot be used together with GPIO20.)<br/>GPIO46 – Pin13 (It cannot be used together with GPIO21.)<br/>GPIO47 – Pin99 (It cannot be used together with GPIO9.)<br/>
</details>
<details>
  <summary>Pin Correspondences of EC200U Series Module</summary>
GPIO1 – Pin27 (It cannot be used together with GPIO31.)<br />GPIO2 – Pin26 (It cannot be used together with GPIO32.)<br />GPIO3 – Pin24 (It cannot be used together with GPIO33.)<br />GPIO4 – Pin25 (It cannot be used together with GPIO34.)<br />GPIO5 – Pin13 (It cannot be used together with GPIO17.)<br />GPIO6 – Pin135 (It cannot be used together with GPIO36.)<br />GPIO7 – Pin136 (It cannot be used together with GPIO44.)<br />GPIO8 – Pin133<br />GPIO9 – Pin3 (It cannot be used together with GPIO37.)<br />GPIO10 – Pin40 (It cannot be used together with GPIO38.)<br />GPIO11 – Pin37 (It cannot be used together with GPIO39.)<br />GPIO12 – Pin38 (It cannot be used together with GPIO40.)<br />GPIO13 – Pin39 (It cannot be used together with GPIO41.)<br />GPIO14 – Pin5<br />GPIO15 – Pin141<br/>GPIO16 – Pin142<br/>GPIO17 – Pin121 (It cannot be used together with GPIO5.)<br/>GPIO18 – Pin65 (It cannot be used together with GPIO42.)<br/>GPIO19 – Pin64 (It cannot be used together with GPIO43.)<br/>GPIO20 – Pin139 (It cannot be used together with GPIO45.)<br/>GPIO21 – Pin126 (It cannot be used together with GPIO46.)<br/>GPIO22 – Pin127 (It cannot be used together with GPIO47.)<br/>GPIO23 – Pin33<br/>GPIO24– Pin31<br/>GPIO25 – Pin30<br/>GPIO26 – Pin29<br/>GPIO27 – Pin28<br/>GPIO28 – Pin1<br/>GPIO29 – Pin2<br/>GPIO30 – Pin4<br/>GPIO31 – Pin125 (It cannot be used together with GPIO1.)<br/>GPIO32 – Pin124 (It cannot be used together with GPIO2.)<br/>GPIO33 – Pin123 (It cannot be used together with GPIO3.)<br/>GPIO34 – Pin122 (It cannot be used together with GPIO4.)<br/>GPIO35 – Pin42<br/>GPIO36 – Pin119 (It cannot be used together with GPIO6.)<br/>GPIO37 – Pin134 (It cannot be used together with GPIO9.)<br/>GPIO38– Pin132 (It cannot be used together with GPIO10.)<br/>GPIO39 – Pin131 (It cannot be used together with GPIO11.)<br/>GPIO40 – Pin130 (It cannot be used together with GPIO12.)<br/>GPIO41 – Pin129 (It cannot be used together with GPIO13.)<br/>GPIO42 – Pin61 (It cannot be used together with GPIO18.)<br/>GPIO43 – Pin62 (It cannot be used together with GPIO19.)<br/>GPIO44 – Pin63 (It cannot be used together with GPIO7.)<br/>GPIO45 – Pin66 (It cannot be used together with GPIO20.)<br/>GPIO46 – Pin6 (It cannot be used together with GPIO21.)<br/>GPIO47 – Pin23 (It cannot be used together with GPIO22.)<br/>
</details>

<details>
  <summary>Pin Correspondences of EC200A Series Module</summary>
GPIO1 – Pin27<br />GPIO2 – Pin26<br />GPIO3 – Pin24<br />GPIO4 – Pin25<br />GPIO5 – Pin5<br />GPIO6 – Pin135<br />GPIO7 – Pin136<br />GPIO9 – Pin3<br />GPIO10 – Pin40<br />GPIO11 – Pin37<br />GPIO12 – Pin38<br />GPIO13 – Pin39<br />GPIO18 – Pin65<br />GPIO19 – Pin64<br />GPIO20 – Pin139<br />GPIO22 – Pin127<br />GPIO28 – Pin1<br />GPIO29 – Pin2<br />GPIO30 – Pin4<br />GPIO35 – Pin42<br />GPIO36 – Pin119<br />GPIO43 – Pin62<br />GPIO44 – Pin63<br />GPIO45 – Pin66<br />GPIO46 – Pin6<br />GPIO47 – Pin23<br/>
</details>

<details>
  <summary>Pin Correspondences of EC800N Module</summary>
GPIO1 – Pin30<br />GPIO2 – Pin31<br />GPIO3 – Pin32<br />GPIO4 – Pin33<br />GPIO5 – Pin49<br />GPIO6 – Pin50<br />GPIO7 – Pin51<br />GPIO8 – Pin52<br />GPIO9 – Pin53<br />GPIO10 – Pin54<br />GPIO11 – Pin55<br />GPIO12 – Pin56<br />GPIO13 – Pin57<br />GPIO14 – Pin58<br />GPIO15 – Pin80<br/>GPIO16 – Pin81<br/>GPIO17 – Pin76<br/>GPIO18 – Pin77<br/>GPIO19 – Pin82<br/>GPIO20 – Pin83<br/>GPIO21 – Pin86<br/>GPIO22 – Pin87<br/>GPIO23 – Pin66<br/>GPIO24 – Pin67<br/>GPIO25 – Pin17<br/>GPIO26 – Pin18<br/>GPIO27 – Pin19<br/>GPIO28 – Pin20<br/>GPIO29 – Pin21<br />GPIO30 – Pin22<br />GPIO31 – Pin23<br />GPIO32 – Pin28<br />GPIO33 – Pin29<br />GPIO34 – Pin38<br />GPIO35 – Pin39<br />GPIO36 – Pin16<br />GPIO37 – Pin78<br />
</details>

<details>
  <summary>Pin Correspondences of BC25 Series Module    </summary>
GPIO1 – Pin3<br />GPIO2 – Pin4<br />GPIO3 – Pin5<br />GPIO4 – Pin6<br />GPIO5 – Pin16<br />GPIO6 – Pin20<br />GPIO7 – Pin21<br />GPIO8 – Pin22<br />GPIO9 – Pin23<br />GPIO10 – Pin25<br />GPIO11 – Pin28<br />GPIO12 – Pin29<br />GPIO13 – Pin30<br />GPIO14 – Pin31<br />GPIO15 – Pin32<br/>GPIO16 – Pin33<br/>GPIO17 – Pin2<br/>GPIO18 – Pin8<br/>
</details>


<details>
  <summary>Pin Correspondences of BG95-M3 Module</summary>
GPIO1 – Pin4<br />GPIO2 – Pin5<br />GPIO3 – Pin6<br />GPIO4 – Pin7<br />GPIO5 – Pin18<br />GPIO6 – Pin19<br />GPIO7 – Pin22<br />GPIO8 – Pin23<br />GPIO9 – Pin25<br />GPIO10 – Pin26<br />GPIO11 – Pin27<br />GPIO12 – Pin28<br />GPIO13 – Pin40<br />GPIO14 – Pin41<br />GPIO15 – Pin64<br/>GPIO16 – Pin65<br/>GPIO17 – Pin66<br />GPIO18 – Pin85<br />GPIO19 – Pin86<br />GPIO20 – Pin87<br />GPIO21 – Pin88<br />
</details>

<details>
  <summary>Pin Correspondences of EG915U Series Module</summary>
GPIO1 – Pin4 (It cannot be used together with GPIO41.)<br />GPIO2 – Pin5 (It cannot be used together with GPIO36.)<br />GPIO3 – Pin6 (It cannot be used together with GPIO35.)<br />GPIO4 – Pin7 (It cannot be used together with GPIO24.)<br />GPIO5 – Pin18<br />GPIO6 – Pin19<br />GPIO7 – Pin1 (It cannot be used together with GPIO37.)<br />GPIO8 – Pin38<br />GPIO9 – Pin25<br />GPIO10 – Pin26<br />GPIO11 – Pin27 (It cannot be used together with GPIO32.)<br />GPIO12 – Pin28 (It cannot be used together with GPIO31.)<br />GPIO13 – Pin40<br />GPIO14 – Pin41<br />GPIO15 – Pin64<br/>GPIO16 – Pin20 (It cannot be used together with GPIO30.)<br/>GPIO17 – Pin21<br/>GPIO18 – Pin85<br/>GPIO19 – Pin86<br/>GPIO20 – Pin30<br/>GPIO21 – Pin88<br/>GPIO22 – Pin36 (It cannot be used together with GPIO40.)<br/>GPIO23 – Pin37 (It cannot be used together with GPIO38.)<br/>GPIO24 – Pin16 (It cannot be used together with GPIO4.)<br/>GPIO25 – Pin39<br/>GPIO26 – Pin42 (It cannot be used together with GPIO27.)<br/>GPIO27 – Pin78 (It cannot be used together with GPIO26.)<br/>GPIO28 – Pin83 (It cannot be used together with GPIO33.)<br/>GPIO29 – Pin84<br />GPIO30 – Pin92 (It cannot be used together with GPIO16.)<br />GPIO31 – Pin95 (It cannot be used together with GPIO12.)<br />GPIO32 – Pin97 (It cannot be used together with GPIO11.)<br />GPIO33 – Pin98 (It cannot be used together with GPIO28.)<br />GPIO34 – Pin104<br />GPIO35 – Pin105 (It cannot be used together with GPIO3.)<br />GPIO36 – Pin106 (It cannot be used together with GPIO2.)<br />GPIO37 – Pin108 (It cannot be used together with GPIO4.)<br />GPIO38 – Pin111 (It cannot be used together with GPIO23.)<br />GPIO39 – Pin114<br />GPIO40 – Pin115 (It cannot be used together with GPIO22.)<br />GPIO41 – Pin116 (It cannot be used together with GPIO1.)<br />
</details>

<details>
  <summary>Pin Correspondences of EC800M Module</summary>
GPIO1 – Pin30<br />GPIO2 – Pin31<br />GPIO3 – Pin32<br />GPIO4 – Pin33<br />GPIO5 – Pin49<br />GPIO6 – Pin50<br />GPIO7 – Pin51<br />GPIO8 – Pin52<br />GPIO9 – Pin53<br />GPIO10 – Pin54<br />GPIO11 – Pin55<br />GPIO12 – Pin56<br />GPIO13 – Pin57<br />GPIO14 – Pin58<br />GPIO15 – Pin80<br/>GPIO16 – Pin81<br/>GPIO17 – Pin76<br/>GPIO18 – Pin77<br/>GPIO19 – Pin82<br/>GPIO20 – Pin83<br/>GPIO21 – Pin86<br/>GPIO22 – Pin87<br/>GPIO23 – Pin66<br/>GPIO24 – Pin67<br/>GPIO25 – Pin17<br/>GPIO26 – Pin18<br/>GPIO27 – Pin19<br/>GPIO28 – Pin20<br/>GPIO29 – Pin21<br />GPIO30 – Pin22<br />GPIO31 – Pin23<br />GPIO32 – Pin28<br />GPIO33 – Pin29<br />GPIO34 – Pin38<br />GPIO35 – Pin39<br />GPIO36 – Pin16<br />GPIO37 – Pin78<br />GPIO38 – Pin68<br />GPIO39 – Pin69<br />GPIO40 – Pin74<br />GPIO41 – Pin75<br />GPIO42 – Pin84<br />GPIO43 – Pin85<br />GPIO44 – Pin25<br />
</details>

<details>
  <summary>Pin Correspondences of EG912N Module</summary>
GPIO1 – Pin4<br />GPIO2 – Pin5<br />GPIO3 – Pin6<br />GPIO4 – Pin7<br />GPIO5 – Pin18<br />GPIO6 – Pin19<br />GPIO7 – Pin1<br />GPIO8 – Pin16<br />GPIO9 – Pin25<br />GPIO10 – Pin26<br />GPIO11 – Pin27<br />GPIO12 – Pin28<br />GPIO13 – Pin40<br/>GPIO14 – Pin41<br/>GPIO15 – Pin64<br/>GPIO16 – Pin20<br/>GPIO17 – Pin21<br/>GPIO18 – Pin30<br/>GPIO19 – Pin34<br/>GPIO20 – Pin35<br/>GPIO21 – Pin36<br/>GPIO22 – Pin37<br/>GPIO23 – Pin38<br/>GPIO24 – Pin39<br/>GPIO25 – Pin42<br />GPIO26 – Pin78<br />GPIO27 – Pin83<br />GPIO28 – Pin92<br />GPIO29 – Pin95<br />GPIO30 – Pin96<br />GPIO31 – Pin97<br />GPIO32 – Pin98<br />GPIO33 – Pin103<br />GPIO34 – Pin104<br />GPIO35 – Pin105<br />GPIO36 – Pin106<br />GPIO37 – Pin107<br />GPIO38 – Pin114<br />GPIO39 – Pin115<br />GPIO40 – Pin116
</details>



## Methods

### `Pin.read`

```python
Pin.read()
```

This method reads the pin level.

**Return Value:**

Pin level.  `0`  - low level.  `1`  - high level.

### `Pin.write`

```
Pin.write(value)
```

This method sets the pin level.

> Note: You need to ensure that the pin is in the output mode before you set the pin level.

**Parameter:**

- `value` - Integer type. Pin level. `0` - low level. `1` - high level. 

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

**Example:**

```python
>>> from machine import Pin
>>> gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
>>> gpio1.write(1)
0
>>> gpio1.read()
1
```

### `Pin.set_dir`

```python
Pin.set_dir(value)
```

This method sets I/O mode of the pin. 

**Parameter:**

- `value` - Integer type. Pin level. `0` - low level. `1` - high level.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `Pin.get_dir`

```python
Pin.get_dir()
```

This method gets I/O mode of the pin.   

**Return Value:**

I/O mode of pins. 

`0` - Input mode.

`1` - Output mode.

**Example:**

```python
>>> from machine import Pin
>>> gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
>>> gpio1.get_dir()
1
>>> gpio1.set_dir(Pin.IN)
0
>>> gpio1.get_dir()
0
```

## Constants

| Constant         | Module                                                       | Description    |
| ---------------- | ------------------------------------------------------------ | -------------- |
| Pin.GPIO1        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO1          |
| Pin.GPIO2        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO2          |
| Pin.GPIO3        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO3          |
| Pin.GPIO4        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO4          |
| Pin.GPIO5        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO5          |
| Pin.GPIO6        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO6          |
| Pin.GPIO7        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO7          |
| Pin.GPIO8        | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO8          |
| Pin.GPIO9        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO9          |
| Pin.GPIO10       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO10         |
| Pin.GPIO11       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO11         |
| Pin.GPIO12       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO12         |
| Pin.GPIO13       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO13         |
| Pin.GPIO14       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO14         |
| Pin.GPIO15       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO15         |
| Pin.GPIO16       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO16         |
| Pin.GPIO17       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC800N/BC25/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO17         |
| Pin.GPIO18       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/EC800N/BC25/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO18         |
| Pin.GPIO19       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO19         |
| Pin.GPIO20       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO20         |
| Pin.GPIO21       | EC600S / EC600N/EC600U/EC200U/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO21         |
| Pin.GPIO22       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO22         |
| Pin.GPIO23       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO23         |
| Pin.GPIO24       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO24         |
| Pin.GPIO25       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO25         |
| Pin.GPIO26       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO26         |
| Pin.GPIO27       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO27         |
| Pin.GPIO28       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO28         |
| Pin.GPIO29       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO29         |
| Pin.GPIO30       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO30         |
| Pin.GPIO31       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO31         |
| Pin.GPIO32       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO32         |
| Pin.GPIO33       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO33         |
| Pin.GPIO34       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO34         |
| Pin.GPIO35       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO35         |
| Pin.GPIO36       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO36         |
| Pin.GPIO37       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO37         |
| Pin.GPIO38       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG912N    | GPIO38         |
| Pin.GPIO39       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG912N    | GPIO39         |
| Pin.GPIO40       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG912N    | GPIO40         |
| Pin.GPIO41       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M           | GPIO41         |
| Pin.GPIO42       | EC600U/EC200U/EC600M/EC800M                                  | GPIO42         |
| Pin.GPIO43       | EC600U/EC200U/EC200A/EC600M/EC800M                           | GPIO43         |
| Pin.GPIO44       | EC600U/EC200U/EC200A/EC600M/EC800M                           | GPIO44         |
| Pin.GPIO45       | EC600U/EC200U/EC200A/EC600M                                  | GPIO45         |
| Pin.GPIO46       | EC600U/EC200U/EC200A                                         | GPIO46         |
| Pin.GPIO47       | EC600U/EC200U/EC200A                                         | GPIO47         |
| Pin.IN           | --                                                           | Input mode     |
| Pin.OUT          | --                                                           | Output mode    |
| Pin.PULL_DISABLE | --                                                           | Floating mode  |
| Pin.PULL_PU      | --                                                           | Pull-up mode   |
| Pin.PULL_PD      | --                                                           | Pull-down mode |
