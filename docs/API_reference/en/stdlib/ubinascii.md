# ubinascii - Binary/ASCII Conversions

```
This article introduces the use of QuecPython's ubinascii module and describes features of the latest version of the ubinascii module.
```

The module realizes the conversion between binary data and various ASCII encoding (bidirectional), and subsets of the corresponding CPython module. See CPython file [binascii](https://docs.python.org/3.5/library/binascii.html#module-binascii) for more detailed information.

## Constructor

### `ubinascii.a2b_base64`

```python
ubinascii.a2b_base64(data)
```

This function decodes the data encoded by base64. When decoding, invalid characters inputed by base64 will be ignored, and the bytes object will be returned.

### `ubinascii.b2a_base64`

```python
ubinascii.b2a_base64(data)
```

Encodes binary data in base64 format and returns encoded data. The encoded data followed by a line break is represented as the bytes object.

### `ubinascii.hexlify`

```python
ubinascii.hexlify(data, [sep])
```

Converts the binary data to the hexadecimal character string.

**Example**

```python
>>> import ubinascii
# No sep parameter
>>> ubinascii.hexlify('\x11\x22123')
b'1122313233'
>>> ubinascii.hexlify('abcdfg')
b'616263646667'
# The second parameter sep is specified, which will be used to separate two hexadecimal numbers
>>> ubinascii.hexlify('\x11\x22123', ' ')
b'11 22 31 32 33'
>>> ubinascii.hexlify('\x11\x22123', ',')
b'11,22,31,32,33'
```

### `ubinascii.unhexlify`

```python
ubinascii.unhexlify(data)
```

Converts the hexadecimal character string to the binary character string.

**Example**

```python
>>> import ubinascii
>>> ubinascii.unhexlify('313222')
b'12"'
```
