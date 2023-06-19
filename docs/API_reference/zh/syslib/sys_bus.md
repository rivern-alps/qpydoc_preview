# sys_bus - 会话总线

用于消息的订阅和发布广播, 多线程处理等,用于一对多的广播, 类似于内部的mqtt



## 订阅topic

### `sys_bus.subscribe`

```python
sys_bus.subscribe(topic, handler)
```

**参数描述：**

* `topic`-主题,  string/int类型, 所需要订阅的topic 
* `handler`-处理函数,  func函数类型,   处理函数, 当有对应topic过来时, 会对应调用其中的处理函数去处理 handler 需要有两个参数(topic, msg) 



## 发布topic消息

### `sys_bus.publish`

```python
sys_bus.publish(topic , msg)
```

发布消息, 对应订阅的topic将收到并多线程对此消息处理

**参数描述：**

* `topic`-主题,  string/int类型, 所需要订阅的topic 
* `msg`-消息,  任意类型,  发布的消息



## 查看会话总线注册表

### `sys_bus.sub_table`

```python
sys_bus.sub_table(topic=None)
```

查看订阅注册表, 注册表中有所有topic和订阅的函数

**参数描述：**
* `topic`-主题,  string/int类型, 传参表示查看此topic的注册表, 不传参表示查看所有的topic的注册表

**返回值描述：**

dict / list类型的订阅函数列表或注册表



## 解除订阅

### `sys_bus.unsubscribe`

```python
sys_bus.unsubscribe(topic , cb=None)
```

解除已订阅的topic, 或者对应topic下的某个函数, 当只传入topic参数时, 会删除topic和从topic下所有的订阅函数,  如果传了cb则删除订阅topic下面订阅列表中的对应的cb函数



**参数描述：**

* `topic`-主题,  string/int类型, 订阅的topic事件
* `cb`-回调函数,  func函数类型, 要删除的订阅函数, 不传则删除topic

**返回值描述：**

True 删除成功, False删除失败



**示例：**

```python
import sys_bus


def test(topic, msg):
    print("test ... topic = {} msg = {}".format(topic, msg))

# 订阅
sys_bus.subscribe("test", test)
# 发布
sys_bus.publish("test", "this is a test msg")

#  test ... topic = test msg = this is a test msg

# 解绑对应test topic下的订阅的test函数
sys_bus.unsubscribe("test", test)

# 解绑对应test topic下的所有订阅函数
sys_bus.unsubscribe("test")
```