# pm - Power Management

When there is no service being processed, the system is in the sleep status and enters a low-power mode.

**Example**

Only for simulation tests. Please use the feature according to business scenarios in actual development.

```python
import pm
import utime

# Creates a wakelock
lpm_fd = pm.create_wakelock("test_lock", len("test_lock"))
# Sets the automatic sleep mode
pm.autosleep(1)

# Only for simulation tests. Please use the feature according to business scenarios in actual development.
while 1:
    utime.sleep(20)  # Sleep
    res = pm.wakelock_lock(lpm_fd)
    print("ql_lpm_idlelock_lock, g_c1_axi_fd = %d" %lpm_fd)
    print("unlock  sleep")
    utime.sleep(20)
    res = pm.wakelock_unlock(lpm_fd)
    print(res)
    print("ql_lpm_idlelock_unlock, g_c1_axi_fd = %d" % lpm_fd)
    num = pm.get_wakelock_num()  # Gets the number of created wakelocks.
    print(num)
```

## Create Wakelock

### `pm.create_wakelock`

```python
pm.create_wakelock(lock_name, name_size)
```

Creates a wakelock.

**Parameter**

* `lock_name` - String type. Custom lock name.
* `name_size` - Integer type. Length of `lock_name`. It is an optional parameter.

**Return Value**

The wakelock ID: Successful execution

`-1` - Failed execution

> Note: BC25 series module does not support this method.

## Delete Wakelock

### `pm.delete_wakelock`

```python
pm.delete_wakelock(lpm_fd)
```

Deletes a wakelock.

**Parameter**

* `lpm_fd` - Integer type. ID of the wakelock to be deleted.

**Return Value**

 `0` - Successful execution

Other values - Failed execution

> Note: BC25 series module does not support this method.

## Lock Wakelock

### `pm.wakelock_lock`

```python
pm.wakelock_lock(lpm_fd)
```

Sets the specified wakelock to lock status. When there is a locked wakelock, the module will not enter the low power mode.

**Parameter**

* `lpm_fd` - Integer type. ID of the wakelock to be locked.

**Return Value**

 `0` -  Successful execution

 `-1` - Failed execution

> Note: BC25 series module does not support this method.

## Release Wakelock

### `pm.wakelock_unlock`

```python
pm.wakelock_unlock(lpm_fd)
```

Releases a wakelock. Only when all wakelocks are released will the module enter the low-power mode.

**Parameter**

* `lpm_fd` - Integer type. ID of the wakelock to be released.

**Return Value**

 `0` -  Successful execution

 `-1` - Failed execution

> Note: BC25 series module does not support this method.

## Set Automatic Sleep Mode

### `pm.autosleep`

```python
pm.autosleep(sleep_flag)
```

Sets automatic sleep mode.

**Parameter**

* `sleep_flag`  - Integer type. `0` - Disable automatic sleep mode;  `1` - Enable automatic sleep mode.

**Return Value**

 `0` -  Successful execution

 `-1` - Failed execution

## Get the Number of Created Wakelocks

### `pm.get_wakelock_num`

```python
pm.get_wakelock_num()
```

Gets the number of created wakelocks.

**Return Value**

Integer type. The number of created wakelocks.

> Note: BC25 series module does not support this method.

## Set PSM Time

### `pm.set_psm_time`

```python
pm.set_psm_time(tau_uint,tau_time,act_uint,act_time)  # Sets and enables PSM <Mode 1>

pm.set_psm_time(mode)# Enables or disables PSM <Mode 2>
```

**Parameter**

* `mode` - Integer type. Whether to enable PSM.
  `0 ` - Disable PSM
  `1 ` - Enable PSM
  `2 ` - (Only for BC25 series module) Disable PSM and delete all parameters of PSM. If there is a default value, this method will reset the default value.  (Please note that if you disable PSM in this way, you must call *pm.set_psm_time(tau_uint,tau_time,act_uint,act_time)* to enable PSM, because calling *pm.set_psm_time(mode)* is relatively nonsensical when all PSM parameters are deleted.
* `tau_uint` - Integer type. Unit of TAU (T3412).

| Value of TAU Unit | Type | Description |
| ----------------- | ---- | ----------- |
| 0                 | int  | 10 minutes  |
| 1                 | int  | 1 hour      |
| 2                 | int  | 10 hours    |
| 3                 | int  | 2 seconds   |
| 4                 | int  | 30 seconds  |
| 5                 | int  | 1 minute    |
| 6                 | int  | 320 hours   |
| 7                 | int  | Disabled    |

* `tau_time` - Integer type. Periodic value of TAU (T3412).
* `act_uint` - Integer type. Unit of ATC (T3324).

| Value of ATC Unit | Type | Description |
| ----------------- | ---- | ----------- |
| 0                 | int  | 2 seconds   |
| 1                 | int  | 1 minute    |
| 2                 | int  | 6 minutes   |
| 7                 | int  | Disabled    |

* `act_time` - Integer type. Periodic value of ATC (T3324).

> The TAU and ATC actually set is the product of the unit value and the periodic value.

**Return Value**

`True ` - Successful execution
`False` - Failed execution

**Example**

```python
>>> import pm
>>> pm.set_psm_time(1,2,1,4)  # Sets the periodic TAU request to 2 hours (1 hour * 2 = 2 hours) and ATC request to 4 minutes (1 minute * 4 = 4 minutes).
True
>>>
```

> Only BC25/ECX00U/ECX00E series module supports this method.

## Get PSM Time

### `pm.get_psm_time`

```python
pm.get_psm_time()
```

**Return Value**

List type - Successful execution 

The parameters are described below.

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| list[0]   | int  | mode<br />0- Disable PSM. <br />1- Enable PSM. <br />2- (Only for BC25 series module) Disable PSM and delete all parameters of PSM. If there is a default value, this method will reset the default value. |
| list[1]   | int  | TAU unit                                                     |
| list[2]   | int  | Periodic value of TAU                                        |
| list[3]   | int  | ACT unit                                                     |
| list[4]   | int  | Periodic value of ACT                                        |

 `None` - Failed execution

**Example**

```python
>>> pm.get_psm_time()

[1, 1, 1, 1, 2]


```

> Only BC25/ECX00U/ECX00E series module supports this method.
