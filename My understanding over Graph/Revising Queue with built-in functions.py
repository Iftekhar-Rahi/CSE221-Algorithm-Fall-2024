from queue import Queue
my_queue=Queue()
my_queue.put(5)         # Enqueue
my_queue.put(10)        # Enqueue
print(my_queue.get())   # Dequeue
print(my_queue.qsize()) # Size
