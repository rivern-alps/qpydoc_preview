
# ucollections - 集合和容器类型

`ucollections`模块可以创建一个新的容器类型，用于保存各种对象。该模块实现了CPython模块相应模块的子集。更多信息请参阅CPython文档：[collections](https://docs.python.org/3/library/collections.html)

## `ucollections`方法
### `ucollections.namedtuple`

```python
mytuple = ucollections.namedtuple(name, fields)
```

创建一个具有特定名称和一组字段的新`namedtuple`容器类型，`namedtuple`是元组的子类，允许通过索引来访问它的字段。

**参数描述：**

- `name` - str类型，表示新建容器的类型名称
- `fields` - tuple类型，表示新创建容器类型包含子类型的字段

**示例：**

```python
>>> import ucollections
>>> mytuple = ucollections.namedtuple("mytuple", ("id", "name"))
>>> t1 = mytuple(1, "foo")
>>> t2 = mytuple(2, "bar")
>>> print(t1.name)
foo
```

### `ucollections.deque`

```python
ucollections.deque(iterable, maxlen, flag)
```

创建`deque`双向队列

**参数描述：**

- `iterable` - tuple类型，必须是一个空元组
- `maxlen` - int类型，表示指定maxlen并将双端队列限制为此最大长度
- `flag` - int类型，可选参数；`0`(默认)：不检查队列是否溢出，达到最大长度时继续append会丢弃之前的值  ，`1`：当队列达到最大设定长度会抛出IndexError: full

**返回值描述：**

- deque对象



## deque对象方法

### `deque.append`

```python
deque.append(data)
```

往队列中插入值。

**参数描述：**

- `data` - 基本数据类型，表示需要添加到队列的数值



### `deque.popleft`

```python
deque.popleft()
```

从`deque`的左侧移除并返回移除的数据。如果`deque`为空，会引起索引错误

**返回值描述：**

- 返回pop出的值

**示例**

```python
from ucollections import deque

>>> dq = deque((),5)
>>> dq.append(1)
>>> dq.append(['a'])
>>> dq.append('a')

>>> dq.popleft()
1
>>> dq.popleft()
['a']
>>> dq.popleft()
'a'
```