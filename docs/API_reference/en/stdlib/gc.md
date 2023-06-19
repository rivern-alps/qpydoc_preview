# gc- Control the Garbage Collector

`gc` module realizes the garbage collection of the memory, and subsets of the corresponding CPython module. See CPython file [gc](https://docs.python.org/3.5/library/gc.html#module-gc) for more detailed information.

## Memory Reclamation

### `gc.enable`

```python
gc.enable()
```

Enables the mechanism for automatic reclaiming memory fragments.

### `gc.disable`

```python
gc.disable()
```

Disables the mechanism for automatic reclaiming memory fragments.

### `gc.isenabled`

```python
gc.isenabled()
```

Queries whether the mechanism for automatic reclaiming memory fragments is enabled.

**Return Value**

- True-The mechanism for automatic reclaiming memory fragments is enabled;

  False-The mechanism for automatic reclaiming memory fragments is disabled.

### `gc.collect`

```python
gc.collect()
```

Reclaims the memory fragments actively.

## Memory Query

### `gc.mem_alloc`

```python
gc.mem_alloc()
```

Queries the applied memory size which has been applied.

**Return Value**

- Returns the applied memory size. Unit: byte.

### `gc.mem_free`

```python
gc.mem_free()
```

Queries the remaining available memory size.

**Return Value**

- Returns the remaining available memory size. Unit: byte.

