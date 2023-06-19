# urandom - 生成随机数

urandom 模块提供了生成随机数的工具。

## 随机生成对象 obj 中的元素

### `urandom.choice`

```python
urandom.choice(obj)
```

随机生成对象 obj 中的元素，obj 类型 string。

**参数描述**

* `obj`，str类型

**返回值描述**

`obj`中随机某个元素，str

**示例**：

```
>>> import urandom
>>> urandom.choice("QuecPython")
't'
```

## 随机产生一个在k bits范围内的十进制数

### `urandom.getrandbits`

```python
urandom.getrandbits(k)
```

随机产生一个在k bits范围内的十进制数。

**参数描述**

* `k`，int类型，表示范围（单位bit）

**返回值描述**

int类型，在k bits范围内的十进制随机数

**示例**：

```
>>> import urandom
>>> urandom.getrandbits(1)  #1位二进制位，范围为0~1（十进制：0~1）
1
>>> urandom.getrandbits(1)
0
>>> urandom.getrandbits(8)  #8位二进制位，范围为0000 0000~1111 11111（十进制：0~255）
224
```

## 随机生成一个 start 到 end 之间的整数

### `urandom.randint`

```
urandom.randint(start, end)
```

随机生成一个 start 到 end 之间的整数。

**参数描述**

* `start`，int类型，区间最小值
* `end`，int类型，区间最大值

**返回值描述**

int类型，在`start `到 `end` 之间的随机整数

**示例**：

```
>>> import urandom
>>> urandom.randint(1, 4)
4
>>> urandom.randint(1, 4)
2
```

## 随机生成一个 0 到 1 之间的浮点数

### `urandom.random`

```python
urandom.random()
```

随机生成一个 0 到 1 之间的浮点数。

**返回值描述**

浮点数，在0 到 1 之间。

**示例**：

```
>>> import urandom
>>> urandom.random()
0.8465231
```

## 随机生成 start 到 end 间并且递增为 step 的正整数

### `urandom.randrange`

```python
urandom.randrange(start, end, step)
```

随机生成 start 到 end 间并且递增为 step 的正整数。

**参数描述**

* `start`，int类型，区间最小值
* `end`，int类型，区间最大值
* `step`，int类型，递增长度

**返回值描述**

int类型，在 `start `到 `end` 之间的随机整数

**示例**：

```
>>> import urandom
>>> urandom.randrange(0, 8, 2)
0
>>> urandom.randrange(0, 8, 2)
6
```

## 指定随机数种子

### `urandom.seed`

```python
urandom.seed(sed)
```

指定随机数种子，通常和其它随机数生成函数搭配使用。

**参数描述**

* `sed`，int类型

**示例**：

```python
>>> import urandom
>>> urandom.seed(20)  #指定随机数种子
>>> for i in range(0, 15): #生成0~15范围内的随机序列
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

## 随机生成 start 到 end 范围内的浮点数

### `urandom.uniform`

```python
urandom.uniform(start, end)
```

**参数描述**

* `start`，任意实数类型，区间最小值
* `end`，任意实数类型，区间最大值

**返回值描述**

浮点数类型，在 `start `到 `end` 之间的随机数

**示例**：

```
>>> import urandom
>>> urandom.uniform(3, 5)
3.219261
>>> urandom.uniform(3, 5)
4.00403
```

**使用示例**

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
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Random_example"
PROJECT_VERSION = "1.0.0"

log.basicConfig(level=log.INFO)
random_log = log.getLogger("random")


if __name__ == '__main__':
    # urandom.randint(start, end)
    # 随机1 ~ 4之间
    num = random.randint(1, 4)
    random_log.info(num)

    # random between 0~1
    num = random.random()
    random_log.info(num)

    # urandom.unifrom(start, end)
    # 在开始和结束之间生成浮点数
    num = random.uniform(2, 4)
    random_log.info(num)

    # urandom.randrange(start, end, step)
    # 2-bit binary,the range is [00~11] (0~3)
    num = random.getrandbits(2)
    random_log.info(num)

    # 8-bit binary,the range is [0000 0000~1111 11111] (0~255)
    num = random.getrandbits(8)
    random_log.info(num)

    # urandom.randrange(start, end, step)
    # 从开始到结束随机生成递增的正整数
    num = random.randrange(2, 8, 2)
    random_log.info(num)

    # urandom.choice(obj)
    # 随机生成对象中元素的数量
    num = random.choice("QuecPython")
    random_log.info(num)

```
