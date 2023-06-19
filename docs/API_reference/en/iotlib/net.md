# net - Networks

This feature is related to the network and provides interfaces of configuring and querying the information of the network mode, such as getting the network registration status and setting the network searching mode.

>Note: It is recommended that you should configure the APN information of the corresponding operator when using SIM cards of different operators. If the APN information is not configured or the configuration is incorrect, the module may not register on the network. See `dataCall.setPDPContext` for methods of how to configure the APN information. 



## Get Signal Strength

### `net.csqQueryPoll`

```python
net.csqQueryPoll()
```

This method gets the signal strength.

**Return Value:**

 Value of CSQ signal strength - Successful execution

`-1` - Failed execution

`99` - Error

>Note: Range of the value of signal strength: 0–31. The higher the value, the better the signal strength.



**Example:**

```python
>>> import net
>>> net.csqQueryPoll()
31
```



## Get Cell Information

### `net.getCellInfo`

```python
net.getCellInfo()
```

This method gets the information of neighbour cells.

**Return Value:**

 List of the information of three network modes `（GSM, UMTS, LTE）` - Successful execution.

`-1` - Failed execution.

An empty list - The information of the corresponding network mode is empty.

`([(flag, cid, mcc, mnc, lac, arfcn, bsic, rssi)], [(flag, cid, licd, mcc, mnc, lac, uarfcn, psc, rssi)], [(flag, cid, mcc, mnc, pci, tac, earfcn, rssi, rsrq, sinr),...])`

* Descriptions of `GSM` network mode

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| `flag`    | Cell type. Range: 0–3. 0: Current serving cell. 1: Neighbour cell. 2: Intra-frequency neighbour cell. 3: Inter-frequency neighbour cell. |
| `cid`     | Cell ID in GSM network. 0 indicates empty. Range: 0–65535.   |
| `mcc`     | Mobile Country Code. Range: 0–999.<br>Note: For EC100Y/EC600S/EC600N/EC600E/EC800E/EC200A/EC600M/EC800M series module, this value is in hexadecimal. For example, Decimal number 1120 is 0x460 in hexadecimal in which 460 indicates MCC460. For other series modules, this value is in decimal format. |
| `mnc`     | Mobile Network Code. Range: 0–99.                            |
| `lac`     | Location Area Code. Range: 1–65534.                          |
| `arfcn`   | Absolute Radio Frequency Channel Number. Range: 0–65535.     |
| `bsic`    | Base Station Identification Code. Range: 0–63.               |
| `rssi`    | In GSM network, this value indicates Rx level and describes the received signal strength. 99 indicates unknown or undetectable. <br/>RSSI = RXLEV - 111. Unit: dBm. Range of RXLEV: 0–63. Range of RSSI: -111 to -48 dBm. |

* Descriptions of `UMTS` network mode

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| `flag`    | Cell type. Range: 0–3. 0: Current serving cell. 1: Neighbour cell. 2: Intra-frequency neighbour cell. 3: Inter-frequency neighbour cell. |
| `cid`     | Cell identity in UMTS network mode. Cell identity = RNC_ID × 65536 + Cell_ID. Range of cell identity: 0x0000000–0xFFFFFFF (The cell identity is 28 bits). It means that the first two bytes of cell identity indicate RNC_ID and the last two bytes indicate Cell_ ID. Range of Cell_ID: 0–65535. |
| `lcid`    | URA ID. Range: 0–65535. 0 indicates that the information does not exist. |
| `mcc`     | Mobile Country Code. Range: 0–999.                           |
| `mnc`     | Mobile Network Code. Range:  0–99.                           |
| `lac`     | Location Area Code. Range: 1–65534.                          |
| `uarfcn`  | UTRA Absolute Radio Frequency Channel Number. Range: 0–65535. |
| `psc`     | Primary Scrambling Code. This parameter determines the primary scrambling code of the scanned cell. Range: 0–511. |
| `rssi`    | In UMTS network, this value indicates received signal code power (RSCP), that is CPICH/PCCPCH. <br>RSSI = RSCP - 115. Unit: dBm. Range: -121 to -25 dBm. |

* Descriptions of `LTE` network mode

