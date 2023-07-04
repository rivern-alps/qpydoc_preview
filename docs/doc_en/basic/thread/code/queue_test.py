import _thread
from queue import Queue
import utime
# Initialize queue
q = Queue(maxsize=100)
def get():
    while True:
# The q.get will wait until get the message. Whenever the q.put is executed, the q.get will delete block and carry on if influenced by relevant signal. 
        item = q.get()
        print(item)
# Start the thread and wait for message in which place. 
_thread.start_new_thread(get,())
# put the message to queue
q.put(1)
utime.sleep(2)
q.put(2)
utime.sleep(2)
q.put(3)