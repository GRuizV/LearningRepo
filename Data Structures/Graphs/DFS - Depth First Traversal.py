from Graphs_Implementation import WAMGraph, WALGraph, ALGraph
import collections


'The base algorithm'

# Explicit Stack Version
def es_dfs(graph, start):

    visited = set()
    stack = [start]

    while stack:

        node = stack.pop()

        if node not in visited:

            visited.add(node)

            print(node, end=' ') # Process the node (you can replace this with your own logic)

            if node in graph:

                for neighbor in graph[node]:

                    if neighbor not in visited:

                        stack.extend(neighbor)


# Recursive Version
def rec_dfs(graph, node, visited):
    
    if node not in visited:
        visited.add(node)
        print(node, end = ' ')

        if node in graph:

            for neighbor in graph[node]:

                if neighbor not in visited:
                    rec_dfs(graph, neighbor, visited)








'Testing'

#Graph Creation
al_graph = ALGraph()

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
    "M": []  

}

# print(al_graph)
# print()

dummy_graph = al_graph.get_graph()
start = 'A'


#Explicit Stack DFS Version
print(f"Explicit Stack BFS Traversal strating from node: '{start}'")

# Travesal result: A C G M F L K B E J D I H
es_dfs(dummy_graph, start)
print()
print()


#Recursive DFS Version
visited = set()

# Travesal result: A B D H I E J C F K L G M 
print(f"Recursive BFS Traversal strating from node: '{start}'")

rec_dfs(dummy_graph, start, visited)
print()






'A more complex case'

# #Graph Creation
# al_graph = ALGraph(undir=False)

# al_graph.graph = {

#    "A": ["B", "C"],
#    "B": ["D"],
#    "E": ["F"],
#    "G": ["H"],
# }

# print(al_graph)
# print()

# graph = al_graph.get_graph()


# # The task is to find all the connected components in an undirected graph

# def dfs_connected_components(graph, start):

#     visited = set()
#     stack = [start]
#     component = list()


#     while stack:

#         node = stack.pop()

#         if node not in visited:
            
#             visited.add(node)
#             component.append(node)

#         if node in graph:

#             for neighbor in graph[node]:

#                 if neighbor not in visited:

#                     stack.extend(neighbor)

#     return component


# def find_connected_components(graph):

#     visited = set()
#     components = list()

#     for node in graph:

#         if node not in visited:
            
#             component = dfs_connected_components(graph, node)
#             visited.update(component)
#             components.append(component)
    
#     return components


# components = find_connected_components(graph)

# print('Conected components in the graph:')

# for component in components:
#     print(component)







