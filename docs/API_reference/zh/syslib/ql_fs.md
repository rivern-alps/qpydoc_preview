# ql_fs - 高级文件操作

模块功能: 用于文件的高级操作



## 查看文件或文件夹是否存在

### `ql_fs.path_exists`

```python
ql_fs.path_exists(file_path)
```

**参数描述：**

* `file_path`-文件路径, string类型, 文件或文件夹的绝对路径 

**返回值描述：**

存在返回 True, 不存在返回False

**示例:**

```python
>>> import ql_fs
>>> ret = ql_fs.path_exists("/usr/xxx.py")
>>> print(ret)

# 存在打印True 不存在 FalseCopy to clipboardErrorCopied
```



## 获取文件所在文件夹路径

### `ql_fs.path_dirname`

```python
ql_fs.path_dirname(file_path)
```

**参数描述：**

* `file_path`-文件路径, string类型, 文件或文件夹的绝对路径 

**返回值描述：**

string类型的路径地址

**示例:**

```python
>>> import ql_fs
>>  ret = ql_fs.path_dirname("/usr/bin")
>>> print(ret)

# 打印结果如下
# /usr
```



## 创建文件夹

### `ql_fs.mkdirs`

```python
ql_fs.mkdirs(dir_path)
```

该方法递归式创建文件夹, 传入文件夹路径

**参数描述：**

* `dir_path`-文件路径, string类型, 所要创建的文件夹绝对路径 

**示例:**

```python
>>> import ql_fs
>>> ql_fs.mkdirs("usr/a/b")
```





## 删除文件夹

### `ql_fs.rmdirs`

```python
ql_fs.rmdirs(dir_path)
```

**参数描述：**

* `dir_path`-文件路径, string类型, 所要创建的文件夹绝对路径 

**示例:**

```python
>>> import ql_fs

>>> ql_fs.rmdirs("usr/a/b")
```



## 获取文件大小

### `ql_fs.path_getsize`

```python
ql_fs.path_getsize(file_path)
```

**参数:**

* `file_path`-文件路径, string类型, 文件或文件夹的绝对路径 

**返回值**

int类型的数字, 单位是字节

**示例**

```python
import ql_fs

ql_fs.path_getsize('usr/system_config.json')
```



## 创建文件

### `ql_fs.touch`

```python
ql_fs.touch(file, data)
```

创建文件或者更新文件数据, 创建指定文件也可传入文本文件更新, 会自动创建文件夹然后创建或更新文件的内容

**参数描述：**

* `file`-文件路径, string类型, 文件的绝对路径 

* `data`-数据, dict类型, 所要写入的数据,目前只支持json文件

**返回值描述：**

int类型, 0为成功, -1则失败

**示例**：

```python
>>> import ql_fs
>>> data = {"test":1}
>>> ql_fs.touch("/usr/bin/config.json", data)
```



## 读取json文件

### `ql_fs.read_json`

```python
ql_fs.read_json(file)
```

json文件类型的直接读取json文件并返回, 非json文件类型返回为读取的字符串数据类型

**参数描述：**

* `file`-文件路径, string类型, 文件或文件夹的绝对路径 

**返回值描述：**

读取成功, 返回dict类型

失败, 返回None

**示例**：

```python
>>> import ql_fs
>>> data = ql_fs.read_json("/usr/system_config.json")
```



## 文件拷贝

### `ql_fs.file_copy`

```python
ql_fs.file_copy(dst, src)
```

将文件从原路径拷贝到目标路径

**参数描述：**

* `dst`-目标文件,  string类型,   目标路径路径
*`src`-源文件,  string类型, 源文件路径

**返回值描述：**

True代表拷贝成功

**示例：**：

```python
>>> import ql_fs
>>> ql_fs.file_copy("usr/a.json", "usr/system_config.json")
```