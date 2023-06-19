# ussl - SSL加密通信

ussl模块实现了TLS/SSL加密通信功能, 主要用于单向和双向认证使用。



## 创建SSL连接通道

### `ussl.wrap_socket`

```python
ussl.wrap_socket(sock,server_hostname=None,cert=None,key=None)
```

**参数描述：**

- `sock` - usocket.socket对象, 必须参数,要包装的套接字（usocket.socket）对象

- `server_hostname` - 字符串类型, 可选参数, 服务器IP地址

- `cert` - 字符串类型,  可选参数, 数字证书数据

- `key` - 字符串类型, 可选参数, 私钥数据

**返回值描述：**

返回一个被包装的`usocket.socket`对象



**示例：**

```python
# 导入ussl模块
# -*- coding: UTF-8 -*-
import ussl
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
        # 1. 单向认证说明
        # 创建一个socket实例
        sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
        # 解析域名
        sockaddr=usocket.getaddrinfo('myssl.com', 443)[0][-1]
        # 建立连接
        sock.connect(sockaddr)
        # SSL连接. 前提需要服务器支持
        sock = ussl.wrap_socket(sock, server_hostname="myssl.com")
        # 向服务端发送消息
        ret = sock.write('GET / HTTP/1.0\r\nHost: myssl.com\r\nAccept-Encoding: deflate\r\n\r\n')
        socket_log.info('write %d bytes' % ret)
        #接收服务端消息
        data=sock.read(256)
        socket_log.info('read %s bytes:' % len(data))
        socket_log.info(data.decode())

        # 关闭连接
        sock.close()
        socket_log.info('--------------------Socket Ussl End-------------------')
    else:
        socket_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))

# 2. 双向认证说明
cert = "数据证书"
key = "私钥"
sock = ussl.wrap_socket(sock, server_hostname="myssl.com", cert=cert, key=key)

```



## ssl加密算法套件支持



| 算法套件                                               |
| ------------------------------------------------------ |
| TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 (0xcca9) |
| TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (0xccaa)     |
| TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (0xcca8)   |
| TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 (0xc02c)       |
| TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xc030)         |
| TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 (0x009f)           |
| TLS_ECDHE_ECDSA_WITH_AES_256_CCM (0xc0ad)              |
| TLS_DHE_RSA_WITH_AES_256_CCM (0xc09f)                  |
| TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 (0xc024)       |
| TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (0xc028)         |
| TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 (0x006b)           |
| TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA (0xc00a)          |
| TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (0xc014)            |
| TLS_DHE_RSA_WITH_AES_256_CBC_SHA (0x0039)              |
| TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8 (0xc0af)            |
| TLS_DHE_RSA_WITH_AES_256_CCM_8 (0xc0a3)                |
| TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc087)  |
| TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc08b)    |
| TLS_DHE_RSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc07d)      |
| TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 (0xc073)  |
| TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384 (0xc077)    |
| TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256 (0x00c4)      |
| TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA (0x0088)         |
| TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 (0xc02b)       |
| TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)         |
| TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 (0x009e)           |
| TLS_ECDHE_ECDSA_WITH_AES_128_CCM (0xc0ac)              |
| TLS_DHE_RSA_WITH_AES_128_CCM (0xc09e)                  |
| TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 (0xc023)       |
| TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (0xc027)         |
| TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 (0x0067)           |
| TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA (0xc009)          |
| TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (0xc013)            |
| TLS_DHE_RSA_WITH_AES_128_CBC_SHA (0x0033)              |
| TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8 (0xc0ae)            |
| TLS_DHE_RSA_WITH_AES_128_CCM_8 (0xc0a2)                |
| TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc086)  |
| TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc08a)    |
| TLS_DHE_RSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc07c)      |
| TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 (0xc072)  |
| TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 (0xc076)    |
| TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 (0x00be)      |
| TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA (0x0045)         |
| TLS_RSA_WITH_AES_256_GCM_SHA384 (0x009d)               |
| TLS_RSA_WITH_AES_256_CCM (0xc09d)                      |
| TLS_RSA_WITH_AES_256_CBC_SHA256 (0x003d)               |
| TLS_RSA_WITH_AES_256_CBC_SHA (0x0035)                  |
| TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384 (0xc032)          |
| TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384 (0xc02a)          |
| TLS_ECDH_RSA_WITH_AES_256_CBC_SHA (0xc00f)             |
| TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384 (0xc02e)        |
| TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384 (0xc026)        |
| TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA (0xc005)           |
| TLS_RSA_WITH_AES_256_CCM_8 (0xc0a1)                    |
| TLS_RSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc07b)          |
| TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256 (0x00c0)          |
| TLS_RSA_WITH_CAMELLIA_256_CBC_SHA (0x0084)             |
| TLS_ECDH_RSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc08d)     |
| TLS_ECDH_RSA_WITH_CAMELLIA_256_CBC_SHA384 (0xc079)     |
| TLS_ECDH_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc089)   |
| TLS_ECDH_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 (0xc075)   |
| TLS_RSA_WITH_AES_128_GCM_SHA256 (0x009c)               |
| TLS_RSA_WITH_AES_128_CCM (0xc09c)                      |
| TLS_RSA_WITH_AES_128_CBC_SHA256 (0x003c)               |
| TLS_RSA_WITH_AES_128_CBC_SHA (0x002f)                  |
| TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256 (0xc031)          |
| TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256 (0xc029)          |
| TLS_ECDH_RSA_WITH_AES_128_CBC_SHA (0xc00e)             |
| TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256 (0xc02d)        |
| TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256 (0xc025)        |
| TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA (0xc004)           |
| TLS_RSA_WITH_AES_128_CCM_8 (0xc0a0)                    |
| TLS_RSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc07a)          |
| TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256 (0x00ba)          |
| TLS_RSA_WITH_CAMELLIA_128_CBC_SHA (0x0041)             |
| TLS_ECDH_RSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc08c)     |
| TLS_ECDH_RSA_WITH_CAMELLIA_128_CBC_SHA256 (0xc078)     |
| TLS_ECDH_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc088)   |
| TLS_ECDH_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 (0xc074)   |
| TLS_EMPTY_RENEGOTIATION_INFO_SCSV (0x00ff)             |