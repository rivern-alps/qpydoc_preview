# uhashlib - Hash Algorithm

```
This article introduces the use of QuecPython's uhashlib module and describes features of the latest version of the uhashlib module.
```

This module realizes the hash algorithm of the binary data.

> Note: Only supports SHA256, SHA1, MD5 currently.

**Example**

```python
import uhashlib
import ubinascii

hash_obj  = uhashlib.sha256()  # Creates the hash object
hash_obj.update(b"QuecPython")
res = hash_obj.digest()
# b"\x1e\xc6gq\xb3\xa9\xac>\xa4\xc4O\x00\x9eTW\x97\xd4.\x9e}Bo\xff\x82u\x89Th\xfe'\xc6\xcd"
# Converts to hexadecimal
hex_msg = ubinascii.hexlify(res)
# b'1ec66771b3a9ac3ea4c44f009e545797d42e9e7d426fff8275895468fe27c6cd'
```


## Constructor

### `uhashlib.sha256`

```python
class uhashlib.sha256(bytes)
```

Creates a SHA256 hash object.

**Parameter**

- `bytes` - Bytes type. Optional parameter. Bytes data can be passed when creating a SHA256 hash object or via hash_obj.update().

### `uhashlib.sha1`

```python
class uhashlib.sha1(bytes)
```

Creates a SHA1 hash object.

**Parameter**

- `bytes` - Bytes type. Optional parameter. Bytes data can be passed when creating a SHA256 hash object or via hash_obj.update().

### `uhashlib.md5`

```python
class uhashlib.md5(bytes)
```

Creates a MD5 hash object.

**Parameter**

- `bytes` - Bytes type. Optional parameter. Bytes data can be passed when creating a SHA256 hash object or via hash_obj.update().


## Methods

### hash_obj.update()

```python
hash_obj.update(bytes)
```

Adds more bytes data to the hash.

**Parameter**

- `bytes` - Bytes type. Need to be encrypted. 

### hash_obj.digest()

```python
hash_obj.digest(bytes)
```

Returns the hash of all data passed by the hash algorithm. The type of data is bytes. No more data can be sent into the hash after this method is called.

