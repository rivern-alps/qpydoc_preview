# class usocket - socket模块


该模块提供对BSD套接字接口的访问。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：[socket](https://docs.python.org/3.5/library/socket.html#module-socket)

**示例：**

```python
# 导入usocket模块
# -*- coding: UTF-8 -*-
import usocket
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Socket_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
socket_log = log.getLogger("SOCKET")

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        socket_log.info('Network connection successful!')

        # 创建一个socket实例
        sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
        # 解析域名
        sockaddr=usocket.getaddrinfo('www.tongxinmao.com', 80)[0][-1]
        # 建立连接
        sock.connect(sockaddr)
        # 向服务端发送消息
        ret=sock.send('GET /News HTTP/1.1\r\nHost: www.tongxinmao.com\r\nAccept-Encoding: deflate\r\nConnection: keep-alive\r\n\r\n')
        socket_log.info('send %d bytes' % ret)
        #接收服务端消息
        data=sock.recv(256)
        socket_log.info('recv %s bytes:' % len(data))
        socket_log.info(data.decode())

        # 关闭连接
        sock.close()
    else:
        socket_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```


## 构造函数

### `usocket.socket`

```python
class usocket.socket(af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP)
```

根据给定的地址族、套接字类型以及协议类型参数，创建一个新的套接字对象。注意，在大多数情况下不需要指定*proto*，也不建议这样做，因为某些MicroPython端口可能会省略 `IPPROTO_*`常量。

**参数描述：**

- `af` - 地址族（参考常量说明）。

- `type` - socket类型（参考常量说明）。

- `proto` - 协议号（参考常量说明）。


示例：
```python
import usocket
# 创建基于TCP的流式套接字
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
# 创建基于UDP的数据报套接字
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
# 创建基于TCP的服务端套接字
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM, usocket.IPPROTO_TCP_SER)
# 创建基于TCP的客户端套接字(配合bind使用，可自定义socket address)
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM, usocket.TCP_CUSTOMIZE_PORT)
```

### `usocket.getaddrinfo`

```python
usocket.getaddrinfo(host, port)
```

DNS域名解析，将主机域名（host）和端口（port）解析为用于创建套接字的5元组序列，元组结构如下：
`(family, type, proto, canonname, sockaddr)`

**参数描述：**

- `host` - 主机域名。
- `port` - 端口。

**返回值描述：**

- `family` - 地址族（参考常量说明）。
- `type` - socket类型（参考常量说明）。
- `proto` - 协议号（参考常量说明）。
- `canonname` - 主机域名。
- `sockaddr` - 包含地址和端口号的列表。

## 方法

### `socket.bind`

```python
socket.bind(address)
```

该方法用于套接字绑定指定address，必须尚未绑定。

> 1.作为服务器时，需要进行绑定，以固定服务器的address。
> 2.作为客户端时，绑定address用来指定套接字进行数据处理（配合usocket.TCP_CUSTOMIZE_PORT使用）。

**参数描述**

- `address` - 包含地址和端口号的元组或列表。

示例：
```
#绑定指定address
socket.bind(("192.168.0.1",80))
#绑定拨号IP，端口自定义（端口为0时，会自动分配）
socket.bind(("",0))
```

### `socket.listen`

```python
socket.listen(backlog)
```

该方法用于套接字服务端开启监听客户端连接，可指定最大客户端连接数。

**参数描述：**

- `backlog` - 接受套接字的最大个数，至少为0。

### `socket.accept`

```python
socket.accept()
```

该方法用于套接字服务端接受连接请求，成功返回元组，包含新的套接字和客户端地址以及客户端端口，形式为：`(conn, address, port)`。

**返回值：** 

- `conn` - 新的套接字对象，用来和客户端交互。
- `address` - 连接到服务器的客户端地址。
- `port` - 连接到服务器的客户端端口。

### `socket.connect`

```python
socket.connect(address)
```

该方法用于套接字连接到指定address的服务器。

**参数描述：**

- `address` - 包含地址和端口号的元组或列表。

示例：
```
#连接指定address
socket.connect(("192.168.0.1",80))
```

### `socket.read`

```python
socket.read( [ size ] )
```

该方法用于从套接字中读取size字节数据，返回一个字节对象。如果没有指定size，则会从套接字读取所有可读数据，直到读取到数据结束，此时作用和 `socket.readall()` 相同。

### `socket.readinto`

```python
socket.readinto(buf, [ , nbytes ])
```

该方法用于从套接字读取字节到缓冲区buf中。如果指定了nbytes，则最多读取nbytes数量的字节；如果没有指定nbytes，则最多读取len(buf)字节。返回值是实际读取的字节数。

### `socket.readline`

```python
socket.readline()
```

该方法用于从套接字按行读取数据，遇到换行符结束，返回读取的数据行。

### `socket.write`

```python
socket.write(buf)
```

该方法用于套接字发送缓冲区的数据，buf为待发送的数据，返回实际发送的字节数。

### `socket.send`

```python
socket.send(bytes)
```

该方法用于套接字发送数据，返回实际发送的字节数。

**参数描述：**

- `bytes` - bytes型数据。

### `socket.sendall`

```python
socket.sendall(bytes)
```

该方法用于套接字将所有数据都发送到套接字。与`send()`方法不同的是，此方法将尝试通过依次逐块发送数据来发送所有数据。
> 该方法再非阻塞套接字上的行为是不确定的，建议在MicroPython中，使用 `write()` 方法，该方法具有相同的“禁止短写”策略来阻塞套接字，并且将返回在非阻塞套接字上发送的字节数。

**参数描述：**

- `bytes` - bytes型数据。

### `socket.sendto`

```python
socket.sendto(bytes, address)
```

该方法用于套接字发送数据到指定*address*，返回实际发送的字节数。

**参数描述：**

- `bytes` - bytes型数据。
- `address` - 包含地址和端口号的元组或列表。

### `socket.recv`

```python
socket.recv(bufsize)
```

该方法用于从套接字接收数据。返回值是一个字节对象，表示接收到的数据。一次接收的最大数据量由bufsize指定。

**参数描述：**

- `bufsize` - 一次接收的最大数据量。

### `socket.recvfrom`

```python
socket.recvfrom(bufsize)
```

该方法用于从套接字接收数据。返回一个元组，包含字节对象和地址。返回值形式为：`(bytes, address)`。

**参数描述：**

- `bufsize` - 一次接收的最大数据量。

**返回值：**

- `bytes` ：接收数据的字节对象。
- `address` ：发送数据的套接字的地址。

### `socket.close`

```python
socket.close()
```

该方法用于将套接字标记为关闭并释放所有资源。

### `socket.setsockopt`

```python
socket.setsockopt(level, optname, value)
```

该方法用于设置套接字选项的值。

**参数描述：**

- `level` - 套接字选项级别。
- `optname` - socket功能选项。
- `value` - 既可以是一个整数，也可以是一个表示缓冲区的bytes类对象。

示例：
```
#设置端口复用允许
socket.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
#设置TCP保活包间隔时间，value 单位为分钟，范围：1-120
socket.setsockopt(usocket.SOL_SOCKET, usocket.TCP_KEEPALIVE, 1)
```

### `socket.setblocking`

```python
socket.setblocking(flag)
```

该方法用于设置套接字为阻塞模式或者非阻塞模式。该方法是 `settimeout()` 调用的简写。

**参数描述：**

- `flag` - 设置套接字是否阻塞（默认为阻塞模式）。

示例：
```
#将套接字设置为阻塞
`socket.setblocking(True)` 相当于 `socket.settimeout(None)`
#将套接字设置为非阻塞
`socket.setblocking(False)` 相当于 `socket.settimeout(0)`
```

### `socket.settimeout`

```python
socket.settimeout(value)
```

该方法用于设置套接字的发送和接收数据超时时间，单位秒。

**参数描述：**

- `value` - 可以是表示秒的非负浮点数，也可以是None。如果给定零，则将套接字置为非阻塞模式，否则套接字将处于阻塞模式。

### `socket.makefile`

```python
socket.makefile(mode='rb')
```

该方法用于返回与套接字关联的文件对象，返回值类型与指定的参数有关。仅支持二进制模式 (rb和wb)。

### `socket.getsocketsta`

```python
socket.getsocketsta()
```

该方法用于获取TCP套接字的状态。

> 1.BG95平台不支持该API。
> 2.如果调用了 `socket.close()` 方法之后，再调用 `socket.getsocketsta()` 会返回-1，因为此时创建的对象资源等都已经被释放。

**返回值：** 

| 状态值 | 状态        | 描述                                                         |
| ------ | ----------- | ------------------------------------------------------------ |
| 0      | CLOSED      | 套接字创建了，但没有使用这个套接字                           |
| 1      | LISTEN      | 套接字正在监听连接                                           |
| 2      | SYN_SENT    | 套接字正在试图主动建立连接，即发送SYN后还没有收到ACK         |
| 3      | SYN_RCVD    | 套接字正在处于连接的初始同步状态，即收到对方的SYN，但还没收到自己发过去的SYN的ACK |
| 4      | ESTABLISHED | 套接字已成功建立连接                                                   |
| 5      | FIN_WAIT_1  | 套接字已关闭，正在关闭连接，即发送FIN，没有收到ACK也没有收到FIN |
| 6      | FIN_WAIT_2  | 套接字已关闭，正在等待远程套接字关闭，即在FIN_WAIT_1状态下收到发过去FIN对应的ACK |
| 7      | CLOSE_WAIT  | 远程套接字已经关闭，正在等待关闭这个套接字，被动关闭的一方收到FIN |
| 8      | CLOSING     | 套接字已关闭，远程套接字正在关闭，暂时挂起关闭确认，即在FIN_WAIT_1状态下收到被动方的FIN |
| 9      | LAST_ACK    | 远程套接字已关闭，正在等待本地套接字的关闭确认，被动方在CLOSE_WAIT状态下发送FIN |
| 10     | TIME_WAIT   | 套接字已经关闭，正在等待远程套接字的关闭，即FIN、ACK、FIN、ACK都完毕，经过2MSL时间后变为CLOSED状态 |


## 常量

### `usocket.AF_INET`

地址族，IPV4类型。

### `usocket.AF_INET6`

地址族，IPV6类型。

### `usocket.SOCK_STREAM`

socket类型，TCP的流式套接字。

### `usocket.SOCK_DGRAM`

socket类型，UDP的数据包套接字。

### `usocket.SOCK_RAW`

socket类型，原始套接字。

### `usocket.IPPROTO_TCP`

协议号，TCP协议。

### `usocket.IPPROTO_UDP`

协议号，UDP协议。

### `usocket.IPPROTO_TCP_SER`

协议号，TCP服务器。

### `usocket.TCP_CUSTOMIZE_PORT`

协议号，TCP客户端自定义address使用。

### `usocket.SOL_SOCKET`

套接字选项级别。

### `usocket.SO_REUSEADDR`

socket功能选项，允许设置端口复用。

### `usocket.TCP_KEEPALIVE`

socket功能选项，设置TCP保活包间隔时间。
