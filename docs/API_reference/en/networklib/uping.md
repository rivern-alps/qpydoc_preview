# class uping - Ping Package

This class pings IPv4 request packages.

> Note: 1. It may occur that the socket cannot be set up at the host address, causing a connection error. 2. Determine the ping period by initializing `COUNT` and `INTERVAL`.

**Example**

```python
# Mode 1
# Print the output mode.
import uping
uping.ping('baidu.com')

# The following lists the output of uping.start(), without return values.
#72 bytes from 49.49.48.46: icmp_seq=1, ttl=53, time=1169.909000 ms
#72 bytes from 49.49.48.46: icmp_seq=2, ttl=53, time=92.060000 ms
#72 bytes from 49.49.48.46: icmp_seq=3, ttl=53, time=94.818000 ms
#72 bytes from 49.49.48.46: icmp_seq=4, ttl=53, time=114.879000 ms
#4 packets transmitted, 4 packets received, 0 packet loss
#round-trip min/avg/max = 92.06000000000001/367.916/1169.909 ms


# Mode 2
# Set quiet to get the output.
import uping
result = uping.ping('baidu.com', quiet=True)
# The corresponding data can be gotten in the result.
# result(tx=4, rx=4, losses=0, min=76.93899999999999, avg=131.348, max=226.697)
```

## Constructor

### `uping.ping`

```python
uping.ping(HOST, SOURCE=None, COUNT=4, INTERVAL=1000, SIZE=64, TIMEOUT=5000, quiet=False)
```

Pings packages periodically.

**Parameter**

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| HOST      | str  | The IP address to be pinged, such as "baidu.com".            |
| SOURCE    | str  | Source IP address, used for binding and with no need for input. |
| COUNT     | int  | Default value: 4. Unit: time.                                |
| INTERVAL  | int  | Interval. Default value: 1000. Unit: ms.                     |
| SIZE      | int  | Size of the package read every time. Default value: 64. Unit: byte. No change is required. |
| TIMEOUT   | int  | Timeout. Default value: 5000. Unit: ms.                      |
| quiet     | bool | False: print and output directly. <br />True: The default value printed by *start* is converted to an object and returned.<br />Default: false. |

