---
title: Wi-Fi
keywords: Wi-Fi
description: Wi-Fi Development
---
# About document

**Revision history**

| **Version** | **Date** | **Author** | **Description** |
| --- | --- | --- | --- |
| 1.0.0 | 2021-07-23 | Xjin.gao | Added the debugging procedure of ESP8266 wifi chip in document. |

## Preamble

In this document, based on QuecPython structure, it mainly illustrates how to integrate ESP8266 wifi chip on EC600N module, communicate over uart by AT commands, and get access to Aliyun to handle services. 


## Explicit introduction

### About development procedure 

Before that, we should confirm the environment: 

1. Whether the EC600N module is equipped with uart function and carry out actual test. 

2. Whether the ESP8266 module can response related info normally after receiving AT commands. 

#### Test uart function on module

For more specifications, please refer to API introduction on official website: QuecPython API illustrationQuecPython class library HW-related function of machine

&amp;uart&amp;Pin

// Referential links：
[https://uart](https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=uart)
[https://Pin](https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=pin)

#### Verify ESP 8266 via AT command

Note: In this test, we ignore the specific HW and SW designs relevant to esp8266 since they are all contrived by client. Before that, you just should make sure whether the wifi chip can run smoothly. (Receive and response AT command normally). 

#### Verification procedure 

Set gpio to enable ESP8266 wifi chip 

```python
gpio_en = Pin(Pin.GPIO28, Pin.OUT, Pin.PULL_DISABLE, 0)

gpio_bat = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_DISABLE, 0)

gpio_bat.write(1)

gpio_en.write(0)
```

Create UART2-MAIN PORT object

```python
serial = UART(UART.UART2, 115200, 8, 0, 1, 0)
```

Write in AT command via serial

```python
 serial.write('AT\r\n') # "\r\n" shall be appended to standard AT command
```

Read response via serial

```python
serial.read(serial.any())
```

If it is valid to read **OK\r\n** normally, which means the uart is ok and the 8366 chip can run normally.

### Development via AT command

About development on AT command, it is preferred to refer to the official AT documentary of ESPRESSIF.

Referential link

[https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html)

Main focus

html <div align=center> 

**Basic AT commands** 

- [AT](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-at): Test AT startup.
- [AT+RST](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-rst): Restart a module.
- [AT+GMR](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-gmr): Check version information.
- [AT+CMD](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-cmd): List all AT commands and types supported in current firmware.
- [AT+GSLP](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-gslp): Enter Deep-sleep mode.
- [ATE](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-ate): Configure AT commands echoing.
- [AT+RESTORE](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-restore): Restore factory default settings of the module.
- [AT+UART_CUR](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-uartc): Current UART configuration, not saved in flash.
- [AT+UART_DEF](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-uartd): Default UART configuration, saved in flash.
- [AT+SLEEP](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-sleep): Set the sleep mode.
- [AT+SYSRAM](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-sysram): Query current remaining heap size and minimum heap size.
- [AT+SYSMSG](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-sysmsg): Query/Set System Prompt Information.
- [AT+SYSFLASH](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-sysflash): Query/Set User Partitions in Flash.
- [AT+FS](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-fs): Filesystem Operations.
- [AT+RFPOWER](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-rfpower): Query/Set RF TX Power.
- [AT+SYSROLLBACK](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-sysrollback): Roll back to the previous firmware.
- [AT+SYSTIMESTAMP](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-settime): Query/Set local time stamp.
- [AT+SYSLOG](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-syslog): Enable or disable the AT error code prompt.
- [AT+SLEEPWKCFG](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-wkcfg): Query/Set the light-sleep wakeup source and awake GPIO.
- [AT+SYSSTORE](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-sysstore): Query/Set parameter store mode.
- [AT+SYSREG](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Basic_AT_Commands.html#cmd-sysreg): Read/write the register.



**WI-FI AT commands**

- [AT+CWMODE](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-mode): Set the Wi-Fi mode (Station/SoftAP/Station+SoftAP).

- [AT+CWSTATE](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-wstate): Query the Wi-Fi state and Wi-Fi information.

- [AT+CWJAP](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-jap): Connect to an AP.

- [AT+CWRECONNCFG](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-reconncfg): Query/Set the Wi-Fi reconnecting configuration.

- [AT+CWLAPOPT](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-lapopt): Set the configuration for the command [AT+CWLAP](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-lap).

- [AT+CWLAP](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-lap): List available APs.

- [AT+CWQAP](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-qap): Disconnect from an AP.

- [AT+CWSAP](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-sap): Query/Set the configuration of an ESP SoftAP.

- [AT+CWLIF](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-lif): Obtain IP address of the station that connects to an ESP SoftAP.

- [AT+CWQIF](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-qif): Disconnect stations from an ESP SoftAP.

- [AT+CWDHCP](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-dhcp): Enable/disable DHCP.

- [AT+CWDHCPS](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-dhcps): Query/Set the IP addresses allocated by an ESP SoftAP DHCP server.

- [AT+CWAUTOCONN](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-autoc): Connect to an AP automatically when powered on.

- [AT+CWAPPROTO](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-approto): Query/Set the 802.11 b/g/n protocol standard of SoftAP mode.

- [AT+CWSTAPROTO](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-staproto): Query/Set the 802.11 b/g/n protocol standard of station mode.

- [AT+CIPSTAMAC](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-stamac): Query/Set the MAC address of an ESP station.

- [AT+CIPAPMAC](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-apmac): Query/Set the MAC address of an ESP SoftAP.

- [AT+CIPSTA](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-ipsta): Query/Set the IP address of an ESP station.

- [AT+CIPAP](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-ipap): Query/Set the IP address of an ESP SoftAP.

- [AT+CWSTARTSMART](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-starts): Start SmartConfig.

- [AT+CWSTOPSMART](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-stops): Stop SmartConfig.

- [AT+WPS](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-wps): Enable the WPS function.

- [AT+MDNS](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-mdns): Configure the mDNS function.

- [AT+CWJEAP](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-jeap): Connect to a WPA2 Enterprise AP.

- [AT+CWHOSTNAME](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-hostname): Query/Set the host name of an ESP station.

- [AT+CWCOUNTRY](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-country): Query/Set the Wi-Fi Country Code.

  

**TCP/IP AT commands**

- [AT+CIPV6](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-ipv6): Enable/disable the network of Internet Protocol Version 6 (IPv6).
- [AT+CIPSTATE](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-ipstate): Obtain the TCP/UDP/SSL connection information.
- [AT+CIPSTATUS (deprecated)](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-status): Obtain the TCP/UDP/SSL connection status and information.
- [AT+CIPDOMAIN](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-domain): Resolve a Domain Name.
- [AT+CIPSTART](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-start): Establish TCP connection, UDP transmission, or SSL connection.
- [AT+CIPSTARTEX](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-startex): Establish TCP connection, UDP transmission, or SSL connection with an automatically assigned ID.
- [[Data Mode Only\] +++](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-plus): Exit from the [data mode](https://docs.espressif.com/projects/esp-at/en/latest/index_of_abbreviations.html#term-data-mode).
- [AT+CIPSEND](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-send): Send data in the [normal transmission mode](https://docs.espressif.com/projects/esp-at/en/latest/index_of_abbreviations.html#term-normal-transmission-mode) or Wi-Fi [normal transmission mode](https://docs.espressif.com/projects/esp-at/en/latest/index_of_abbreviations.html#term-normal-transmission-mode).
- [AT+CIPSENDL](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sendl): Send long data in parallel in the [normal transmission mode](https://docs.espressif.com/projects/esp-at/en/latest/index_of_abbreviations.html#term-normal-transmission-mode).
- [AT+CIPSENDLCFG](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sendlcfg): Set the configuration for the command [AT+CIPSENDL](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sendl).
- [AT+CIPSENDEX](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sendex): Send data in the [normal transmission mode](https://docs.espressif.com/projects/esp-at/en/latest/index_of_abbreviations.html#term-normal-transmission-mode) in expanded ways.
- [AT+CIPCLOSE](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-close): Close TCP/UDP/SSL connection.
- [AT+CIFSR](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-ifsr): Obtain the local IP address and MAC address.
- [AT+CIPMUX](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-mux): Enable/disable the multiple connections mode.
- [AT+CIPSERVER](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-server): Delete/create a TCP/SSL server.
- [AT+CIPSERVERMAXCONN](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-servermax): Query/Set the maximum connections allowed by a server.
- [AT+CIPMODE](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-ipmode): Query/Set the transmission mode.
- [AT+SAVETRANSLINK](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-savet): Set whether to enter Wi-Fi [normal transmission mode](https://docs.espressif.com/projects/esp-at/en/latest/index_of_abbreviations.html#term-normal-transmission-mode) on power-up.
- [AT+CIPSTO](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sto): Query/Set the local TCP Server Timeout.
- [AT+CIPSNTPCFG](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sntpcfg): Query/Set the time zone and SNTP server.
- [AT+CIPSNTPTIME](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sntpt): Query the SNTP time.
- [AT+CIPSNTPINTV](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sntpintv): Query/Set the SNTP time synchronization interval.
- [AT+CIUPDATE](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-update): Upgrade the firmware through Wi-Fi.
- [AT+CIPDINFO](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-ipdinfo): Set “+IPD” message mode.
- [AT+CIPSSLCCONF](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sslcconf): Query/Set SSL clients.
- [AT+CIPSSLCCN](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sslccn): Query/Set the Common Name of the SSL client.
- [AT+CIPSSLCSNI](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sslcsni): Query/Set SSL client Server Name Indication (SNI).
- [AT+CIPSSLCALPN](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sslcalpn): Query/Set SSL client Application Layer Protocol Negotiation (ALPN).
- [AT+CIPSSLCPSK](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-sslcpsk): Query/Set SSL client Pre-shared Key (PSK).
- [AT+CIPRECONNINTV](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-autoconnint): Query/Set the TCP/UDP/SSL reconnection interval for the Wi-Fi [normal transmission mode](https://docs.espressif.com/projects/esp-at/en/latest/index_of_abbreviations.html#term-normal-transmission-mode).
- [AT+CIPRECVMODE](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-ciprecvmode): Query/Set socket receiving mode.
- [AT+CIPRECVDATA](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-ciprecvdata): Obtain socket data in passive receiving mode.
- [AT+CIPRECVLEN](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-ciprecvlen): Obtain socket data length in passive receiving mode.
- [AT+PING](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-cipping): Ping the remote host.
- [AT+CIPDNS](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-dns): Query/Set DNS server information.
- [AT+CIPTCPOPT](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/TCP-IP_AT_Commands.html#cmd-tcpopt): Query/Set the socket options.

> Currently, not all of these AT commands are fulfilled except that connecting to Aliyun. 

**Two ways are available to fulfill AT command** 

 **1. Set AT command in a normal way** **(Features: Relatively fixed and uniform when returning)**

For such AT command, we can handle unitedly via at_command. After receiving string as "ok" and returning 0, it means the execution is a success. 

def at_command (self, cmd=&quot;AT&quot;, TIMEOUT=30, CNT_WHITES_LIMIT=10):

Just input corresponding AT commands. 

**2. In terms of some special AT commands, we should judge the return separately. ：**

client_getaddrinfo // Resolute dns. It will return corresponding IP address directly when returning OK at the same time. 

client_connect // Connect to the server. Please bear in mind that certain latency shall be added when waiting for the successful connection.

client_recv // Receive the returned data of server, currently, only the data format with +IPD:--size--,--msg— can be identified. As for others, please handle it individually. 

client_send // Send data by module. However, we should carry out separately. Firstly, we should send **size** via AT command **AT+CIPSEND=\&lt;length\&gt**. Once it returns "ok" and  &quot;\&gt;" , input concrete contents. 

The current situation:  It is demanded to input data by API, as for **len**, you can handle it interiorly. 

The development of all AT commands should be in accord with the input & response of official document. In addition, there is a need to test the return value in multiple scenarios of esp8266, after that, the return can be confirmed since the result will output only when there exists latency for some AT commands. 

The main reason: When handling one AT command, the result can be returned only when complete AT command is executed; otherwise, the next  AT command will be stuck into busy status or invalid judgment when carrying out response, consequently, leading to error.  

### MQTT API development on Aliyun 

After finishing AT commands, you can complete mqtt-related function and get connection to Aliyun server in which the corresponding services can be done. 

**Provided API currently:** 

aliyun_wifi_connect // Connect to wifi for test. When used in actual scenario, the Airkiss should be used to configure network. 

aliyun_set_wifi_mode &amp; aliyun_get_wifi_mode// Set/obtain wifi mode

aliyun_connect // When connecting to Aliyun server, you should import relevant parameters. 

aliyun_setCallback // Set callback to display the info sent by server. 

aliyun_subscribe // Subscribe topic

aliyun_publish // Publish message to related server

aliyun_disconnect // Disconnect

aliyun_start // Receive server info for one time by default. If the data is not received, it will exit (The "while" will be continuous) 

/ Never split the package since the data package should be intact when sending AT commands. As a result, the microPython umqtt is not suitable for this scheme since its data package shall be re-developed. 

Note: Till now, the connection is normally; however,whether the data package resolution is normally once the data size surpasses certain quantity. Therefore, we should confirm it in actual scenario. 

### Configure network via Airkiss

Since it does not support inputting wifi name & password manually in actual product, we should configure network via Airkiss and by which sending wifi connection parameter to device via cellphone actively.  

Referential document for configuring network via Airkiss：[https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-starts](https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/Wi-Fi_AT_Commands.html#cmd-starts)

```python
print('!******* set_wifi_mode =%s' % c.set_wifi_def_mode(1))# Set it as single STA mode and save the configuration in the flash. 
print('!******* get_wifi_mode =%s' % c.get_wifi_mode())#
print('!******* set_wifi_auto_conn  1 =%s' % c.set_wifi_auto_conn(1))#Enable power on and connect to AP actively. 
print('!******* set_wifi_start_smart 3 =%s' % c.set_wifi_start_smart(3)) # Support configuring network intellectually via ESP-Touch and Airkiss.  
# After getting wifi ssid&password, it will connect to WIFI automatically. 
utime.sleep(6)
print('!******* set_wifi_stop_smart  =%s' % c.set_wifi_stop_smart())# There is a need to release the memory occupied by Quick Connection no matter the configuration is a success or not. 
print('!******* get_wifi_status  =%s' % c.get_AP_connected_info())# Get the connected wifi info currently 

```

When configuring network via Airkiss, the wifi module shall be set as single STA mode. While executing *set_wifi_start_smart*, stopping smart is also necessary release resource correspondingly. 

It is available to set as auto-connect  or get access to wifi via decoding the wifi parameter received by smart and calling the *aliyun_wifi_connect*.

When configuring, the module should get into the smart to receive beforehand. After that, match by cellphone. In addition, certain time should be left for smart to receive. 

