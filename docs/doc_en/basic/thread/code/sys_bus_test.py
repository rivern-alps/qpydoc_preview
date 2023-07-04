import sys_bus
import utime 
def cb_callback(topic, msg):
    print(topic, msg)
# Support registering multiple subscription functions by one topic. 
sys_bus.subscribe("topic1", cb_callback)
sys_bus.subscribe("topic2", cb_callback)
sys_bus.subscribe("topic3", cb_callback)


" The subscriber will receive message after publishing"
sys_bus.publish("topic1", " What printed here is the message published by topic 1")
utime.sleep(2)
sys_bus.publish("topic2", " What printed here is the message published by topic 2")
utime.sleep(2)
sys_bus.publish("topic3", " What printed here is the message published by topic 3")
utime.sleep(2)

print(sys_bus.sub_table())
# Return {"topic1": set(cb_callback...)}
utime.sleep(2)
print(sys_bus.sub_table("topic1"))
# Return set(cb_callback...)

sys_bus.unsubscribe("topic1", cb_callback)
# As suscribing callback has been cancelled above, the following publication won' t slide into the former callback. That means: the subscribed message can still be received, however, there is no callback.  
sys_bus.publish("topic1", "What printed here is the message published by topic 1")

sys_bus.unsubscribe("topic1")
# As the subscription of topic 1 has been cancelled, the following publication won't receive any message. 
sys_bus.publish("topic1", " What printed here is the message published by topic 1")