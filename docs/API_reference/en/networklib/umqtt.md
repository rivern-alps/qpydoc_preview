# umqtt - MQTT Protocol

This feature is used to create MQTT clients to publish and subscribe to topics.

```
QoS Level Description
In MQTT protocol, three levels of QoS are defined.
QoS0 – At most once. Lowest level. After sending the message, the sender does not care whether the message has been received by the receiver.
QoS1 – At least once. Middle level. The message is guaranteed to be received by the receiver at least once.
QoS2 – Only once. Highest level. The message is guaranteed to be received by the receiver only once.
```

## Initialize MQTT

### `MQTTClient`

```python
MQTTClient(client_id, server, port=0, user=None, password=None, keepalive=0, ssl=False, ssl_params={},reconn=True,version=4)
```

Creates MQTT clients.

* Parameter

| Parameter  | Type    | Description                                                  |
| ---------- | ------- | ------------------------------------------------------------ |
| client_id  | String  | Client ID. Each client ID is unique.                         |
| server     | String  | Server address, which can be an IP address or domain name.   |
| port       | Integer | Server port (optional). Default value: 1883. The default port of MQTT over SSL/TLS is 8883. |
| user       | String  | Username registered on the server (optional).                |
| password   | String  | Password registered on the server (optional).                |
| keepalive  | Integer | Timeout of keep-alive (optional). Default value: 0. Unit: s. |
| ssl        | bool    | Enable or disable SSL/TSL encryption.                        |
| ssl_params | String  | SSL/TLS parameter (optional).                                |
| reconn     | bool    | Enable or disable the internal reconnection mechanism (optional). Default value: True (enable). |
| version    | Integer | The selected MQTT version (optional). version=3 indicates MQTTv3.1. Default value: 4. version=4 indicates MQTTv3.1.1. |

* Return Value 

An MQTT client.

## Set Callback Function

### `MQTTClient.set_callback`

```python
MQTTClient.set_callback(callback)
```


Sets the callback function of receiving messages.

* Parameter

| Parameter | Type     | Description                                  |
| --------- | -------- | -------------------------------------------- |
| callback  | function | The callback function of receiving messages. |

* Return Value

None

### `MQTTClient.error_register_cb`

```python
MQTTClient.error_register_cb(callback)
```

Sets the callback function of error occurrence. When the MQTT internal thread is abnormal, the error message is returned by the callback function. The callback function can be called only when the internal reconnection is not enabled. 

* Parameter 

| Parameter | Type     | Description                                 |
| --------- | -------- | ------------------------------------------- |
| callback  | function | The callback function of error occurrences. |

* Return Value

None

Example

```python
from umqtt import MQTTClient

def err_cb(err):
    print("thread err:")
    print(err)
    
c = MQTTClient("umqtt_client", "mq.tongxinmao.com", 18830)
c.error_register_cb(err_cb)
```

### `MQTTClient.set_last_will`

```python
MQTTClient.set_last_will(topic,msg,retain=False,qos=0)
```

Sets the last will to be sent to the MQTT server. If a client ungracefully disconnects from the server without calling *MQTTClient.disconnect()*, the last will will be sent to other clients.

* Parameter

| Parameter | Type    | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ |
| topic     | String  | Last-will topic.                                             |
| msg       | String  | Last-will content                                            |
| retain    | bool    | When *retain* = True, the MQTT broker will retain the message. Default value: False. |
| qos       | Integer | Quality of Service, 0 or 1.                                  |

* Return Value

None

## MQTT Connection Related Features

### `MQTTClient.connect`

```python
MQTTClient.connect(clean_session=True)
```


Connects to MQTT server. Failed connection leads to an MQTT exception.

* Parameter

| Parameter     | Type | Description                                                  |
| ------------- | ---- | ------------------------------------------------------------ |
| clean_session | bool | Client session type, optional parameter. If this value is True, the MQTT server will delete all information about the client when the client disconnects from the MQTT server. If this value is False, the client session is persistent, that is, when the client disconnects from the MQTT server, the subscription and queuing information will be retained. Default value: False. |

* Return Value

0 – Successful execution

Error message – Failed execution

### `MQTTClient.disconnect`

```python
MQTTClient.disconnect()
```

Disconnects from the MQTT server.

* Parameter

None

* Return Value

None

### `MQTTClient.close`

```python
MQTTClient.close()
```

