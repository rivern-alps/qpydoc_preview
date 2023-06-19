# ql_fs - Advanced Operations of Files

This feature is used for advanced operations of files.



## Query Whether File or Folder Exists

### `ql_fs.path_exists`

```python
ql_fs.path_exists(file_path)
```

**Parameter**

* `file_path` - String type. The absolute path of the file or folder.

**Return Value**

True - The file or folder exists.

False - The file or folder does not exist.

**Example**

```python
>>> import ql_fs
>>> ret = ql_fs.path_exists("/usr/xxx.py")
>>> print(ret)

# If files or folders exist, True will be printed. Otherwise, False will be printed.
```



## Get Folder or File Path

### `ql_fs.path_dirname`

```python
ql_fs.path_dirname(file_path)
```

**Parameter**

* `file_path` - String type. The absolute path of the file or folder.

**Return Value**

String type. File or folder path.

**Example**

```python
>>> import ql_fs
>>  ret = ql_fs.path_dirname("/usr/bin")
>>> print(ret)

# Print result:
# /usr
```



## Create Folder

### `ql_fs.mkdirs`

```python
ql_fs.mkdirs(dir_path)
```

Creates a folder recursively and configures a folder path.

**Parameter**

* `dir_path` - String type. The absolute path of the folder to be created.

**Example**

```python
>>> import ql_fs
>>> ql_fs.mkdirs("usr/a/b")
```





## Delete Folder

### `ql_fs.rmdirs`

```python
ql_fs.rmdirs(dir_path)
```

**Parameter**

* `dir_path` - String type. The absolute path of the folder to be created.

**Example**

```python
>>> import ql_fs

>>> ql_fs.rmdirs("usr/a/b")
```



## Get File Size

### `ql_fs.path_getsize`

```python
ql_fs.path_getsize(file_path)
```

**Parameter**

* `file_path` - String type. The absolute path of the file or folder.

**Return Value**

An integer. Unit: byte.

**Example**

```python
import ql_fs

ql_fs.path_getsize('usr/system_config.json')
```



## Create File

### `ql_fs.touch`

```python
ql_fs.touch(file, data)
```

Creates a file or updates file data. If the configured file path already exists, update the file content. If the configured file path does not exist, create a file and write the file content.

**Parameter**

* `file` - String type. The absolute path of the file.

* `data` - Dict type. The data to be written. Currently only files in JSON format are supported.

**Return Value**

Integer type.

0 - Successful execution

-1 - Failed execution

**Example**

```python
>>> import ql_fs
>>> data = {"test":1}
>>> ql_fs.touch("/usr/bin/config.json", data)
```



## Read File in JSON Format

### `ql_fs.read_json`

```python
ql_fs.read_json(file)
```

Files in JSON format will be read directly and returned. The data of string type will be returned for files in other formats.  

**Parameter**

* `file` - String type. The absolute path of files or folders.

**Return Value**

Dictionary type - Successful execution

None - Failed execution

**Example**

```python
>>> import ql_fs
>>> data = ql_fs.read_json("/usr/system_config.json")
```



## Copy File

### `ql_fs.file_copy`

```python
ql_fs.file_copy(dst, src)
```

Copies files from the source path to the target path.

**Parameter**

* `dst` - String type. The target file path.
*`src` - String type. The source file path.

**Return Value**

True - Successful execution

**Example**

```python
>>> import ql_fs
>>> ql_fs.file_copy("usr/a.json", "usr/system_config.json")
```