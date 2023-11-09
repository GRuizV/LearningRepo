from Graphs_Implementation import AMGraph, ALGraph
import collections



'Adjacency Matrix'
# am_graph = WAMGraph(5)

# print(am_graph)
# print()

# am_graph.add_edge(0,1,5)

# print(am_graph)
# print()

# am_graph.remove_edge(0,1)

# print(am_graph)



'Adjacency List'
al_graph = ALGraph()

# print(al_graph)
# print()

[al_graph.add_vertex(x) for x in range(1, 5)]

# print(al_graph)
# print()

[al_graph.add_edge(1,x) for x in range(2,5)]

# print(al_graph)
# print()

al_graph.remove_edge(0, 4)
al_graph.add_edge(2,4,5)

# print(al_graph)


# print(al_graph.graph, end='\n\n')

al_graph.graph = {

    "A": ["B", "C"],
    "B": ["D", "E"],
    "D": ["H", "I"],
    "H": [],
    "I": [],
    "E": ["J"], 
    "J": [],
    "C": ["F", "G"],
    "F": ["K", "L"],
    "K": [],
    "L": [],
    "G": ["M"],
    "M": [],
}

al_graph.graph = {

    "A": ["B", "C"],
    "B": ["D", "E"],
    "D": ["H", "I"],
    "E": ["J"], 
    "C": ["F", "G"],
    "F": ["K", "L"],
    "G": ["M"],
}

al_graph.pretty_print()


















