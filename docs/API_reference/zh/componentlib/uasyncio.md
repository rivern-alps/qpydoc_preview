#  uasyncio - 协程

`uasyncio`是MicroPython中的异步IO库，它是`asyncio`模块的一个轻量级子集。它提供了类似于标准库中的协程和事件循环的抽象，用于并发运行多个协程并管理协程的执行和挂起。`uasyncio`适用于嵌入式系统和资源受限设备，具有小巧的代码体积和低的内存占用。它提供了一组API和工具来创建和管理协程、支持异步IO的网络和协议相关类。



## coro创建



### uasyncio.create_task

从给定的协程创建一个新任务并安排它运行。返回相应的`Tsk`对象。只是创建未执行, 注意这个创建是在

```python
uasyncio.create_task(coro)
```

**参数描述：**

* `coro`-协程对象,  coro类型, 协程对象

**示例：**

```python
import usr.uasyncio as asyncio
async def bar(x):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        await asyncio.sleep(2)  # Pause 1s
        print("sleep count instance = {} count = {}".format(x, count))

asyncio.create_task(bar(1))
```



##  coro运行

### uasyncio.run

启动task, 这里可以启动多个coro

```python
uasyncio.run(coro)
```

**参数描述：**

* `coro`-协程对象,  coro类型, 协程对象

**示例：**

```python
import usr.uasyncio as asyncio
async def bar(x):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        # 触发调度,让出资源给其他携程执行
        await asyncio.sleep(2)  # Pause 1s
        print("sleep count instance = {} count = {}".format(x, count))
# 启动一个携程        
asyncio.run(bar(1))        

async def main():
    for x in range(10):
        asyncio.create_task(bar(x))
    await asyncio.sleep(10)
# 启动携程, 携程中创建的所有task也会被启动
asyncio.run(main())
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

休眠让出cpu, 单位秒级别

```python
uasyncio.sleep(t)
```

**参数描述：**

* `t`-睡眠*t*秒,  int |（可以是浮点数), 睡眠触发调度, 让出cpu给其他携程运行, `只能在携程中使用`



### uasyncio.sleep

休眠让出cpu, 单位毫秒级别

```python
uasyncio.sleep_ms(t)
```

**参数描述：**

* `t`-睡眠*t*毫秒,  int |（可以是浮点数), 睡眠触发调度, 让出cpu给其他携程运行, `只能在携程中使用`



##  coro任务超时取消

### uasyncio.wait_for

等待*awaitable*完成，但如果它需要更长的*超时*秒数，请取消它。如果*awaitable*不是任务，那么将从它创建一个任务。

如果发生超时，它会取消任务并引发`asyncio.TimeoutError`：这应该被调用者捕获。

返回*awaitable*的返回值。

```python
uasyncio.wait_for(awaitable, timeout)
```

**参数描述：**

* `awaitable`-协程对象,  coro类型, 一个执行的协程对象
* `timeout`-超时时间,  int/float类型, 单位秒级别的延迟

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
    """设置携程wait task"""
    task = asyncio.wait_for(bar(10), 7)
    """启动携程, 上面携程表示在7秒内如果执行的task没退出,则关闭携程, 跑出error"""
    asyncio.run(task)
    await asyncio.sleep(10)

asyncio.run(main())
```



### uasyncio.wait_for_ms

类似于wait_for但*超时*是以毫秒为单位的整数。

```python
uasyncio.wait_for_ms(awaitable, timeout)
```

**参数描述：**

* `awaitable`-协程对象,  coro类型, 一个执行的协程对象

* `timeout`-超时时间,  int/float类型, 单位秒级别的延迟

  

## coro并发执行

### uasyncio.gather

同时运行所有*等待*。任何不是任务的*等待项*都被提升为任务。

返回所有*awaitables*的返回值列表。

```python
uasyncio.gather(*awaitables, return_exceptions=False)
```

**参数描述：**

* `awaitables`-单个或多个协程对象,  *coro类型, 一个执行的协程对象
* `return_exceptions`-单个任务异常是否取消后续任务,  bool类型,  确定任务取消或超时时的行为,如果`False`将`gather` 立即终止, 如果`True`将`gather`继续阻塞，直到所有要么运行至完成或取消或超时被终止。在这种情况下，已终止的任务将在返回值列表中返回异常对象

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
        # return_exceptions=True, 出现异常, 代表要等待所有任务才会返回异常任务的列表
        res = await asyncio.gather(*tasks, return_exceptions=True)
    except asyncio.TimeoutError:  # These only happen if return_exceptions is False
        print('Timeout')  # With the default times, cancellation occurs first
    except asyncio.CancelledError:
        print('Cancelled')
    print('Result: ', res)

asyncio.run(main())
```

