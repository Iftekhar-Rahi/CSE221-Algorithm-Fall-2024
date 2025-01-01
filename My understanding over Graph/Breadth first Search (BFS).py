# Steps of BFS
# Say you have already created the graph
# 1. Create a queue
# 2. Create an array to track visited vertexes
# 3. enqueue the source before the searching
# 4. Start the searching with a while loop until the queue is empty
# 5. steps of searching
#   1. dequeue an element from the queue and check if it is visited or not.                                 -1= unvisited,
#          if visited, update 1 in visited array                                                             0= visited but not explored,
#   2. push all the adjecent vertex in the queue and mark them as 0 in the visited array                     1= visited and explored

from queue import Queue
from create_graph_from_input_file_and_print import *              #from the_file import the_function
graph=create_graph_from_input_file_and_print()
def BFS(graph, source):
    q = Queue()
    visited = [0] *len(graph)
    q.put(source)
    while q.qsize()!=0:
        current=q.get()
        if visited[current]==0:
            visited[current] = 1
            print(current, end=" ")
            for neigh in graph[current]:
                # print(neigh)
                if visited[neigh[0]] == 0:
                    q.put(neigh[0])
        else:
            q.get()
BFS(graph,1)
# print_the_graph(graph)