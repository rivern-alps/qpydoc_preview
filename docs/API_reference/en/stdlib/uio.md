# uio - Input/Output Streams

`uio` contains additional types of stream (file-like) objects and helper functions. This feature implements a subset of the corresponding CPython feature, as described below. For more information, refer to the original CPython documentation: [io](https://docs.python.org/3.5/library/io.html#module-io).

**Example**

```python
fd = uio.open('/usr/test.py', mode='r', encoding='UTF-8')
fd.close()
```

## Open File

### `uio.open`

```python
uio.open(name, mode='r', **kwarg)
```

Opens a file. This is an alias for the built-in  `open()` function.

**Parameter**

* `name`: String type. File name. 

* `mode`: String type. Open mode.

|Open Mode|Description|
| ---- | ---- |
|   'r'  |Open a file for reading.|
|   'w'  |Open a file for writing only. Overwrites the file if the file exists.|
|   'a'  |Opens a file for appending. The file pointer is at the end of the file, so the content is added to the end.|

* `**kwarg`: Variable-length parameter list.

**Return Value**
uio object – Successful execution

Error – Failed execution 

## Close File

### `uio.close`

```python
uio.close()
```

Closes the open files.