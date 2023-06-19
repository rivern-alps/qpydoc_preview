## 修订历史

| Version | **Date**   | **Author** | **Change expression** |
| ------- | ---------- | ---------- | --------------------- |
| 1.0     | 2021-09-14 | Pawn       | 新建文档              |


## Blinker介绍
Blinker是一个基于Python的强大的信号库，支持一对一、一对多的订阅发布模式，支持发送任意大小的数据等等，且线程安全。

## APIs

### blinker.ANY
静态值, 使用此值为向任何人发送信息

* 参数

无

* 返回值

无

### Signal.connect(receiver, sender=ANY, weak=False)
向发送者订阅信号
* 参数

| 参数     | 类型     | 说明                                    |
| -------- | -------- | --------------------------------------- |
| receiver | function | 回调函数                                |
| sender   | int      | 订阅的发送者, 当值为ANY时订阅所有发布者 |
| weak     | Boolean  | 弱引用选项, 功能不可用, 默认值为FALSE   |

* 返回

receiver



### Signal.connect_via(sender, weak=False)
以装饰器形式订阅指定发送者

* 参数

| 参数   | 类型    | 说明                                    |
| ------ | ------- | --------------------------------------- |
| sender | int     | 订阅的发送者, 当值为ANY时订阅所有发布者 |
| weak   | Boolean | 弱引用选项, 功能不可用, 默认值为FALSE   |

* 返回

返回装饰器


### Signal.send(*sender, **kwargs)
使用send通知订阅者

* 参数

|  参数   | 类型  |  说明 |
|  ----  | ----  | ---- |
| sender | object | 任何对象, 如果省略则为None |
| kwargs | dict | 需要发送到接受者的数据 |
* 返回

订阅sender的receiver list

### Signal.has_receivers_for(sender)
查订阅者是否订阅了某个具体的信号发布者

* 参数

|  参数   | 类型  |  说明 |
|  ----  | ----  | ---- |
| sender | object | 发送方object |

* 返回
返回 True 或 False

### Signal.receivers_for(sender)
返回订阅者的迭代器

* 参数

|  参数   | 类型  |  说明 |
|  ----  | ----  | ---- |
| sender | object | 发送方object |

* 返回
包含所有订阅者的迭代器

### Signal.disconnect(receiver, sender=ANY)
取消订阅

* 参数

| 参数     | 类型     | 说明                                    |
| -------- | -------- | --------------------------------------- |
| receiver | function | 回调函数                                |
| sender   | int      | 订阅的发送者, 当值为ANY时订阅所有发布者 |

* 返回
无

## 使用实例

```python
from blinker import signal, Signal

FLAGS = None

"""
定义类Processor，在它的go()方法中触发前面声明的ready信号，
send()方法以self为参数，Processor的实例是信号的发送者
"""
class Processor(object):

   def __init__(self, name):
       self.name = name

   def go(self):
       ready = signal('ready')
       ready.send(self)
       print('Processing...')
       complete = signal('complete')
       complete.send(self)

   def __repr__(self):
       return '<Processor {}>'.format(self.name)

# 实例化类
processor_a = Processor('a')

"""
1.使用Signal.connect()方法注册一个函数，
每当触发信号的时候，就会调用该函数。
该函数以触发信号的对象作为参数，这个函数其实就是信号订阅者。
"""
# 定义函数
def subscriber(sender):
    print("Got a signal sent by %r" % sender)

# 在命名为 ready 的signal注册subscriber函数,并发送消息
ready = signal('ready')
ready.connect(subscriber, sender=processor_a, weak=False)
processor_a.go()

"""
2.默认情况下，任意发布者触发信号，都会通知订阅者。
可以给Signal.connect()传递一个可选的参数，
以便限制订阅者只能订阅特定发送者。
"""
# 定义函数
def b_subscriber(sender):
    print("Caught signal from processor_b.")
    assert sender.name == 'b'

# 订阅特定的发布者
processor_b = Processor('b')
print(ready.connect(b_subscriber, sender=processor_b))


"""
3.可以给send()方法传递额外的关键字参数，
这些参数会传递给订阅者。
"""
# 定义收发数据signal
send_data = signal('send-data')

# 除了使用connect()方法订阅信号之外，使用@connect修饰器可以达到同样的效果
@send_data.connect
def receive_data(sender, **kw):
    FLAGS = kw
    print("Caught signal from %r, Flags: %r" % (sender, FLAGS))
    return 'received!'

# send()方法的返回值收集每个订阅者的返回值，
# 拼接成一个元组组成的列表。
# 每个元组的组成为(receiver function, return value)。
result = send_data.send('anonymous', abc=123)
print(result)


"""
4.信号可以是匿名的，可以使用Signal类来创建唯一的信号
（S大写，这个类不像之前的signal，为非单例模式）。
下面的on_ready和on_complete为两个不同的信号
"""

# 创建匿名信号类
class AltProcessor:
   on_ready = Signal()
   on_complete = Signal()

   def __init__(self, name):
       self.name = name

   def go(self):
       self.on_ready.send(self)
       print("Alternate processing.")
       self.on_complete.send(self)

   def __repr__(self):
       return '<AltProcessor %s>' % self.name

# 匿名信号订阅
apc = AltProcessor('c')
@apc.on_complete.connect
def completed(sender):
    print("AltProcessor %s completed!" % sender.name)

apc.go()

"""
5.可使用connect_via()装饰器订阅指定发送者
"""

# 订阅指定发送者
dice_roll = signal('dice_roll')
@dice_roll.connect_via(1)
@dice_roll.connect_via(3)
@dice_roll.connect_via(5)
def odd_subscriber(sender):
    print("Observed dice roll %r." % sender)

result = dice_roll.send(3)

# 检查订阅者
print(bool(signal('ready').receivers))
print(bool(signal('complete').receivers))
print(bool(AltProcessor.on_complete.receivers))

# 检查订阅者是否订阅了某个发布者
signal('ready').has_receivers_for(processor_a)
```




