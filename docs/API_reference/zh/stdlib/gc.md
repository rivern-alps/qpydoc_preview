# gc-内存相关功能

`gc` 模块实现内存垃圾回收机制，该模块实现了CPython模块相应模块的子集。更多信息请参阅CPython文档：[gc](https://docs.python.org/3.5/library/gc.html#module-gc)

## 内存回收相关功能

### `gc.enable`

```python
gc.enable()
```

启用自动回收内存碎片机制。

### `gc.disable`

```python
gc.disable()
```

禁用自动回收内存碎片机制。

### `gc.isenabled`

```python
gc.isenabled()
```

查询是否启动了自动回收内存碎片机制。

**返回值描述：**

True-已启动自动回收内存碎片机制，False-未启动自动回收内存碎片机制。

### `gc.collect`

```python
gc.collect()
```

主动回收内存碎片。

## 内存查询相关功能

### `gc.mem_alloc`

```python
gc.mem_alloc()
```

查询已申请的内存大小。

**返回值描述：**

返回已申请的内存大小，单位字节。

### `gc.mem_free`

```python
gc.mem_free()
```

查询剩余可用的内存大小。

**返回值描述：**

返回剩余可用的内存大小，单位字节。