| Parameter | Description                                          |
| ------ | ------------------------------------------------------------ |
| `flag` | Cell type. Range: 0–3. 0: Current serving cell. 1: Neighbour cell. 2: Intra-frequency neighbour cell. 3: Inter-frequency neighbour cell. |
| `cid`  | Cell identity, also called E-UTRAN cell identifier (ECI) in LTE network. ECI = eNodeB ID × 256 + Cell ID. Range: 0x0000000–0xFFFFFFF (The cell identity is 28 bits). The first 20 bits indicate eNodeB ID. The last 8 bits indicate LTE Cell ID. |
| `mcc`  | Mobile Country Code. Range: 0–999. |
| `mnc`  | Mobile Network Code. Range: 0–99. |
| `pci`  | Physical-layer cell identity. Range: 0–503. |
| `tac`  | Tracking Area Code. Range: 0–65535.           |
| `earfcn` | E-UTRA Absolute Radio Frequency Channel Number. Range: 0–65535. |
| `rssi` | In LTE network, RSSI indicates all received signal strength. Range: -140 to -44. Unit: dBm. <br>Note: All series modules cannot get RSSI currently but use RSRP, excluding BC25/BG77/BG95 series module.<br>RSRP indicates received effective signal strength. Range: -140 to -44. Unit: dBm. |
| `rsrq` |Reference signal receiving quality (RSRQ) of the LTE network. Range: -20 to -3. <br>Note: Theoretically, RSRQ ranges from -19.5 to -3. But due to the problem of calculation method, the supported RSRQ ranges from -20 to -3.<br>Currently, it is meaningful to get this parameter only for BC25/BG77/BG95/EC600E/EC800E series module. This parameter is meaningless for other modules.|



>Note: This interface will block for 3–5 seconds when searching for cells. In areas without signals, the blocking time will be longer.



**Example:**

```python
>>> import net
>>> net.getCellInfo()
([], [], [(0, 232301375, 1120, 17, 378, 26909, 1850, -66, -8), (3, 110110494, 1120, 17, 10, 26909, 2452, -87, -17), (3, 94542859, 1120, 1, 465, 56848, 1650, -75, -10), 
(3, 94472037, 1120, 1, 369, 56848, 3745, -84, -20)])

>>> net.getCellInfo()
([], [], [(0, 17104243, 460, 4, 121, 19472, 3688, -76, -15)])
```



## Network Mode and Roaming Configuration

### `net.getConfig`

```python
net.getConfig()
```

This method gets the current network mode and roaming configuration. 

**Return Value:**

 `-1` - Failed execution

A tuple containing the current preferred network mode and roaming enabling status - Successful execution

* Network mode

| Value | Network mode                  |      | Value | Network mode                                     |
| ----- | :---------------------------- | ---- | ----- | ------------------------------------------------ |
| 0     | GSM                           |      | 17    | UMTS_LTE (Dual-link)                             |
| 1     | UMTS                          |      | 18    | GSM_UMTS_LTE (Dual-link)                         |
| 2     | GSM_UMTS (Automatic)          |      | 19    | CATM supported by BG95/BG77 series module.       |
| 3     | GSM_UMTS (GSM preferred)      |      | 20    | GSM_CATM supported by BG95 series module.        |
| 4     | GSM_UMTS (UMTS preferred)     |      | 21    | CATNB supported by BG95/BG77 series module.      |
| 5     | LTE                           |      | 22    | GSM_CATNB supported by BG95 series module.       |
| 6     | GSM_LTE (Automatic)           |      | 23    | CATM_CATNB supported by BG95/BG77 series module. |
| 7     | GSM_LTE (GSM preferred)       |      | 24    | GSM_CATM_CATNB supported by BG95 series module.  |
| 8     | GSM_LTE (LTE preferred)       |      | 25    | CATM_GSM supported by BG95 series module.        |
| 9     | UMTS_LTE (Automatic)          |      | 26    | CATNB_GSM supported by BG95 series module.       |
| 10    | UMTS_LTE (UMTS preferred)     |      | 27    | CATNB_CATM supported by BG95/BG77 series module. |
| 11    | UMTS_LTE (LTE preferred)      |      | 28    | GSM_CATNB_CATM supported by BG95 series module.  |
| 12    | GSM_UMTS_LTE (Automatic)      |      | 29    | CATM_GSM_CATNB supported by BG95 series module.  |
| 13    | GSM_UMTS_LTE (GSM preferred)  |      | 30    | CATM_CATNB_GSM supported by BG95 series module.  |
| 14    | GSM_UMTS_LTE (UMTS preferred) |      | 31    | CATNB_GSM_CATM supported by BG95 series module.  |
| 15    | GSM_UMTS_LTE (LTE preferred)  |      | 32    | CATNB_CATM_GSM supported by BG95 series module.  |
| 16    | GSM_LTE (Dual-link)           |      |       |                                                  |



