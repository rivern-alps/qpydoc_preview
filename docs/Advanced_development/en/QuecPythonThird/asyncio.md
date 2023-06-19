

## About document

**Revision history **

| **Version** | **Date**   | **Author** | **Description** |
| ----------- | ---------- | ---------- | --------------- |
| 1.0         | 2021-09-26 | jaxsen.xu  | Initial version |



## Brief introduction

Asynchronous I/O Scheduler

## Terms explanation

- *uasyncio / asyncio*
  - Asyncio I/O module
- *coro*
  - *Coroutine*
  - Coroutine
- *
  - Shall exist
  - As for others, which can be cut



## Function modules

### core(Core function)

#### Create coro

> *uasyncio.create_task(coro)*

从给定的协程创建一个新任务并安排它运行。返回相应的[`Task`](https://docs.micropython.org/en/latest/library/uasyncio.html#uasyncio.Task)对象。只是创建未执行, 注意这个创建是在

Create a new task and run it based on the assigned coroutine. Correspondingly, the  [`Task`](https://docs.micropython.org/en/latest/library/uasyncio.html#uasyncio.Task) will be returned.

E. g

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

#### Run Coro

> *uasyncio.run(coro)*

Start task, multiple coros can be started here. 

```python
import usr.uasyncio as asyncio
async def bar(x):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        # Trigger the scheduler and concede these resources for the execution of other coroutimes. 
        await asyncio.sleep(2)  # Pause 1s
        print("sleep count instance = {} count = {}".format(x, count))
# Start a coroutine        
asyncio.run(bar(1))        

async def main():
    for x in range(10):
        asyncio.create_task(bar(x))
    await asyncio.sleep(10)
# Start the coroutines. Meanwhile, all tasks in coroutines will also be started. 
asyncio.run(main())
```

#### Cancel coro task

> task.cancel()

The task is created in coro.

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
    # Cancel task
    task.cancel()

def main():
    task = asyncio.wait_for(bar(10), 7)
    asyncio.create_task(do_cancel(task))
    asyncio.sleep(1)

asyncio.run(main())
```



#### Sleep coro

##### In millisecond level

> *uasyncio.sleep(t)*

Sleep ***t*** second (Floating Point  is also available), the sleep will trigger the scheduler and concede the cpu for the usage of other coroutines.

##### In second level

> *uasyncio.sleep_ms(t)*

Sleep ***t*** millisecond (Floating Point  is also available), the sleep will trigger the scheduler and concede the cpu for the usage of other coroutines.

### funcs (Appended function)

#### Strength coro, cancel task when timeout(second level)

> *uasyncio.wait_for(awaitable, timeout)*

It is a must to wait for the finish of awaitable, however, if there is a need in longer timeout, please cancel it. If the awitatable does not play the role of task, then create a task based on it. 

If timeout happens, it will cancel task and trigger `asyncio.TimeoutError`, which should be captured by scheduler.

Return the returned value of *awaitable*.

This is one coroutine.

- Parameter

| Parameter | Type      | Illustration                      |
| --------- | --------- | --------------------------------- |
| awaitable | coro      | Coroutine, one executed coroutine |
| timeout   | int/float | Delay at the level of second      |

E. g

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
    """Set coro to wait task"""
    task = asyncio.wait_for(bar(10), 7)
    """Start the coro, the above coro means that if the executed task does not exit within 7 seconds, the coro will be close, the error will happen correspondingly."""  
    asyncio.run(task)
    await asyncio.sleep(10)

asyncio.run(main())

```



#### Strength coro, cancel task when timeout (millisecond level)

> *uasyncio.wait_for_ms(awaitable, timeout)*

It is similar to wait_for, however, the timeout is an integer at the level of millisecond. 

This is also a coro.

E. g: Same as wait_for.



#### Concurrent execution of coro

> *uasyncio.gather(\*awaitables, return_exceptions=False)*

Run all awaitables simultaneously. And all awaitables who are not task will be upgraded to task. 

Return the returned list of all awaitables.

This is also a coro. 

| Parameter         | Type    | Illustration                                                 |
| ----------------- | ------- | ------------------------------------------------------------ |
| awaitables        | coro(s) | Multiple tasks                                               |
| return_exceptions | bool    | **The behaviour to confirm task cancellation or timeout is limited to key words such as `return_exceptions` of boolean type.  If the `gather`is suspended by `False`, then related exceptions will be stuck by scheduler if improve it. If the `gather`is congested by `True`, it will be suspended till all are executed to the end, or cancelled or overtime occurred. Under this circumstance, the suspended task will return exception object in returned value list** |



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
        # return_exceptions=True, Error occurs. It means the error task lsit will be returned only when waiting all tasks. 
        res = await asyncio.gather(*tasks, return_exceptions=True)
    except asyncio.TimeoutError:  # These only happen if return_exceptions is False
        print('Timeout')  # With the default times, cancellation occurs first
    except asyncio.CancelledError:
        print('Cancelled')
    print('Result: ', res)

asyncio.run(main())
```



### Event

> *from usr.uasyncio import Event*
>
> *event = Event()*

Create an new event that can be used to synchronise task. which starts from deleting status. 



#### Setting event

> *event.set()*

Setting event, all task of waiting events should run. 

Note: this task should be called from task. 



#### is_set event

> *event.is_set()*

IF the event is set, then return `True`, otherwise, it will return `False`. 



#### Clear event

> *event.clear()*

Clear event



#### Set waiting event

> *event.wait()*

Waiting event is set, if the event is set, it will return immediately. 

This is a coro.



### Lock

#### Create lock

> *from usr.uasyncio import Lock*
>
> *lock = asyncio.Lock()*

Create one new lock to coordinate tasks. The lock starts from unlock status. 

Except for following methods, it is also available to use lock in sentences.`async with`

 

E. g

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

#### Check lock status

> lock.locked()

If the lock is locked, it will return `True`, otherwise, it will return `False`.

#### Acquire lock

>  lock.acquire( )

The waiting lock is in as status of unlocking, then lock it via atomic. Only one task can acquire task at any time. 

This is a coro.

#### Release lock

> lock.release()

The waiting lock is in as status of unlocking, then lock it via atomic. Only one task can acquire task at any time. 

This is a coro.

### Cycle loop event

#### Get loop

- The call and the object of the running task can only be gotten via get_event_loop or resetting new_event_loop() instead of creating directly. 

> *import usr.uasyncio as asyncio*
>
> *loop = asyncio.get_event_loop()*

Return the event cycle used to call and run task. 

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



#### Reset loop

Reset event cycle and return it. 

Kindly reminder: Since there exists only one event cycle in MicroPython, this function just reset the cycle status without creating a new cycle. 

> *asyncio.new_event_loop()*

E. g.

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

#### Create loop task

> *loop.create_task(coro)*

Create a task via assigned coro and return new [`Task`] object. 



#### Run loop forever

> *loop.run_forever()*

Run event cycle till the [`stop()`] is called. 



#### Stop loop cycle

> *loop.stop()*

Stop event cycle



#### Close loop cycle

> *loop.close()*

Close event cycle



#### Running till the coro is finished

> *loop.run_until_complete(awaitable)*



#### Set exception handler in loop

> *loop.set_exception_handler(handler)*

Set exception handler program and call under the circumstance that the acquisition does not triggered by Task. Two parameters shall be accepted by this handler: `(loop, context)`.

#### Get exception handler in loop

> *loop.get_exception_handler()*

Get current exception handler program. It will return handler program or `None` if self-assigned handler program is not set.  



#### Set loop as default exception handler program

> *loop.default_exception_handler(context)*

Call default exception handler program.

#### Call current exception handler in loop actively

> *loop.call_exception_handler(context)*

Call current exception handler program. The contents of parameters with a dictionary of keys appended will be transmitted: `'message'`, `'exception'`, `'future'`.

## Stream[Does not support temporarily] 

## ThreadSafeFlag[Does not support temporarily]