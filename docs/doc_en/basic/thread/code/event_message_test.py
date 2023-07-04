from event_message import Event
import utime
"""
1. Initialize event
2. Initialize event manager
3. Register event to event manager
4. Start event manager
5. Add event manager
6. Dispatch data
"""
from event_message import Event, EventManager
# Initialize event and event manager
event = Event("test")
event_manager = EventManager()
# Register event
event_manager.register_event(event)
# Start event manager
event_manager.start()
# Add event manager, you can comment different event types by patches. 
@event.add_handler_via()
def handler(**kwargs):
    em = kwargs["event_message"]
    """
    The first way to get data
    kwargs:{
        "event_message":EventMessageObject
    }
    Four attributes are invloved in EventMessageObject
        event_name
        msg
        event
        callback
        It provides the method to get by itself and by combination. As for getting by combination, following methods are available, the model_to_dict()will get the dictionary of combination. 
        {
            'name': 'test',
            'event': event_object,
            'msg': '1111',
            'callback': None
        }
    """
    
    print("handler1 {}".format(kwargs))
    """
    1. Method to get the first attribute
        # Get the event name
            event_name = em.event_name
        # Get the event message
            msg = em.msg
        # Get the original event
            ev = em.event
        # None Get the transmitted callback, it is None by default if there is no transmission. 
            cb = em.callback
    """
    """
    2. The way to get the second attribute value(Recommended)
        data_map = em.model_to_dict()
            {
                'name': 'test',
                'event': event_object,
                'msg': '1111',
                'callback': None
            }
    """
# Asynchronous dispatch data instead of block 
while True:
    event.post(message="1111")
    utime.sleep(2)