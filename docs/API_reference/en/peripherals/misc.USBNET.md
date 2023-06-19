# USBNET - USB Network Card

Module feature: USB network card.

> Note: EC600S, EC600N, EC800N, EC200U, EC600U and EC600M series modules support this feature.

## Set Work Type of USB Network Card 

### `USBNET.set_worktype`

```python
USBNET.set_worktype(type)
```

**Parameter:**

- `type` - USBNET working type. Integer type. Type_ECM: ECM mode. Type_RNDIS: RNDIS mode. 

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

> Note: It takes effect after the module is rebooted.

## Get Work Type of USB Network Card 

### `USBNET.get_worktype`

```python
USBNET.get_worktype()
```

**Return Value:**

If successful, it returns current work type of USBNET. If failed, it returns integer type `-1`; `1` indicates ECM mode. `3 ` indicates RNDIS mode.

## Get USENET Current State

### `USBNET.get_status`

```python
USBNET.get_status()
```

**Return Value:**

If successful, it returns the USBNET current state. If failed, it returns the integer  `-1`; `0` indicates no  connection. `1` indicates successful connection.

## Enable USB Network Card

### `USBNET.open`

```python
USBNET.open()
```

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

## Disable USB Network Card

### `USBNET.close`

```
USBNET.close()
```

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

**Example:**

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

## Get NAT Enabling Status

### `USBNET.getNat`

```python
USBNET.getNat(simid, pid)
```

Gets NAT enabling status of a specified network card (whether IPv6 dial-up is supported).

> Note: Only EC200U and EC600U series modules support this function.

**Parameter:**

- `simid` - Integer type. Range: 0 and 1. Currently only `0` is supported. 
- `pid` - Integer type. PDP index. Range: `1-7`.

**Return Value:**

If successful, it returns NAT enable situation. Integer type: 0 and 1. `0`: Enable and IPv6 dial-up is supported.  `1`: Disable and IPv6 dial-up is not supported.

If failed, it returns integer `-1`.

**Example:**

```python
from misc import USBNET
USBNET.getNat(0, 1)
0
```

## NAT Settings

### `USBNET.setNat`

```python
USBNET.setNat(simid, pid, nat)
```

Sets NAT. After NAT is set successfully, the configuration takes effect after the module is rebooted. The nat value changes to 1 when you call *USBNET.set_worktype()*, in which case `pid` cannot perform IPv6 dial-up, thus this function can be called to disable NAT to turn IPv6 dial-up back to normal after USBNET is disabled.

> Note: Only EC200U and EC600U series modules support this function.

**Parameter:**

- `simid` - Integer type. Range: 0 and 1. Currently only `0` is supported. 
- `pid` - Integer type. PDP index. Range: `1-7`.
- `Nat` - Integer type. Range: 0 and 1. `0`: IPv6 dial-up is supported; `1`: IPv6 dial-up is not supported.

**Return Value:**

 `0` indicates successful setting. `-1` indicates setting failure.

**Example:**

```python
USBNET.setNat(0, 1, 0)
0
```

## Constants

### `USBNET.Type_ECM`

ECM mode.

### `USBNET.Type_RNDIS`

RNDIS mode.