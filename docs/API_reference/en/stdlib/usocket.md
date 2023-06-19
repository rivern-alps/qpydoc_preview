# usocket - Socket Module

```
This article introduces the use of QuecPython's usocket module and describes features of the latest version of the usocket module.
```

This module provides access to the BSD socket interface, and realizes subsets of the corresponding CPython module. See CPython file [socket](https://docs.python.org/3.5/library/socket.html#module-socket) for more detailed information.

**Example**

```python
# Imports the usocket module
import usocket
import log
import utime
import checkNet


'''
The following two global variables are necessary. You can modify the values of these two global variables based on project requirement
'''
PROJECT_NAME = "QuecPython_Socket_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Sets the log output level
log.basicConfig(level=log.INFO)
socket_log = log.getLogger("SOCKET")

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        socket_log.info('Network connection successful!')

    	# Creates a socket instance
    	sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
    	# Parses the name of domain
    	sockaddr=usocket.getaddrinfo('www.tongxinmao.com', 80)[0][-1]
    	# Establishes the connection
    	sock.connect(sockaddr)
    	# Sents messages to the server
    	ret=sock.send('GET /News HTTP/1.1\r\nHost: www.tongxinmao.com\r\nAccept-Encoding: deflate\r\nConnection: keep-alive\r\n\r\n')
    	socket_log.info('send %d bytes' % ret)
    	# Receives meaasges from the server
    	data=sock.recv(256)
    	socket_log.info('recv %s bytes:' % len(data))
    	socket_log.info(data.decode())

    	# Closes the connection
    	sock.close()
    else:
        socket_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```


## Constructors

### `usocket.socket`

```python
class usocket.socket(af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP)
```

Creates a socket object based on the specified address family, socket type, and protocol type parameters. Note that it is not necessary to specify *proto* in most cases, nor is it recommended, because some MicroPython ports may omit the `IPPROTO_*` constant.

**Parameter**

- `af` - The address family (please refer to the Constants).

- `type` - The socket type (please refer to the Constants).

- `proto` - The protocol number (please refer to the Constants).


Example:
```python
import usocket
# Creates a TCP-based stream socket
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
# Creates a UDP-based datagram socket
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
# Creates a TCP-based server socket
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM, usocket.IPPROTO_TCP_SER)
# Creates a TCP-based client socket(It should be used with bind, and the socket address can be customized)
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM, usocket.TCP_CUSTOMIZE_PORT)
```

### `usocket.getaddrinfo`

```python
usocket.getaddrinfo(host, port)
```

Parses the domain name of DNS. Parses the domain name of the host (host) and port (port) into a 5-tuple sequence used to create the socket. The structure of the tuple is below:
`(family, type, proto, canonname, sockaddr)`

**Parameter**

- `host` - The domain name of the host.
- `port` - The port.

**Return Value**

- `family` - The address family (please refer to Constants).
- `type` - The socket type (please refer to Constants).
- `proto` - The protocol number (please refer to Constants).
- `canonname` - The domain name of the host.
- `sockaddr` - The list containing addresses and port numbers.

## Methods

### `socket.bind`

```python
socket.bind(address)
```

This method binds the socket to the specified address. The socket must not yet be bound.

> **Note:** 1. When the socket is a server, it must be bound to fix the address of the server.  2. When the socket is a client, it should be bound to address to specify the socket for data processing (It should be used with usocket.TCP_CUSTOMIZE_PORT).

**Parameter**

- `address` - The list or tuple containing addresses and port numbers.

Example:
```
#Binds the specified address
socket.bind(("192.168.0.1",80))
#Binds dial-up IP address, and the port can be customlized (When the port is 0, it will be automatically allocated)
socket.bind(("",0))
```

### `socket.listen`

```python
socket.listen(backlog)
```

This method allows the socket server to listen to the client connection and specify the maximum connection number of the client.

**Parameter**

- `backlog` - The maximum number for accepting the socket, at least 0.

### `socket.accept`

```python
socket.accept()
```

This method allows the socket server to accept the connection request. If successful, a tuple, which contains the new socket, client address and client port, will be returned. The form is : `(conn, address, port)`.

**Return Value** 

- `conn` - The new socket object which is used to interact with the client.
- `address` - The client address connected to the server.
- `port` - The client port connected to the server.

### `socket.connect`

```python
socket.connect(address)
```

This method allows the socket to connect the server of the specified address parameter.

**Parameter**

- `address` - The list or tuple containing addresses and port numbers.

Example:
```
# Connects the specified address
socket.connect(("192.168.0.1",80))
```

### `socket.read`

```python
socket.read( [ size ] )
```

This method reads size byte data from the socket and returns a byte object. If size is not specified, all readable data will be read from the socket until there is no more data to be read. At this time, this function is the same as `socket.readall()` .

### `socket.readinto`

```python
socket.readinto(buf, [ , nbytes ])
```

This method reads bytes from the socket into the buffer buf. If nbytes is specified, the most maximum bytes can be read is the number of nbytes. If nbytes is not specified, len(buf) bytes can be read at most. The return value is the actual number of read bytes.

```python
socket.readline()
```

This method reads data from a socket by line and stops reading when a newline character is encountered, and returns the read line.

### `socket.write`

```python
socket.write(buf)
```

This method allows the socket to send the data in buffer, and buf is the data to be sent. Then the actual sent bytes number is returned.

### `socket.send`

```python
socket.send(bytes)
```

This method allows the socket to send data and returns the the actual sent bytes number.

**Parameter**

- `bytes` - The data in bytes type.

### `socket.sendall`

```python
socket.sendall(bytes)
```

This method allows the socket to send all data to the socket. Unlike `send()`, this method attempts to send all the data block by block.
Note: The operation of this method on the non-blocking socket is indeterminate, so in MicroPython, it is recommended to use `write()`.  The `write()` method has the same "No-short-writing" policy to block the socket, and will return the number of bytes sent on the non-blocking socket.

**Parameter**

- `bytes` - The data in bytes type.

### `socket.sendto`

```python
socket.sendto(bytes, address)
```

This method allows the socket to send data to the specified *address*, and returns the actual sent bytes number.

**Parameter**

- `bytes` - The data in bytes type.
- `address` - The list or tuple containing addresses and port numbers.

### `socket.recv`

```python
socket.recv(bufsize)
```

This method receives the data from the socket. The return value is a byte object which indicates the received data. The maximum data size received at a time is determined by bufsize.

**Parameter**

- `bufsize` - The maximum data size received at a time.

### `socket.recvfrom`

```python
socket.recvfrom(bufsize)
```

This method receives the data from the socket. The return value is a tuple which contains the byte object and address. The form of the return value is:  `(bytes, address)`.

**Parameter**

- `bufsize` - The maximum data size received at a time.

**Return Value**

- `bytes` -The byte object that receives the data.
- `address` -The address of the socket that sends the data.

### `socket.close`

```python
socket.close()
```

This method marks the socket as closed and releases all resources.

### `socket.setsockopt`

```python
socket.setsockopt(level, optname, value)
```

This method sets the value of the socket option.

**Parameter**

- `level` - The level of the socket option.
- `optname` - The feature option of the socket.
- `value` - It can be either an integer or an object in bytes type which represents the buffer.

Example:
```
#Sets the port multiple is enabled
socket.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
#Sets intervals of the TCP keep-alive packet.The unit of the value parameter is minute,ranging from 1 to 120
socket.setsockopt(usocket.SOL_SOCKET, usocket.TCP_KEEPALIVE, 1)
```

### `socket.setblocking`

```python
socket.setblocking(flag)
```

This method sets the socket as either blocking mode or non-blocking mode.  This method is a simplification of `settimeout()`.

**Parameter**

- `flag` - Sets whether the socket mode is blocking (default mode: blocking mode).

Example:
```
#Sets the socket as the blocking mode
`socket.setblocking(True)` equals to `socket.settimeout(None)`
#sets the socket as the non-blocking mode
`socket.setblocking(False)` equals to `socket.settimeout(0)`
```

### `socket.settimeout`

```python
socket.settimeout(value)
```

This method sets timeouts of the send and received data of the socket. Unit: second.

**Parameter:**

- `value` - It can be a non-negative floating point which represents second or None. If the parameter value is 0, the socket will be set to non-blocking mode, otherwise the socket will be in blocking mode.

### `socket.makefile`

```python
socket.makefile(mode='rb')
```

This method returns the file object associated with the socket. The type of the return value is related to the specified parameter. The mode parameter only supports binary pattern (rb and wb).

### `socket.getsocketsta`

```python
socket.getsocketsta()
```

This method gets the status of TCP socket.

> **Note: **1. BG95 series module does not support this API. 2. After calling `socket.close()` , -1 will be returned if `socket.getsocketsta()` is called, because the created object resources and other things have been released.

**Return Value** 

| Status Value | Status      | Description                                                  |
| ------------ | ----------- | ------------------------------------------------------------ |
| 0            | CLOSED      | The socket is created but not used.                          |
| 1            | LISTEN      | The socket is listening to the connection.                   |
| 2            | SYN_SENT    | The socket is trying to establish a connection actively. That is, ACK has not been received after sending the SYN. |
| 3            | SYN_RCVD    | The socket is in the initial synchronization status of the connection. That is, the SYN sent from the opposite has been received, but the ACK of the sent SYN has not been received. |
| 4            | ESTABLISHED | The socket has successfully established the connection.      |
| 5            | FIN_WAIT_1  | The socket is closed and the TCP connection is closing. That is, the FIN is sent actively, but the ACK or FIN sent from the party closed passively has not been received. |
| 6            | FIN_WAIT_2  | The local socket is closed and the remote socket is waiting to be closed. That is, the ACK corresponding to the sent FIN is received in the FIN_WAIT_1 status. |
| 7            | CLOSE_WAIT  | The remote socket is closed and the local socket is waiting to be closed. The passively closed party receives the FIN. |
| 8            | CLOSING     | The local socket is closed and the remote socket is closing. The close confirmation is suspended. That is, the FIN sent from the passively closed party has been received in FIN_WAIT_1 status. |
| 9            | LAST_ACK    | The remote socket is closed , and the close confirmation of the local socket is being waited. The passively closed party sends the FIN in CLOSE_WAIT status. |
| 10           | TIME_WAIT   | The remote socket is closed and the local socket is waiting to be closed. That is, the four-way wavehand FIN, ACK, FIN, and ACK are complete. The TCP connection is disconnected after 2MSL time. |


## Constants

### usocket.AF_INET

IPV4 type. Address family.

### usocket.AF_INET6

IPV6 type. Address family.

### usocket.SOCK_STREAM

socket type. A TCP-based stream socket.

### usocket.SOCK_DGRAM

socket type. A UDP-based datagram socket

### usocket.SOCK_RAW

socket type. A raw socket

### usocket.IPPROTO_TCP

Protocol number. TCP protocol.

### usocket.IPPROTO_UDP

Protocol number. UDP protocol.

### usocket.IPPROTO_TCP_SER

Protocol number. TCP server.

### usocket.TCP_CUSTOMIZE_PORT

Protocol number. TCP client can customize address.

### usocket.SOL_SOCKET

The level of the socket option.

### usocket.SO_REUSEADDR

The socket feature option. The port multiple is enabled.

### usocket.TCP_KEEPALIVE

The socket feature option. Sets intervals of the TCP keep-alive packet.
