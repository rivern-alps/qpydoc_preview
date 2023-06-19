# uwebsocket – WebSocket Client

This feature establishes a WebSocket connection.



## Connect to Client

### uwebsocket.Client.connect

```python
ws_client = uwebsocket.Client.connect(url, headers=None, debug=False)
```

**Parameter**

* `url` –  String type. WebSocket connection URL, usually in the form of "ws://xxx/" or "wss://xxx/".
* `headers` – Dict type. The additional header to be added, used in the scenarios where both the standard header and the additional header passed by users are allowed. 
* `debug` – Bool type. True – Output logs. False – Not output logs. Default value: False.



## Send Data

### ws_client.send

```python
ws_client.send(msg)
```

**Parameter**
* `msg` – String type. The data to be sent. 



## Receive Data

### ws_client.recv

```python
ws_client.recv()
```

**Return Value**

* `result `– String type. The returned result. When this value is null or None, the connection is closed.



## Close Connection

### ws_client.close

```python
ws_client.close()
```



**Example**

```python
import uwebsocket
import _thread


def recv(cli):
    while True:
        # Receive data in an infinite loop.
        recv_data = cli.recv()
        print("recv_data = {}".format(recv_data))
        if not recv_data:
            # The server or client closes the connection.
            print("cli close")
            client.close()
            break


# Create a WebSocket client. "debug=True" indicates outputing logs. You need to customize the IP address, port or domain name.
client = uwebsocket.Client.connect('ws://xxx/', debug=True)

# Receive data in threads.
_thread.start_new_thread(recv, (client,))

# Send data.
client.send("this is a test msg")
```