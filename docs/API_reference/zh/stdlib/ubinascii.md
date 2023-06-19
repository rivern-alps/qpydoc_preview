# ubinascii - 二进制与ASCII转换


该模块实现了二进制数据与各种ASCII编码之间的转换(双向)。该模块实现相应CPython模块的子集，更多信息请参阅阅CPython文档：[binascii](https://docs.python.org/3.5/library/binascii.html#module-binascii)

## 解码base64编码的数据

### `ubinascii.a2b_base64`

```python
ubinascii.a2b_base64(data)
```

解码base64编码的数据，会自动忽略输入中的无效字符，返回 bytes 对象。

## 以base64格式编码二进制数据

### `ubinascii.b2a_base64`

```python
ubinascii.b2a_base64(data)
```

以base64格式编码二进制数据，返回编码数据。后面跟换行符，作为 bytes 对象。

## 将二进制数据转换为十六进制字符串表示

### `ubinascii.hexlify`

```python
ubinascii.hexlify(data, [sep])
```

将二进制数据转换为十六进制字符串表示。

**示例：**

```python
>>> import ubinascii
# 没有sep参数
>>> ubinascii.hexlify('\x11\x22123')
b'1122313233'
>>> ubinascii.hexlify('abcdfg')
b'616263646667'
# 指定了第二个参数sep，它将用于分隔两个十六进制数
>>> ubinascii.hexlify('\x11\x22123', ' ')
b'11 22 31 32 33'
>>> ubinascii.hexlify('\x11\x22123', ',')
b'11,22,31,32,33'
```

## 将十六进制形式的字符串转换成二进制形式的字符串表示

### `ubinascii.unhexlify`

```python
ubinascii.unhexlify(data)
```

将十六进制形式的字符串转换成二进制形式的字符串表示。

**示例：**

```python
>>> import ubinascii
>>> ubinascii.unhexlify('313222')
b'12"'
```
