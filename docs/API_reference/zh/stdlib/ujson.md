# ujson - JSON编码和解码
`ujson`模块实现在Python对象和JSON数据格式之间进行转换的功能。该模块实现相应CPython模块的子集。更多信息请参阅CPython文档：[json](https://docs.python.org/3.5/library/json.html#module-json)

**示例：**

```python
# ujson使用。

import ujson
from uio import StringIO

# 初始化空数据流io。
io = StringIO()
# 解析字典类型数据并转换成json字符串到io。
ujson.dump({"say": "hello"}, io)
# 获取io信息。
io.getvalue()

# 解析字典类型数据并返回json字符串。
ujson.dumps({"say": "hello"})

# 初始化数据流io，并写入json字符串。
io = StringIO('{"say": "hello"}')
# 加载io中json字符串，返回字典类型数据。
ujson.load(io)

# 加载json字符串，返回字典类型数据。
ujson.loads('{"say": "hello"}')

```

## 编码json数据

将`Python`对象编码成json字符串

### `ujson.dump`

```python
ujson.dump(obj, stream)
```

序列化`obj`对象转化成`JSON`字符串，并将其写入到给定的`stream`中。

**参数描述：**

- `obj` - `Python`对象，需要转换成`JSON`字符串的数据对象。
- `stream` - 数据流对象，转换成`JSON`字符串后写入的位置。

### `ujson.dumps`

```python
ujson.dumps(obj)
```

将`Python`对象转换成`JSON`字符串。

**参数描述：**

- `obj` - `Python`对象，需要转换成`JSON`字符串的数据对象。

**返回值描述：**   

返回`JSON`字符串。


## 解码json数据

将JSON数据解码成`Python`对象。

### `ujson.load`

```python
ujson.load(stream)
```

解析给定的数据`stream`，将其解析为`JSON`字符串并反序列化成`Python`对象，最终将对象返回。

**参数描述：**

- `stream` -数据流对象，能够读取`JSON`字符串的数据流对象。

**返回值描述：**   

返回`Python`对象。

### `ujson.loads`

```python
ujson.loads(str)
```

解析`JSON`字符串`str`并返回一个`Python`对象。

**参数描述：**

- `str` -`JSON`字符串。

**返回值描述：**   

返回`Python`对象。