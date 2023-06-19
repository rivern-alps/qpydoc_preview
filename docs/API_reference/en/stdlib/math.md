# math - Mathematical Functions

Math module provides mathematical operation functions, and realizes subsets of the corresponding CPython module. See CPython file [math](https://docs.python.org/3.5/library/math.html#module-math) for more detailed information.

## Returning x to the yth Power

### `math.pow`

```python
math.pow(x, y)
```

Returns x to the yth power.

**Parameter**

* `x`: Any type of real numbers.
* `y`: Any type of real numbers.

**Return Value**
Floating point.  `x` to the `y`th power.

**Example**

```
>>> import math
>>> math.pow(2, 3)
8.0
```

## Returning the Arccosine Radian Value of x 

### `math.acos`

```python
math.acos(x)
```

Returns the arccosine radian value of x. 

**Parameter**

* `x`: Any type of real numbers that range from -1 to 1, including -1 and 1. If it is smaller than -1 or larger than 1, the error will be generated.

**Return Value**
Floating point. The arccosine radian value of `x`. 

**Example**

```
>>> import math
>>> math.acos(0.6)
0.9272952
```

## Returning the Arcsine Radian Value of x

### `math.asin`

```python
math.asin(x)
```

Returns the arcsine radian value of x.

**Parameter**

* `x`: Any type of real numbers that range from -1 to 1, including -1 and 1. If it is less than -1 or greater than 1, the error will be generated.

**Return Value**
Floating point. The arcsine radian value of `x`.

**Example**

```
>>> import math
>>> math.asin(-1)
-1.570796
```

## Returning the Arctangent Radian Value of x

### `math.atan`

```python
math.atan(x)
```

Returns the arctangent radian value of x.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**
Floating point. The arctangent radian value of `x`.

**Example**

```
>>> import math
>>> math.atan(-8)
-1.446441
>>> math.atan(6.4)
1.4158
```

## Returning the Arc-tangent Value of the Given x and y Coordinate Values

### `math.atan2`

```python
math.atan2(x, y)
```

Returns the arctangent value of the given X and Y coordinate values.

**Parameter**

* `x`: Any type of real numbers.
* `y`: Any type of real numbers.

**Return Value**
Floating point. The arctangent value of the coordinate (`x` ,`y`).

**Example**

```
>>> import math
>>> math.atan2(-0.50,0.48)
-0.8058035
>>> math.atan2(7, 9)
0.6610432
```

## Returning the Integer of A Number Obtained by Rounding up

### `math.ceil`

```python
math.ceil(x)
```

Returns the integer of a number obtained by rounding up.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**
Integer type. `x`: The minimum integer which is greater than or equal to the input parameter.

**Example**

```
>>> import math
>>> math.ceil(4.1)
5
```

## Putting the Plus or Minus Symbol of y in front of x

### `math.copysign`

```python
math.copysign(x, y)
```

Puts the plus or minus symbol of y in front of x.

**Parameter**

* `x`: Any type of real numbers.
* `y`: Any type of real numbers.

**Return Value**
Floating point. The value after putting the  plus or minus symbol of `y` in front of `x`.

**Example**

```
>>> import math
>>> math.copysign(5, 0)
5.0
>>> math.copysign(5, -4)
-5.0
>>> math.copysign(5, 9)
5.0
```

## Returning the Cosine Value of the x Radian

### `math.cos`

```python
math.cos(x)
```

Returns the cosine value of the x radian.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**
Floating point. The cosine value of the `x` radian which ranges from -1 to 1.

**Example**

```python
>>> import math
>>> math.cos(3)
-0.9899925
```

## Converting the Radian to the Angle

### `math.degrees`

```python
math.degrees(x)
```

Converts the radian to the angle.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**
Floating point. The angle which is converted by radian `x`.

**Example**

```
>>> import math
>>> math.degrees(5)
286.4789
>>> math.degrees(math.pi/2)
90.0
```

## Mathematical Constant `e`

### `math.e`

The mathematical constant `e` is a natural constant.

## Returning e to the xth Power

### `math.exp`

```python
math.exp(x)
```

Returns e to the xth power.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**
Floating point.  `e` to the `x`th power.

**Example**

```
>>> import math
>>> math.exp(1)
2.718282
>>> print(math.e)
2.718282
```

## Returning the Absolute Value of a Number

### `math.fabs`

```python
math.fabs(x)
```

Returns the absolute value of a number.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**
Floating point. The absolute value of `x`.

**Example**

```
>>> import math
>>> math.fabs(-3.88)
3.88
```

## Returning the Integer of a Number Obtained by Rounding down

### `math.floor`

```python
math.floor(x)
```

Returns the integer of a number obtained by rounding down.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**
Integer type. `x`: The maximum integer which is less than or equal to the input parameter.

**Example**

```
>>> import math
>>> math.floor(8.7)
8
>>> math.floor(9)
9
>>> math.floor(-7.6)
-8
```

## Returning the Remainder of x/y

### `math.fmod`

```python
math.fmod(x, y)
```

Returns the remainder of x/y.

**Parameter**

* `x`: Any type of real numbers.
* `y`: Any type of real numbers.

**Return Value**
Floating point. The remainder of `x`/`y`.

**Example**

```
>>> import math
>>> math.fmod(15, 4)
3.0
>>> math.fmod(15, 3)
0.0
```

## Returning a Tuple Consisting of the Decimal and Integer Parts of x

### `math.modf`

```python
math.modf(x)
```

Returns a tuple consisting of the decimal and integer parts of x.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**
Floating point. The remainder of `x`/`y`.

**Example**

```
>>> import math
>>> math.modf(17.592)
(0.5919991, 17.0)
```

## Returning a Tuple (m,e)

### `math.frexp`

```python
math.frexp(x)
```

Returns a tuple (m,e).

**Parameter**

* `x`: Floating point.

**Return Value**
Returns a tuple `(m,e)` , and returns the mantissa and exponent of x in the form of (m,e) . m is a floating point, e is an integer, and x == m * 2**e. If x is 0, (0.0, 0) will be returned, otherwise 0.5 <= abs(m) < 1 will be returned.

**Example**

```
>>> import math
>>> math.frexp(52)
(0.8125, 6)
```

## Determining Whether x Is a Finite Number

### `math.isfinite`

```python
math.isfinite(x)
```

Determines whether x is a finite number.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**

Determines whether `x` is a finite number. If `x` is a finite number, `True` will be returned, otherwise `False` will be returned.

**Example**

```
>>> import math
>>> math.isfinite(8)
True
```

## Determining Whether x Is an Infinity Number or a Minus Infinity Number

### `math.isinf`

```python
math.isinf(x)
```

Determines whether x is an infinity number or a minus infinity number.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**

If `x` is an infinity number or a minus infinity number, `True` will be returned, otherwise `False` will be returned.

**Example**

```
>>> import math
>>> math.isinf(123)
False
```

## Determining Whether x Is Not a Number

### `math.isnan`

```python
pymath.isnan(x)
```

Determines whether x is not a number (NaN).

**Parameter**

* `x`: Any type of real numbers.

**Return Value**

If `x` is not a number, `True` will be returned, otherwise `False` will be returned.

**Example**

```
>>> import math
>>> math.isnan(23)
False
```

## Returning the Value of x*(2**i)

### `math.ldexp`

```python
math.ldexp(x, exp)
```

**Returns the value of x*(2^i)**

**Parameter**

* `x`: Any type of real numbers.

**Return Value**

Floating point. The value of `x`*(2**i).

**Example**

```
>>> import math
>>> math.ldexp(2, 1)
4.0
```

## Returning the Natural Logarithm of x

### `math.log`

```python
math.log(x)
```

Returns the natural logarithm of x.

**Parameter**

* `x` : Any type of real numbers. If it is less than 0, the error will be reported.

**Return Value**

Floating point. The natural logarithm of `x`.

**Example**

```
>>> import math
>>> math.log(2)
0.6931472
```

## Mathematical Constant pi

### `math.pi`

Mathematical constant pi (Pi, which is generally expressed as π).

## Converting the Angle to the Radian

### `math.radians`

```python
math.radians(x)
```

Converts the angle to the radian.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**

Floating point. The radian which is converted by the angle `x`.

**Example**

```
>>> import math
>>> math.radians(90)
1.570796
```

## Returning the Sine Value of x Radian

### `math.sin`

```python
math.sin(x)
```

Returns the sine value of x radian.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**

Returns the sine value of `x` radian which ranges from -1 to 1.

**Example**

```
>>> import math
>>> math.sin(-18)
0.7509873
>>> math.sin(50)
-0.2623749
```

## Returning the Square Root of the Number x

### `math.sqrt`

```python
math.sqrt(x)
```

Returns the square root of x.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**

Floating point. The square root of `x`.

**Example**

```
>>> import math
>>> math.sqrt(4)
2.0
>>> math.sqrt(7)
2.645751
```

## Returning the Tangent Value of x Radian

### `math.tan`

```python
math.tan(x)
```

Returns the tangent value of x radian.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**

Floating point. The tangent value of `x` radian which ranges from -1 to 1.

**Example**

```
>>> import math
>>> math.tan(9)
-0.4523157
```

## Returning the Integer Part of x.

### `math.trunc`

```python
math.trunc(x)
```

Returns the integer part of x.

**Parameter**

* `x`: Any type of real numbers.

**Return Value**

Integer type. The integer part of x.

**Example**

```
>>> import math
>>> math.trunc(7.123)
7
```

**Example**

```python
# The example of mathematical operation math()

import math
import log
import utime


'''
The following two global variables are necessary. You can modify the values of these two global variables based on project requirement
'''
PROJECT_NAME = "QuecPython_Math_example"
PROJECT_VERSION = "1.0.0"


if __name__ == '__main__':
    # Sets the log output level
    log.basicConfig(level=log.INFO)
    math_log = log.getLogger("Math")

    # The value of x**y
    result = math.pow(2,3)
    math_log.info(result)
    # 8.0

    # Takes the minimum integer that is greater than or equal to x. If x is an integer, x will be returned
    result = math.ceil(4.12)
    math_log.info(result)
    # 5

    # You can use 0 when putting the plus or minus symbol of y in front of x
    result = math.copysign(2,-3)
    math_log.info(result)
    # -2.0

    # x must be a radian when evaluating the cosine value of x
    result = math.cos(math.pi/4)
    math_log.info(result)
    # 0.7071067811865476

    # Converts x from the radian to the angle
    result = math.degrees(math.pi/4)
    math_log.info(result)
    # 45.0

    # e indicates a constaant 
    result = math.e
    math_log.info(result)
    # 2.718281828459045

    # exp() returns math.e(the value is 2.71828) to the xth power
    result = math.exp(2)
    math_log.info(result)
    # 7.38905609893065

    # fabs() returns the abosulate value of x  
    result = math.fabs(-0.03)
    math_log.info(result)
    # 0.03

    # floor() takes the maximum integer less than or equal to x. If x is an integer, x will be returned
    result = math.floor(4.999)
    math_log.info(result)
    # 4

    # fmod() gets the remainder of x/y. It is a floating point
    result = math.fmod(20,3)
    math_log.info(result)
    # 2.0

    # frexp() returns a tuple (m,e), the following is its formula method: Divide x by 0.5 and 1 respectively, then get a range of the value in which the value of 2e is in this range.e takes the maximum integer that meets the requirement. Then evaluates x/(2e), and the value of m will be got.If x is equal to 0, then both the value of m and e are 0.The absolute value of m ranges from (0.5,1), excluding 0.5 and 1
    result = math.frexp(75)
    math_log.info(result)
    # (0.5859375, 7)

    # isfinite() If x is a finite number, True will be returned. Otherwise False will be returned
    result = math.isfinite(0.1)
    math_log.info(result)
    # True

    # isinf() If x is an infinity number or a minus infinity number, True will be returned. Otherwise False will be returned
    result = math.isinf(234)
    math_log.info(result)
    # False

    # isnan() If x is not a number, True will be returned. Otherwise False will be returned.
    result = math.isnan(23)
    math_log.info(result)
    # False

    # ldexp() returns the value of x*(2**i)
    result = math.ldexp(5,5)
    math_log.info(result)
    # 160.0

    # modf() returns a tuple consisting of the decimal and integer parts of x
    result = math.modf(math.pi)
    math_log.info(result)
    # (0.14159265358979312, 3.0)

    # pi: Mathematical constant,Pi
    result = math.pi
    math_log.info(result)
    # 3.141592653589793

    # sin() evaluates the sine value of x(x is a radian)
    result = math.sin(math.pi/4)
    math_log.info(result)
    # 0.7071067811865476

    # sqrt() evaluates the square root of x
    result = math.sqrt(100)
    math_log.info(result)
    # 10.0

    # tan() returns the tangent value of x(x is a radian)
    result = math.tan(math.pi/4)
    math_log.info(result)
    # 0.9999999999999999

    # trunc() returns the integer part of x
    result = math.trunc(6.789)
    math_log.info(result)
    # 6

```
