
# ustruct - Pack and Unpack Primitive Data Types

Module feature: `ustruct` module realizes subsets of the corresponding CPython module. See CPython file [struct](https://docs.python.org/3.5/library/struct.html#module-struct) for detailed information.


## Format String

The format string is the mechanism used to specify the expected layout when packing and unpacking data. Format strings are built through the format character of the specified data type that to be packed or unpacked. In addition, there are special characters that control byte order, size, and alignment.


### Byte Order, Size, and Alignment

By default, C types are represented in the machine's native format and byte order, and properly aligned by skipping pad bytes if necessary (according to the rules used by the C compiler). According to the following table, the first character of the format string can be used to indicate the byte order, size, and alignment of the packed data:

| Character | Byte **Order **        | Size     | Alignment |
| --------- | ---------------------- | -------- | --------- |
| `@`       | native                 | native   | native    |
| `=`       | native                 | standard | none      |
| `<`       | little-endian          | standard | none      |
| `>`       | big-endian             | standard | none      |
| `!`       | network (= big-endian) | standard | none      |

> If the first character is not one of the format string, it is assumed to be '@' .


### **List of Format Character**

| Format | C Type               | Python Type | Standard Size |
| ------ | -------------------- | ----------- | ------------- |
| `b`    | `signed char`        | integer     | 1             |
| `B`    | `unsigned char`      | integer     | 1             |
| `h`    | `short`              | integer     | 2             |
| `H`    | `unsigned short`     | integer     | 2             |
| `i`    | `int`                | integer     | 4             |
| `I`    | `unsigned int`       | integer     | 4             |
| `l`    | `long`               | integer     | 4             |
| `L`    | `unsigned long`      | integer     | 4             |
| `q`    | `long long`          | integer     | 8             |
| `Q`    | `unsigned long long` | integer     | 8             |
| `f`    | `float`              | float       | 4             |
| `d`    | `double`             | float       | 8             |
| `P`    | `void *`             | integer     | 4             |


## `ustruct` Methods

### `ustruct.calcsize`

```python
ustruct.calcsize(fmt)
```

Returns the number of bytes for storing `fmt`.

**Parameter**

- `fmt` - Format character type. See the list of format character above for details.

**Example:**

```python
>>> import ustruct
>>> ustruct.calcsize('i')
4
>>> ustruct.calcsize('f')
4
>>> ustruct.calcsize('d')
8
```



### `ustruct.pack`

```python
ustruct.pack(fmt, v1, v2, ...)
```

Compresses parameters v1, v2, ... according to the format string `fmt`.

**Parameter**

- `fmt` - Format character type. See the list of format character above for details.
- `v1`, `v2`, `...` - The variable name or value which requires data conversion. 

**Return Value**

- Returns the byte object of the encoded parameter.

**Example**

```python
>>> import ustruct

>>> ustruct.pack('ii', 7, 9)  # Packs two integers
b'\x07\x00\x00\x00\t\x00\x00\x00'

```

### `ustruct.unpack`

```python
ustruct.unpack(fmt, data)
```

Decompresses the data according to the format string `fmt` . The return value is a tuple.

**Parameter**

- `fmt` - Format character type. See the list of format character above for details.
- `data` - Data needs to be decompressed.

**Return Value**

- Returns the tuple containing the decompression value (even if it contains only one value).

**Example**

```python
>>> import ustruct

>>> ustruct.unpack('ii', b'\x07\x00\x00\x00\t\x00\x00\x00')  # Decompresses two previous packed integers
(7, 9)

```



### `ustruct.pack_into`

```python
ustruct.pack_into(fmt, buffer, offset, v1, v2, ...)
```

Packs values  v1, v2, … into a buffer starting with `offset` according to the format string `fmt`. If you counts from the end of the buffer, the value of `offset` may be negative.

**Parameter**

- `fmt` - Format character type. See the list of format character above for details.
- `buffer` - Buffer for writing data. 
- `offset` - Starting position for writing data.
- `v1`, `v2`, `...` - Data needs to be written in the buffer.

**Example**

```python
>>> import ustruct

# Defines the format string
>>> fmt = "3sB"
# Defines a character string and an integer
>>> name = "Tom"
>>> age = 25

# Packs two values in the specified format and writes them to an empty buffer in bytes type
>>> buf = bytearray(8) # Create a buffer of 8 bytes
>>> ustruct.pack_into(fmt, buf, 0, name.encode(), age) # Encodes "name" as bytes type and writes in three characters (three bytes), followed by a integer "age" (one byte)

>>>  print(buf) # Output: bytearray(b'Tom\x19\x00\x00\x00')
bytearray(b'Tom\x19\x00\x00\x00\x00')
```


### `ustruct.unpack_from`

```python
ustruct.unpack_from(fmt, data, offset=0)
```

Parses the decompressed data starting from `offest` according to the format string `fmt`. If you counts from the end of the buffer, the value of offset may be negative.

**Parameter**

- `fmt` - Format character type. See the list of format character above for details.
- `data` - Data buffer. (The unit of the buffer size is byte.)
- `offset` - (Optional) Starting position of decompression. 0 is by default.

**Return Value**

- Returns the tuple containing the decompression value (even if it contains only one value).

**Example**

```python
>>> import ustruct

# Defines the format string
>>> fmt = "3sB"
# Defines the byte sequence which needs to unpack
>>> data = bytearray(b'Tom\x19\x00\x00\x00\x00')

# Unpacks from the first byte of the byte sequence
>>> result = ustruct.unpack_from(fmt, data, 0)
>>> print(result) # Output: (b'Tom', 25)
(b'Tom', 25)

```