>BC25 series module does not support this method.
>
>BG95-M1 series module only supports CAT-M network mode.
>
>BG95-M2/BG77 series module only supports two network modes: CAT-M and CATNB.
>
>BG95-M3/M8 series module supports three network modes: CAT-M, CATNB and GSM.  



**Example:**

```python
>>> import net
>>>net.getConfig ()
(8, False)
```



### `net.setConfig`

```python
net.setConfig(mode [, roaming])
```

This method sets the network mode and roaming configuration.

**Parameter:**

* `mode` - Integer type. Network mode. See the above table of network modes for details.

* `roaming` - Integer type. Roaming switch. Optional parameter (`0`: Disable,  `1`: enable).

**Return Value:**

`0` - Successful execution

`-1` - Failed execution



>* roaming is an optional parameter, which can be omitted for unsupported module models.
>* BC25 series module does not support this method.
>* EC200U/EC600U/EG915U series module does not support the configuration of roaming parameters and only supports network modes GSM, GSM_LTE (automatic) and GSM_LTE (LTE preferred).
>* EC600E/EC800E series module only supports LTE network mode.  



**Example:**

```python
>>> import net
>>>net.setConfig(6)
0

>>>net.getConfig ()
(6, False)
```



## Get Network Configuration Mode

### `net.getNetMode`

```python
net.getNetMode()
```

This method gets the network configuration mode. 

**Return Value:**

`-1` - Failed execution

A tuple `(selection_mode, mcc, mnc, act)` - Successful execution

| Parameter        | Type    | Description                              |
| ---------------- | ------- | ---------------------------------------- |
| `selection_mode` | Integer | Method. 0 - Automatically. 1 - Manually. |
| `mcc`            | String  | Mobile Country Code.                     |
| `mnc`            | String  | Mobile Network Code.                     |
| `act`            | Integer | ACT mode of the preferred network.       |

Enumeration values of `ACT` modes:

| Value | ACT Mode           |
| ----- | ------------------ |
| 0     | GSM                |
| 1     | COMPACT            |
| 2     | UTRAN              |
| 3     | GSM wEGPRS         |
| 4     | UTRAN wHSDPA       |
| 5     | UTRAN wHSUPA       |
| 6     | UTRAN wHSDPA HSUPA |
| 7     | E UTRAN            |
| 8     | UTRAN HSPAP        |
| 9     | E TRAN A           |
| 10    | NONE               |

Enumeration values of `ACT` modes of BG95 series module:

| Value | ACT Mode        |
| ---- | ------------------ |
| 0    | GSM                |
| 1    | GSM COMPACT        |
| 2    | UTRAN              |
| 3    | GSM wEGPRS         |
| 4    | UTRAN wHSDPA       |
| 5    | UTRAN wHSUPA       |
| 6    | UTRAN wHSDPA HSUPA |
| 7    | E_UTRAN            |
| 8    | UTRAN HSPAP        |
| 9    | E_UTRAN_CA         |
| 10   | E_UTRAN_NBIOT      |
| 11   | E_UTRAN_EMTC       |
| 12   | NONE               |

**Example:**

```python
>>> import net
>>> net.getNetMode()
(0, '460', '46', 7)
```



## Get Detailed Signal Strength

### `net.getSignal`

```python
net.getSignal([sinrEnable])
```

This method gets the detailed signal strength.

**Parameter:**

* `sinrEnable` - Integer type. Optional parameter. Enable or disable to get SINR.

| Value | Description |
|-----| ------------- |
| 0   | Disable to get SINR |
| 1   | Enable to get SINR |

**Return Value:**

`-1` - Failed execution

A tuple containing `(GW, LTE)` - Successful execution

 `([rssi, bitErrorRate, rscp, ecno], [rssi, rsrp, rsrq, cqi, sinr])`

* Descriptions of `GSM/WCDMA` :

