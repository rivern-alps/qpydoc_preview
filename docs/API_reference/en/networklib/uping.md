# uping - 发送ping包

该模块实现了 IPv4 ping 请求功能。

>1.可能会存在host地址无法建立socket连接异常。
>2.通过初始化参数中的`COUNT`和`INTERVAL`来确认发Ping包周期。

**示例：**

```python
# 方式一
# 打印输出方式
import uping
uping.ping('www.baidu.com')

# 以下是uping的输出, 无返回值
#72 bytes from 49.49.48.46: icmp_seq=1, ttl=53, time=1169.909000 ms
#72 bytes from 49.49.48.46: icmp_seq=2, ttl=53, time=92.060000 ms
#72 bytes from 49.49.48.46: icmp_seq=3, ttl=53, time=94.818000 ms
#72 bytes from 49.49.48.46: icmp_seq=4, ttl=53, time=114.879000 ms
#4 packets transmitted, 4 packets received, 0 packet loss
#round-trip min/avg/max = 92.06000000000001/367.916/1169.909 ms


# 方式二
# 设置quiet会得到输出结果
import uping
result = uping.ping('baidu.com', quiet=True)
# result可以拿到对应数据
# result(tx=4, rx=4, losses=0, min=76.93899999999999, avg=131.348, max=226.697)
```

## 发送 ping 请求

### `uping.ping`

```python
uping.ping(HOST, SOURCE=None, COUNT=4, INTERVAL=1000, SIZE=64, TIMEOUT=5000, quiet=False)
```

周期性发送Ping包。

**参数描述：**

- `HOST` - 主机名，字符串类型，所要ping的域名地址, 例如"baidu.com"。
- `SOURCE` - 源地址，字符串类型，用于绑定, 一般情况下不需要传。
- `COUNT` - 默认请求次数，整型，默认是4次,发送4次ping包。
- `INTERVAL` - 间隔时间，整型，用于绑定, 一般情况下不需要传。
- `SIZE` - 每次读取的包大小，整型，默认64, 无需修改。
- `TIMEOUT` - 超时时间，整型，单位:ms, 默认5000ms。
- `quiet` - 打印是否直接输出，布尔类型，默认:False,打印直接输出。若设为True, 默认打印的值会被转换成对象返回。

