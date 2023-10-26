from Graphs_Implementation import WAMGraph, WALGraph, ALGraph
import collections


'Topological Sort'

# def topological_sort(graph):

#     def topological_sort_util(node, visited, stack):

#         visited[node] = True

#         for neighbor in graph.get(node, []):

#             if neighbor not in visited or not visited[neighbor]:

#                 topological_sort_util(neighbor, visited, stack)

#         stack.insert(0, node)


#     visited = {node: False for node in graph}
#     stack = list()

#     for node in graph:
        
#         if not visited[node]:
            
#             topological_sort_util(node, visited, stack)

#     return ' '.join(str(x) for x in stack)




# # Graph initialization
# al_graph = ALGraph()

# al_graph.graph = {

#     "A": ["B", "C"],
#     "B": ["D", "E"],
#     "D": ["H", "I"],
#     "E": ["J"], 
#     "C": ["F", "G"],
#     "F": ["K", "L"],
#     "G": ["M"],
# }


# graph = al_graph.get_graph()
# result = topological_sort(graph)

# # A C G M F L K B E J D I H
# print(result)









