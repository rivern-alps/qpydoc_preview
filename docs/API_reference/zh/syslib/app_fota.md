# app_fota - 用户文件升级相关功能

`app_fota`模块用于用户文件升级。

**示例**：

```python
import app_fota
from misc import Power

fota = app_fota.new()
download_list = [{'url': 'http://www.example.com/app.py', 'file_name': '/usr/app.py'}, {'url': 'http://www.example.com/test.txt', 'file_name': '/usr/text.txt'}]
fota.bulk_download(download_list) # 下载
fota.set_update_flag() # 设置升级标志
Power.powerRestart() # 重启
```

## 初始化相关功能

### `app_fota.new`

```python
app_fota.new()
```

创建app_fota对象。

**返回值描述：**

app_fota对象。

**示例**：

```python
import app_fota
fota = app_fota.new()
```

## 下载相关功能

### `fota.download`

```python
fota.download(url, file_name)
```

下载单个文件。

**参数描述：**

- `url`-待下载文件的url，类型为str。
- `file_name`-本地待升级文件的绝对路径，类型str。

**返回值描述**：

成功返回0，否则返回-1。

### `fota.bulk_download`

```python
fota.bulk_download(info=[])
```

下载批量文件。

**参数描述：**

- `info`-批量下载列表，列表的元素均为包含了`url`和`file_name`的字典，类型为list。

**返回值描述**：

下载失败时返回下载失败的列表，类型为list。下载成功时返回空。

**示例**：

```python
download_list = [{'url': 'http://www.example.com/app.py', 'file_name': '/usr/app.py'}, {'url': 'http://www.example.com/test.txt', 'file_name': '/usr/text.txt'}]
fota.bulk_download(download_list)
```

该示例中，假设`http://www.example.com/test.txt`下载失败，则该方法返回值为`[{url: 'http://www.example.com/test.txt', file_name: '/usr/text.txt'}]`。

## 设置升级标志相关功能

### `fota.set_update_flag`

```python
fota.set_update_flag()
```

设置升级标志。设置完成升级标志后，调用重启接口，重启后即可启动升级工作。升级完成后会直接进入应用程序。

