from queue import Queue
from create_graph_from_input_file_and_print import *
graph=create_graph_from_input_file_and_print()
print_the_graph(graph)

visited=[-1]*len(graph)
def DFS(elem):
    for d,w in graph[elem]:
        if visited[d]==-1:
            visited[d]=0
            DFS(d)
    visited[elem]=1
    print(d)
visited[1]=0
DFS(1)
