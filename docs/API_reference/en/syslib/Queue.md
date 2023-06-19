# Queue - Message Queue

This feature is used for inter-thread communication.


## Constructor

### `queue.Queue`

```python
class queue.Queue(maxsize=100)
```

**Parameter**

`maxsize` - Integer type. The maximum queue length. Default value: 100. 

**Example**

```python
>>> from queue import Queue
>>> q = Queue(100)
```



## Put Data into Queue

### `Queue.put`

Puts data into the queue.

```python
Queue.put(data=None)
```

**Parameter**

* `data` - Data or signal put into the queue. Optional parameter. If this parameter is omitted, *data=None* will be configured by default. 

**Return Value**

True - Successful execution

False - Failed execution



## Get Data

### `Queue.get`

Gets data from the queue by blocking the queue.

```python
Queue.get()
```

**Return Value**

Data in the queue. 

None - The data in the queue is empty.



## Query Whether Queue Is Empty

### `Queue.empty`

```python
Queue.empty()
```

**Return Value**

True - Empty

False - Not empty



## Query Data Length in Queue

### `Queue.size`

```python
Queue.size()
```

**Return Value**

Integer type. The current data length.

**Example**

```python
import _thread
from queue import Queue

# Initialize the queue. The default length is 100. 
q = Queue()


def get():
    while True:
        # Get data by blocking the queue
        data = q.get()
        print("data = {}".format(data))

# Unblock the queue with a thread
_thread.start_new_thread(get, ())

# Put data into the queue
text = "hello world"
q.put(text)

# Get the data length in the queue
q.size()

# Determine whether the queue is empty 
q.empty()
```