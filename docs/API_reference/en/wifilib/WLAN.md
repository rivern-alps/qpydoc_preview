
# WLAN - WLAN

`WLAN` contains features of WLAN control and network configuration. It provides unified management for different types of Wi-Fi modules.

> The module that currently supports this feature: EC600N series module.<br>The Wi-Fi module that currently supports this feature: ESP8266.

**Example**

Taking ESP8266 as an example, this part displays the initial use process of Wi-Fi modules in `station` mode, `ap` mode and `web` mode respectively.

**Station Mode**

```python
# In station mode, after ESP8266 connects to a Wi-Fi router, the router allocates an IP address and other information to enable the module to connect to the external network through ESP8266.
>>> from usr.WLAN import ESP8266
>>> from machine import UART


# Load ESP8266 driver and initialize the configurations.
>>> ESP8266 = ESP8266(UART.UART2, ESP8266.STA)

# Configure ESP8266 to start and connect to the Wi-Fi hotspot in station mode.
>>> ESP8266.station('wifiname','wifipassword')
0

# View the IP address of ESP8266.
>>> ESP8266.ipconfig()
 ('172.16.1.2', '255.255.255.0', '172.16.1.1', 1500, '0.0.0.0',
'0.0.0.0')

# Configure the DNS server.
>>> ESP8266.set_dns('8.8.8.8','114.114.114.114')
0

# View the IP address of ESP8266 and the following information indicates the DNS server has been configured successfully.
>>> ESP8266.ipconfig()
('172.16.1.2', '255.255.255.0', '172.16.1.1', 1500, '8.8.8.8',
'114.114.114.114')

# Set ESP8266 as the default Wi-Fi module for network communication.
>>> ESP8266.set_default_NIC('172.16.1.2')
0

# Get the current status of ESP8266. 1 indicates ESP8266 has connected to the Wi-Fi router, while 2 indicates ESP8266 has not connected to the Wi-Fi router.
>>> ESP8266.status()
1

# You can start other network services and access wireless networks by ESP8266.
```



**AP Mode**

```python
# In AP mode, ESP8266 enables the AP, uses the 4G network of the module to connect to the external network, and assigns IP addresses to terminals connected to the hotspot. Then other terminals can connect to the external network.
>>> from usr.WLAN import ESP8266
>>> from machine import UART
>>> import dataCall


# Load ESP8266 driver and initialize the configurations.
>>> ESP8266 = ESP8266(UART.UART2, ESP8266.AP)

# Configure ESP8266 to start and connect to the Wi-Fi hotspot in AP mode.
>>> ESP8266.ap('wifiname','wifipassword')
0

# Get the data call information.
>>> Info = dataCall.getInfo(1,0)

# Set 4G as the default network in AP mode.
>>> ESP8266.set_default_NIC(Info[2][2])
0

# Add the route information and set ESP8266 forwarding rules.
>>> ESP8266.router_add('192.168.4.0', '255.255.255.0')
0

# Get the current status of ESP8266. 4 indicates ESP8266 has enabled AP mode.
>>> ESP8266.status()
4

# In this case, other terminal devices can connect to the AP for network access.
```



**Web Mode**

```python
# In web mode, you can use a device such as a mobile phone to connect to the Wi-Fi hotspot of ESP8266, access the web page of a browser, and configure the network information of ESP8266.
>>> from usr.WLAN import ESP8266
>>> from machine import UART


# Initialize ESP8266. The following example uses the web mode to configure the station mode. If you use the web mode to configure AP mode, set the mode field to ESP8266.AP.
>>> ESP8266 = ESP8266(UART.UART2, ESP8266.STA)

# Get the current status of ESP8266.
>>> ESP8266.status()
2

# Set hotspot information in web mode.
>>> ESP8266.web_config('admin','adminpwd')
0

# Get the current status of ESP8266. 3 indicates the web mode has been enabled and the module can access the web mode.
>>> ESP8266.status()
3

# In this case, other terminal devices can connect to the Wi-Fi hotspot for network access. Log in to the web page (192.168.4.1) to configure the network.
```


## Classes
- [class ESP8266 – ESP8266 Driver](./WLAN.ESP8266.md)