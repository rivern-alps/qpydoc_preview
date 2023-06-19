# _thread- 多线程

`_thread` 模块包含线程操作相关的功能。提供创建、删除线程的方法，提供互斥锁、信号量相关的接口。

**示例：**

```python
import _thread
import log
import utime


# 设置日志输出级别
log.basicConfig(level=log.INFO)
thread_log = log.getLogger("Thread")

a = 0
state = 1
state1 = 1
# 创建一个lock的实例
lock = _thread.allocate_lock()

def th_func(delay, id):
	global a
	global state,state1
	while True:
		lock.acquire()  # 获取锁
		if a >= 10:
			thread_log.info('thread %d exit' % id)
			lock.release()  # 释放锁
			if id == 1:
				state = 0
			else:
				state1 = 0
			break
		a += 1
		thread_log.info('[thread %d] a is %d' % (id, a))
		lock.release()  # 释放锁
		utime.sleep(delay)

def th_func1():
	while True:
		thread_log.info('thread th_func1 is running')
		utime.sleep(1)

if __name__ == '__main__':
	for i in range(2):
		_thread.start_new_thread(th_func, (i + 1, i))   # 创建一个线程，当函数无参时传入空的元组
        
	thread_id = _thread.start_new_thread(th_func1, ())   # 创建一个线程，当函数无参时传入空的元组
    
	while state or state1:
		utime.sleep(1)
		pass
    
	_thread.stop_thread(thread_id)   # 删除线程
	_thread.delete_lock(lock)   # 删除锁
	thread_log.info('thread th_func1 is stopped')
```

## 线程相关功能

### `_thread.get_ident`

```python
_thread.get_ident()
```

获取当前线程号。

**返回值描述：**

返回当前线程号。


### `_thread.stack_size`

```python
_thread.stack_size(size)
```

设置或获取创建新线程使用的栈大小（以字节为单位），取决于参数`size`是否提供。默认为8448字节，最小8192字节。

**参数描述：**

- `size`- 提供该参数，用于创建新线程使用的栈大小。

**返回值描述：**

当参数`size`没有提供时，返回创建新线程使用的栈大小。

### `_thread.start_new_thread`

```python
_thread.start_new_thread(function, args)
```

创建一个新线程。接收执行函数和被执行函数参数，当 function 函数无参时传入空的元组。

**参数描述：**

- `function`- 线程执行函数。函数参数由`args`传入。
- `args`- 线程执行函数的参数，类型为元组。当 `function` 函数无参时传入空的元组。

**返回值描述：**

返回创建的新线程的id。

**示例**：

```python
import _thread
import utime

def th_func(test1, test2, test3):
    while True:
        print('param1 %d, param2 %d, param3 %d' % (test1, test2, test3))
        utime.sleep(1)
        
def th_func1():
	while True:
		print('thread th_func1 is running')
		utime.sleep(1)
 
_thread.start_new_thread(th_func, (1, 2, 3))# 创建一个线程

_thread.start_new_thread(th_func1, ())   # 创建一个线程，当函数无参时传入空的元组
```



### `_thread.stop_thread`

```python
_thread.stop_thread(thread_id)
```

停止并删除一个线程。不可停止或删除主线程。

**参数描述：**

- `thread_id`- 为创建线程时返回的线程id，为0时则停止并删除当前线程。

### `_thread.get_heap_size`

```python
_thread.get_heap_size()
```

获取系统heap内存剩余大小。

**返回值描述：**

返回系统heap内存剩余大小（以字节为单位）。

## 互斥锁相关功能

### `_thread.allocate_lock`

```python
_thread.allocate_lock()
```

创建一个互斥锁对象。

**返回值描述：**

返回创建的互斥锁对象。

**示例**：

```python
import _thread
lock = _thread.allocate_lock()
```

### `lock.acquire`

```python
lock.acquire()
```

获取锁。

**返回值描述：**

成功返回True，失败返回False。

### `lock.release`

```python
lock.release()
```

释放锁。

### `lock.locked`

```python
lock.locked()
```

返回锁的状态。

**返回值描述：**

True表示被某个线程获取，False则表示没有。

### `_thread.delete_lock`

```python
_thread.delete_lock(lock)
```

删除已经创建的互斥锁。

**参数描述：**

- `lock`- 为创建时返回的互斥锁对象。

## 信号量相关功能

### `_thread.allocate_semphore`

```python
_thread.allocate_semphore(initcount)
```

创建一个信号量对象。

**参数描述：**

`initcount`- 为信号量的计数初始值，也是最大值。

**返回值描述：**

返回创建的信号量对象。

**示例**：

```
import _thread
semphore = _thread.allocate_semphore(1)
```

### `semphore.acquire`

```python
semphore.acquire()
```

获取信号量。

**返回值描述：**

成功返回True，失败返回False。

### `semphore.release`

```python
semphore.release()
```

释放信号量。

### `semphore.getCnt`

```python
semphore.getCnt()
```

获取信号量计数最大值和当前剩余计数值。

**返回值描述：**

`(maxCnt, curCnt)`-元组：maxCnt为计数最大值，curCnt为当前剩余计数值。

### `_thread.delete_semphore`

```python
_thread.delete_semphore(semphore)
```

删除已经创建的信号量。

**参数描述：**

`semphore`- 为创建时返回的信号量对象。

