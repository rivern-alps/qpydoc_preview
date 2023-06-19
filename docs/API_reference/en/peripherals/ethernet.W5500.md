# class W5500 - W5500 Ethernet NIC Control

This class controls Ethernet NIC devices of `W5500`.

> Currently, only EC600N and EC600U module series support this feature.


## Constructor

### `ethernet.W5500`

```python
class ethernet.W5500(mac, ip='', subnet='', gateway='', spi_port=-1, spi_cs_pin=-1, extint_pin=-1, reset_pin=-1, work_mode=0)
```

Loads W5500 driver, initializes W5500 Ethernet NIC and returns W5500 NIC object.   

**Parameter:**

- `mac` - Byte stream. MAC address with a length of 6 bytes.
- `ip` -  IP address of Ethernet NIC. The default value is an empty string'', indicating that the default IP address is `192.168.1.100` in the program.  
- `subnet` - Subnet mask address of Ethernet NIC. The default value is an empty string'', indicating that `255.255.255.0` is used as the subnet mask.
- `gateway` - Gateway address of Ethernet NIC. The default value is an empty string'', indicating that the last bit of IP address is replaced with `1` as the gateway address.
- `spi_port` - Connect to [SPI port](./machine.SPI.md) of `W5500`. The default value is `-1`, indicating that the last configured value is used and the default configuration in the program is `SPI1` port.
- `spi_cs_pin` - Connect to `SPI` chip select [GPIO pin](./machine.Pin.md) of `W5500`. The default value is `-1`, indicating that the last configured value is used and the default configuration in the program is `Pin.GPIO34`.
- `extint_pin` - Connect to external interrupt [GPIO pin](./machine.Pin.md) of `W5500`. The default value is `-1`, indicating that the last configured value is used and the default configuration in the program is `Pin.GPIO19`.
- `reset_pin` - Connect to reset [GPIO pin](./machine.Pin.md) of `W5500`. The default value is `-1`, indicating that the last configured value is used and the default configuration in the program is `Pin.GPIO17`.
- `work_mode` - Configure Ethernet working mode. The default mode is terminal mode. `0` and `1` respectively represents terminal mode and gateway mode. Terminal mode indicates that the module is used as a terminal device to connect to a network supply device to access the network. Gateway mode indicates that the module is used as a gateway to provide network access for external devices through LTE network.

## Methods 

### `W5500.set_addr`
```python
nic.set_addr(ip, subnet, gateway)
```

Configures NIC static IP Address.

**Parameter:**

- `ip` -  IP address of Ethernet NIC. The value is an empty string'', indicating that the default IP address is `192.168.1.100` in the program.  
- `subnet` - Subnet mask address of Ethernet NIC. The value is an empty string'', indicating that `255.255.255.0` is used as the subnet mask.
- `gateway` - Gateway address of Ethernet NIC. The value is an empty string'', indicating that the last bit of IP address is replaced with `1` as the gateway address.

**Return Value:**   

0 - Successful execution

Other values - Failed execution

* Example

```python
nic.set_addr('192.168.1.100', '', '')
```

### `W5500.set_dns`

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

### `W5500.set_up`

```python
nic.set_up()
```

Enables NIC and then NIC processes network interfaces and messages normally.

### `W5500.set_down`

```python
nic.set_down()
```

Disables NIC and then NIC no longer processes network interfaces and messages.

### `W5500.dhcp`

```python
nic.dhcp()
```

Obtains dynamic IP. This method is used in the terminal mode so that IP information can be automatically obtained.

**Return Value:**   

0 - Successful execution

Other values - Failed execution

### `W5500.ipconfig`

```python
nic.ipconfig()
```

Obtains NIC network information. MAC address, host name, IP address type, IP address, subnet mask, gateway address and DNS server address can be obtained through this method.

**Return Value:**   

List type.

The format is as follows:

 [(mac, hostname), (iptype, ip, subnet, gateway, primary_dns，secondary_dns)].  

|  Parameter  | Type | Description |
| ---- | ---- |---------- |
| `mac`    | `str` | `mac` address and the format is`'XX-XX-XX-XX-XX-XX'`. |
| `hostname`| `str` | NIC name |
| `iptype`  | `str` | `ip` type. `4` indicates `IPv4` and `6` indicates `IPv6`. Currently, only `IPv4` is supported. |
| `ip`     | `str` | IP address |
| `subnet` | `str` | Subnet mask |
| `gateway`| `str` | Gateway address |
| `primary_dns`| `str` | Primary address of DNS server |
| `secondary_dns`| `str` | Secondary address of DNS server |

### `W5500.set_default_NIC`

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
