# ntptime - Network Time Protocol

This feature is used for time synchronization.

Note: You need to confirm with the carrier whether the current SIM card supports this feature.


### `ntptime.host`

```python
ntptime.host
```

Returns the current NTP server address. Default value: "ntp.aliyun.com".


### `ntptime.sethost`

```python
ntptime.sethost(host)
```

Sets NTP server address.

* Parameter

| Parameter | Type   | Description        |
| :-------- | :----- | ------------------ |
| host      | String | NTP server address |

* Return Value

0 - Successful execution

-1 - Failed execution


### `ntptime.settime`

```python
ntptime.settime(timezone=0)
```

Synchronize NTP server time.

* Parameter

| Parameter | Type | Description |
| :------- | :----- | ------------- |
| timezone | Integer | Range: -12 to 12. Default value: 0. |

* Return Value

0 - Successful execution

-1 - Failed execution



**Example**

```python
import ntptime
import log
import utime
import checkNet


'''
The following two global variables are required. You can modify the values of the following two global variables according to your actual projects.
'''
PROJECT_NAME = "QuecPython_NTP_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Set the log output level.
log.basicConfig(level=log.INFO)
ntp_log = log.getLogger("NtpTime")

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        ntp_log.info('Network connection successful!')

        # View the default NTP server address.
        ntp_log.info(ntptime.host)
        # Set NTP server address.
        ntptime.sethost('pool.ntp.org')

        # Synchronize NTP server time.
        ntptime.settime()
    else:
        ntp_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```