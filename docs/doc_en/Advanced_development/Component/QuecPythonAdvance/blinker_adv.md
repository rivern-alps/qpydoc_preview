---
title: Blinker
keywords: Blinker
description: Blinker Development
---
## Revision history

| Version | **Date**   | **Author** | Description     |
| ------- | ---------- | ---------- | --------------- |
| 1.0     | 2021-09-14 | Pawn       | Initial Version |


## About Blinker
Blinker, a powerful signal library based on Python, supports the subscription and publication mode of one-to-one and one-to many. Meanwhile, it supports transmitting the data with various sizes and makes the thread safe. 

## APIs

### blinker.ANY
Static value, this value is used to send message to anyone.

* Parameter

​        None

* Returned value

​       None

### Signal.connect (receiver, sender=ANY, weak=False)
Subscribe signal to sender
* Parameter

| Parameter | Type     | Illustration                                                 |
| --------- | -------- | ------------------------------------------------------------ |
| receiver  | function | Callback function                                            |
| sender    | int      | The subscribed sender. If the value is ANY, it means subscribing all publishers. |
| weak      | Boolean  | Weak Reference option, this function is invalid with a default value of FALSE. |

* Return 

​       Receiver



### Signal.connect_via (sender, weak=False)
Subscribe assigned sender via decorators 

* Parameter

| Parameter | Type    | Illustration                                                 |
| --------- | ------- | ------------------------------------------------------------ |
| sender    | int     | The subscribed sender. If the value is ANY, it means subscribing all publishers. |
| weak      | Boolean | Weak Reference option, this function is invalid with a default value of FALSE. |

* Return

​       Return to decorator


### Signal.send (*sender, **kwargs)
Notify subscriber via "send"

* Parameter

| Parameter | Type | Illustration |
|  ----  | ----  | ---- |
| sender | object | Any object is available,  if omitted, the value will be None |
| kwargs | dict | The data should be sent to receiver |
* Return 

​       The receiver list for subscribing sender

### Signal.has_receivers_for (sender)
Query whether the subscriber subscribes the exact signal publisher. 

* Parameter

| Parameter | Type | Illustration |
|  ----  | ----  | ---- |
| sender | object | Sender object |

* Return 
Return True or False

### Signal.receivers_for (sender)
Return the *iterator* of subscriber 

* Parameter

| Parameter | Type | Illustration |
|  ----  | ----  | ---- |
| sender | object | Sender object |

* Return 
It includes the iterator of all subscribers. 

### Signal.disconnect (receiver, sender=ANY)
Cancel subscription

* Parameter

| Parameter | Type     | Illustration                                                 |
| --------- | -------- | ------------------------------------------------------------ |
| receiver  | function | Callback function                                            |
| sender    | int      | The subscribed sender. If the value is ANY, it means subscribing all publishers. |

* Return 
None

## Application 

```python
from blinker import signal, Signal

FLAGS = None

"""
Class Processor, it will trigger the ready signal mentioned beforehand in go() method.
However, in send() method, the self serves as parameter and the real case of Processor is the signal sender.
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

# 实例化类 instantiation class
processor_a = Processor('a')

"""
1.Register one function via the method of Signal.connect()
when triggering signal, this function will be called
Since this function takes the object of triggering signal as parameter, actually, it is the signal subscriber. 
"""
# Define function
def subscriber(sender):
    print("Got a signal sent by %r" % sender)

# Register the subscriber function to the signal named ready as well as send message
ready = signal('ready')
ready.connect(subscriber, sender=processor_a, weak=False)
processor_a.go()

"""
2.It will notify subscriber by default no matter which publisher triggers signal.
Transmit one optional parameter to Signal.connect() so as to make the subscriber subscribes the specific sender only. 
"""
# Define function
def b_subscriber(sender):
    print("Caught signal from processor_b.")
    assert sender.name == 'b'

# Subscribe specific publisher
processor_b = Processor('b')
print(ready.connect(b_subscriber, sender=processor_b))


"""
3.It is available to transmit extra parameters of key words via send().
These parameter will be transmitted to subscribers. 
"""
# Define the data signal of receiving and sending
send_data = signal('send-data')

# Besides subscribing signal via connect(), it also works via @connect decorator. 
@send_data.connect
def receive_data(sender, **kw):
    FLAGS = kw
    print("Caught signal from %r, Flags: %r" % (sender, FLAGS))
    return 'received!'

# The returned value of send() will gather the returned value of each subscriber. 
# Integrate one list with tuples.
# The very elements of each tuple serve as (receiver function, return value)
result = send_data.send('anonymous', abc=123)
print(result)


"""
4.The signal can be anonymous or to create the unique signal via Signal class.
(Kind reminder: The S shuould be capital since this class is differnt from the former signal, it is non-single case mode)
As following on_ready and on_complete show, they are different signals.
"""

# Create anonymous signal class
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

# Subscribe anonymous signal
apc = AltProcessor('c')
@apc.on_complete.connect
def completed(sender):
    print("AltProcessor %s completed!" % sender.name)

apc.go()

"""
5.Subscribe assigned sender via connect_via() decorator. 
"""

# Subscribe assigned sender
dice_roll = signal('dice_roll')
@dice_roll.connect_via(1)
@dice_roll.connect_via(3)
@dice_roll.connect_via(5)
def odd_subscriber(sender):
    print("Observed dice roll %r." % sender)

result = dice_roll.send(3)

# Check subscriber
print(bool(signal('ready').receivers))
print(bool(signal('complete').receivers))
print(bool(AltProcessor.on_complete.receivers))

# Check whether the subscriber subscribes the exact publisher
signal('ready').has_receivers_for(processor_a)
```




