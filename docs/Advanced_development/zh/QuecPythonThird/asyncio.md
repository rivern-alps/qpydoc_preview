

## 文档历史

**修订记录**

| **版本** | **日期**   | **作者**  | **变更表述** |
| -------- | ---------- | --------- | ------------ |
| 1.0      | 2021-09-26 | jaxsen.xu | 初始版本     |



## 概述

异步 I/O 调度器

## 名词解释

- *uasyncio / asyncio*
  - 异步I/O模块
- *coro*
  - *Coroutine*
  - 协程
- *
  - 必须存在
  - 别的可裁剪



## 功能模块

### core(核心功能)

#### coro创建

> *uasyncio.create_task(coro)*

从给定的协程创建一个新任务并安排它运行。返回相应的[`Task`](https://docs.micropython.org/en/latest/library/uasyncio.html#uasyncio.Task)对象。只是创建并未执行

例:

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

#### coro运行

> *uasyncio.run(coro)*

启动task, 这里可以启动多个coro

```python
import usr.uasyncio as asyncio
async def bar(x):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        # 触发调度,让出资源给其他协程执行
        await asyncio.sleep(2)  # Pause 1s
        print("sleep count instance = {} count = {}".format(x, count))
# 启动一个协程        
asyncio.run(bar(1))        

async def main():
    for x in range(10):
        asyncio.create_task(bar(x))
    await asyncio.sleep(10)
# 启动协程, 协程中创建的所有task也会被启动
asyncio.run(main())
```

#### coro取消任务

> task.cancel()

task为创建的任务

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



#### coro睡眠

##### 毫秒及别

> *uasyncio.sleep(t)*

睡眠*t*秒（可以是浮点数), 睡眠触发调度, 让出cpu给其他协程运行, `只能在协程中使用`





##### 秒级别

> *uasyncio.sleep_ms(t)*

睡眠t毫秒(可以是浮点数), 睡眠触发调度, 让出cpu给其他协程运行, `只能在coro中使用`



### funcs(附加功能)

#### coro增强, 任务超时取消(秒级)

> *uasyncio.wait_for(awaitable, timeout)*

等待*awaitable*完成，但如果它需要更长的*超时*秒数，请取消它。如果*awaitable*不是任务，那么将从它创建一个任务。

如果发生超时，它会取消任务并引发`asyncio.TimeoutError`：这应该被调用者捕获。

返回*awaitable*的返回值。

这是一个协程。

- 参数

| 参数      | 类型      | 说明                 |
| --------- | --------- | -------------------- |
| awaitable | coro      | 协程, 一个执行的协程 |
| timeout   | int/float | 单位秒级别的延迟     |

例:

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



#### coro增强, 任务超时取消(毫秒级)

> *uasyncio.wait_for_ms(awaitable, timeout)*

类似于wait_for但*超时*是以毫秒为单位的整数。

这是一个协程

例:同wait_for



#### coro并发执行

> *uasyncio.gather(\*awaitables, return_exceptions=False)*

同时运行所有*等待*。任何不是任务的*等待项*都被提升为任务。

返回所有*awaitables*的返回值列表。

这是一个协程。

| 参数              | 类型    | 说明                                                         |
| ----------------- | ------- | ------------------------------------------------------------ |
| awaitables        | coro(s) | 多个task任务                                                 |
| return_exceptions | bool    | 仅关键字布尔型 `return_exceptions`确定任务取消或超时时的行为。<br>如果`False`将`gather` 立即终止，提高相关的异常应该被调用者被困。<br>如果`True`将`gather`继续阻塞，直到所有要么运行至完成或取消或超时被终止。在这种情况下，已终止的任务将在返回值列表中返回异常对象 |

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



### event(事件对象)

> *from usr.uasyncio import Event*
>
> *event = Event()*

创建一个可用于同步任务的新事件。事件以清除状态开始。



#### set设置事件

> *event.set()*

设置事件。任何等待事件的任务都将被安排运行。

注意：这必须从任务中调用。



#### is_set事件是否存在

> *event.is_set()*

