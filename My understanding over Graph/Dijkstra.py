import math
import queue
from create_graph_from_input_file_and_print import *

graph=create_graph_from_input_file_and_print()
# print_the_graph(graph)

q=queue.PriorityQueue()
def Dijkstra(graph,source):
    dis=[math.inf]*len(graph)
    par=[-1]*len(graph)
    dis[source]=0
    q.put((dis[source],source))
    while q.qsize()!=0:
        w,u=q.get()
        for v in graph[u]:
            node_of_v, weight_of_v=v
            if w+weight_of_v<dis[node_of_v]:
                dis[node_of_v]=w+weight_of_v
                par[node_of_v]=u
                q.put((dis[node_of_v], node_of_v))

    print(dis[1:])
    print(par[1:])
Dijkstra(graph,1)