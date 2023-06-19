# sys_bus - Session Bus

This feature subscribes to messages and publishes one-to-many broadcasts with multithreading, similar to an internal MQTT protocol.



## Subscribe to Topics

### `sys_bus.subscribe`

```python
sys_bus.subscribe(topic, handler)
```

**Parameter**

* `topic` – String or integer type. The topic to be subscribed to.
* `handler` – Function type. Event handler function. This function will be called to handle the subscribed topics. This function has two parameters, *topic* and *msg* (See *sys_bus.publish()* for details).



## Publish Topics

### `sys_bus.publish`

```python
sys_bus.publish(topic , msg)
```

Publishes messages. The server will receive the subscribed topics and process the message with multithreading.

**Parameter**

* `topic` – String or integer type. The topic to be subscribed to.
* `msg` – The published messages.



## View Session Bus Registry

### `sys_bus.sub_table`

```python
sys_bus.sub_table(topic=None)
```

Views the subscription registry, including all topics and the subscribed functions.

**Parameter**
* `topic` – String or integer type. Topics. If this parameter is specified, view the registry of the specified topic. If this parameter is omitted, view the registry of all topics.

**Return Value**

Dict or list type. The list or registry of the subscribed functions.



## Unsubscribe from Topics

### `sys_bus.unsubscribe`

```python
sys_bus.unsubscribe(topic , cb=None)
```

Unsubscribes from the subscribed topics or a function under the topics. If only *topic* is specified, unsubscribe from the topics and all subscribed functions under the topics. If both *topic* and *cb* are specified, unsubscribe from the callback function under the subscribed topics.

**Parameter**

* `topic`– String or integer type. The subscribed topics.
* `cb` – Function type. Callback function. The function to be unsubscribed from. Unsubscribe from the subscribed topics if this parameter is omitted.

**Return Value**

True – Successful execution

False –  Failed execution



**Example**

```python
import sys_bus


def test(topic, msg):
    print("test ... topic = {} msg = {}".format(topic, msg))

# Subscribe
sys_bus.subscribe("test", test)
# Publish
sys_bus.publish("test", "this is a test msg")

#  test ... topic = test msg = this is a test msg

# Unsubscribe from the test function under the test topic
sys_bus.unsubscribe("test", test)

# Unsubscribe from all subscribed functions under the test topic
sys_bus.unsubscribe("test")
```