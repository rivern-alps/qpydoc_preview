# misc- 其他

 提供关机、软件重启、PWM以及ADC相关功能。

## 分集天线配置接口功能

### `misc.antennaSecRXOffCtrl`

```python
misc.antennaSecRXOffCtrl(*args)
```

分集天线配置、查询接口(EC200A系列支持该接口)。

**参数描述：**

该接口为可变参形式：
  参数个数为0，查询：misc.antennaSecRXOffCtrl()；
  参数个数为1，配置：misc.antennaSecRXOffCtrl(SecRXOff_set)。

- `SecRXOff_set`-int类型，范围0/1, `0`:不关闭分集天线 `1`:关闭分集天线。

**返回值描述：**

查询：成功返回分集天线配置，失败返回整型值`-1`；

设置：成功返回整形`0`,失败返回整型值`-1`。

**示例：**

```python
import misc

misc.antennaSecRXOffCtrl()
0
misc.antennaSecRXOffCtrl(1)
0
misc.antennaSecRXOffCtrl()
1
```

## 禁止网络灯功能

### `misc.net_light`

```python
misc.net_light([arg])
```

设置是否打开网络灯功能或查询网络灯是否打开。<a href="#label_pwmmap">点此查看</a>网络灯对应引脚。

> EC200A/EC600U/EC200U系列支持。

**参数描述：**
  传入参数时：设置网络灯功能是否打开；不传参数时：查询网络灯是否打开。

- `arg`-int类型，范围0/1，`0`：关闭网络灯功能；`1`：打开网络灯功能。

**返回值描述：**

查询：成功返回网络灯是否打开，`0`：关闭，`1`：打开；未设置过返回整型值`-1`；

设置：成功返回整形`0`,失败返回整型值`-1`。

> 设置重启生效；未设置过默认网络灯功能打开。

**示例：**

```python
import misc
misc.net_light()#未设置过
-1
misc.net_light(0)#设置关闭网络灯后重启模组
misc.net_light()#查询
0
misc.net_light(1)#设置打开网络灯后重启模组
misc.net_light()#查询
1
```

<span id="label_pwmmap">**网络灯引脚：**</span>

| 系列   | 对应引脚     |
| ------ | ------------ |
| EC200A | PIN4，PIN6   |
| EC200U | PIN5，PIN6   |
| EC600U | PIN52，PIN54 |

## Classes

- [class PowerKey – PowerKey按键回调注册](./misc.PowerKey.md)
- [class PWM – 脉宽调制](./misc.PWM.md)
- [class ADC - 模数转换](./misc.ADC.md)
- [class USB– USB插拔检测](./misc.USB.md)

## Submodules

- [module Power – 关机以及软件重启](./misc.Power.md)

- [module USBNET – USB网卡](./misc.USBNET.md)