# modem - 设备相关

modem模块提供读取设备信息的方法

## 获取设备的IMEI

### `modem.getDevImei`

```python
modem.getDevImei()
```

获取设备的IMEI。

**返回值描述**

成功返回string类型设备的IMEI，失败返回整型值 `-1`。

**示例**

```python
>>> import modem
>>> modem.getDevImei()
'866327040830317'
```

## 获取设备型号

### `modem.getDevModel`

```python
modem.getDevModel()
```

获取设备型号。

**返回值描述**

 成功返回string类型设备型号，失败返回整型值 `-1`。

**示例**

```python
>>> modem.getDevModel()
'EC100Y'
```

## 获取设备序列号

### `modem.getDevSN`

```python
modem.getDevSN()
```

获取设备序列号。

**返回值描述**

 成功返回string类型设备序列号，失败返回整型值 `-1`。

**示例**

```python
>>> modem.getDevSN()
'D1Q20GM050038341P'
```

## 获取固件版本号

### `modem.getDevFwVersion`

```python
modem.getDevFwVersion()
```

获取设备固件版本号。

**返回值描述**

 成功返回string类型固件版本号，失败返回整型值 `-1`。

**示例**

```python
>>> modem.getDevFwVersion()
'EC100YCNAAR01A01M16_OCPU_PY'
```

## 获取设备制造商ID

### `modem.getDevProductId`

```python
modem.getDevProductId()
```

获取设备的制造商ID。

**返回值描述**

 成功返回设备制造商ID，失败返回整型值`-1`。

**示例**

```python
>>> modem.getDevProductId()
'Quectel'
```
