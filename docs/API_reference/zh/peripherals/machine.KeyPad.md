# class KeyPad - 矩阵键盘

该类提供矩阵键盘接口。

> 支持的平台：EC200U系列、EC600U系列、EG915U系列、EC600M系列、EC800M/EG810M系列、EC600S系列、EC600N系列、EC800N系列、EG912N系列、EG915N系列

## 构造函数

### `machine.KeyPad`

```python
class machine.KeyPad(row,col)
```

**参数描述：**

- `row` - 行，int类型，大于0，不超过平台支持最大值。
- `col` - 列，int类型，大于0，不超过平台支持最大值。

> 如果row和col均不设置,默认为4X4。

| 平台          | 最大行 | 最大列 |
| ------------- | ------ | ------ |
| EC800N/EC600N | 4      | 4      |
| EC600S        | 5      | 5      |
| EC200U        | 4      | 3      |
| EC600U        | 6      | 6      |
| EC600M        | 5      | 5      |
| EC800M/EG810M | 5      | 5      |
| EG912N        | 3      | 3      |

**KeyPad引脚对应关系：**

> 当不使用全部引脚时，接线按行列号从小到大顺序接线，比如EC600M使用2x2矩阵键盘时，硬件使用49、51和48、50引脚。

| 平台          | 引脚                                                         |
| ------------- | ------------------------------------------------------------ |
| EC600M        | 行号（输出）对应引脚如下：<br/>行号0 – 引脚号49<br/>行号1 – 引脚号51<br/>行号2 – 引脚号53<br/>行号3 – 引脚号55<br/>行号4 – 引脚号56<br/>列号（输入）对应引脚如下：<br/>列号0 – 引脚号48<br/>列号1 – 引脚号50<br/>列号2 – 引脚号52<br/>列号3 – 引脚号54<br />列号4 – 引脚号57 |
| EC800M/EG810M | 行号（输出）对应引脚如下：<br/>行号0 – 引脚号86<br/>行号1 – 引脚号76<br/>行号2 – 引脚号85<br/>行号3 – 引脚号82<br/>行号4 – 引脚号74<br/>列号（输入）对应引脚如下：<br/>列号0 – 引脚号87<br/>列号1 – 引脚号77<br/>列号2 – 引脚号84<br/>列号3 – 引脚号83<br/>列号4 – 引脚号75 |
| EG912N        | 行号（输出）对应引脚如下：<br/>行号1 – 引脚号20<br/>行号2 – 引脚号16<br/>行号3 – 引脚号116<br/>列号（输入）对应引脚如下：<br/>列号2 – 引脚号105<br/>列号3 – 引脚号21<br/>列号4 – 引脚号1 |

**示例：**

```python
>>> # 创建keypad对象
>>> import machine
>>> keypad=machine.KeyPad(2,3)  # 设置为2行3列矩阵键盘
>>> keypad=machine.KeyPad()     # 参数缺省,默认设置为4行4列矩阵键盘
>>> keypad=machine.KeyPad(2)    # 行值设置为2,列值缺省,列值默认为4,初始化为2行4列矩阵键盘
```

## 方法

### `keypad.init`

```python
keypad.init()
```

该方法用于初始化keypad设置。

**返回值描述：**

设置成功返回整型值`0`，设置失败返回整型值`-1` 。

### `keypad.set_callback`

```python
keypad.set_callback(usrFun)
```

该方法用于设置回调函数，外接按键接入模组后，当外接键盘按键按放时会触发此回调函数。

**参数描述：**

- `usrFun` - 矩阵键盘回调函数，回调函数原型：

  ```python
  usrFun(result_list)
  ```

  回调函数参数描述：

  - `result_list[0]`：按键状态(1表示按下，0表示抬起)

  - `result_list[1]`：行号

  - `result_list[2]`：列号

**返回值描述：**

设置成功返回整型值`0`，设置失败返回整型值`-1` 。

### `keypad.deinit`

```python
keypad.deinit()
```

该方法用于解除初始化，释放初始化的资源和回调函数设置。

**返回值描述：**

设置成功返回整型值`0`，设置失败返回整型值`-1` 。

**使用示例：**

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
