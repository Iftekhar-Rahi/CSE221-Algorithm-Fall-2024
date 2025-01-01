from queue import Queue
from create_graph_from_input_file_and_print import *
graph=create_graph_from_input_file_and_print()



def BFS(graph,source):
    q=Queue()
    visited=[0]*len(graph)
    q.put(source)
    while q.qsize()!=0:
        current=q.get()
        if visited[current]==0:
            visited[current] =1
            print(current, end=" ")
            for neigh in graph[current]:
                if visited[neigh[0]]==0:
                    q.put(neigh[0])
        else:
            q.get()
BFS(graph,1)