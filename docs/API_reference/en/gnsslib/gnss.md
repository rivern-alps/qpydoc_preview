# gnss - External GNSS Resolver

For L76K module or GNSS modules with similar data type, you can get information such as whether the positioning is successful, the latitude and longitude, UTC time, the positioning mode, the number of satellites used for positioning, the number of visible satellites, the azimuth angle of positioning, the ground speed and the geodetic height. Currently, for L76K module, the data got through the interface provided by this module is read from the GNGGA, GNRMC and GPGSV sentences in the original GNSS data package read through the UART.  

> Note: Currently, only EC600S/EC600N/EC800N/EC200U/EC600U/EC600M/EC800M series module supports this method.

## Create GNSS Object

### `gnss.GnssGetData`

```python
gnss.GnssGetData(uartn,baudrate,databits,parity,stopbits,flowctl)
```

Creates a GNSS object to get the GNSS data. Parameters are the type of UARTs for mounting the GNSS module and communication parameters. 

**Parameter**

* `uartn` - Integer type.
  uartn
  `0`-uart0 - DEBUG PORT
  `1`-uart1 – BT PORT
  `2`-uart2 – MAIN PORT
  `3`-uart3 – USB CDC PORT
  
* `baudrate` - Integer type. Baud rate. Some common baud rates are supported, like `4800`, `9600`, `19200`, `38400`, `57600`, `115200` and `230400`. 

* `databits` - Integer type. Data bit. Range: [5–8]. ECX00U series module only supports 8 data bits. 

* `parity` - Integer type. Parity check. 

   `0` – NONE

   `1` – EVEN

   `2` – ODD

* `stopbits` - Integer type. Stop bit. Range: [1–2].

* `flowctl` - Integer type. Hardware control flow.

  `0` – FC_NONE

  `1` – FC_HW

**Return Value**<br />A GNSS object

**Example**

```python
from gnss import GnssGetData
gnss = GnssGetData(1, 9600, 8, 0, 1, 0)
```

## Read and Analyze GNSS Data 

### `gnss.read_gnss_data`

```python
gnss.read_gnss_data(max_retry=1, debug=0)
```

Reads the GNSS data through the UART and returns the length of the GNSS data. 

**Parameter**

* `max_retry` – Integer type. It is an optional parameter. When the GNSS data is invalid, this parameter indicates the maximum times of automatic data-reading. Exit when the data length is 0, that is, no data has been read. Default value: 1. 
* `debug` – Integer type. It is an optional parameter indicating that whether the debugging information is output in the progress of reading and analyzing the GNSS data. 0 – Not output. 1 – Output. Default value: 0. 

**Return Value**

Integer type. Length of the GNSS data read through the UART. Unit: byte.

**Example**

```python
#=========================================================================
gnss.read_gnss_data()	# Uses the dafault settings and reads GNSS data only once. The detailed debugging information is not output.
4224	# Reads data and analyzes GNGGA, GNRMC and GPGSV sentences successfully. Returns the length of the original data read.
#=========================================================================
gnss.read_gnss_data()  # Uses the dafault settings and reads GNSS data only once. The detailed debugging information is not output.
GNGGA data is invalid. # Reads data successfully. The GNGGA sentences got is invalid.
GNRMC data is invalid. # Reads data successfully. The GNRMC sentences got is invalid.
648		# Returns the length of the original data read.
#=========================================================================
gnss.read_gnss_data(max_retry=3)  # Sets the maximum times of automatic data-reading to 3
Not find GPGSV data or GPGSV data is invalid.  # For the first time, no GPGSV sentence is found or invaild. 
continue read.        # Continues to read the next package of data.
Not find GNGGA data.  # For the second time, no GNGGA sentence is found. 
Not find GNRMC data.  # For the second time, no GNRMC sentence is found. 
continue read.        # Continues to read the next package of data
Not find GNGGA data.  # For the third time, no GNGGA sentence is found. 
Not find GNRMC data.  # For the third time, no GNRMC sentence is found. 
continue read.        # Exits. Fails to read data and continues to read but it has reached the maximum times of automatic data-reading.  
128
#=========================================================================
gnss.read_gnss_data(debug=1)  # Sets to output the detailed information in the progress of reading and analyzing data.
GGA data : ['GNGGA', '021224.000', '3149.27680', 'N', '11706.93369', 'E', '1', '19', '0.9', '168.2', 'M', '-5.0', 'M', '', '*52']  # Outputs GNGGA sentence that was matched and simply processed from the original GNSS data.
RMC data : ['GNRMC', '021224.000', 'A', '3149.27680', 'N', '11706.93369', 'E', '0.00', '153.28', '110122', '', '', 'A', 'V*02']  # Outputs GNRMC sentence that was matched and simply processed from the original GNSS data.
total_sen_num = 3, total_sat_num = 12  # Outputs the total number of a complete set of GPGSV sentences and number of visible satellites.
# The following is the specific GPGSV sentences matched.
[0] : ['$GPGSV', '3', '1', '12', '10', '79', '210', '35', '12', '40', '070', '43', '21', '08', '305', '31', '23', '46', '158', '43', '0*6E']
[1] : ['$GPGSV', '3', '2', '12', '24', '', '', '26', '25', '54', '125', '42', '31', '', '', '21', '32', '50', '324', '34', '0*64']
[2] : ['$GPGSV', '3', '3', '12', '193', '61', '104', '44', '194', '58', '117', '42', '195', '05', '162', '35', '199', '', '', '32', '0*54']
4224
```

