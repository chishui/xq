from xq.worker import Worker
from xq.queue import Queue
import time
import redis
from datetime import datetime, timedelta 

r = redis.Redis(host='localhost', port=6379)

q = Queue(r)

current_time = datetime.now()
for i in range(1, 10):

    future_time = current_time + timedelta(seconds=10*i)
    q.enqueue(str(i), future_time)
