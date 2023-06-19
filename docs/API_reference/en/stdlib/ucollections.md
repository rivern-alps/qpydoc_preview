
# ucollections - Collection and Container Types

Module features: ucollections module can create a container type that saves various objects. This module realizes subsets of the corresponding CPython module. See CPython file [collections](https://docs.python.org/3/library/collections.html) for more detailed information.

## `ucollections` Method
### `ucollections.namedtuple`

```python
mytuple = ucollections.namedtuple(name, fields)
```

Creates a `namedtuple` container type with a specific name and a set of fields. `namedtuple` is a subclass of the tuple that allows its fields to be accessed by index.

**Parameter**

- `name` - String type. Type name of the new container.
- `fields` - Tuple type. The new container type contains fields of the subtype.

**Example**

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

Creates a bidirectional queue for `deque`.

**Parameter**

- `iterable` - Tuple type. It must be an empty tuple.
- `maxlen` - Integer type. Specifies maxlen and limits the bidirectional queue to its maximum length.
- `flag` - Integer type. Optional parameter; 0 (default): Not check whether the queue overflows. If the queue continues to increase when it reaches the maximum length, the previous value will be discarded. 1: When the queue reaches the maximum specified length, IndexError: full will be displayed.

**Return Value:**

- deque object.



## deque Object Methods

### `deque.append`

```python
sdeque.append(data)
```

Inserts values into the queue.

**Parameter**

- `data` - Basic data type. Values need to be added to the queue.



### `deque.popleft`

```python
deque.popleft()
```

Removes the data on the left side of `deque` and returns the removed data. If `deque` is empty, it will lead to an index error.

**Return Value**

- Returns the popped value.

**Example**

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