| Parameter      | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| `rssi`         | In GSM and WCDMA network, this value indicates Rx level and describes the received signal strength. 99 indicates unknown or undetectable. <br/>RSSI = RXLEV - 111. Range of RXLEV: 0–63. Unit: dBm. |
| `bitErrorRate` | Bit error rate. Range: 0–7. 99 indicates unknown or undetectable. |
| `rscp`         | Receive Signal Channel Power. Range: -121 to -25 dBm. 255 indicates unknown or undetectable. |
| `ecno`         | 【Pilot channel参考参数名修改缩写】. Range: -24–0. 255 indicates unknown or undetectable. |

* Descriptions of  `LTE` :

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| `rssi`    | Received Signal Strength Indicator. Range: -140 to -44 dBm. 99 indicates unknown or undetectable. |
| `rsrp`    | Reference Signal Receiving Power. Range: -140 to -44 dBm. 99 indicates unknown or undetectable. |
| `rsrq`    | Reference Signal Receiving Quality. Range: -20 to -3 dBm. The higher the value, the better the reference signal received quality. 255 indicates unknown or undetectable. |
| `cqi`     | Channel Quality Indication. 255 indicates unknown or undetectable. |
| `sinr`    | Signal to interference plus Noise Ratio. Range: -10–40 dBm. 255 indicates unknown or undetectable. |



>*  `sinrEnable` is an optional parameter, which can be omitted for the unsupported modules. If you do not enter this parameter, `sinr` won't be got by default.
>* All Quectel series modules support to get `sinr`, excluding BC25 series module.



**Example:**

```python
>>> import net
>>>net.getSignal()
([99, 99, 255, 255], [-51, -76, -5, 255])
>>>net.getSignal(0)
([99, 99, 255, 255], [-51, -76, -5, 255])
>>>net.getSignal(1)
([99, 99, 255, 255], [-51, -76, -5, 255, 18])
```



## Get Current Base Station Time

### `net.nitzTime`

```python
net.nitzTime()
```

This method gets the current base station time, which is the time issued by the base station when the module boots and registers on the network successfully.

**Return Value:**

`-1` - Failed execution

A tuple `(date, abs_time, leap_sec)` containing the base station time and corresponding timestamps and leap seconds (0 indicates that the current base station time is unavailable.)   - Successful execution

| Parameter  | Type    | Description                                                  |
| ---------- | ------- | ------------------------------------------------------------ |
| `date`     | String  | Base time. The part of the time zone varies with module models. See the example below for details.<br>Please use `setTimeZone(offset)` and `getTimeZone()` of `utime` feature if you need to set and get the time zone.<br>The unit of  these two interfaces is hour for different modules. See [`utime`](../QuecPython标准库/utime.md) for details. |
| `abs_time` | Integer | Absolute seconds of the base station time.                   |
| `leap_sec` | Integer | Leap seconds.                                                |

**Example:**

```python
>>> import net
>>> net.nitzTime() 
# For return values of EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A series module, the unit of the time zone is hour. 8 indicates UTC + 08:00. 
('21/10/26 06:08:03 8 0', 1635228483, 0)  
# For return values of BC25/EC600E/EC800E/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G series module, the unit of the time zone is 15 minutes. +32 indicates UTC + 08:00.
('20/11/26 02:13:25 +32 0', 1606356805, 0)
# For return values of BG77/BG95 series module, there is no time zone.  
('23/02/14 02:25:13', 1676312713, 0)
```



## Get Operator Information

### `net.operatorName`

```python
net.operatorName()
```

This method gets the operator information of the current network registration.

**Return Value:**

 `-1` - Failed execution

A tuple `(long_eons, short_eons, mcc, mnc)` containing the operator information of the current network registration - Successful execution

| Parameter    | Type   | Description                   |
| ------------ | ------ | ----------------------------- |
| `long_eons`  | String | Operator's full name.         |
| `short_eons` | String | Operator's name abbreviation. |
| `mcc`        | String | Mobile Country Code           |
| `mnc`        | String | Mobile Network Code           |

**Example:**

```python
>>> import net
>>> net.operatorName()
('CHN-UNICOM', 'UNICOM', '460', '01')
```



## Get Network Registration Information

### `net.getState`

```python
net.getState()
```

This interface gets the network registration information.

**Return Value:**

 `-1` - Failed execution

