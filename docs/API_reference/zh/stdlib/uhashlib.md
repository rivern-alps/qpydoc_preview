# class uhashlib - 哈希算法

该模块实现二进制数据散列算法。

> 目前仅支持sha256，sha1，MD5。

**示例：**

```python
import uhashlib
import ubinascii

hash_obj  = uhashlib.sha256()  # 创建hash对象
hash_obj.update(b"QuecPython")
res = hash_obj.digest()
# b"\x1e\xc6gq\xb3\xa9\xac>\xa4\xc4O\x00\x9eTW\x97\xd4.\x9e}Bo\xff\x82u\x89Th\xfe'\xc6\xcd"
# 转成十六进制表示
hex_msg = ubinascii.hexlify(res)
# b'1ec66771b3a9ac3ea4c44f009e545797d42e9e7d426fff8275895468fe27c6cd'
```


## 构造函数

### `uhashlib.sha256`

```python
class uhashlib.sha256(bytes)
```

创建一个SHA256哈希对象

**参数描述：**

- `bytes` - 可选参数，bytes型数据。可在创建时传入bytes数据，也可通过update方法。

### `uhashlib.sha1`

```python
class uhashlib.sha1(bytes)
```

创建一个SHA1哈希对象

**参数描述：**

- `bytes` - 可选参数，bytes型数据。可在创建时传入bytes数据，也可通过update方法。

### `uhashlib.md5`

```python
class uhashlib.md5(bytes)
```

创建一个MD5哈希对象

**参数描述：**

- `bytes` - 可选参数，bytes型数据。可在创建时传入bytes数据，也可通过update方法。


## 方法

### `hash_obj.update()`

```python
hash_obj.update(bytes)
```

将更多的bytes数据加到散列。

**参数描述**

- `bytes` - 需要被加密的bytes类型数据。

### `hash_obj.digest()`

```python
hash_obj.digest()
```

返回通过哈希传递的所有数据的散列，数据为字节类型。调用此方法后，无法再将更多的数据送入散列。

**返回值描述：**

返回加密后字节类型的数据。