Releases socket resources. (Please note the differences between *MQTTClient.disconnect()* and *MQTTClient.close()*, where *MQTTClient.close()* only releases socket resources but *MQTTClient.disconnect()* releases resources including threads.)

Note: This method can be used only when the client needs to reconnect to the MQTT server. See ***Example of MQTT Reconnection After Ungraceful Disconnection*** below for details. Call *MQTTClient.disconnect()* to normally disconnect from the MQTT server.

* Parameter

None

* Return Value

None

### `MQTTClient.ping`

```python
MQTTClient.ping()
```

Pings to MQTT server to check the connection when *keepalive* is not 0. When *keepalive* is 0, this method is disabled.

* Parameter

None

* Return Value

None

## Publish and Subscribe Related Features

### `MQTTClient.publish`

```python
MQTTClient.publish(topic,msg, retain=False, qos=0)
```

Publishes messages.

* Parameter

| Parameter | Type | Description                                                |
| ----- | ----- | ------------------------------------------------------------ |
| topic  | String | Message topic.                                  |
| msg    | String | Data to be sent.                             |
| retain | bool   | Default value: False. If this value is set to True when you send a message, the message is retained.<br />The MQTT server retains the last received message with a RETAIN flag bit of True on the server. Whenever the MQTT client connects to the MQTT server and subscribes to a topic, if there is a Retained message under that topic, the MQTT server immediately pushes the Retained message to the client. <br />Note: The MQTT server will only save the last received message with the RETAIN flag bit of True for each topic, that is, if the MQTT server saves one retained message for a Topic, when the client publishes a new retained message, the original message on the server is overwritten. |
| qos    | Integer | MQTT QoS, 0 or 1. Default value: 0. <br />0 – The sender sends a message only once.<br />1 – The sender sends a message at least once and guarantees that the message has been delivered to the MQTT broker. |

* Return Value

None

### `MQTTClient.subscribe`

```python
MQTTClient.subscribe(topic,qos)
```

Subscribes to MQTT topics.

* Parameter

| Parameter | Type | Description                                                |
| ---- | ----- | ------------------------------------------------------------ |
| topic | String | topic                                                        |
| qos   | Integer | MQTT QoS, 0 or 1. Default value: 0. <br />0 – The sender sends a message only once.<br />1 – The sender sends a message at least once and guarantees that the message has been delivered to the MQTT broker. |

* Return Value

None

### `MQTTClient.check_msg`

```python
MQTTClient.check_msg()
```

Checks whether the MQTT server has messages to be processed.

* Parameter

None

* Return Value

None

### `MQTTClient.wait_msg`

```python
MQTTClient.wait_msg()
```

Blocks waiting for a message response from the MQTT server.

* Parameter

None

* Return Value

None

### `MQTTClient.get_mqttsta`

```python
MQTTClient.get_mqttsta()
```

Gets MQTT connection status.

Note:

 1. BG95 series module does not support the API.

2. If you call *MQTTClient.disconnect()* before calling *MQTTClient.get_mqttsta()*, -1 will be returned, because the created object resources are released.

* Parameter

None

* Return Value

0 – Successful connection

1 – Connecting

2 – Server connection closed 

-1 – Connection error 



**Example**

```python
'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2020-04-24 17:06:08
@Description: example for module umqtt
@FilePath: example_mqtt_file.py
'''
from umqtt import MQTTClient
import utime
import log
import checkNet


'''
The following two global variables are required. You can modify the values of the following two global variables according to your actual projects.
'''
PROJECT_NAME = "QuecPython_MQTT_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Set the log output level.
log.basicConfig(level=log.INFO)
mqtt_log = log.getLogger("MQTT")


state = 0

def sub_cb(topic, msg):
    global state
    mqtt_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    state = 1


if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        mqtt_log.info('Network connection successful!')

        # Create an MQTT example.
        c = MQTTClient("umqtt_client", "mq.tongxinmao.com", 18830)
        # Set the callback function of receiving messages.
        c.set_callback(sub_cb)
        # Connect to the MQTT server.
        c.connect()
        # Subscribe to a topic.
        c.subscribe(b"/public/TEST/quecpython")
        mqtt_log.info("Connected to mq.tongxinmao.com, subscribed to /public/TEST/quecpython topic" )
        # Publish a message.
        c.publish(b"/public/TEST/quecpython", b"my name is Quecpython!")
        mqtt_log.info("Publish topic: /public/TEST/quecpython, msg: my name is Quecpython")

        while True:
            c.wait_msg()  # Blocking function of monitoring messages.
            if state == 1:
                break
        # Disconnects from the MQTT server.
        c.disconnect()
    else:
        mqtt_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))

```

