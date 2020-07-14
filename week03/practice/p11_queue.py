import queue

q = queue.Queue(5)
q.put(111)
q.put(222)
q.put(333)

print(q.get())
print(q.get())
q.task_done()

print(q.qsize())
print(q.empty())
print(q.full())