## Get Original GNSS Data 

### `gnss.getOriginalData`

```python
gnss.getOriginalData()
```

This interface gets the original GNSS data read through the UART. You can get the original GNSS data through this interface for data processing or confirmation. The original GNSS data will be returned after `gnss.read_gnss_data(max_retry=1, debug=0)` is called.

**Return Value**

String type. The original GNSS data read from the UART. 

**Example**

```python
data = gnss.getOriginalData()
print(data)
# Only part of the original GNSS data is listed due to the limited space. 
00,A,3149.28094,N,11706.93869,E,0.00,153.28,110122,,,A,V*04
$GNVTG,153.28,T,,M,0.00,N,0.00,K,A*2E
$GNZDA,021555.000,11,01,2022,00,00*4D
$GPTXT,01,01,01,ANTENNA OK*35
$GNGGA,021556.000,3149.28095,N,11706.93869,E,1,24,0.6,166.5,M,-5.0,M,,*5E
$GNGLL,3149.28095,N,11706.93869,E,021556.000,A,A*47
$GNGSA,A,3,10,12,21,23,24,25,32,193,194,195,199,,1.0,0.6,0.8,1*35
$GNGSA,A,3,01,04,07,09,14,21,22,24,38,39,42,45,1.0,0.6,0.8,4*36
... 
$GNGGA,021600.000,3149.28096,N,11706.93877,E,1,25,0.6,166.4,M,-5.0,M,,*52
$GNGLL,3149.28096,N,11706.93877,E,021600.000,A,A*4B
$GNGSA,A,3,10,12,21,23,24,25,31,32,193,194,195,199,1.0,0.6,0.8,1*37
$GNGSA,A,3,01,04,07,09,$GNGGA,021601.000,3149.28096,N,11706.93878,E,1,25,0.6,166.4,M,-5.0,M,,*5C
$GNGLL,3149.2809
```

## Check Validity of GNSS Data

### `gnss.checkDataValidity`

```python
gnss.checkDataValidity()
```

This interface checks the validity of GNGGA, GNRMC and GPGSV sentences in the GNSS data package read. The GNSS module provides an interface for reading GNGGA, GNRMC and GPGSV sentences in the original GNSS data package through the UART. 

**Return Value**

A list ` (gga_valid, rmc_valid, gsv_valid)`.

`gga_valid` - Whether the GNGGA sentence is read and has been analyzed successfully. 0 – The GNGGA sentence is not read or the data is invalid. 1 – The GNGGA sentence is valid. 

`rmc_valid` - Whether the GNRMC sentence is read and has been analyzed successfully. 0 – The GNRMC sentence is not read or the data is invalid. 1 – The GNRMC sentence is valid. 

`gsv_valid` - Whether the GPGSV sentence is read and has been analyzed successfully. 0 – The GPGSV sentence is not read or the data is invalid. 1 – The GPGSV sentence is valid. 

If you only want to get the positioning result, that is whether the GNGGA sentence is valid, you can set `gga_valid` as 1 or check whether the positioning is successful through *gnss.isFix()* . The GNRMC sentence is analyzed to get the ground speed and the GPGSV sentence is analyzed to get the number of visible satellites and the corresponding azimuth angles of these satellites. Therefore, `rmc_valid` and `gsv_valid` can be omitted.

