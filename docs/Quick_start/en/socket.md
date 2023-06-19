## Establish Your First TCP Connection

For the services that need to connect to the network, it is recommended to use the built-in checkNet feature of QuecPython. Wait until the network connection is successful before executing the subsequent steps. For details, see [checkNet in QuecPython_classlib](https://python.quectel.com/doc/doc/API_reference/en/QuecPython_classlib/checkNet.html)).

```python
pythonCopy code# -*- coding: UTF-8 -*-
import utime
utime.sleep(10)	# Sleep for 10 seconds to wait for the system to be ready.

import checkNet
from machine import Pin
from usr import test

# Set the following items as global variables.
PROJECT_NAME = "My_Test"	# Your project name
PROJECT_VERSION = "0.2.1"	# Your project version
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# ......

if __name__ == '__main__':
    # Check the network readiness state at the program entry.
    stagecode, subcode = checknet.wait_network_connected(30)	
    # You can determine the current network state by the following two status codes.
    print('stagecode = {}, subcode = {}'.format(stagecode, subcode))

# ......
```

### request

Access HTTP web pages by calling *request.get()*. For details, see [request in QuecPython classlib](https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonThirdlib?id=request-http).

```python
pythonCopy code# Add the following codes after the codes above.
if stagecode == 3 and subcode == 1:   # The network is ready.
    http_log.info('Network connection successful!')
    response = request.get("http://httpbin.org/get")   # Initiate an HTTP GET request.
    http_log.info(response.json())  # Read the returned server information in JSON format.
```

### socket

[Socket Usage Example](https://python.quectel.com/doc/doc/Quick_start/zh/socket.html)