# class CH395 - CH395以太网卡控制

该类用于控制`CH395`型号以太网网卡设备。

> 当前仅支持EC600U系列

## 构造函数

### `ethernet.CH395`

```python
class ethernet.CH395(mac, ip='', subnet='', gateway='', spi_port=-1, spi_cs_pin=-1, extint_pin=-1, reset_pin=-1, work_mode=0)
```

加载CH395驱动，初始化CH395以太网卡，并返回CH395网卡对象。

**参数描述：**

- `mac` - 字节流，6字节长度的 `mac` 地址。
- `ip` - 以太网卡的 `ip` 地址，若值为空字符串''，表示使用默认值`192.168.1.100`。
- `subnet` - 以太网卡的子网掩码地址，若值为空字符串''，表示使用默认值`255.255.255.0`。
- `gateway` - 以太网卡的网关地址，若值为空字符串''，表示将 `ip` 地址的最后一位替换成`1`作为网关。
- `spi_port` - 连接`CH395`的[SPI端口](./machine.SPI.md)，默认值为`-1`，表示使用上次配置的值，程序中默认配置为了 `SPI1` 端口。
- `spi_cs_pin` - 连接`CH395`的 `SPI` 片选[GPIO管脚](./machine.Pin.md)，默认值为`-1`，表示使用上次配置的值，程序中默认配置为了 `Pin.GPIO4`。
- `extint_pin` - 连接`CH395`的外部中断[GPIO管脚](./machine.Pin.md)，默认值为`-1`，表示上次配置的值，程序中默认配置为 `Pin.GPIO24`。
- `reset_pin` - 连接`CH395`的重置[GPIO管脚](./machine.Pin.md), 表示上次配置的值，程序中默认配置为 `Pin.GPIO30`。
- `work_mode` - 以太网工作模式配置，默认为终端模式，`0`/`1` 分别表示终端模式/网关模式。终端模式表示该模块作为终端设备连接供网设备上网。网关模式表示该模块作为网关，为外部设备提供网络访问，通过`4G`上网。

## 方法

### `CH395.set_addr`
```python
nic.set_addr(ip, subnet, gateway)
```

网卡静态ip地址配置。

**参数描述：**

- `ip` - 以太网卡的 `ip` 地址，若值为空字符串''，表示使用默认值`192.168.1.100`。
- `subnet` - 以太网卡的子网掩码地址，若值为空字符串''，表示使用默认值`255.255.255.0`。
- `gateway` - 以太网卡的网关地址，若值为空字符串''，表示将 `ip` 地址的最后一位替换成`1`作为网关。

**返回值描述：**   

成功返回整型值0，失败返回整型值-1。

**示例：**

```python
nic.set_addr('192.168.1.100', '', '')
```

### `CH395.set_dns`

```python
nic.set_dns(primary_dns, secondary_dns)
```

网卡dns服务器配置。

**参数描述：**

- `primary_dns` - `DNS`服务器主地址。
- `secondary_dns` - `DNS`服务器辅地址。

**返回值描述：**   

成功返回整型值0，失败返回整型值-1。

**示例：** 

```python
nic.set_dns('8.8.8.8', '114.114.114.114')
```

### `CH395.set_up`

```python
nic.set_up()
```

网卡启动，启动后网卡正常处理网口网络报文。

**返回值描述：**   

成功返回整型值0，失败返回整型值-1。

### `CH395.set_down`

```python
nic.set_down()
```

网卡禁用，禁用后网卡不再处理网口网络报文。

**返回值描述：**   

成功返回整型值0，失败返回整型值-1。

### `CH395.dhcp`

```python
nic.dhcp()
```

动态ip获取，此方法是作为终端模式下使用，从而自动获取ip信息。

**返回值描述：**   

成功返回整型值0，失败返回整型值-1。

### `CH395.ipconfig`

```python
nic.ipconfig()
```

获取网卡网络信息，通过该方法获取到mac地址、主机名、IP地址类型、IP地址、子网掩码、网关地址和DNS服务器地址。

**返回值描述：**   

返回list类型。

格式如下:  
[(mac, hostname), (iptype, ip, subnet, gateway, primary_dns，secondary_dns)]  

|  参数   | 类型  | 说明 |
| ---- | ---- |---------- |
| `mac`    | `str` | `mac`地址,格式为`'XX-XX-XX-XX-XX-XX'` |
| `hostname`| `str` | 网卡名称 |
| `iptype`  | `str` | `ip`类型，`4`表示`ipv4`，`6`表示`ipv6`，目前仅支持`ip4` |
| `ip`     | `str` | `ip`地址 |
| `subnet` | `str` | 子网掩码 |
| `gateway`| `str` | 网关 |
| `primary_dns`| `str` | DNS服务器主地址 |
| `secondary_dns`| `str` | DNS服务器辅地址 |

### `CH395.set_default_NIC`

```python
nic.set_default_NIC(ip)
```

默认网卡配置。

**参数描述：**

- `ip` - 默认网卡ip地址。

**返回值描述：**   

成功返回整型值0，失败返回整型值-1。

**示例：** 

```python
nic.set_default_NIC('192.168.1.100')
```

### `CH395.status`

```python
nic.status()
```

获取网卡当前状态。

**返回值描述：**   

返回tuble类型。

格式内容如下:  
(dev, active, link)

|  参数   | 类型  | 说明 |
| ---- | ---- |---------- |
| `dev`   | `bool` | 表示网卡设备是否连接正常，`True`/`False`表示有连接/未连接 |
| `active`| `bool` | 表示网卡是否激活使用，`True`/`False`表示启用/禁用，与`set_up`/`set_down`对应 |
| `link`  | `bool` | 表示网卡网线是否连接，`True`/`False`表示已连接/未连接 |