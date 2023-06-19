# math - 数学运算

math 模块提供数学运算函数。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：[math](https://docs.python.org/3.5/library/math.html#module-math)

## 返回x的y次方

### `math.pow`

```python
math.pow(x, y)
```

返回x的y次方

**参数描述**

* `x`：任意实数类型
* `y`：任意实数类型

**返回值描述**
浮点数：`x`的 `y`次方

**示例：**

```
>>> import math
>>> math.pow(2, 3)
8.0
```

## 返回x的反余弦弧度值

### `math.acos`

```python
math.acos(x)
```

返回x的反余弦弧度值

**参数描述**

* `x`：任意实数类型，是-1~1之间的数，包括-1和1，如果小于-1或者大于1，会产生错误。

**返回值描述**
浮点数：`x`的反余弦弧度值

**示例：**

```
>>> import math
>>> math.acos(0.6)
0.9272952
```

## 返回x的反正弦弧度值

### `math.asin`

```python
math.asin(x)
```

返回x的反正弦弧度值

**参数描述**

* `x`：任意实数类型，是-1~1之间的数，包括-1和1，如果小于-1或者大于1，会产生错误。

**返回值描述**
浮点数：`x`的反正弦弧度值

**示例**：

```
>>> import math
>>> math.asin(-1)
-1.570796
```

## 返回x的反正切弧度值

### `math.atan`

```python
math.atan(x)
```

返回x的反正切弧度值

**参数描述**

* `x`：任意实数类型

**返回值描述**
浮点数：`x`的反正切弧度值

**示例：**

```
>>> import math
>>> math.atan(-8)
-1.446441
>>> math.atan(6.4)
1.4158
```

## 返回给定的 X 及 Y 坐标值的反正切值

### `math.atan2`

```python
math.atan2(x, y)
```

返回给定的 X 及 Y 坐标值的反正切值

**参数描述**

* `x`：任意实数类型
* `y`：任意实数类型

**返回值描述**
浮点数：坐标 (`x` ,`y`)的反正切值

**示例：**

```
>>> import math
>>> math.atan2(-0.50,0.48)
-0.8058035
>>> math.atan2(7, 9)
0.6610432
```

## 返回数字的上入整数

### `math.ceil`

```python
math.ceil(x)
```

返回数字的上入整数

**参数描述**

* `x`：任意实数类型

**返回值描述**
整数：`x`：大于等于入参的最小整数

**示例：**

```
>>> import math
>>> math.ceil(4.1)
5
```

## 把y的正负号加到x前面

### `math.copysign`

```python
math.copysign(x, y)
```

把y的正负号加到x前面

**参数描述**

* `x`：任意实数类型
* `y`：任意实数类型

**返回值描述**
浮点数，把 `y`的正负号加到 `x`前面

**示例：**

```
>>> import math
>>> math.copysign(5, 0)
5.0
>>> math.copysign(5, -4)
-5.0
>>> math.copysign(5, 9)
5.0
```

## 返回x的弧度的余弦值

### `math.cos`

```python
math.cos(x)
```

返回x的弧度的余弦值

**参数描述**

* `x`：任意实数类型

**返回值描述**
浮点数，`x`的弧度的余弦值，范围-1~1之间

**示例：**

```python
>>> import math
>>> math.cos(3)
-0.9899925
```

## 将弧度转换为角度

### `math.degrees`

```python
math.degrees(x)
```

将弧度转换为角度

**参数描述**

* `x`：任意实数类型

**返回值描述**
浮点数，弧度 `x`转换为角度

**示例：**

```
>>> import math
>>> math.degrees(5)
286.4789
>>> math.degrees(math.pi/2)
90.0
```

## 数学常量 `e`

### `math.e`

数学常量 `e`，`e`即自然常数。

## 返回e的x次幂

### `math.exp`

```python
math.exp(x)
```

返回e的x次幂

**参数描述**

* `x`：任意实数类型

**返回值描述**
浮点数，`e`的 `x`次幂

**示例：**

```
>>> import math
>>> math.exp(1)
2.718282
>>> print(math.e)
2.718282
```

## 返回数字的绝对值

### `math.fabs`

```python
math.fabs(x)
```

返回数字的绝对值

**参数描述**

* `x`：任意实数类型

**返回值描述**
浮点数，`x`的绝对值

**示例：**

```
>>> import math
>>> math.fabs(-3.88)
3.88
```

## 返回数字的下舍整数

### `math.floor`

```python
math.floor(x)
```

返回数字的下舍整数

**参数描述**

* `x`：任意实数类型

**返回值描述**
整数，`x`:小于等于入参的最大整数

**示例：**

```
>>> import math
>>> math.floor(8.7)
8
>>> math.floor(9)
9
>>> math.floor(-7.6)
-8
```

## 返回x/y的余数

### `math.fmod`

```python
math.fmod(x, y)
```

返回x/y的余数

**参数描述**

* `x`：任意实数类型
* `y`：任意实数类型

**返回值描述**
  `x`/`y`的余数，浮点数

**示例：**

```
>>> import math
>>> math.fmod(15, 4)
3.0
>>> math.fmod(15, 3)
0.0
```

## 返回由x的小数部分和整数部分组成的元组

### `math.modf`

```python
math.modf(x)
```

返回由x的小数部分和整数部分组成的元组。

**参数描述**

* `x`：任意实数类型
  

**返回值描述**
  `x`/`y`的余数，浮点数

**示例：**

```
>>> import math
>>> math.modf(17.592)
(0.5919991, 17.0)
```

## 返回一个元组(m,e)

### `math.frexp`

```python
math.frexp(x)
```

返回一个元组(m,e)

**参数描述**

* `x`：浮点数

**返回值描述**
返回一个元组 `(m,e)`,	以 (m, e) 对的形式返回 x 的尾数和指数。 m 是一个浮点数， e 是一个整数，正好是 x == m * 2**e 。 如果 x 为零，则返回 (0.0, 0) ，否则返回 0.5 <= abs(m) < 1 

**示例：**

```
>>> import math
>>> math.frexp(52)
(0.8125, 6)
```

## 判断 x 是否为有限数

### `math.isfinite`

```python
math.isfinite(x)
```

判断 x 是否为有限数

**参数描述**

* `x`,任意实数类型

**返回值描述**

判断 `x` 是否为有限数，是则返回 `True`，否则返回 `False`。

**示例：**

```
>>> import math
>>> math.isfinite(8)
True
```

## 判断是否无穷大或负无穷大

### `math.isinf`

```python
math.isinf(x)
```

判断是否无穷大或负无穷大

**参数描述**

* `x`,任意实数类型

**返回值描述**

如果 `x`是正无穷大或负无穷大，则返回 `True`,否则返回 `False`。

**示例：**

```
>>> import math
>>> math.isinf(123)
False
```

## 判断是否数字

### `math.isnan`

```python
pymath.isnan(x)
```

判断是否非数字（NaN）

**参数描述**

* `x`,任意实数类型

**返回值描述**

如果 `x`为非数字，返回 `True`,否则返回 `False`。

**示例：**

```
>>> import math
>>> math.isnan(23)
False
```

## 返回x*(2**i)的值

### `math.ldexp`

```python
math.ldexp(x, exp)
```

**返回x*(2^i)的值**

**参数描述**

* `x`,任意实数类型

**返回值描述**

浮点数，返回 `x`*(2**i)的值。

**示例：**

```
>>> import math
>>> math.ldexp(2, 1)
4.0
```

## 返回x的自然对数

### `math.log`

```python
math.log(x)
```

返回x的自然对数

**参数描述**

* `x`,任意实数类型，小于0会报错

**返回值描述**

浮点数，返回 `x`的自然对数

**示例：**

```
>>> import math
>>> math.log(2)
0.6931472
```

## 数学常量 pi

### `math.pi`

数学常量 pi（圆周率，一般以π来表示）。

## 将角度转换为弧度

### `math.radians`

```python
math.radians(x)
```

将角度转换为弧度

**参数描述**

* `x`,任意实数类型

**返回值描述**

浮点数，将角度 `x`转换为弧度

**示例：**

```
>>> import math
>>> math.radians(90)
1.570796
```

## 返回x弧度的正弦值

### `math.sin`

```python
math.sin(x)
```

返回x弧度的正弦值

**参数描述**

* `x`,任意实数

**返回值描述**

返回 `x`弧度的正弦值，数值在 -1 到 1 之间。

**示例：**

```
>>> import math
>>> math.sin(-18)
0.7509873
>>> math.sin(50)
-0.2623749
```

## 返回数字x的平方根

### `math.sqrt`

```python
math.sqrt(x)
```

返回x的平方根

**参数描述**

* `x`,任意实数类型

**返回值描述**

返回数字 `x`的平方根，返回值为浮点数。

**示例：**

```
>>> import math
>>> math.sqrt(4)
2.0
>>> math.sqrt(7)
2.645751
```

## 返回 x 弧度的正切值

### `math.tan`

```python
math.tan(x)
```

返回 x 弧度的正切值

**参数描述**

* `x`,任意实数类型

**返回值描述**

返回 `x` 弧度的正切值，数值在 -1 到 1 之间，为浮点数。

**示例：**

```
>>> import math
>>> math.tan(9)
-0.4523157
```

## 返回x的整数部分

### `math.trunc`

```python
math.trunc(x)
```

返回x的整数部分

**参数描述**

* `x`,任意实数类型

**返回值描述**

返回x的整数部分，为整数。

**示例：**

```
>>> import math
>>> math.trunc(7.123)
7
```

**使用示例**

```python
# 数学运算math函数示例

import math
import log
import utime


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Math_example"
PROJECT_VERSION = "1.0.0"


if __name__ == '__main__':
    # 设置日志输出级别
    log.basicConfig(level=log.INFO)
    math_log = log.getLogger("Math")

    # x**y运算后的值
    result = math.pow(2,3)
    math_log.info(result)
    # 8.0

    # 取大于等于x的最小的整数值，如果x是一个整数，则返回x
    result = math.ceil(4.12)
    math_log.info(result)
    # 5

    # 把y的正负号加到x前面，可以使用0
    result = math.copysign(2,-3)
    math_log.info(result)
    # -2.0

    # 求x的余弦，x必须是弧度
    result = math.cos(math.pi/4)
    math_log.info(result)
    # 0.7071067811865476

    # 把x从弧度转换成角度
    result = math.degrees(math.pi/4)
    math_log.info(result)
    # 45.0

    # e表示一个常量
    result = math.e
    math_log.info(result)
    # 2.718281828459045

    # exp()返回math.e(其值为2.71828)的x次方
    result = math.exp(2)
    math_log.info(result)
    # 7.38905609893065

    # fabs()返回x的绝对值
    result = math.fabs(-0.03)
    math_log.info(result)
    # 0.03

    # floor()取小于等于x的最大的整数值，如果x是一个整数，则返回自身
    result = math.floor(4.999)
    math_log.info(result)
    # 4

    # fmod()得到x/y的余数，其值是一个浮点数
    result = math.fmod(20,3)
    math_log.info(result)
    # 2.0

    # frexp()返回一个元组(m,e),其计算方式为：x分别除0.5和1,得到一个值的范围，2e的值在这个范围内，e取符合要求的最大整数值,然后x/(2e),得到m的值。如果x等于0,则m和e的值都为0,m的绝对值的范围为(0.5,1)之间，不包括0.5和1
    result = math.frexp(75)
    math_log.info(result)
    # (0.5859375, 7)

    # isfinite()如果x不是无穷大的数字,则返回True,否则返回False
    result = math.isfinite(0.1)
    math_log.info(result)
    # True

    # isinf()如果x是正无穷大或负无穷大，则返回True,否则返回False
    result = math.isinf(234)
    math_log.info(result)
    # False

    # isnan()如果x不是数字True,否则返回False
    result = math.isnan(23)
    math_log.info(result)
    # False

    # ldexp()返回x*(2**i)的值
    result = math.ldexp(5,5)
    math_log.info(result)
    # 160.0

    # modf()返回由x的小数部分和整数部分组成的元组
    result = math.modf(math.pi)
    math_log.info(result)
    # (0.14159265358979312, 3.0)

    # pi:数字常量，圆周率
    result = math.pi
    math_log.info(result)
    # 3.141592653589793

    # sin()求x(x为弧度)的正弦值
    result = math.sin(math.pi/4)
    math_log.info(result)
    # 0.7071067811865476

    # sqrt()求x的平方根
    result = math.sqrt(100)
    math_log.info(result)
    # 10.0

    # tan()返回x(x为弧度)的正切值
    result = math.tan(math.pi/4)
    math_log.info(result)
    # 0.9999999999999999

    # trunc()返回x的整数部分
    result = math.trunc(6.789)
    math_log.info(result)
    # 6

```
