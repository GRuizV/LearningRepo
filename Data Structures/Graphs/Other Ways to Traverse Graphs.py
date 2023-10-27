from Graphs_Implementation import WAMGraph, WALGraph, ALGraph
import collections
import heapq


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






"Dijkstra's Algorithm"

def dijkstra(graph, start_vertex):

    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]

    while priority_queue:

        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Ignore outdated entries
        if current_distance > distances[current_vertex]:
            continue

        if current_vertex in graph:

            for neighbor, weight in graph[current_vertex]:

                distance = current_distance + weight

                if distance < distances.get(neighbor, float('infinity')):

                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances



# Graph initialization
al_graph = ALGraph()

al_graph.graph = {

    "A": [("B", 1),("C", 4)],
    "B": [("C", 2),("D", 5)],
    "C": [("D", 1)],
    

}


graph = al_graph.get_graph()
start = "A"

# print(al_graph)

result = dijkstra(graph, start)


# Expected Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
print(result)