A tuple `([voice_state, voice_lac, voice_cid, voice_rat, voice_reject_cause, voice_psc], [data_state, data_lac, data_cid, data_rat, data_reject_cause, data_psc])` containing the information of the phone and network registration  - Successful execution

`voice_state, voice_lac, voice_cid, voice_rat, voice_reject_cause, voice_psc` - Information of the phone registration

`data_state, data_lac, data_cid, data_rat, data_reject_cause, data_psc` - Information of the current network registration

* Parameter：

| Parameter      | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| `state`        | Network registration status. See the table below for details. |
| `lac`          | Location Area Code. Range: 1–65534.                          |
| `cid`          | Cell ID. Range: 0x00000000–0x0FFFFFFF. See return values above of `net.getCellInfo()` for details. |
| ``rat``        | Access technology. See the following table for details.      |
| `reject_cause` | Reasons for registration rejection. For EC200U/EC600U/BC25 series module, this parameter is necessary and it is not an optional parameter. |
| `psc`          | Primary scrambling code. For EC200U/EC600U/BC25 series module, this parameter is necessary and it is not a valid parameter. |

* Enumeration values of `state`:

| Value | Description                                                  |
| ----- | ------------------------------------------------------------ |
| 0     | Not registered and MT is not searching for an operator again. |
| 1     | Registration completed. Local network.                       |
| 2     | Not registered but MT is searching for an operator.          |
| 3     | Registration denied.                                         |
| 4     | Unknown.                                                     |
| 5     | Registration completed. Roaming network.                     |
| 6     | Registered on "SMS only" local network (inapplicable).       |
| 7     | Registered on "SMS only" roaming network (inapplicable).     |
| 8     | Emergency attachment is limited to emergency bearer service. |
| 9     | Registered on "Low priority of CSFB" local network (inapplicable). |
| 10    | Registered on "Low priority of CSFB" roaming network (inapplicable). |
| 11    | Emergency bearer service only.                               |

* `access technology`

| Value | Description        |
| ----- | ------------------ |
| 0     | GSM                |
| 1     | GSM COMPACT        |
| 2     | UTRAN              |
| 3     | GSM wEGPRS         |
| 4     | UTRAN wHSDPA       |
| 5     | UTRAN wHSUPA       |
| 6     | UTRAN wHSDPA HSUPA |
| 7     | E_UTRAN            |
| 8     | UTRAN HSPAP        |
| 9     | E_UTRAN_CA         |
| 10    | NONE               |



> For BG77/BG95 series module:

| Value | Description        |
| ----- | ------------------ |
| 0     | GSM                |
| 1     | GSM COMPACT        |
| 2     | UTRAN              |
| 3     | GSM wEGPRS         |
| 4     | UTRAN wHSDPA       |
| 5     | UTRAN wHSUPA       |
| 6     | UTRAN wHSDPA HSUPA |
| 7     | E_UTRAN            |
| 8     | UTRAN HSPAP        |
| 9     | E_UTRAN_CA         |
| 10    | E_UTRAN_NBIOT      |
| 11    | E_UTRAN_EMTC       |
| 12    | NONE               |

**Example:**

```python
>>> import net
>>> net.getState()
([11, 26909, 232301323, 7, 0, 466], [0, 26909, 232301323, 7, 0, 0])
```



## Get Cell ID

### `net.getCi`

```python
net.getCi()
```

This method gets neighbour cells. The result gotten by this interface is the collection of cell IDs in the result gotten by *net.getCellInfo()*. 

**Return Value:**

 An array `[id, ……, id]` containing cell IDs. List type. The number of array members is not fixed, and different locations, signal strength, and other factors may lead to different results.  - Successful execution

 `-1` - Failed execution

**Example:**

```python
>>> net.getCi()
[14071232, 0]
```



### `net.getServingCi`

```python
net.getServingCi()
```

This method gets the serving cell ID. The result gotten by this interface is the collection of cell IDs in the result gotten by *net.getCellInfo()*. 

**Return Value:**

Serving cell ID - Successful execution

`-1` - Failed execution

**Example:**

```python
>>> import net
>>> net.getServingCi()
94938399
```



## Get MNC of Cell

### `net.getMnc`

```python
net.getMnc()
```

This method gets MNC of the neighbour cell ID. The result gotten by this interface is the collection of MNCs in the result gotten by *net.getCellInfo()*.   

