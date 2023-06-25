#  uasyncio - 协程

`uasyncio`是MicroPython中的异步IO库，它是`asyncio`模块的一个轻量级子集。它提供了类似于标准库中的协程和事件循环的抽象，用于并发运行多个协程并管理协程的执行和挂起。`uasyncio`适用于嵌入式系统和资源受限设备，具有小巧的代码体积和低的内存占用。它提供了一组API和工具来创建和管理协程、支持异步IO的网络和协议相关类。



## coro创建



### uasyncio.create_task

创建一个异步任务，用于执行指定的协程

```python
uasyncio.create_task(coro)
```

**参数描述：**

* `coro`-要执行的协程对象

**示例：**

```python
import usr.uasyncio as asyncio
async def my_coroutine():
    print("Running my_coroutine")

task = asyncio.create_task(my_coroutine())
```



##  coro运行

### uasyncio.run

运行一个协程，阻塞直到该协程完成。这是启动事件循环的主要方式。

```python
uasyncio.run(coro)
```

**参数描述：**

* `coro`-要运行的协程对象

**示例：**

```python
import usr.uasyncio as asyncio

async def my_coroutine():
    print("Running my_coroutine")

asyncio.run(my_coroutine())
```

##  coro取消任务

### task.cancel

取消任务

```python
task.cancel()
```

**示例:**

```python
from usr import uasyncio as asyncio
async def bar(n):
    print('Start cancellable bar()')
    while True:
        await asyncio.sleep(1)
        n += 1
    return n

async def do_cancel(task):
    await asyncio.sleep(5)
    print('About to cancel bar')
    # 取消任务
    task.cancel()

def main():
    task = asyncio.wait_for(bar(10), 7)
    asyncio.create_task(do_cancel(task))
    asyncio.sleep(1)

asyncio.run(main())
```



##  coro睡眠

### uasyncio.sleep

暂停当前任务指定的秒数。这允许其他任务运行。

```python
uasyncio.sleep(delay)
```

**参数描述：**

* `delay`-延迟的秒数,  int |（可以是浮点数)



### uasyncio.sleep_ms

暂停当前任务指定的毫秒数。这允许其他任务运行。

```python
uasyncio.sleep_ms(delay)
```

**参数描述：**

* `t`-延迟的毫秒数,  int |（可以是浮点数)



##  coro任务超时取消

### uasyncio.wait_for

等待一个协程，如果在给定的超时时间内未完成，则引发一个异常。。

```python
uasyncio.wait_for(coro, timeout)
```

**参数描述：**

* `coro`-协程对象
* `timeout`-超时时间, 单位是秒,  int/float类型

**示例:**

```python
from usr import uasyncio as asyncio


async def bar(x):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        await asyncio.sleep(2)  # Pause 1s
        print("sleep count instance = {} count = {}".format(x, count))


async def main():
    """设置协程wait task"""
    task = asyncio.wait_for(bar(10), 7)
    """启动协程, 上面协程表示在7秒内如果执行的task没退出,则关闭协程, 跑出error"""
    asyncio.run(task)
    await asyncio.sleep(10)

asyncio.run(main())
```



### uasyncio.wait_for_ms

这个函数的功能和 `wait_for` 类似，但是超时时间的单位是毫秒。

```python
uasyncio.wait_for_ms(coro, timeout)
```

**参数描述：**

* `coro`-协程对象

* `timeout`-超时时间, 单位是毫秒,  int/float类型

  

## coro并发执行

### uasyncio.gather

运行给定的协程并收集它们的结果。当所有协程都完成时，此函数返回一个结果列表。 `return_exceptions` (默认为`False`)，即在任何协程引发异常时立即中止并引发异常。如果设置为`True`，则将异常包装在结果中返回。

```python
uasyncio.gather(*coros, return_exceptions=False)
```

**参数描述：**

* `coros`-单个或多个协程对象
* `return_exceptions`-是否返回异常作为结果,  bool类型,  默认为False。

**示例:**

```python
from usr import uasyncio as asyncio


async def barking(n):
    print('Start barking')
    for _ in range(6):
        await asyncio.sleep(1)
    print('Done barking.')
    return 2 * n

async def foo(n):
    print('Start timeout coro foo()')
    while True:
        await asyncio.sleep(1)
        n += 1
    return n

async def bar(n):
    print('Start cancellable bar()')
    while True:
        await asyncio.sleep(1)
        n += 1
    return n

async def do_cancel(task):
    await asyncio.sleep(5)
    print('About to cancel bar')
    task.cancel()

async def main():
    tasks = [asyncio.create_task(bar(70))]
    tasks.append(barking(21))
    tasks.append(asyncio.wait_for(foo(10), 7))
    asyncio.create_task(do_cancel(tasks[0]))
    res = None
    try:
        # return_exceptions=True, 默认为False，即在任何协程引发异常时立即中止并引发异常。 如果设置为True，则将异常包装在结果中返回。
        res = await asyncio.gather(*tasks, return_exceptions=True)
    except asyncio.TimeoutError:  # These only happen if return_exceptions is False
        print('Timeout')  # With the default times, cancellation occurs first
    except asyncio.CancelledError:
        print('Cancelled')
    print('Result: ', res)

asyncio.run(main())
```

