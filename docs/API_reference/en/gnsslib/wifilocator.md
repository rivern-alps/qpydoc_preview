# class wifilocator - Wi-Fi Positioning 

This module provides the class of Wi-Fi positioning and gets the module longitude and latitude coordinate.



> Currently, only EC600S, EC600N, EC800N, EC200U and EC600U series modules support this feature.



**Example:**

```python
import wifilocator
# Creates a wifilocator object
wifiloc = wifilocator.wifilocator("xxxxxxxxxxxxxxxx")
# Gets the module coordinate
wifiloc.getwifilocator()
(117.1152877807617, 31.82142066955567, 100)
# The secret key "xxxxxxxxxxxxxxxx" used above refers to token. You can apply for a secret key from Quectel.
```



## Constructors 

### `wifilocator.wifilocator`

```python
class wifilocator.wifilocator(token)
```

Creates a wifilocator object and configures the suite token of Wi-Fi positioning. Creates a wifilocator object and uses a specified token to configure the Wi-Fi positioning suite.

**Parameter:**

- `token` - String type. Secret key. It consists of 16 bit characters and you can apply for it from Quectel.



## Get the Coordinate

### wifilocator.getwifilocator

```python
wifilocator.getwifilocator()
```

This method gets the module longitude and latitude coordinate.

**Return Value:**

If successful, it returns the module longitude and latitude coordinate. Tuple format: `(longtitude, latitude, accuracy)`;

`longtitude` : longitude.

`latitude` : latitude.

`accuracy` : accuracy. Unit: meter.

If failed, it returns the error code. The error code description is as follows: 

`1` – Network error. Please confirm whether the dial is normal.

`2` – Secret key length error. The length must be 16 bytes.

`3` – Error in getting coordinates.