**Return Value:**

 An array `[mnc, ……, mnc]` containing `mnc` of cells. List type. The number of array members is not fixed, and different locations, signal strength, and other factors may lead to different results.  - Successful execution

`-1` - Failed execution

**Example:**

```python
>>> import net
>>> net.getMnc()
[0, 0]
```



### `net.getServingMnc`

```python
net.getServingMnc()
```

This method gets MNC of the serving cell. The result gotten by this interface is the collection of MNCs in the result gotten by *net.getCellInfo()*.  

**Return Value:**

`mnc` of the serving cell - Successful execution 

`-1` - Failed execution

**Example:**

```python
>>> import net
>>> net.getServingMnc()
1
```



## Get MCC of Cell

### `net.getMcc`

```python
net.getMcc()
```

This method gets MCCs of the neighbour cells. The result gotten by this interface is the collection of MCCs in the result gotten by *net.getCellInfo()*.  

**Return Value:**

An array `[mnc, ……, mnc]` containing `mnc` of cells. List type. The number of array members is not fixed, and different locations, signal strength, and other factors may lead to different results.  - Successful execution

`-1` - Failed execution



> For EC100Y/EC600S/EC600N/EC600E/EC800E/EC200A/EC600M/EC800M series module, this value is in hexadecimal. For example, Decimal number 1120 is 0x460 in hexadecimal in which 460 indicates MCC460. For other series modules, this value is in decimal format.



**Example:**

```python
>>> import net
>>> net.getMcc()
[1120, 0]
```



### `net.getServingMcc`

```python
net.getServingMcc()
```

This method gets MCC of the serving cell. The result gotten by this interface is the collection of MCCs in the result gotten by *net.getCellInfo()*.  

**Return Value:**

 `mcc` of the serving cell - Successful execution

`-1` - Failed execution



> For EC100Y/EC600S/EC600N/EC600E/EC800E/EC200A/EC600M/EC800M series module, this value is in hexadecimal. For example, Decimal number 1120 is 0x460 in hexadecimal in which 460 indicates MCC460. For other series modules, this value is in decimal format.



**Example:**

```python
>>> import net
>>> net.getServingMcc()
1120
```



## Get LAC of Cell

### `net.getLac`

```python
net.getLac()
```

This method gets LACs of the neighbour cells. The result gotten by this interface is the collection of LACs in the result gotten by *net.getCellInfo()*.   

**Return Value:**

An array `[lac, ……, lac]` containing `lac` of cells. List type. The number of array members is not fixed, and different locations, signal strength, and other factors may lead to different results.  - Successful execution

`-1` - Failed execution

**Example:**

```python
>>> import net
>>> net.getLac()
[21771, 0]
```



### `net.getServingLac`

```python
net.getServingLac()
```

This method gets LACs of the serving cells. The result gotten by this interface is the collection of LACs in the result gotten by *net.getCellInfo()*. 

**Return Value:**

`lac` of the serving cell - Successful execution

`-1` - Failed execution

**Example:**

```python
>>> import net
>>> net.getServingLac()
56848
```



## Work Mode Configuration

### `net.getModemFun`

```python
net.getModemFun()
```

This method gets the current work mode.

**Return Value:**

The current work mode of the module - Successful execution

`-1` - Failed execution

| Mode | Description |
| --- | ---------- |
| 0   | Disable full functionality |
| 1   | Enable full functionality (default) |
| 4   | Airplane mode |

**Example:**

```python
>>> import net
>>> net.getModemFun()
1
```



### `net.setModemFun`

```python
net.setModemFun(fun [, rst])
```

This method sets the current work mode of the module.

**Parameter:**

* `fun` - Integer type. Work mode of the module.
| Mode | Description |
| --- | ---------- |
| 0   | Disable full functionality |
| 1   | Enable full functionality (default) |
| 4   | Airplane mode |

* `rst` - Integer type. Reboot flag. Optional parameter. 
| Value | Description |
| --- | ---------- |
| 0   | Do not reboot the module after setting the current work mode (default). |
| 1   | Reboot the module after setting the current work mode. |

**Return Value:**

 `0` - Successful execution

`-1` - Failed execution

**Example:**

```python
>>> import net
>>> net.setModemFun(4)
0
```



## Set and Get Band

### `net.setBand`

```python
net.setBand(netRat, gsmBand, bandTuple)
```
This method sets the required band, that is, lock the band specified by the user if the module supports this method.  

