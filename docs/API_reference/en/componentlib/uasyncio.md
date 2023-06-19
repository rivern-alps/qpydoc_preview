#  uasyncio  – Asynchronous I/O Scheduler

`uasyncio` is an asynchronous I/O library in MicroPython, also a lightweight subset of `asyncio` . It provides abstractions similar to coroutines and event loops in the standard library for running multiple coroutines concurrently and managing the execution and suspension of coroutines. `uasyncio` , with a small code size and low memory footprint, is suitable for embedded systems and resource–constrained devices. It provides a set of APIs and tools to create and manage coroutines, network and protocol–related classes that support asynchronous I/O.



## Create Coroutine



### uasyncio.create_task

Creates an asynchronous task to run the given coroutine.

```python
uasyncio.create_task(coro)
```

**Parameter**

* `coro` – The coroutine object to be run.

**Example**

```python
import usr.uasyncio as asyncio
async def my_coroutine():
    print("Running my_coroutine")

task = asyncio.create_task(my_coroutine())
```



##  Run Coroutine

### uasyncio.run

Runs a coroutine until it completes. This is the main way to start the event loop.

```python
uasyncio.run(coro)
```

**Parameter**

* `coro` – The coroutine object to be run.

**Example**

```python
import usr.uasyncio as asyncio

async def my_coroutine():
    print("Running my_coroutine")

asyncio.run(my_coroutine())
```

##  Cancel Task in Coroutine

### task.cancel

Cancels tasks.

```python
task.cancel()
```

**Example**

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
    # Cancel the task.
    task.cancel()

def main():
    task = asyncio.wait_for(bar(10), 7)
    asyncio.create_task(do_cancel(task))
    asyncio.sleep(1)

asyncio.run(main())
```



##  Sleep Coroutine

### uasyncio.sleep

Sleeps for `delay` seconds. Other tasks can run in the meanwhile.

```python
uasyncio.sleep(delay)
```

**Parameter**

* `delay` – Integer (or float) type. The time in seconds that the current task or coroutine will block. 



### uasyncio.sleep_ms

Sleeps for `delay` milliseconds. Other tasks can run in the meanwhile.

```python
uasyncio.sleep_ms(delay)
```

**Parameter**

* `t` – Integer (or float) type. The time in milliseconds that the current task or coroutine will block.



##  Cancel Task in Coroutine when Timeout

### uasyncio.wait_for

Waits for a coroutine to complete with a timeout in seconds. If the timeout elapses before the task is completed, the task is canceled and an exception will occur.

```python
uasyncio.wait_for(coro, timeout)
```

**Parameter**

* `coro` – Coroutine type. The coroutine object.
* `timeout` – Integer (or float) type. The timeout in seconds.

**Example**

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
    """Set the coroutine wait task"""
    task = asyncio.wait_for(bar(10), 7)
    """Start the coroutine. The coroutine displayed above indicates that if the task does not exit within 7 seconds, the coroutine is closed and an exception will occur."""
    asyncio.run(task)
    await asyncio.sleep(10)

asyncio.run(main())
```



### uasyncio.wait_for_ms

Waits for a coroutine to complete within a timeout in milliseconds. If the timeout elapses before the task is completed, the task is canceled and an exception will occur.

```python
uasyncio.wait_for_ms(coro, timeout)
```

**Parameter**

* `coro` – Coroutine type. The coroutine object.

* `timeout` – Integer (or float) type. The timeout in milliseconds.

  

## Run Coroutine Concurrently

### uasyncio.gather

Runs the given coroutines and collects the results. When all coroutines are completed, the function returns a result list. If `return_exceptions` is True, the raised exception will be returned as a result rather than raised immediately.

```python
uasyncio.gather(*coros, return_exceptions=False)
```

**Parameter**

* `coros` – Coroutine type. Single or multiple coroutine objects. 

* `return_exceptions` – Boolean type. Whether to return exceptions as the result.

  True: Return exceptions as the result.

  False: Not return exceptions as the result. (Default)

**Example**

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
        # When all coroutines are completed, if return_exceptions is True, the raised exception will be returned as a result rather than raised immediately.
        res = await asyncio.gather(*tasks, return_exceptions=True)
    except asyncio.TimeoutError:  # These only happen if return_exceptions is False
        print('Timeout')  # With the default times, cancellation occurs first
    except asyncio.CancelledError:
        print('Cancelled')
    print('Result: ', res)

asyncio.run(main())
```