`True`如果设置了事件，则返回，`False`否则返回。



#### clear清除事件

> *event.clear()*

清除事件



#### wait等待事件设置

> *event.wait()*

等待事件被设置。如果事件已经设置，那么它会立即返回。

这是一个协程。



### Lock(锁)

#### lock创建锁

> *from usr.uasyncio import Lock*
>
> *lock = asyncio.Lock()*

创建一个可用于协调任务的新锁。锁从解锁状态开始。

除了以下方法之外，还可以在语句中使用锁。`async with`

例:

```python
from usr.uasyncio import Lock
import usr.uasyncio as asyncio

async def task(i, lock):
    while 1:
        async with lock:
            print("Acquired lock in task", i)
            await asyncio.sleep(0.5)
 
async def main():
    lock = asyncio.Lock()  # The Lock instance
    for n in range(1, 4):
        asyncio.create_task(task(n, lock))
    await asyncio.sleep(10)

asyncio.run(main())  # Run for 10s
```

#### lock查看锁状态

> lock.locked()

`True`如果锁被锁定，则返回，否则返回`False`。

#### lock上锁

>  lock.acquire( )

等待锁处于解锁状态，然后以原子方式将其锁定。任何时候只有一个任务可以获取锁。

这是一个协程。

#### lock释放锁

> lock.release()

等待锁处于解锁状态，然后以原子方式将其锁定。任何时候只有一个任务可以获取锁。

这是一个协程。



### loop事件循环

#### loop获取

- 这表示调度和运行任务的对象。无法直接创建, 只能通过get_event_loop获取, 和new_event_loop()重置

> *import usr.uasyncio as asyncio*
>
> *loop = asyncio.get_event_loop()*

返回用于调度和运行任务的事件循环

```python
import usr.uasyncio as asyncio
import usys as sys

def _handle_exception(loop, context):
    print('Global handler')
    sys.print_exception(context["exception"])
    #loop.stop()
    sys.exit()  # Drastic - loop.stop() does not work when used this way

async def bar():
    await asyncio.sleep(0)
    1/0  # Crash

async def main():
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(_handle_exception)
    asyncio.create_task(bar())
    for _ in range(5):
        print('Working')
        await asyncio.sleep(0.5)

asyncio.run(main())
```



#### loop重置

重置事件循环并返回它。

注意：由于 MicroPython 只有一个事件循环，这个函数只是重置循环的状态，它不会创建一个新的循环。

> *asyncio.new_event_loop()*

例:

```python
import usr.uasyncio as asyncio

async def main():
    await asyncio.sleep(5)  # Dummy test script

def test():
    try:
        asyncio.run(main())
    except KeyboardInterrupt:  # Trapping this is optional
        print('Interrupted')  # or pass
    finally:
        asyncio.new_event_loop()  # Clear retained state
```

#### loop创建task

> *loop.create_task(coro)*

从给定的*coro*创建一个任务并返回新[`Task`]对象。



#### loop一直运行

> *loop.run_forever()*

运行事件循环直到[`stop()`]被调用。



#### loop停止循环

> *loop.stop()*

停止事件循环。



#### loop关闭循环

> *loop.close()*

关闭事件循环。



#### loop运行直到coro完成

> *loop.run_until_complete(awaitable)*



#### loop设置异常处理

> *loop.set_exception_handler(handler)*

设置异常处理程序以在 Task 引发未捕获的异常时调用。该*处理器*应该接受两个参数：。`(loop, context)`



#### loop获取异常处理器

> *loop.get_exception_handler()*

获取当前异常处理程序。返回处理程序，或者`None`如果未设置自定义处理程序。



#### loop设置默认异常处理程序

> *loop.default_exception_handler(context)*

调用的默认异常处理程序。



#### loop主动调用当前异常处理

> *loop.call_exception_handler(context)*

调用当前异常处理程序。参数*上下文*被传递并且是一个包含键的字典：`'message'`, `'exception'`, `'future'`。





## Stream[暂不支持]

## ThreadSafeFlag[暂不支持]