* Comparison Table of Band Values

| Network Mode    | Band Value                                                   |
| --------------- | ------------------------------------------------------------ |
| EGPRS(GSM)      | EGSM900 - 0x1<br/>DCS1800 - 0x2<br/>GSM850 - 0x4<br/>PCS1900 - 0x8 |
| LTE/eMTC/NB-IoT | BAND1 - 0x1<br/>BAND2 - 0x2<br/>BAND3 - 0x4<br/>BAND4 - 0x8<br/>BAND5 - 0x10<br/>BAND8 - 0x80<br/>BAND12 - 0x800<br/>BAND13 - 0x1000<br/>BAND18 - 0x20000<br/>BAND19 - 0x40000<br/>BAND20 - 0x80000<br/>BAND25 - 0x1000000<br/>BAND26 - 0x2000000<br/>BAND27 - 0x4000000<br/>BAND28 - 0x8000000<br/>BAND31 - 0x40000000<br/>BAND66 - 0x20000000000000000<br/>BAND71 - 0x400000000000000000<br/>BAND72 - 0x800000000000000000<br/>BAND73 - 0x1000000000000000000<br/>BAND85 - 0x1000000000000000000000<br/> |

* Supported `band` of BG95-M3 Series Module

| Network Mode | Supported Band                                               |
| ------------ | ------------------------------------------------------------ |
| eMTC         | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B26/B27/B28/B66/B85 |
| NB-IoT       | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B28/B66/B71/B85    |
| EGPRS        | GSM850/EGSM900/DCS1800/PCS1900                               |

* Supported `band` of EG912N-ENAA Series Module  

| Network Mode | Supported Band                 |
| ------------ | ------------------------------ |
| LTE          | B1/B3/B5/B7/B8/B20/B28/B31/B72 |
| EGPRS        | EGSM900/DCS1800                |

**Parameter:**

* `netRat` - Integer type. Network mode. It indicates the kind of network mode whose band is to be set.
| RAT Value | Description    |
| --------- | -------------- |
| 0         | GSM network    |
| 1         | LTE network    |
| 2         | Cat M network  |
| 3         | NB-IoT network |

* `gsmBand` - Integer type. The `band` value of `GSM` network. See the `band` value comparison table above.  

* `bandtuple` - The `band` value of other network modes excluding `GSM` network and it is a tuple containing 4 elements `(band_hh, band_hl, band_lh, band_ll)`, each of which cannot exceed 4 bytes.

  `band_hh` - The first 4 bytes of the first 8 bytes of the band value.
  `band_hl` - The last 4 bytes of the first 8 bytes of the band value.
  `band_lh` - The first 4 bytes of the last 8 bytes of the band value. 
  `band_ll` - The last 4 bytes of the last 8 bytes of the band value. 
  If you want to set the `band` value to the `band_value` :
  `band_hh = (band_value & 0xFFFFFFFF000000000000000000000000) >> 96`
  `band_hl = (band_value & 0x00000000FFFFFFFF0000000000000000) >> 64`
  `band_lh = (band_value & 0x0000000000000000FFFFFFFF00000000) >> 32`
  `band_ll = (band_value & 0x000000000000000000000000FFFFFFFF)`

**Return Value:**

 `0` - Successful execution

`-1` - Failed execution



>* Currently, BG95 series module/EG912N-ENAA module supports this method. 
>* BG95 series module does not support the `band` of LTE network.
>* EG912N-ENAA module only supports the band of GSM network and LTE network. 



**Example:**

