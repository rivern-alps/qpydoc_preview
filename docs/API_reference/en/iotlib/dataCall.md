# dataCall - Data Call

Establishing a cellular network channel refers to the activation of PDP context, and after a successful activation, the PDN gateway of the core network will assign an IP address to the QuecPython module.

The `dataCall` module contains features of configuring, obtaining , activating and deactivating PDP context, and feature of obtaining the module's IP information. After burning the QuecPython firmware into the module, it will automatically establish a cellular network channel upon startup. If you have configured the APN, the module will use the configured APN information for establishment; otherwise, it will use the default APN.



> When using a SIM card from a different operator, you should configure the APN information of the corresponding operator. Failure to configure or incorrect configuration may result in the module's failure to register to the network, failure to establish the network channel, inability to obtain an IP address, and failure to access the Internet. For information on configuring the APN, refer to the `dataCall.setPDPContext` method.



**Example:**

```python
import dataCall
from misc import Power

# The APN information that the user needs to configure. Modify it according to the actual situation
usrConfig = {'apn': '3gnet', 'username': '', 'password': ''}

# Obtains the information of the first APN, confirming whether the currently used APN is the one specified by the user
pdpCtx = dataCall.getPDPContext(1)
if pdpCtx != -1:
    if pdpCtx[1] != pdpConfig['apn']:
        # If it is not the APN that the user needs, configure it as follows
        ret = dataCall.setPDPContext(1, 0, pdpConfig['apn'], pdpConfig['username'], pdpConfig['password'], 0)
        if ret == 0:
            print('APN configuration succeeded.')
            # After restarting, establish the channel according to the configured information
            Power.powerRestart()  
        else:
            print('APN configuration failed.')
    else:
        print('APN has already been configured.')
else:
    print('Failed to obtain PDP Context.')
```



## APN Configuration and Retrieval

### `dataCall.setPDPContext`

```
dataCall.setPDPContext(profileID, ipType, apn, username, password, authType)
```

Configures the relevant information of the PDP context, and saves the configuration information when power is off. When establishing the channel, use the parameters configured by this method to activate the PDP context.

**Parameter:**

* `profileID` - Integer type. PDP context ID. Range: 1–3. It is usually set to `1`.
* `ipType` - Integer type. IP protocol type. See the table below for possible values:

| Value | Description   |
| ----- | ------------- |
| 0     | IPv4          |
| 1     | IPv6          |
| 2     | IPv4 and IPv6 |

- `apn` - String type. Access Point Name. It can be null, in which case it should be written as `''`. Range: 0–64. Unit: byte.

- `username` - String type. Username. It can be null, in which case it should be written as `''`. Range: 0–64. Unit: byte.

- `password` - String type. Password. It can be null, in which case it should be written as `''`. Range: 0–64. Unit: byte.

- `authType` - Integer type. APN authentication method. See the table below for possible values:

| Value | Description  |
| ----- | ------------ |
| 0     | None         |
| 1     | PAP          |
| 2     | CHAP         |
| 3     | PAP and CHAP |

**Return Value:**

`0` - Successful execution;  `-1` - Failed execution.



> For BG77 and BG95 series modules, the range of `profileID` is 1–2 in the NB network mode.
>
> Only BG77 and BG95 series modules support the value 3 of `authType` .
>
> Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95 series module.



**Example:**

```python
>>> import dataCall
>>> dataCall.setPDPContext(1, 0, '3gnet', '', '', 0)
0
```



### `dataCall.getPDPContext`

```python
dataCall.getPDPContext(profileID)
```

Gets the relevant information of the PDP context for the specified `profileID`.

**Parameter：**

- `profileID` - Integer value. PDP context ID. Range: 1–3.


**Return Value：**

Returns `-1` for failed execution and returns a tuple containing PDP context information for successful execution. The format of the tuple is as follows:

`(ipType, apn, username, password, authType)`

See the parameter of `dataCall.setPDPContext` method for the tuple parameter.



>Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95 series module.



**Example: **

