# uwebsocket - websocket客户端

提供用于websocket连接使用



## 客户端连接

### uwebsocket.Client.connect

```python
ws_client = uwebsocket.Client.connect(url, headers=None, debug=False)
```

**参数描述：**:

* `url` -  str类型,  websocket的连接地址, 一般以"ws://xxx/"或"wss://xxx/"形式存在
* `headers` - dict类型,  额外需要添加的headers, 用于除了标准连接头之外, 允许用户自己传额外的头部
* `debug` - bool类型,  默认False, 当为True的情况下, 会输出日志



## send发送数据

### ws_client.send

```python
ws_client.send(msg)
```

**参数描述：**
* `msg` - str类型, 需要发送的数据



## recv接收数据

### ws_client.recv

```python
ws_client.recv()
```

**返回值描述：**
* `result `- str类型， recv接受返回的结果, 当接受空值或None的时候, 为连接被关闭



## 关闭连接

### ws_client.close

```python
ws_client.close()
```



**示例：**：

```python
import uwebsocket
import _thread


def recv(cli):
    while True:
        # 死循环接收数据
        recv_data = cli.recv()
        print("recv_data = {}".format(recv_data))
        if not recv_data:
            # 服务器关闭连接或客户端关闭连接
            print("cli close")
            client.close()
            break


# 创建客户端, debug=True输出日志, ip和端口需要自己填写, 或者是域名
client = uwebsocket.Client.connect('ws://xxx/', debug=True)

# 线程接收数据
_thread.start_new_thread(recv, (client,))

# 发送数据
client.send("this is a test msg")
```