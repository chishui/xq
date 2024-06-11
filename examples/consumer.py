from xq.worker import Worker
from xq.queue import Queue
import redis

r = redis.Redis(host='localhost', port=6379)

q = Queue(r)
worker = Worker(q, print)


worker.run()
