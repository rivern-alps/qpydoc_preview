# uio - 输入输出流

`uio`模块包含其他类型的stream（类文件）对象和辅助函数。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：[io](https://docs.python.org/3.5/library/io.html#module-io)

**示例**：

```python
fd = uio.open('/usr/test.py', mode='r', encoding='UTF-8')
fd.close()
```

## 打开文件

### `uio.open`

```python
uio.open(name, mode='r', **kwarg)
```

打开文件，内置`open()`函数是该函数的别名。

**参数描述**

* `name` ：字符串，表示文件名

* `mode` ：字符串，打开模式

|打开模式|含义|
| ---- | ---- |
|   'r'  |只读模式打开文件|
|   'w'  |写入模式打开文件，每次写入会覆盖上次写入数据|
|   'a'  |只写追加模式打开文件，可连续写入文件数据而不是覆盖数据|

* `**kwarg`：可变长参数列表

**返回值描述**
成功则返回uio的对象，失败则根据不同的失败类型抛出error

## 关闭打开的文件

### `uio.close`

```python
uio.close()
```

关闭打开的文件。