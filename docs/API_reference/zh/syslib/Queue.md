# Queue - 消息队列

用于线程间通信


## 构造函数

### `queue.Queue`

```python
class queue.Queue(maxsize=100)
```

**参数描述：**

`maxsize`-队列最大长度,   int类型,  默认长度是100

**示例：**

```python
>>> from queue import Queue
>>> q = Queue(100)
```



## 往队列放入数据

### `Queue.put`

往队列中塞入数据

```python
Queue.put(data=None)
```

**参数描述：**

* `data`-数据或信号,  任意类型,   插入的数据, 可以为空不传参, 不传的默认会传个None信号

**返回值描述：**

True 为成功, False 为失败



## 获取数据

### `Queue.get`

从队列中获取数据, 这里需要注意一下获取数据这块的是阻塞获取

```python
Queue.get()
```

**返回值描述：**

为队列中的数据, 如果是空信号则会获取为None



## 查看队列是否为空

### `Queue.empty`

```python
Queue.empty()
```

**返回值描述：**

True则为空, False则不为空



## 查看队列中存在的数据个数

### `Queue.size`

```python
Queue.size()
```

**返回值描述：**

int类型的当前数据长度



**示例：**

```python
import _thread
from queue import Queue

# 初始化队列  默认长度100
q = Queue()


def get():
    while True:
        # 阻塞获取
        data = q.get()
        print("data = {}".format(data))

# 线程去阻塞
_thread.start_new_thread(get, ())

# put数据
text = "hello world"
q.put(text)

# 获取size
q.size()

# 判断队列是否已空
q.empty()
```