# atcmd - 发送AT指令功能

该模块提供发送AT指令的方法，使模组能够通过Python代码发送AT指令。



## 发送AT指令

### `atcmd.sendSync`

```
atcmd.sendSync(atcmd,resp,expect,timeout)
```

该方法用于向模组发送AT指令。

**参数描述：**

* `atcmd` - 需要发送的AT指令，字符串类型，必须包含'\r\n'。
* `resp` - AT指令返回的字符串内容，字符串类型。
* `expect` - 期望指令返回的结果中所包含的字符串，字符串类型，具体作用见下表：

| 值         | 含义                                                         |
| ---------- | ------------------------------------------------------------ |
| `空字符串` | 获取AT指令返回的所有数据(不包含‘OK’等结果性的字符数据)放入`resp`参数中; |
| `不为空`   | 筛选包含该字符串的数据放入`resp`参数中。                     |

* `timeout` - 超时时间，整型值，单位/秒。

**返回值描述：**

返回一个整型值，`0`表示成功，`非0`表示失败。

**示例：**

```python
>>> import atcmd
>>> resp=bytearray(50)
>>> atcmd.sendSync('at+cpin?\r\n',resp,'',20)
0
>>> print(resp)
bytearray(b'\r\n+CPIN: READY\r\n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

atcmd.sendSync('at+cpin\r\n',resp,'',20)
1
>>> print(resp)
bytearray(b'\r\nERROR\r\n\n
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
```
