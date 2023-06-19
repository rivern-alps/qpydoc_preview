# class PWM - 脉宽调制

提供脉宽调制输出功能。

> BC25系列不支持此模块。

## 构造函数

### `misc.PWM`

```python
class misc.PWM(PWM.PWMn,PWM.ABOVE_xx, highTime, cycleTime)
```

**参数描述：**

- `PWM.PWMn`-PWM通道，int类型,<a href="#label_pwmmap">点此查看</a>支持的通道与对应引脚；

- `PWM.ABOVE_xx`-时间取值范围，int类型,说明如下：

  EC200U/EC600U/EG915U系列:<br />PWM.ABOVE_MS				          ms级取值范围：(0,10]<br/>PWM.ABOVE_1US				        us级取值范围：(0,10000]<br/>PWM.ABOVE_10US				      us级取值范围：(1,10000]<br/>PWM.ABOVE_BELOW_US			ns级取值范围[100,65535]

- `highTime`-高电平时间，int类型，说明如下：

  ms级时，单位为ms<br/>us级时，单位为us<br/>ns级别：需要使用者计算<br/>               频率 = 13Mhz / cycleTime<br/>               占空比 = highTime/ cycleTime

- `cycleTime`-周期时间，int类型，说明如下：

  ms级时，单位为ms<br/>us级时，单位为us<br/>ns级别：需要使用者计算<br/>             频率 = 13Mhz / cycleTime<br/>             占空比 = highTime/ cycleTime

**示例：**

```python
 from misc import PWM
 pwm1 = PWM(PWM.PWM1, PWM.ABOVE_MS, 1, 2)
```

<span id="label_pwmmap">**PWM通道与物理引脚的映射关系：**</span>

| 系列   | 对应引脚                                                     |
| ------ | ------------------------------------------------------------ |
| EC600N | PWM0 – 引脚号52<br/>PWM1 – 引脚号53<br/>PWM2 – 引脚号70<br/>PWM3 – 引脚号69 |
| EC800N | PWM0 – 引脚号79<br/>PWM1 – 引脚号78<br/>PWM2 – 引脚号16<br/>PWM3 – 引脚号49 |
| EC200U | PWM0 – 引脚号135                                             |
| EC600U | PWM0 – 引脚号70                                              |
| EC600M | PWM0 – 引脚号57<br/>PWM1 – 引脚号56<br/>PWM2 – 引脚号70<br/>PWM3 – 引脚号69 |
| EG915U | PWM0 – 引脚号20                                              |
| EC800M | PWM0 – 引脚号83<br/>PWM1 – 引脚号78<br/>PWM2 – 引脚号16<br/>PWM3 – 引脚号49 |
| EG912N | PWM0 – 引脚号21<br/>PWM1 – 引脚号116<br/>PWM2 – 引脚号107<br/>PWM3 – 引脚号92 |
| EC200A | PWM0 – 引脚号1<br/>PWM1 – 引脚号4<br/>PWM2 – 引脚号6         |

## 方法

### `PWM.open`

```python
PWM.open()
```

该方法用于开启PWM输出。

**返回值描述：**

`0`表示开启成功，`-1`表示开启失败。

### `PWM.close`

```
PWM.close()
```

该方法用于关闭PWM输出。

**返回值描述：**

`0`表示关闭成功，`-1`表示关闭失败。

**示例：**

```python
from misc import PWM
import utime
if __name__ == '__main__':
    pwm = PWM(PWM.PWM0, PWM.ABOVE_MS, 1, 2)  # 初始化一个pwm对象
    pwm.open()  # 开启PWM输出
    utime.sleep(10)
    pwm.close()  # 关闭pwm输出
```

## 常量

| 常量     | 说明 | 使用平台                                                     |
| -------- | ---- | ------------------------------------------------------------ |
| PWM.PWM0 | PWM0 | EC600S / EC600N / EC100Y/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N |
| PWM.PWM1 | PWM1 | EC600S / EC600N / EC100Y/EC800N/EC600M/EC800M/EG912N         |
| PWM.PWM2 | PWM2 | EC600S / EC600N / EC100Y/EC800N/EC600M/EC800M/EG912N         |
| PWM.PWM3 | PWM3 | EC600S / EC600N / EC100Y/EC800N/EC600M/EC800M/EG912N         |

