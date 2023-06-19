# wifiScan - Wi-Fi Scan

`wifiScan` provides both synchronous and asynchronous modes to scan the Wi-Fi hotspot information around the module.



> The following modules support the `wifiScan` feature.
>
> EC100Y/EC200N/EC600N/EC600S/EC600M/EC800M/EC800N/EG912N/EG915N/EG810M/EC600G/EC800G/EC200U/EC600U/EG912U/EG915U series module.
>
> In EC600M series module, EC600MCN_LC/EC600MCN_LF module does not support the `wifiScan` feature.
>
> In EC800M series module, EC800MCN_GC/EC800MCN_LC/EC800MCN_LF does not support the `wifiScan` feature.
>
> In EC600U series module, EC600UEC_AC does not support the `wifiScan` feature.



## Enable/Disable Wi-Fi Scan

### `wifiScan.control`

```python
wifiScan.control(option)
```

Enables or disables Wi-Fi scan.

**Parameter**

* `option` - Integer type. Wi-Fi scan control option.

  `0` - Disable Wi-Fi scan

  `1` - Enable Wi-Fi scan

**Return Value**

`0` - Successful execution

`-1` - Failed execution

**Example**

```python
>>> import wifiScan
>>> wifiScan.control(1) # Enable Wi-Fi scan.
0
>>> wifiScan.control(0) # Disable Wi-Fi scan.
0
```



### `wifiScan.getState`

```python
wifiScan.getState()
```

Gets the current status of Wi-Fi scan.

**Return Value**

`True` - The Wi-Fi scan is enabled.

`False` - The Wi-Fi scan is disabled.



## Set and Get the Scan Parameters of Wi-Fi Scan

### `wifiScan.setCfgParam`

```python
wifiScan.setCfgParam(timeout, round, maxNums[, priority])
```

Sets the scan parameters of Wi-Fi scan.

**Parameter**

* `timeout` - Integer type. Timeout. When a timeout is triggered, the system automatically reports the detected hot spots. If the specified number of hot spots is detected before the timeout, the system stops scanning and returns the scanning result. Range: 4–60. Unit: s.

* `round` - Integer type. Number of scan rounds. When the number of scan rounds is reached, the scan ends and the scan result is returned. Range: 1–3. Unit: time.

* `maxNums` - Integer type. The maximum number of scanned hotspots. When the number of scanned hotspots reaches the upper limit, the scan ends and the scan result is returned. Range: 4–30.

* `priority` - Integer type. Priority of businesses. 

  `0` - Network business first. Wi-Fi scan will be interrupted when a data service is initiated.

  `1` - Wi-Fi scan first. When a data service is initiated, the RRC connection is not set up. To ensure that the Wi-Fi scan is performed properly, the RRC connection is set up only after the scan is complete. 

**Return Value**

`0` - Successful execution

`-1` - Failed execution



> EC200U/EC600U/EG912U/EG915U/EC600G/EC800G series module does not support `priority`, so `priority` can be omitted.



### `wifiScan.getCfgParam`

```python
wifiScan.getCfgParam()
```

Gets the scan parameters of Wi-Fi scan.

**Return Value**

A tuple `(timeout, round, maxNums, priority)` - Successful execution

` -1` - Failed execution 

See `(timeout, round, maxNums, priority)` in `wifiScan.setCfgParam` for details.



## Register Callback Function

### `wifiScan.setCallback`

```python
wifiScan.setCallback(fun)
```

Registers the callback function. When asynchronous scanning is used, you need to register the callback function, and the scan result is returned to the user through the callback function.

**Parameter**

* `fun` - Callback function name. The callback function format and parameters are described below.

```python
def wifiscanCallback(args):
	pass
```

| Parameter | Type  | Description                                                  |
| --------- | ----- | ------------------------------------------------------------ |
| args      | Tuple | `(nums,  [(mac, rssi),...,(mac, rssi)])`<br>`nums` - Integer type. The number of scanned Wi-Fi hotspots.<br>`mac` - String type. MAC address of the Wi-Fi hotspots.<br>`rssi` - Integer type. Signal strength of the Wi-Fi hotspots. |

**Return Value**

`0` - Successful execution

`-1` - Failed execution



## Start Scanning

### `wifiScan.asyncStart`

```python
wifiScan.asyncStart()
```

Starts scanning in Wi-Fi scan asynchronous mode.  The scan result is returned through the registered callback function.

**Return Value**

`0` - Successful execution

`-1` - Failed execution

**Example**

```python
import wifiScan

def wifiscanCallback(args):
	print('wifi list:{}'.format(args))
wifiScan.setCallback(wifiscanCallback)

wifiScan.control(1)
wifiScan.asyncStart()

'''
Execution result
wifi list:(2, [('F0:B4:29:86:95:C7', -79),('44:00:4D:D5:26:E0', -92)])
'''
```



### `wifiScan.start`

```python
wifiScan.start()
```

Starts scanning in Wi-Fi scan synchronous mode.  The scan result is returned after the scan is complete. Because the interface is synchronous, the program will be blocked in the interface when the scan does not end.

**Return Value**

A tuple `(wifiNums, [(mac, rssi), ... , (mac, rssi)])` - Successful execution

`-1` - Failed execution



| Parameter | Type    | Description                            |
| --------- | ------- | -------------------------------------- |
| wifiNums  | Integer | The number of scanned Wi-Fi hotspots.  |
| mac       | String  | MAC address of the Wi-Fi hotspots.     |
| rssi      | Integer | Signal strength of the Wi-Fi hotspots. |

**Example**

```python
>>> wifiScan.start()
(7, [('34:CE:00:09:E5:A8', -30), ('30:FC:68:E2:2D:F7', -44), ('12:CA:41:D4:B2:50', -54), ('D0:DB:B7:90:2D:07', -58), ('00:03:7F:12:CB:CB', -61), ('60:38:E0:C2:84:D9', -62), ('08:4F:0A:05:22:8F', -63)])
```

