# class YT8512H - YT8512H PHY Control

This class controls Ethernet NIC devices of `YT8512H and SZ18201`.

> Currently, only EC600A module series support this feature.

## Constructor

### `ethernet.YT8512H`

```python
class ethernet.YT8512H(mac, ip='', subnet='', gateway='')
```

Loads YT8512H driver, initializes YT8512H phy device and returns YT8512H NIC object.   

**Parameter:**

- `mac` - Byte stream. MAC address with a length of 6 bytes.
- `ip` - IP address of Ethernet NIC. The default value is an empty string'', indicating that the default IP address is `192.168.1.100` in the program. 
- `subnet` - Subnet mask address of Ethernet NIC. The default value is an empty string'', indicating that `255.255.255.0` is used as the subnet mask.
- `gateway` - Gateway address of Ethernet NIC. The default value is an empty string'', indicating that the last bit of IP address is replaced with `1` as the gateway address.

## Methods 

### `YT8512H.set_addr`
```python
nic.set_addr(ip, subnet, gateway)
```

Configures NIC static IP Address.

**Parameter:**

- `ip` - `ip` address of Ethernet NIC. The value is an empty string'', indicating that the default IP address is `192.168.1.100` in the program. 
- `subnet` - Subnet mask address of Ethernet NIC. The value is an empty string'', indicating that `255.255.255.0` is used as the subnet mask.
- `gateway` - Gateway address of Ethernet NIC. The value is an empty string'', indicating that the last bit of IP address is replaced with `1` as the gateway address.

**Return Value:**   

0 - Successful execution

Other values - Failed execution

* Example

```python
nic.set_addr('192.168.1.100', '', '')
```

### `YT8512H.set_dns`

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

### `YT8512H.set_up`

```python
nic.set_up()
```

Enables NIC and then NIC processes network interfaces and messages normally.

### `YT8512H.set_down`

```python
nic.set_down()
```

Disables NIC and then NIC no longer processes network interfaces and messages.

### `YT8512H.dhcp`

```python
nic.dhcp()
```

Obtains dynamic IP. This method is used in the terminal mode so that IP information can be automatically obtained.

**Return Value:**   

0 - Successful execution

Other values - Failed execution

### `YT8512H.ipconfig`

```python
nic.ipconfig()
```

Obtains NIC network information. MAC address, host name, IP address type, IP address, subnet mask, gateway address and DNS server address can be obtained through this method.

**Return Value:**   

List type.

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
| `primary_dns`| `str` | Primary address of DNS server |
| `secondary_dns`| `str` | Secondary address of DNS server |

### `YT8512H.set_default_NIC`

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

### `YT8512H.status`

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
