# ussl – SSL/TLS Protocol

ussl realizes the encrypted communication using TLS/SSL protocol, mainly for unidirectional and bidirectional authentication.



## Create Secure Channel over SSL

### `ussl.wrap_socket`

```python
ussl.wrap_socket(sock,server_hostname=None,cert=None,key=None)
```

**Parameter**

- `sock` – The usocket.socket object to be wrapped. Required parameter.

- `server_hostname` – String type. Server IP address. Optional parameter. 

- `cert` – String type. Digital certificate. Optional parameter. 

- `key` – String type. Private key. Optional parameter. 

**Return Value**

A wrapped `usocket.socket` object.



**Example**

```python
# Import ussl
# -*- coding: UTF-8 -*-
import ussl
import usocket
import log
import utime
import checkNet

'''
The following two global variables are required. You can modify the values of the following two global variables according to your actual projects.
'''
PROJECT_NAME = "QuecPython_Socket_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Set the log output level.
log.basicConfig(level=log.INFO)
socket_log = log.getLogger("SOCKET")

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        socket_log.info('Network connection successful!')
        # 1. Unidirectional-authentication description
        # Create a socket instance.
        sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
        # Resolve a domain name.
        sockaddr=usocket.getaddrinfo('myssl.com', 443)[0][-1]
        # Set up a connection.
        sock.connect(sockaddr)
        # Create Secure Channel over SSL, supported by the server.
        sock = ussl.wrap_socket(sock, server_hostname="myssl.com")
        # Send messages to the server.
        ret = sock.write('GET / HTTP/1.0\r\nHost: myssl.com\r\nAccept-Encoding: deflate\r\n\r\n')
        socket_log.info('write %d bytes' % ret)
        # Receive the messages from the server.
        data=sock.read(256)
        socket_log.info('read %s bytes:' % len(data))
        socket_log.info(data.decode())

        # Close the connection.
        sock.close()
        socket_log.info('--------------------Socket Ussl End-------------------')
    else:
        socket_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))

# 2. Bidirectional-authentication description
cert = "Certificate"
key = "Private Key"
sock = ussl.wrap_socket(sock, server_hostname="myssl.com", cert=cert, key=key)

```



## List of Supported Cipher Suites



| Cipher Suite                                           |
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