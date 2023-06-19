# modem - Device

The modem module provides the method of reading device information. 

## Get Device IMEI

### `modem.getDevImei`

```python
modem.getDevImei()
```

Gets the device IMEI.

**Return Value**

If successful, it returns the device IMEI in string type. If failed, it returns the integer value `-1`.

**Example**

```python
>>> import modem
>>> modem.getDevImei()
'866327040830317'
```

## Get Device Model

### `modem.getDevModel`

```python
modem.getDevModel()
```

Gets the device model.

**Return Value**

If successful, it returns the device model in string type. If failed, it returns the integer value `-1`.

**Example**

```python
>>> modem.getDevModel()
'EC100Y'
```

## Get Device Serial number

### `modem.getDevSN`

```python
modem.getDevSN()
```

Gets the device serial number.

**Return Value**

If successful, it returns the device serial number in string type. If failed, it returns the integer value `-1`.

**Example**

```python
>>> modem.getDevSN()
'D1Q20GM050038341P'
```

## Get Firmware Version

### `modem.getDevFwVersion`

```python
modem.getDevFwVersion()
```

Gets the device firmware version.

**Return Value**

If successful, it returns the device firmware version in string type. If failed, it returns the integer value `-1`.

**Example**

```python
>>> modem.getDevFwVersion()
'EC100YCNAAR01A01M16_OCPU_PY'
```

## Get Device Manufacture ID

### `modem.getDevProductId`

```python
modem.getDevProductId()
```

Gets the device manufacture ID.

**Return Value**

If successful, it returns the device manufacture ID in string type. If failed, it returns the integer value `-1`.

**Example**

```python
>>> modem.getDevProductId()
'Quectel'
```