**Example of MQTT Reconnection After Ungraceful Disconnection**

Note：

1. The parameter *reconn* in the following example enables or disables the internal reconnection mechanism. Default value: True (enable).

2. If you need to test or use the external reconnection mechanism, please refer to this example code below. Before testing, set reconn to False, otherwise, the internal reconnection mechanism will be used by default.

```python
'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2021-05-25 17:06:08
@Description: example for module umqtt
@FilePath: example_mqtt_file.py
'''
'''
The following two global variables are required. You can modify the values of the following two global variables according to your actual projects.
The values of these two variables are printed before the user code is executed.
'''
import utime
import log
import net
import _thread
import checkNet
import dataCall
from umqtt import MQTTClient

PROJECT_NAME = "QuecPython_MQTT_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Reclaim the thread resource through the status after calling MQTTClient.disconnect().
TaskEnable = True
# Set the log output level.
log.basicConfig(level=log.INFO)
mqtt_log = log.getLogger("MQTT")


# Encapsulate MQTT so it can support more custom logic.
class MqttClient():
    '''
    mqtt init
    '''

    # Note: The parameter reconn enables or disables the internal reconnection mechanism. Default value: True (enable).
    # If you need to test or use the external reconnection mechanism, please refer to this example code below. Before testing, set reconn to False, otherwise, the internal reconnection mechanism will be used by default.
    def __init__(self, clientid, server, port, user=None, password=None, keepalive=0, ssl=False, ssl_params={},
                 reconn=True):
        self.__clientid = clientid
        self.__pw = password
        self.__server = server
        self.__port = port
        self.__uasename = user
        self.__keepalive = keepalive
        self.__ssl = ssl
        self.__ssl_params = ssl_params
        self.topic = None
        self.qos = None
        # Network status flag.
        self.__nw_flag = True
        # Create a mutex.
        self.mp_lock = _thread.allocate_lock()
        # Create a class to initialize the MQTT object.
        self.client = MQTTClient(self.__clientid, self.__server, self.__port, self.__uasename, self.__pw,
                                 keepalive=self.__keepalive, ssl=self.__ssl, ssl_params=self.__ssl_params,
                                 reconn=reconn)

    def connect(self):
        '''
        Connect to the MQTT server.
        '''
        self.client.connect()
        # Register the callback function of network status. When the network status changes, the function will be called.
        flag = dataCall.setCallback(self.nw_cb)
        if flag != 0:
            # The network callback registration failed.
            raise Exception("Network callback registration failed")

    def set_callback(self, sub_cb):
        '''
        Set the callback function of receiving messages.
        '''
        self.client.set_callback(sub_cb)

    def error_register_cb(self, func):
        '''
        Set the callback function of receiving MQTT thread error occurrence.
        '''
        self.client.error_register_cb(func)

    def subscribe(self, topic, qos=0):
        '''
        Subscribe to topics.
        '''
        self.topic = topic  # Save the topic. Multiple topics can be saved by a list.
        self.qos = qos  # Save the QoS.
        self.client.subscribe(topic, qos)

    def publish(self, topic, msg, qos=0):
        '''
        Publish a message.
        '''
        self.client.publish(topic, msg, qos)

    def disconnect(self):
        '''
        Disconnect from the MQTT server.
        '''
        global TaskEnable
        # Close the monitoring thread of wait_msg.
        TaskEnable = False
        # Disconnect from the MQTT server and release the resources.
        self.client.disconnect()

    def reconnect(self):
        '''
        MQTT reconnection mechanism (The following example is for your reference only and you can adjust based on actual needs.)
        Note: 1. If other services need to be restarted after the client reconnects to the server, determine whether to release the resources of the previous services before restarting the services.
              2. This section needs to be added based on the actual business logic, and this example only covers the process that the client resubscribes to topics after reconnecting to the MQTT server.
        '''
        # Determine whether the lock has been acquired.
        if self.mp_lock.locked():
            return
        self.mp_lock.acquire()
        # Close the previous connection before reconnecting to release resources. Please note the differences between *MQTTClient.disconnect()* and *MQTTClient.close()*, where MQTTClient.close() only releases socket resources but *MQTTClient.disconnect()* releases resources including threads.
        self.client.close()
        # Reconnect to the MQTT server.
        while True:
            net_sta = net.getState()  # Get network registration information.
            if net_sta != -1 and net_sta[1][0] == 1:
                call_state = dataCall.getInfo(1, 0)  # Get data call information.
                if (call_state != -1) and (call_state[2][0] == 1):
                    try:
                        # The network is normal. Reconnect to the MQTT server.
                        self.connect()
                    except Exception as e:
                        # Reconnection to the MQTT server failed. Try again 5 s later.
                        self.client.close()
                        utime.sleep(5)
                        continue
                else:
                    # The network is unrestored. Please wait.
                    utime.sleep(10)
                    continue
                # Connect to the MQTT server successfully and subscribe to the topic.
                try:
                    # Multiple topics can be saved by a list. Traverse the list to resubscribe the topic.
                    if self.topic is not None:
                        self.client.subscribe(self.topic, self.qos)
                    self.mp_lock.release()
                except:
                    # Subscription failed. Reconnect to the MQTT server.
                    self.client.close()
                    utime.sleep(5)
                    continue
            else:
                utime.sleep(5)
                continue
            break  # Stop loop.
        # Exit and reconnect.
        return True

    def nw_cb(self, args):
        '''
        Call the callback function of data call.
        '''
        nw_sta = args[1]
        if nw_sta == 1:
            # Network connected.
            mqtt_log.info("*** network connected! ***")
            self.__nw_flag = True
        else:
            # Network disconnected.
            mqtt_log.info("*** network not connected! ***")
            self.__nw_flag = False

    def __listen(self):
        while True:
            try:
                if not TaskEnable:
                    break
                self.client.wait_msg()
            except OSError as e:
                # Determine whether the network is disconnected.
                if not self.__nw_flag:
                    # Reconnect after the network is restored from disconnection.
                    self.reconnect()
                # Reconnect when the socket status is abnormal.
                elif self.client.get_mqttsta() != 0 and TaskEnable:
                    self.reconnect()
                else:
                    # You can call the raise method to return an exception or -1.
                    return -1

    def loop_forever(self):
        _thread.start_new_thread(self.__listen, ())

if __name__ == '__main__':
    '''
    When running this routine manually, you can remove this delay. If you change the file name of the routine to main.py, you need to add this delay when you want to start the routine automatically. Otherwise, you cannot see the information printed in poweron_print_once() below from the CDC interface.
    '''
    utime.sleep(5)
    checknet.poweron_print_once()
    '''
    If the user program contains network-related codes, it must execute wait_network_connected() to wait for the network to be ready (successful data call); If it is a network-independent code, you can mask wait_network_connected().
    【This routine must retain the following line.】
    '''
    checknet.wait_network_connected()

    def sub_cb(topic, msg):
        # global state
        mqtt_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    
    c = MqttClient("umqtt_client_753", "mq.tongxinmao.com", 18830, reconn=False)
    
    def err_cb(error):
        '''
        Set the callback function of receiving MQTT thread error occurrence.

        '''
    	mqtt_log.info(error)
    	c.reconnect() # Reconnect to MQTT server after error occurrences.
        
    # c = MqttClient("umqtt_client_753", "mq.tongxinmao.com", 18830, reconn=False)
    # Set the callback function of receiving messages.
    c.set_callback(sub_cb)
    # Set the callback function of error occurrence.
    c.error_register_cb(err_cb)
    # Connect to the MQTT server.
    c.connect()
    # Subscribe to topics.
    c.subscribe(b"/public/TEST/quecpython758")
    mqtt_log.info("Connected to mq.tongxinmao.com, subscribed to /public/TEST/quecpython topic")
    # Publish a message.
    c.publish(b"/public/TEST/quecpython758", b"my name is Quecpython!")
    mqtt_log.info("Publish topic: /public/TEST/quecpython758, msg: my name is Quecpython")
    # Monitor MQTT messages. 
    c.loop_forever()
    # Wait for 5 s to receive the message.
    # Note: Comment c.disconnect () and utime.sleep(5) if you want to test the reconnection mechanism, including server disconnection.
    # utime.sleep(5)
    # Disconnect to the MQTT server.
    # c.disconnect()
```