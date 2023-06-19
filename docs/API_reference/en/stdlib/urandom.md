# urandom - Generate Random Numbers

urandom module provides the tool for random number generation.

## Generating Elements in Object obj Randomly

### `urandom.choice`

```python
urandom.choice(obj)
```

Generates elements in object obj randomly. The type of obj is string.

**Parameter**

* `obj` - String type.

**Return Value**

String type. Some random element in `obj`.

**Example**

```
>>> import urandom
>>> urandom.choice("QuecPython")
't'
```

## Generating A Decimal Number in the Range of k bits Randomly

### `urandom.getrandbits`

```python
urandom.getrandbits(k)
```

Generates a decimal number in the range of k bits randomly.

**Parameter**

* `k` - Integer type. Indicates the range.(Unit: bit)

**Return Value**

Integer type. A random decimal number in the range of k bits.

**Example**

```
>>> import urandom
>>> urandom.getrandbits(1)  #1 bit binary, ranging from 0 to 1 (decimal: 0–1)
1
>>> urandom.getrandbits(1)
0
>>> urandom.getrandbits(8)  #8 bit binary,ranging from 0000 0000 to 1111 11111 (decimal:0–255)
224
```

## Generating An Integer Between start And end Randomly

### `urandom.randint`

```
urandom.randint(start, end)
```

Generates an integer between start and end.

**Parameter**

* `start` - Integer type. The minimum value in the interval.
* `end` - Integer type. The maximum value in the interval.

**Return Value**

Integer type. A random integer between `start ` and  `end`.

**Example**

```
>>> import urandom
>>> urandom.randint(1, 4)
4
>>> urandom.randint(1, 4)
2
```

## Generating A Floating Point Between 0 and 1 Randomly

### `urandom.random`

```python
urandom.random()
```

Generates a floating point between 0 and 1.

**Return Value**

Floating point. The floating point between 0 and 1.

**Example**

```
>>> import urandom
>>> urandom.random()
0.8465231
```

## Generating A Positive Integer Ascending to step And Between start and end Randomly

### `urandom.randrange`

```python
urandom.randrange(start, end, step)
```

Generates a positive integer ascending to step and between start and end randomly.

**Parameter**

* `start` - Integer type. The minimum value in the interval.
* `end` - Integer type. The maximum value in the interval.
* `step` - Integer type. The length of ascending.

**Return Value**

Integer type. A random integer between  `start ` and `end`.

**Example**

```
>>> import urandom
>>> urandom.randrange(0, 8, 2)
0
>>> urandom.randrange(0, 8, 2)
6
```

## Specifying the Seed of A Random number

### `urandom.seed`

```python
urandom.seed(sed)
```

Specifies the seed of a random number, generally used in conjunction with other random number generation functions.

**Parameter**

* `sed` - Integer type.

**Example**

```python
>>> import urandom
>>> urandom.seed(20)  #Specifies the seed of a random number
>>> for i in range(0, 15): #Generates the random sequence in the range of 0–15
...     print(urandom.randint(1, 10))
...   
8
10
9
10
2
1
9
3
2
2
6
1
10
9
6
```

## Generating A Floating Point Between start And end Randomly

### `urandom.uniform`

```python
urandom.uniform(start, end)
```

**Parameter**

* `start` - Any type of real numbers. The minimum value in the interval.
* `end` - Any type of real numbers. The maximum value in the interval.

**Return Value**

Floating point. A random number between `start ` and  `end`.

**Example**

```
>>> import urandom
>>> urandom.uniform(3, 5)
3.219261
>>> urandom.uniform(3, 5)
4.00403
```

**Example**

```python
'''
@Author: Baron
@Date: 2020-06-22
@LastEditTime: 2020-06-22 17:16:20
@Description: example for module urandom
@FilePath: example_urandom_file.py
'''
import urandom as random
import log
import utime

'''
The following two global variables are necessary. You can modify the values of these two global variables based on project requirement
'''
PROJECT_NAME = "QuecPython_Random_example"
PROJECT_VERSION = "1.0.0"

log.basicConfig(level=log.INFO)
random_log = log.getLogger("random")


if __name__ == '__main__':
    # urandom.randint(start, end)
    # random between 1–4
    num = random.randint(1, 4)
    random_log.info(num)

    # random between 0–1
    num = random.random()
    random_log.info(num)

    # urandom.unifrom(start, end)
    # Generates a floating point between start and end
    num = random.uniform(2, 4)
    random_log.info(num)

    # urandom.randrange(start, end, step)
    # 2-bit binary,the range is [00–11] (0–3)
    num = random.getrandbits(2)
    random_log.info(num)

    # 8-bit binary,the range is [0000 0000–1111 11111] (0–255)
    num = random.getrandbits(8)
    random_log.info(num)

    # urandom.randrange(start, end, step)
    # Generates an ascending positive integer from start to end randomly
    num = random.randrange(2, 8, 2)
    random_log.info(num)

    # urandom.choice(obj)
    # Generates the number of elements in the object randomly
    num = random.choice("QuecPython")
    random_log.info(num)

```
