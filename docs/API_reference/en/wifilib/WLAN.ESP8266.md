
# class ESP8266 - Control ESP8266

This class controls `ESP8266`.

## Constructor

### `ESP8266`

```python
class ESP8266(uart=UART.UART1, mod=ESP8266.STA， callback=None)
```

Load ESP8266 driver, initialize the virtual Wi-Fi module and return the ESP8266 object.

**Parameter**

- `uart` - Module UART option, indicating the `UART ID` that the module connects to ESP8266. Default: `UART1`.
- `mode` - The working mode of the Wi-Fi module, which specifies the `working mode` of ESP8266. The working mode of station mode is ESP8266.STA, while the working mode of AP mode is ESP8266.AP. Default: `Station ` mode.
- `callback` - Enable or disable the callback function, used for the notifications of `network changes` and `OTA upgrades`.  Default: disable.

**callback Parameter**

- `content` - The reported content.

**The Reported Content**

Once the callback function is enabled, the module will report the notifications when an OTA upgrade occurs and the network connectio mode changes in `station` mode.

Report `ota` information:
- `ota,begin` - OTA upgrade starts.
- `ota,downloading,xx` - Percentage of OTA upgrade.
- `ota,restart` - Reboot after the OTA upgrade is completed.
- `ota,err_code,x` - OTA upgrade error code.
    - `1` - Failed to analyze the URL
    - `2` - Failed to connect to the HTTP server
    - `3` - Failed to allocate memory for a GET request 
    - `4` - Failed to send a GET request to the server
    - `5` - An error occurred when the OTA upgrade started
    - `6` - Failed to receive data
    - `7` - Failed to write OTA upgrade files
    - `8` - An error occurred when the OTA upgrade ended
    - `9` - Failed to set boot partition

Report the network connection change in `station` mode:
- `station, connected` - The Wi-Fi has been connected.
- `station, disconnected` - The Wi-Fi has been disconnected.

**Example**

```python
# callback Example
from usr.WLAN import ESP8266
from machine import UART

def cb(args):
    content = args
    print('wifi content:{}'.format(content))

ESP8266 = ESP8266(UART.UART2, ESP8266.STA, cb)

```


## Method

### `ESP8266.status`

```python
ESP8266.status()
```

Gets the Wi-Fi module status to determine the current working mode of the Wi-Fi module.

**Return Value**

Integer type. The enumerations are as follows.
- `0` - ESP8266 does not exist.
- `1` - ESP8266 station mode has been connected.
- `2` - ESP8266 station mode has not been connected.
- `3` - ESP8266 web mode
- `4` - ESP8266 AP mode
- `5` - ESP8266 OTA upgrading




### `ESP8266.version`

```python
ESP8266.version()
```

Gets the current firmware information of the Wi-Fi module.

**Return Value**

String type. Format: (sdk, model, version, time).
- `sdk` - SDK information
- `model` - Wi-Fi module model
- `version` - Version number
- `time` - Version time



### `ESP8266.ipconfig`

```python
ESP8266.ipconfig()
```

Gets the current network configuration of the Wi-Fi module, including the IP address and DNS server.

**Return Value**

A Tuple (ip, subnet, gateway, mtu, primary_dns, secondary_dns).

- `ip` - IP address
- `subnet` - Subnet mask
- `gateway` - Gateway address
- `mtu` - Maximum transmission unit
- `primary_dns` - IP address of the primary DNS server 
- `secondary_dns` - IP address of the secondary DNS server 



### `ESP8266.station`

```python
ESP8266.station(username，password)
```

Enables the Wi-Fi module to work in `station` mode to connect to a specified Wi-Fi router.

**Parameter**

- `username` - Name of the Wi-Fi to be connected. Range: 1–32 characters.
- `password` - Password of the Wi-Fi to be connected. Range: 8–64 characters.

**Return Value**

`0` - Successful execution

Other values - Failed execution



### `ESP8266.ap`

```python
ESP8266.ap(username，password)
```

Enables the Wi-Fi module to work in `ap` mode as an AP.

**Parameter**

- `username` - Name of the `Wi-Fi hotspot`. Range: 1–32 characters.
- `password` - Password of the `Wi-Fi hotspot`. Range: 8–64 characters.

**Return Value**

`0` - Successful execution

Other values - Failed execution



### `ESP8266.web_config`

```python
ESP8266.web_config(username，password)
```

Enables the Wi-Fi module to work in `web` mode. You can configure the network on the web page.

> Note: After enabling the network configuration, use a terminal device such as a mobile phone or computer to connect to a Wi-Fi module (with a custom name and password) over a wireless network. Then enter 192.168.4.1 in the browser to access the web page.

**Parameter**

- `username` - Name of the `web hotspot`. Range: 1–32 characters.
- `password` - Password of the `web hotspot`. Range: 8–64 characters.

**Return Value**

`0` - Successful execution

Other values - Failed execution



### `ESP8266.ota`

```python
ESP8266.ota(url)
```

Updates the firmware after an `OTA upgrade` is enabled.

> Note: Only when the module is in station mode can the module be upgraded over the air. In the OTA upgrade process, you can only query the current status rather than perform any other operation.

**Parameter**

- `url` - The URL of firmware download. Only HTTP is supported currently. Length: up to 256 bytes.

**Return Value**

`0` - Successful execution

Other values - Failed execution

**Example**

```python

url='http://www.example.com/fota.bin'

ESP8266.ota(url)

```



### `ESP8266.stop`

```python
ESP8266.stop()
```

Releases the virtual Wi-Fi module configured for the Wi-Fi module.

**Return Value**

`0` - Successful execution

Other values - Failed execution



### `ESP8266.set_default_NIC`

```python
ESP8266.set_default_NIC(ip_str)
```

Specifies the Wi-Fi module to forward the network.

**Parameter**

- `ip_str` - String type. The IP address of the Wi-Fi module used by default to forward network data, such as '192.168.1.100'.

**Return Value**

`0` - Successful execution

Other values - Failed execution



### `ESP8266.set_dns`

```python
ESP8266.set_dns(pri_dns, sec_dns)
```

Specifies the `DNS server`  of the Wi-Fi module for IP address resolution.

**Parameter**

- `pri_dns` - IP address of the `primary DNS` server. Default value:  `8.8.8.8`.
- `sec_dns` - IP address of the `secondary DNS` server. Default value: `114.114.114.114`.

**Return Value**

`0` - Successful execution

Other values - Failed execution



### `ESP8266.router_add`

```python
ESP8266.router_add(ip, mask)
```

Sets forwarding rules of the Wi-Fi module.

**Parameter**

- `ip` - IP address of the Wi-Fi module in `AP` mode. Default value: 192.168.4.1.
- `mask` - Subnet mask. Default value: 255.255.255.0.

**Return Value**

`0` - Successful execution

Other values - Failed execution