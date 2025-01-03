def create_graph_from_input_file_and_print():
    with open("input.txt", "r") as infile:
        vertex, edge = map(int, infile.readline().split())

        graph = {}  # created a dictionary
        for i in range(vertex + 1):  # creating all the vertex+1 (including 0) with a empty list
            graph[i] = []

        for i in range(edge):  # connecting all the edge
            s, d, wt = map(int, infile.readline().split())
            graph[s].append((d, wt))
            # graph[d].append((s, wt))



    return graph
def print_the_graph(graph):
    for k, v in graph.items():  # printing the graph
        print(k, v)