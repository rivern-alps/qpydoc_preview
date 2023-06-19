# system - 环境配置

模块功能：用于配置系统环境的参数以及功能

> 适配版本：EC100Y(V0009)及以上；EC600S(V0002)及以上。


### `system.replSetEnable`

```python
system.replSetEnable(flag，**kw_args)
```

开启/关闭交互保护,交互保护设置，参数设置如下

1、只有一个参数flag时：

0表示关闭，1表示开启，2表示查询当前加密状态；设置开启交互保护后所有外部指令以及代码都无法执行，为不可逆操作，请确认后开启，默认不开启。

2、有两个参数时：

表示交互保护可通过密码开启和关闭(少数平台不支持密码保护功能，所以当遇到不支持的平台，输入密码会直接报错。如：BC25,600M)

**参数描述：**

* `flag` -  int类型， 0 : 不开启（默认）；1 ：开启；2：查询加密状态
* `kw_args` -  password，可为空 ，字符串类型

**返回值描述：**

* 成功返回整型值0；

* 失败返回整型值-1或者是errorlist

如果是查询加密状态，返回值：
-1：查询失败
1：repl enable
2：repl enable but The password has already been set
3：repl refuse
4：repl-protection by password


### `system.replChangPswd`

```python
system.replChangPswd(old_password,new_password)
```

更改交互保护密码

**参数描述：**

* `old_password` -  旧密码 长度限制：6-12字节，字符串类型
* `new_password` -  新密码 长度限制：6-12字节，字符串类型

**返回值描述：**

* 成功返回整型值0；

* 失败返回整型值-1或者是errorlist

**示例：**

```python
>>>import system

>>> system.replSetEnable(1,password='miamia123')//开机首次设置密码并开启交互保护，可设置任意长度在6-12位之间的密码内容
0
>>>                                            //设置成功，交互口被锁，需要输入密码才能正常使用
Please enter password:
>>> ******                                     //密码错误
Incorrect password, please try again:
>>> ********                                   //密码错误
Incorrect password, please try again:
>>> *********                                  //密码正确，可正常交互
REPL enable
>>> system.replSetEnable(2)
2
>>>

>>> system.replSetEnable(1,password='miamia') //已经设置过密码，如果需要重新锁住交互口，需要输入正确密码
Incorrect password!
-1
>>> system.replSetEnable(1,password='miamia123')
0
>>> 
Please enter password:                        //交互口重新锁住
>>> miamia123
*********
REPL enable
>>> system.replSetEnable(2)
2


>>> system.replChangPswd(old_password='miamia123',new_password='123456') //change password
0
>>> system.replSetEnable(1,password='miamia123')                         //更改密码成功之后，继续用老密码锁交互口，提示密码不正确
Incorrect password!
-1
>>> system.replSetEnable(1,password='123456')                            //新密码重新加锁交互口，成功
0
>>> 
Please enter password:
>>> ******
REPL enable

>>> system.replSetEnable(0,password='123456')          //取消密码保护（取消加密保护之后可使用任意新密码重新加锁交互口）

0
>>> 
>>> system.replSetEnable(2)                            //查询状态为repl enable
1
>>> system.replSetEnable(0)                           //默认就已经是0
0
>>>system.replSetEnable(1)                            //开启交互保护
>>>
REPL refuse
>>>
```
