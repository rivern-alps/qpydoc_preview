# USBNET - USB网卡功能

 提供USB网卡功能。

> EC600S/EC600N/EC800N/EC200U/EC600U/EC600M系列支持该功能。

## 设置USB网卡工作类型

### `USBNET.set_worktype`

```python
USBNET.set_worktype(type)
```

**参数描述：**

- `type`-USBNET 工作类型，int类型，Type_ECM：ECM模式, Type_RNDIS：RNDIS模式。

**返回值描述：**

`0`表示设置成功，`-1`表示设置失败。

> 重启生效

## 获取USB网卡工作类型

### `USBNET.get_worktype`

```python
USBNET.get_worktype()
```

**返回值描述：**

成功返回USBNET当前工作类型，失败返回整型`-1`；`1`表示ECM模式,`3 `表示 RNDIS模式。

## 获取USBNET当前状态

### `USBNET.get_status`

```python
USBNET.get_status()
```

**返回值描述：**

成功返回USBNET当前状态，失败返回整型`-1`；`0`表示未连接,`1`表示连接成功。  

## 打开USB网卡

### `USBNET.open`

```python
USBNET.open()
```

**返回值描述：**

`0`表示打开成功，`-1`表示打开失败。

## 关闭USB网卡

### `USBNET.close`

```
USBNET.close()
```

**返回值描述：**

`0`表示关闭成功，`-1`表示关闭失败。

**示例：**

```python
from misc import USBNET
from misc import Power

#work on ECM mode default
USBNET.open()

USBNET.set_worktype(USBNET.Type_RNDIS)

#reset the module
Power.powerRestart()


#After restart
from misc import USBNET

#work on RNDIS mode
USBNET.open()
```

## 获取NAT使能情况

### `USBNET.getNat`

```python
USBNET.getNat(simid, pid)
```

获取某一路网卡的NAT使能情况（是否支持ipv6拨号）。

> 仅在EC200U/EC600U系列支持

**参数描述：**

- `simid`-int类型,范围0/1，目前仅支持`0`；
- `pid`-PDP索引，int类型,范围`1-7`。

**返回值描述：**

成功：返回NAT使能情况，整型0/1，`0`：使能，支持ipv6拨号；`1`：未使能，不支持ipv6拨号。

失败：返回整型`-1`。

**示例：**

```python
from misc import USBNET
USBNET.getNat(0, 1)
0
```

## NAT设置

### `USBNET.setNat`

```python
USBNET.setNat(simid, pid, nat)
```

NAT设置，设置成功后重启生效（USBNET.set_worktype()接口调用的时候会使对应的nat值变为1，使得该pid无法IPV6拨号，所以在close USBnet后，可以使用该接口关闭NAT，使IPV6功能正常）。

> 仅在EC200U/EC600U系列支持

**参数描述：**

- `simid`-int类型,范围0/1,目前仅支持`0`；
- `pid`-PDP索引, int类型,范围`1-7`；
- `Nat`-int类型,范围：0/1,`0`：支持ipv6拨号；`1`：不支持ipv6拨号。

**返回值描述：**

`0`表示设置成功，`-1`表示设置失败。

**示例：**

```python
USBNET.setNat(0, 1, 0)
0
```

## 常量

### `USBNET.Type_ECM`

ECM工作模式

### `USBNET.Type_RNDIS`

RNDIS工作模式