```python
import net
import utime

'''
You can directly use the following two interfaces to set and get the band. 
'''
def set_band(net_rat, band_value):
    if net_rat == 0:
        retval = net.setBand(0, band_value, (0, 0, 0, 0))
    else:
        band_hh = (band_value & 0xFFFFFFFF000000000000000000000000) >> 96
        band_hl = (band_value & 0x00000000FFFFFFFF0000000000000000) >> 64
        band_lh = (band_value & 0x0000000000000000FFFFFFFF00000000) >> 32
        band_ll = (band_value & 0x000000000000000000000000FFFFFFFF)
        retval = net.setBand(net_rat, 0, (band_hh, band_hl, band_lh, band_ll))
    return retval


def get_band(net_rat):
    return net.getBand(net_rat)

#======================================================================================================

'''
Sets the band of GSM network to 0xa, that is,  DCS1800 + PCS1900
0xa = 0x2(DCS1800) + 0x8(PCS1900)
'''
def set_gsm_band_example():
    print('Set GSM band to 0xa example:')
    gsm_band = get_band(0)
    print('GSM band value before setting:{}'.format(gsm_band))
    ret = set_band(0, 0xa)
    if ret == 0:
        print('Set GSM band successfully.')
    else:
        print('Set GSM band failed.')
    utime.sleep(1) # It takes time to set the band. You can wait for a period of time before getting new results.
    gsm_band = get_band(0)
    print('GSM band value after setting:{}'.format(gsm_band))
    return ret


'''
Sets the band of eMTC network to 0x15, that is BAND1 + BAND3 + BAND5
0x15 = 0x1(BAND1) + 0x4(BAND3) + 0x10(BAND5)
'''
def set_camt_band_example():
    print('Set CATM band to 0x15 example:')
    catm_band = get_band(2)
    print('CATM band value before setting:{}'.format(catm_band))
    ret = set_band(2, 0x15)
    if ret == 0:
        print('Set CATM band successfully.')
    else:
        print('Set CATM band failed.')
    utime.sleep(1) # It takes time to set the band. You can wait for a period of time before getting new results.
    catm_band = get_band(2)
    print('CATM band value after setting:{}'.format(catm_band))
    return ret


'''
Sets the band of NB-IoT network to 0x1000800000000000020011, that is BAND1 + BAND5 + BAND18 + BAND71 + BAND85   
0x1000400000000000020011 = 0x1 + 0x10 + 0x20000 + 0x400000000000000000 + 0x1000000000000000000000
'''
def set_nb_band_example():
    print('Set NB band to 0x1000400000000000020011 example:')
    nb_band = get_band(3)
    print('NB band value before setting:{}'.format(nb_band))
    ret = set_band(3, 0x1000400000000000020011)
    if ret == 0:
        print('Set NB band successfully.')
    else:
        print('Set NB band failed.')
    utime.sleep(1) # It takes time to set the band. You can wait for a period of time before getting new results.
    nb_band = get_band(3)
    print('NB band value after setting:{}'.format(nb_band))
    return ret


def main():
    set_gsm_band_example()
    utime.sleep(1)
    set_camt_band_example()
    utime.sleep(1)
    set_nb_band_example()


if __name__ == '__main__':
    main()
    

#===================================================================================================
# Running results
Set GSM band to 0xa example:
GSM band value before setting:0xf
Set GSM band successfully.
GSM band value after setting:0xa

Set CATM band to 0x15 example:
CATM band value before setting:0x10000200000000090e189f
Set CATM band successfully.
CATM band value after setting:0x15

Set NB band to 0x1000400000000000020011 example:
NB band value before setting:0x10004200000000090e189f
Set NB band successfully.
NB band value after setting:0x1000400000000000020011

```



### `net.getBand`

```python
net.getBand(netRat)
```

This method gets the band value in the current network mode.

**Parameter:** 

* `netRat` - Integer type. Network mode. It indicates that the `band` of which network mode you want to set.
| RAT Value | Description    |
| --------- | -------------- |
| 0         | GSM network    |
| 1         | LTE network    |
| 2         | Cat M network  |
| 3         | NB-IoT network |

**Return Value:** 

Band value in hexadecimal.



>* Currently, BG95 series module/EG912N-ENAA module supports this method. 
>* BG95 series module does not support the `band` of LTE network.
>* EG912N-ENAA module only supports the band of GSM network and LTE network. 



**Example:**

```python
>>> import net
>>> net.getBand(2)
'0x10000200000000090e189f'  # The band is in string type. If you need the value in integer type, int(data) can be called for changing the type.
```



### `net.bandRst`

```python
net.bandRst()
```

This method restores the initial set value of the band.

**Return Value:**

 `0` - Successful execution

`-1` - Failed execution



>Note: EG912N-ENAA series module supports this method.



**Example:**

```python
'''
Sets to other bands first, calls this interface and checks whether it is successfully restored to the initial value.    
Initial set value of EG912N-ENAA series module: gsm_band:0x3(EGSM900/DCS1800 )  lte_band:0x8000000000480800D5(B1/B3/B5/B7/B8/B20/B28/B31/B72 )
'''
>>> import net
>>> net.bandRst()
0
```