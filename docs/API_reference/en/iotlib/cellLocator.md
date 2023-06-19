# cellLocator - Base Station Location

This module provides base station location feature and gets the latitude and longitude coordinate information of QuecPython modules.



>Currently, only EC600S/EC600N/EC800N/EC200U/EC600U series module supports this feature.



## Get Location

### `cellLocator.getLocation`

```python
cellLocator.getLocation(serverAddr, port, token, timeout [, profileIdx])
```

This method gets the module's latitude and longitude coordinate information.

**Parameter：**

* `serverAddr` - String type. Server domain name with a length less than 255 bytes. Currently only “[www.queclocator.com”](http://www.queclocator.xn--com-9o0a/) is supported.
* `port` - Integer type. Server port. Currently only port 80 is supported. 
* `token` - String type. A 16-character key, and application is required.
* `timeout` - Integer type. Timeout. Range: 1–300.  Unit: s. Default value: 300.
* `profileIdx` - Integer type. PDP context ID. It is an optional parameter and the default is the one that has been successfully dialed. Setting other values may require a dedicated APN and password.<br>Range: EC600N/EC600S/EC800N series module is 1–8 and EC200U/EC600U series module is 1–7.

**Return Value：**

Returns the longitude and latitude coordinate information in tuple format: `(longtitude, latitude, accuracy)`. `(0.0, 0.0, 0)` indicates invalid coordinate information.

`longtitude`: Longitude.

`latitude`:  Latitude.

`accuracy`: Accuracy. Unit: meter.

The error codes are described as follows:

`1` – Failed initialization

`2` – The server address is too long (more than 255 bytes)

`3` – Key length error (It must be 16 bytes)

`4` – The timeout is out of range. The supported range is 1–300

`5` – The specified PDP is not connected to the network

`6` – Obtaining location error

**Example:**

```python
>>> import cellLocator
>>> cellLocator.getLocation("www.queclocator.com", 80, "xxxxxxxxxxxxxxxx", 8, 1)
(117.1138, 31.82279, 550)
# The key "xxxxxxxxxxxxxxxx" indicates token. Contact Quectel Technical Support to apply it.
```
