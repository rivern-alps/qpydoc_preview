# KeyPad - Matrix Keyboard

This class provides the matrix keyboard interface.

> EC600SCN_LB, EC800NCN_LA, EC600NCN_LC, EC200UCN_LB, EC600UCN_LB, EC600MCN_LA, EC800MCN_LA, EC800MCN_GA, EG912NEN_AA series module is supported this feature.
>

## Constructor

### `machine.KeyPad`

```python
class machine.KeyPad(row,col)
```

**Parameter:**

- `row` - Integer type. Row number. It shall be greater than 0 and cannot exceed the maximum value supported by the module.
- `col` - Integer type. Column number. It shall be greater than 0. The value cannot exceed the maximum value supported by the module.

> If you do not set the row and column value, the default value is 4X4.

| Module        | Maximum Row | Maximum Column |
| ------------- | ----------- | -------------- |
| EC800N/EC600N | 4           | 4              |
| EC600S        | 5           | 5              |
| EC200U        | 4           | 3              |
| EC600U        | 6           | 6              |
| EC600M        | 5           | 5              |
| EC800M        | 5           | 5              |
| EG912N        | 3           | 3              |

**KeyPad Pin Correspondences:**

> When part of pins are used, you shall connect the keyboard and the pin according to row and column numbers in ascending order. For example, for EC600M, when a 2x2 matrix keyboard is used, the hardware will use 49, 51 and 48, 50 pins.  

| Module | Pin                                                          |
| ------ | ------------------------------------------------------------ |
| EC600M | Row number (output) and corresponding pins are as follows:<br/>Row number 0 – pin49<br/>Row number 1 – pin51<br/>Row number 2 – pin53<br/>Row number 3 – pin55<br/>Row number 4 – pin56<br/>Column number (input) and corresponding pins are as follows:<br/>Column number 0 – pin48<br/>Column number 1 – pin50<br/>Column number 2 – pin52<br/>Column number 3 – pin54<br />Column number 4 – pin57 |
| EC800M | Row number (output) and corresponding pins are as follows: <br/>Row number 0 – pin86<br/>Row number 1 – pin76<br/>Row number 2 – pin85<br/>Row number 3 – pin82<br/>Row number 4 – pin74<br/>Column number (input) and corresponding pins are as follows: <br/>Column number 0 – pin87<br/>Column number 1 – pin77<br/>Column number 2 – pin84<br/>Column number 3 – pin83<br/>Column number 4 – pin75 |
| EG912N | Row number (output) and corresponding pins are as follows: <br/>Row number 1 – pin20<br/>Row number 2 – pin16<br/>Row number 3 – pin116<br/>Column number (input) and corresponding pins are as follows:<br/>Column number 2 – pin105<br/>Column number 3 – pin21<br/>Column number 4 – pin1 |

**Example:**

```python
>>> # Creates a keypad object
>>> import machine
>>> keypad=machine.KeyPad(2,3)  # Sets a matrix keyboard with 2 rows and 3 columes
>>> keypad=machine.KeyPad()     # Default parameter. The default setting is a matrix keyboard with 4 rows and 4 columns
>>> keypad=machine.KeyPad(2)    # Sets the row value to 2. Default column Value. The default column value is 4. A matrix keyboard with 2 rows and 4 columes is initialized. 
```

## Methods

### `keypad.init`

```python
keypad.init()
```

This method initializes keypad settings.

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `keypad.set_callback`

```python
keypad.set_callback(usrFun)
```

This method sets callback function. After the external keyboard button is connected to the module, this callback function will be triggered when the external keyboard button is pressed and released.

**Parameter:**

- `usrFun` - Matrix keyboard callback function. Prototype:

  ```
  usrFun(result_list)
  ```

  Parameter of callback function:

  - `result_list[0]`: Key status (1 indicates the button is pressed and 0 indicates the button is released).

  - `result_list[1]`: Row number 

  - `result_list[2]`: Column number

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

### `keypad.deinit`

```python
keypad.deinit()
```

This method deinitializes to release initialized resources and callback function settings. 

**Return Value:**

`0` - Successful execution

`-1` - Failed execution

**Example:**

```python
import machine
import utime
is_loop = 1
keypad=machine.KeyPad()  
keypad.init()
def userfun(l_list):
    global is_loop 
    if  l_list[0] != 1 :
        is_loop = 0
        print('will exit')
    print(l_list)
keypad.set_callback(userfun)
loop_num = 0
while is_loop == 1 and loop_num < 10:
    utime.sleep(5)
    loop_num = loop_num +1
    print(" running..... ",is_loop,loop_num)
keypad.deinit()
print('exit!')
```