```python
>>> import dataCall
>>> dataCall.getPDPContext(1)
(0, '3gnet', '', '', 0)
```



## Establish the Cellular Network Channel Automatically at Startup

### `dataCall.setAutoActivate`

```python
dataCall.setAutoActivate(profileID, enable)
```

Sets whether the PDP context for the specified `profileID` is automatically activated during startup.

**Parameter：**

- `profileID` - Integer value. PDP context ID. Range: 1–3.

- `enable` - Integer type. Controls whether the module automatically activates the PDP context during startup. `0` indicates disable and `1` indicates enable.



>If you have not called `dataCall.setAutoActivate` and `dataCall.setAutoConnect` method, then the PDP context whose `profileID` is 1 is automatically activated and reconnected at startup by default; otherwise, it is executed according to your configuration. 
>
>Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95 series module.



**Example:**

```python
>>> import dataCall
>>> dataCall.setAutoActivate(1, 0) # Disables the PDP context automatic activation feature for the PDP context whose profileID is 1. 
>>> dataCall.setAutoActivate(1, 1) # Enables the PDP context automatic activation feature for the PDP context whose profileID is 1.
```



## Automatic Reconnection

### `dataCall.setAutoConnect`

```python
dataCall.setAutoConnect(profileID, enable)
```

Enables or disables the automatic reconnection feature for the specified `profileID`. Automatic reconnection feature refers to the behavior of the module to automatically reconnect when the module disconnects from the network due to abnormal network conditions, poor signal, or other exceptional scenarios, and the network conditions return to normal.

**Parameter：**

- `profileID` - Integer value. PDP context ID. Range: 1–3.

- `enable` - Integer type. Controls whether to enable automatic reconnection. `0` indicates disable and `1` indicates enable.



> If you have not called `dataCall.setAutoActivate` and `dataCall.setAutoConnect` method, then the PDP context whose `profileID` is 1 is automatically activated and reconnected at startup by default; otherwise, it is executed according to your configuration. 
>
> Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95 series module.



**Example:**

```python
>>> import dataCall
>>> dataCall.setAutoConnect(1, 0) # Disables automatic reconnection feature for the PDP context whose profileID is 1
>>> dataCall.setAutoConnect(1, 1) # Enables automatic reconnection feature for the PDP context whose profileID is 1
```



## DNS Configuration

### `dataCall.setDNSServer`

```python
dataCall.setDNSServer(profileID, simID, priDNS, secDNS)
```

Sets the DNS server address. After establishing the cellular network channel successfully, the module will automatically obtain the DNS server address, and generally it is unnecessary to reconfigure it. If the DNS server address automatically obtained by the module is unavailable, you can reconfigure it with this method.

**Parameter：**

- `profileID` - Integer value. PDP context ID. Range: 1–3.

- `simID` - Integer type. SIM card slot number. `0` indicates SIM0; `1` indicates SIM1. Currently only `0` is supported. 

- `priDNS` - String type. Primary DNS server address.

- `secDNS` - String type. Secondary DNS server address.

**Return Value：**

`0` - Successful execution;  `-1` - Failed execution.



>Modules that support this method: 
>
>EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC200A/EC200U/EC600U/EG912U/EG915U series module.



**Example:**

```python
>>> import dataCall
>>> dataCall.setDNSServer(1, 0, "8.8.8.8", "114.114.114.114")
0
```



## Register Callback Function

### `dataCall.setCallback`

```python
dataCall.setCallback(fun)
```

Registers a callback function. When the network status changes, such as when the network is disconnected or the reconnection is successful, this callback function will be triggered to inform the user of the network status.

**Parameter：**

* `fun` - The name of the callback function. The format and parameters of the callback function is described as follows:

```python
def netCallback(args):
	pass
```

| Parameter | Type    | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ |
| args[0]   | Integer | PDP context ID, indicating which PDP network state has changed |
| args[1]   | Integer | Network status. 0 means the network is disconnected and 1 means the network is connected |

**Return Value：**

`0` - Successful execution;  `-1` - Failed execution.



> Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95 series module.
>



**Example:**

```python
import dataCall

def netCallback(args):
    pdp = args[0]
    datacallState = args[1]
    if datacallState == 0:
        print('### network {} disconnected.'.format(pdp))
    elif datacallState == 1:
        print('### network {} connected.'.format(pdp))
        
dataCall.setCallback(netCallback)
```



## Activation and Deactivation

### `dataCall.activate`

```
dataCall.activate(profileID)
```

Activates the PDP context specified by `profileID`.

**Parameter：**

- `profileID` - Integer value. PDP context ID. Range: 1–3.


**Return Value：**

`0` - Successful execution;  `-1` - Failed execution.



> The PDP context is automatically activated by the module at startup, so you don't have to activate it manually. If you have disabled the automatic PDP context activation feature, you need to call this method to activate the PDP context.
>
> Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95 series module.



**Example:**

```python
>>> import dataCall
>>> dataCall.setPDPContext(1, 0, '3gnet', '', '', 0) # Before activation, you should first configure the APN. Here the first APN is configured
0
>>> dataCall.activate(1) # Activate the first APN
0
```



### `dataCall.deactivate`

```
dataCall.deactivate(profileID)
```

Deactivates the PDP context specified by `profileID`.

**Parameter：**

- `profileID` - Integer value. PDP context ID. Range: 1–3.

**Return Value：**

`0` - Successful execution;  `-1` - Failed execution.



> Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95 series module.



## Cellular Network Channel Establishment Information

### `dataCall.getInfo`

```python
dataCall.getInfo(profileID, ipType)
```

Gets cellular network channel establishment information, including establishment status, IP address, DNS server address, etc.

**Parameter：**

- `profileID` - Integer value. PDP context ID. Range: 1–3.
- `ipType` - Integer type. IP protocol type. The value range is as follows:

| Value | Description   |
| ----- | ------------- |
| 0     | IPv4          |
| 1     | IPv6          |
| 2     | IPv4 and IPv6 |

**Return Value：**

Returns `-1`  for failed execution and returns a tuple containing establishment information for successful execution. See the following description:

`ipType` can be set to 0 or 1. The return value format is as follows:

`(profileID, ipType, [state, reconnect, addr, priDNS, secDNS])`

| Parameter | Type    | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ |
| profileID | Integer | PDP context ID                                               |
| ipType    | Integer | IP protocol type, with the following values:<br>0 indicates IPv4<br>1 indicates IPv6<br>2 indicates IPv4 and IPv6 |
| state     | Integer | Establishment status of IPv4 or IPv6:<br>0 indicates that the establishment has not been performed or has failed<br>1 indicates successful establishment |
| reconnect | Integer | Reconnection flag. It is a reserved parameter and is not currently used. |
| addr      | String  | The address of IPv4 or IPv6, depending on the input value of `ipType`.<br>If `ipType` is 0, `addr` is IPv4<br>If `ipType` is 1, `addr` is IPv6 |
| priDNS    | String  | Primary DNS server address                                   |
| secDNS    | String  | Secondary DNS server address                                 |

If `ipType` is set to 2, the return value format is as follows:

`(profileID, ipType, [state, reconnect, ipv4Addr, priDNS, secDNS], [state, reconnect, ipv6Addr, priDNS, secDNS])`

In the returned tuple, the first list contains IPv4 channel establishment information, and the second list contains IPv6 channel establishment information.



>The return value `(1, 0, [0, 0, '0.0.0.0', '0.0.0.0', '0.0.0.0'])` indicates that the establishment has not been performed or has failed.
>
>Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG77/BG95/BC25/BC95 series module.
>
>Since it should be compatible with the old version of `dataCall.getInfo`, the maximum value of the actual `profileID` is greater than 3, and the actual `profileID` that can be queried shall prevail.



**Example:**

```python
>>> import dataCall
>>> dataCall.getInfo(1, 0)
(1, 0, [1, 0, '10.91.44.177', '58.242.2.2', '218.104.78.2'])
```