**Example**

```python
gnss.checkDataValidity()
(1, 1, 1)  # It indicates the GNGGA, GNRMC and GPGSV sentence all has been read and analyzed successfully. 
```

## Check Whether Positioning Is Successful

### `gnss.isFix`

```python
gnss.isFix()
```

Checks whether the valid GNSS data is read through the specified UART.

**Return Value**

`1` – Successful execution

`0` – Failed execution

**Example**

```
gnss.isFix()
1
```

## Get UTC Time

### `gnss.getUtcTime`

```python
gnss.getUtcTime()
```

Gets UTC time in the GNSS data.

**Return Value**

UTC time in string type – Successful execution

`-1` – Failed execution

**Example**

```python
gnss.getUtcTime()
'06:22:05.000'  # hh:mm:ss.sss
```

## Get Positioning Mode

### `gnss.getLocationMode`

```python
gnss.getLocationMode()
```

Gets the positioning mode in the GNSS data. 

**Return Value**

| Value | Description                                                  |
| ----- | ------------------------------------------------------------ |
| -1    | Failed execution. No data is read through the UART or the data read through the UART is invalid. |
| 0     | Unavailable or invalid positioning data                      |
| 1     | Valid positioning. Positioning mode: GPS or SPS mode.        |
| 2     | Valid positioning. Positioning mode: DGPS or DSPS mode.      |
| 6     | Estimation (dead reckoning) mode                             |

**Example**

```python
gnss.getLocationMode()
1
```

## Get Number of Satellites in Use

### `gnss.getUsedSateCnt`

```python
gnss.getUsedSateCnt()
```

Gets the number of satellites in use in the GNSS data. 

**Return Value**

The number of satellites in use in integer type – Successful execution

 `-1` – Failed execution

**Example**

```
gnss.getUsedSateCnt()
24
```

## Get Latitude and Longitude Information

### `gnss.getLocation`

```python
gnss.getLocation()
```

Gets the latitude and longitude information in the GNSS data.

**Return Value**

Latitude and longitude information `(longitude, lon_direction, latitude, lat_direction)`  – Successful execution

 `-1` – Failed execution

`longitude` - Longitude in float type.

`lon_direction` -  Longitude direction in string type. E – east longitude. W – west longitude.

`latitude` - Latitude in float type.

`lat_direction` - Latitude direction in string type. N – north latitude. S – south latitude. 

**Example**

```python
gnss.getLocation()
(117.1156448333333, 'E', 31.82134916666667, 'N')
```

## Get Number of Visible Satellites

### **`gnss.getViewedSateCnt`**

```python
gnss.getViewedSateCnt()
```

Gets the number of visible satellites in the GNSS data. 

**Return Value**

The number of visible satellites in integer type – Successful execution

 `-1` – Failed execution

**Example**

```python
gnss.getViewedSateCnt()
12
```

## Get Visible Azimuth Angles of GNSS Satellites

### **`gnss.getCourse`**

```python
gnss.getCourse()
```

Gets the visible azimuth angles of GNSS satellites in the GNSS data.

**Return Value**

All visible azimuth angles of GNSS satellites. Range: `0–359`. Take due north as the reference plane. The form of return value is a dictionary in which the key indicates the satellite ID and the value indicates the azimuth angle. Please note that the value may be an integer or empty, which depends on whether there is a value for the azimuth angle in the GPGSV sentences in the original GNSS data. 

 `-1` – Failed execution

The format of the return value is as follows: 

`{key:value, ...,  key:value}`

**Example**

```python
 gnss.getCourse()
{'10': 204, '195': 162, '12': 68, '193': 105, '32': 326, '199': 162, '25': 122, '31': 247, '24': 52, '194': 116, '21': 304, '23': 159}
```

## Get Altitude 

### **`gnss.getGeodeticHeight`**

```python
gnss.getGeodeticHeight()
```

Gets the altitude in the GNSS data.

**Return Value**

Altitude in float type. Unit: meter. – Successful execution

 `-1` – Failed execution

**Example**

```python
gnss.getGeodeticHeight()
166.5
```

## Get Ground Speed 

### `gnss.getSpeed`

```python
gnss.getSpeed()
```

Gets the ground speed in the GNSS data.

**Return Value**

Ground speed in float type. Unit: km/h. – Successful execution

 `-1` – Failed execution

**Example**

```python
gnss.getSpeed()
0.0
```
