# class CH395 - CH395 Ethernet NIC Control

This class controls Ethernet NIC devices of `CH395`.

> Currently, only EC600N module series support this feature.

## Constructor

### `ethernet.CH395`

```python
class ethernet.CH395(mac, ip='', subnet='', gateway='', spi_port=-1, spi_cs_pin=-1, extint_pin=-1, reset_pin=-1, work_mode=0)
```

Loads CH395 driver, initializes CH395 Ethernet NIC and returns CH395 NIC object.   

**Parameter:**

- `mac` - Byte stream. MAC address with a length of 6 bytes.
- `ip` - IP address of Ethernet NIC. The default value is an empty string'', indicating that the default IP address is `192.168.1.100` in the program.  
- `subnet` - Subnet mask address of Ethernet NIC. The default value is an empty string'', indicating that `255.255.255.0` is used as the subnet mask.
- `gateway` - Gateway address of Ethernet NIC. The default value is an empty string'', indicating that the last bit of IP address is replaced with `1` as the gateway address.
- `spi_port` - Connect to [SPI port](./machine.SPI.md) of `CH395`. The default value is `-1`, indicating that the last configured value is used and the default configuration in the program is `SPI1` port.
- `spi_cs_pin` - Connect to `SPI` chip select [GPIO pin](./machine.Pin.md) of `CH395`. The default value is `-1`, indicating that the last configured value is used and the default configuration in the program is `Pin.GPIO4`.
- `extint_pin` - Connect to external interrupt [GPIO pin](./machine.Pin.md) of `CH395`. The default value is `-1`, indicating that the last configured value is used and the default configuration in the program is `Pin.GPIO24`.
- `reset_pin` - Connect to reset [GPIO pin](./machine.Pin.md) of `CH395`. It indicates that the last configured value is used and the default configuration in the program is  `Pin.GPIO30`.
- `work_mode` - Configure Ethernet working mode. The default mode is terminal mode. `0` and `1` respectively represents terminal mode and gateway mode. Terminal mode indicates that the module is used as a terminal device to connect to a network supply device to access the network. Gateway mode indicates that the module is used as a gateway to provide network access for external devices through LTE network.

## Methods

### `CH395.set_addr`
```python
nic.set_addr(ip, subnet, gateway)
```

Configures NIC static IP Address.

**Parameter:**

- `ip` - IP address of Ethernet NIC. The value is an empty string'', indicating that the default IP address is `192.168.1.100` in the program. 
- `subnet` - Subnet mask address of Ethernet NIC. The value is an empty string'', indicating that `255.255.255.0` is used as the subnet mask.
- `gateway` - Gateway address of Ethernet NIC. The value is an empty string'', indicating that the last bit of IP address is replaced with `1` as the gateway address.

**Return Value:**   

0 - Successful execution

Other values - Failed execution

* Example

```python
nic.set_addr('192.168.1.100', '', '')
```

### `CH395.set_dns`

```python
nic.set_dns(primary_dns, secondary_dns)
```

Configures NIC DNS server.

**Parameter:**

- `primary_dns` - Primary address of `DNS` server.
- `secondary_dns` - Secondary address of `DNS` server.

**Return Value:**   

0 - Successful execution

Other values - Failed execution

**Example:** 

```python
nic.set_dns('8.8.8.8', '114.114.114.114')
```

### `CH395.set_up`

```python
nic.set_up()
```

Enables NIC and then NIC processes network interfaces and messages normally.

### `CH395.set_down`

```python
nic.set_down()
```

Disables NIC and then NIC no longer processes network interfaces and messages.

### `CH395.dhcp`

```python
nic.dhcp()
```

Obtains dynamic IP. This method is used in the terminal mode so that IP information can be automatically obtained.

**Return Value:**   

0 - Successful execution

Other values - Failed execution

### `CH395.ipconfig`

```python
nic.ipconfig()
```

Obtains NIC network information. MAC address, host name, IP address type, IP address, subnet mask, gateway address and DNS server address can be obtained through this method.

**Return Value:**   

Returns list type.

The format is as follows:

[(mac, hostname), (iptype, ip, subnet, gateway, primary_dns，secondary_dns)].  

| Parameter | Type | Description |
| ---- | ---- |---------- |
| `mac`    | `str` | `mac` address and the format is`'XX-XX-XX-XX-XX-XX'`. |
| `hostname`| `str` | NIC name |
| `iptype`  | `str` | `ip` type. `4` indicates `IPv4` and `6` indicates `IPv6`. Currently, only `IPv4` is supported. |
| `ip`     | `str` | IP address |
| `subnet` | `str` | Subnet mask |
| `gateway`| `str` | Gateway address |
| `primary_dns`| `str` | Primary address of DNS server      |
| `secondary_dns`| `str` | Secondary address of DNS server |

### `CH395.set_default_NIC`

```python
nic.set_default_NIC(ip)
```

Configures the default NIC.

**Parameter:**

- `ip` - Default NIC IP address.

**Return Value:**   

0 - Successful execution

Other values - Failed execution

**Example:** 

```python
nic.set_default_NIC('192.168.1.100')
```

### `CH395.status`

```python
nic.status()
```

Obtains NIC current status.

**Return Value:**   

Tuple type.

The format is as follows: 

(dev, active, link).

| Parameter | Type | Description |
| ---- | ---- |---------- |
| `dev`   | `bool` | Whether NIC device is normally connected. `True` and `False` respectively indicate that NIC device is connected and is not connected. |
| `active`| `bool` | Whether NIC is activated. `True` and `False` respectively indicate enable and disable, which correspond to `set_up` and `set_down`. |
| `link`  | `bool` | Whether the network cable of NIC is connected. `True` and `False` respectively indicate the network cable is connected and is not connected. |