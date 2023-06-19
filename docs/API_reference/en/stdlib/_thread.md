# _thread- Multi-threading

`_thread` module contains features related to thread operations, and provides methods for creating and deleting threads, and interfaces related to mutex and semaphore.

**Example**

```python
'''
@Author: Baron
@Date: 2020-06-22
@LastEditTime: 2020-06-22 17:16:20
@Description: example for module _thread
@FilePath: example_thread_file.py
'''
import _thread
import log
import utime


'''
The following two global variables are necessary. You can modify the values of these two global variables based on project requirement
'''
PROJECT_NAME = "QuecPython_Thread_example"
PROJECT_VERSION = "1.0.0"


# Sets the log output level
log.basicConfig(level=log.INFO)
thread_log = log.getLogger("Thread")

a = 0
state = 1
state1 = 1
# Creates an instance of lock
lock = _thread.allocate_lock()

def th_func(delay, id):
	global a
	global state,state1
	while True:
		lock.acquire()  # Acquires the lock
		if a >= 10:
			thread_log.info('thread %d exit' % id)
			lock.release()  # Releases the lock
			if id == 1:
				state = 0
			else:
				state1 = 0
			break
		a += 1
		thread_log.info('[thread %d] a is %d' % (id, a))
		lock.release()  # Releases the lock
		utime.sleep(delay)

def th_func1():
	while True:
		thread_log.info('thread th_func1 is running')
		utime.sleep(1)

if __name__ == '__main__':
	for i in range(2):
		_thread.start_new_thread(th_func, (i + 1, i))   # Creates a thread. An empty tuple is paased when the function has no parameters
        
	thread_id = _thread.start_new_thread(th_func1, ())   # Creates a thread. An empty tuple is paased when the function has no parameters
    
	while state or state1:
		pass
    
	_thread.stop_thread(thread_id)   # Deletes the thread
	_thread.delete_lock(lock)   # Deletes the lock
	thread_log.info('thread th_func1 is stopped')
```

## Thread

### `_thread.get_ident`

```python
_thread.get_ident()
```

Requires the current thread number.

**Return Value**

- Returns the current thread number.


### `_thread.stack_size`

```python
_thread.stack_size(size)
```

Setting or getting the stack size which is used to create a thread (Unit: byte) depends on whether `size` is provided. The stack size is 8448 bytes by default, with a minimum of 8192 bytes. 

**Parameter**

- `size`- Sets the stack size which is used to create a thread when `size` is provided.

**Return Value**

- Returns the stack size which is used to create a thread when `size` is not provided.

### `_thread.start_new_thread`

```python
_thread.start_new_thread(function, args)
```

Creates a  thread to receive the executing function and the parameter of the executed function, and passes an empty tuple if `function` has no parameters.

**Parameter:**

- `function`- The executing function of the thread.

- `args`- The parameter of the executing function of the thread, which passes an empty tuple when the function has no parameters.

**Return Value**

- Returns the ID of the created thread.

### `_thread.stop_thread`

```python
_thread.stop_thread(thread_id)
```

Deletes a thread. The main thread cannot be deleted.

**Parameter**

- `thread_id`- The returned ID when the thread is created. If the value is 0, the current thread is deleted.

### `_thread.get_heap_size`

```python
_thread.get_heap_size()
```

Gets the remaining size of heap in the system.

**Return Value**

- Returns the remaining size of heap in the system. (Unit: byte)

## Mutex

### `_thread.allocate_lock`

```python
_thread.allocate_lock()
```

Creates a mutex object.

**Return Value**

- Returns the created mutex object.

**Example**

```python
import _thread
lock = _thread.allocate_lock()
```

### `lock.acquire`

```python
lock.acquire()
```

Acquires the lock.

**Return Value**

- True-Successful execution; False-Failed execution.

### `lock.release`

```python
lock.release()
```

Releases the lock.

### `lock.locked`

```python
lock.locked()
```

Returns the status of the lock.

**Return Value**

- True indicates the status of the lock has been required by some thread; False indicates the status of the lock has not been required by the thread.

### `_thread.delete_lock`

```python
_thread.delete_lock(lock)
```

Deletes the created mutex.

**Parameter**

- `lock`- The returned mutex object when the mutex is created.

## Semphore

### `_thread.allocate_semphore`

```python
_thread.allocate_semphore(initcount)
```

Creates a semphore object.

**Parameter**

`initcount`- The initial count value and also the maximum value of the semaphore.

**Return Value**

- Returns the created semphore object.

**Example:**

```
import _thread
semphore = _thread.allocate_semphore(1)
```

### `semphore.acquire`

```python
semphore.acquire()
```

Acquires the semphore.

**Return Value**

- True-Successful execution; False-Failed execution.

### `semphore.release`

```python
semphore.release()
```

Releases the semphore.

### `semphore.getCnt`

```python
semphore.getCnt()
```

Gets the maximum value of the semaphore count and the current remaining count value.

**Return Value**

- `(maxCnt, curCnt)`-tuple: maxCnt is the maximum count value, and curCnt is the current remaining count value.

### `_thread.delete_semphore`

```python
_thread.delete_semphore(semphore)
```

Deletes the created semphore.

**Parameter**

`semphore`- The returned semphore object when the semphore is created.

