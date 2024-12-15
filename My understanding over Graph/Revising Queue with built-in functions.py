from queue import Queue

q = Queue()
q.put(10)  # Enqueue
q.put(20)  # Enqueue
print(q.qsize())
print(q.get())  # Dequeue: 10
print(q.get())
print(q.qsize())
# for enqueue q.put(10)
#for dequeue q.get()
# for size q.qsize()
