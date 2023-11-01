from Graphs_Implementation import WAMGraph, WALGraph, ALGraph
import collections
import heapq
from timeit import default_timer as timer

'Topological Sort'

def topological_sort(graph):

    def topological_sort_util(node, visited, stack):

        visited[node] = True

        for neighbor in graph.get(node, []):

            if neighbor not in visited or not visited[neighbor]:

                topological_sort_util(neighbor, visited, stack)

        stack.insert(0, node)


    visited = {node: False for node in graph}
    stack = list()

    for node in graph:
        
        if not visited[node]:
            
            topological_sort_util(node, visited, stack)

    return ' '.join(str(x) for x in stack)



'Topological Sort Testing'

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



"Dijkstra's testing"

# # Graph initialization
# al_graph = ALGraph()

# al_graph.graph = {

#     "A": [("B", 1),("C", 4)],
#     "B": [("C", 2),("D", 5)],
#     "C": [("D", 1)],
    
# }


# graph = al_graph.get_graph()
# start = "A"

# # print(al_graph)

# result = dijkstra(graph, start)


# # Expected Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
# print(result)






"A* Search Algorithm"

def astar(graph, start, goal):
    # Initialize open and closed sets
    open_set = []
    closed_set = set()

    # Create a dictionary to keep track of the best known path to each node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # Create a dictionary to store the parent node of each node
    parent = {}

    # Add the starting node to the open set with a priority of 0
    heapq.heappush(open_set, (0, start))

    while open_set:

        # Get the node with the lowest f-score from the open set
        _, current = heapq.heappop(open_set)

        if current == goal:

            # Reconstruct the path if the goal is reached
            path = []

            while current in parent:

                path.insert(0, current)
                current = parent[current]

            path.insert(0, start)

            return path


        closed_set.add(current)

        for neighbor, cost in graph[current]:

            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:

                # This is a better path to the neighbor
                parent[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    # No path found
    return None

def heuristic(node, goal):
    # This is a simple heuristic; you can modify it for specific problems
    return 0  # For Dijkstra's algorithm, set it to 0



'A* Testing'

# # Graph initialization
# al_graph = ALGraph()

# al_graph.graph = {

#     "A": [("B", 1),("C", 4)],
#     "B": [("C", 2),("D", 5)],
#     "C": [("D", 1)],
    

# }

# al_graph.graph = {
#     'A': [('B', 1), ('C', 3)],
#     'B': [('D', 2)],
#     'C': [('D', 2)],
#     'D': [('E', 3)],
#     'E': []
# }



# graph = al_graph.get_graph()
# start = "A"
# goal = "E"


# # print(al_graph)

# path = astar(graph, start, goal)
# cost = int()

# for i in range(len(path[:-1])):

#     node = graph[path[i]]
#     idx = [x[0] for x in node].index(path[i+1])
#     cost += node[idx][1]


# print(f'A* path: {' '.join(str(x) for x in path)}', end= '\n')
# print(f'A* cost: {cost}')
# print()


# dijkstra_path = dijkstra(graph, start)
# print(f"Dijkstra's result ({dijkstra_path})")






"Bellman-Ford Algorithm"

def bellman_ford(graph, source_vertex):

    all_nodes = [x for x in graph]
    all_nodes.extend([x[0] for elem in graph.values() for x in elem if x[0] not in all_nodes])
    all_nodes = sorted((set(all_nodes)))

    distance = {vertex: float('inf') for vertex in all_nodes}
    distance[source_vertex] = 0

    for _ in range(len(all_nodes) - 1):

        for vertex in graph:

            for neighbor in graph[vertex]:

                if distance[vertex] != float('inf'):

                    if isinstance(neighbor, tuple):

                        neighbor_vertex, weight = neighbor

                        if distance[vertex] + weight < distance[neighbor_vertex]:
                            distance[neighbor_vertex] = distance[vertex] + weight
                    
                    else:
                        if distance[vertex] + 1 < distance[neighbor]:
                            distance[neighbor] = distance[vertex] + 1

    return distance



# # Graph initialization
# al_graph = ALGraph()

# al_graph.graph = {

#     "A": [("B", 4), ("C", 3)],
#     "B": [("C", -2),("D", 2)],
#     "C": [("E", 5)],
#     "D": [("C", 1), ("E", 2)]
# }


# graph = al_graph.get_graph()

# start = 'A'

# distances = bellman_ford(graph, start)

# print(f'The shortest distance from "{start}" to each node is:')

# for i in distances:
#     print(f'to "{i}": {distances[i]}', end='\t')






"Iterative Deepening Depth-First Search (IDDFS)"


def iddfs(graph, start, target):

    def dfs(graph, node, target, depth, max_depth, visited):

        if depth > max_depth:
            return None, []
        
        visited.add(node)

        if node == target:
            return [node], visited
           
        for neighbor in graph.get(node, []):

            if neighbor not in visited:
                
                new_path, _ = dfs(graph, neighbor, target, depth + 1, max_depth, visited)

                if new_path:
                    return [node] + new_path, visited
                
        return None, visited


    for depth_limit in range(len(graph)):

        visited = set()

        result, _ = dfs(graph, start, target, 0, depth_limit, visited)

        if result is not None:
            return result
        
    return None





# # Graph Creation
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

# start = "A"
# target = "K"

# result = iddfs(graph, start, target)

# print(result)   # ['A', 'C', 'F', 'K']






" - Now let's make DFS, BFS and IDDFS compete - "


# def bfs(graph, start, target):

#     visited = set()
#     queue = collections.deque([start])
    
#     while queue:

#         node = queue.popleft()
        
#         if node not in visited:

#             visited.add(node)

#             if node == target:
#                 return print(f"found target: '{target}'")

#             # Enqueue unvisited neighbors
#             for neighbor in graph.get(node, []):

#                 if neighbor not in visited:

#                     queue.extend([neighbor])
    
#     print()



# def es_dfs(graph, start, target):

#     visited = set()
#     stack = [start]

#     while stack:

#         node = stack.pop()

#         if node not in visited:

#             visited.add(node)

#             if node == target:
#                 return print(f"found target: '{target}'")

#             if node in graph:

#                 for neighbor in graph[node]:

#                     if neighbor not in visited:

#                         stack.extend(neighbor)



# # Graph Creation
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
# start = "A"
# target = "L"


# print()
# print(f'Depth-First Search')
# s = timer()
# es_dfs(graph, start, target)
# e = timer()
# print(f'time: {e-s:.2e}s')
# print()

# print(f'Breadth-First Search')
# s = timer()
# bfs(graph, start, target)
# e = timer()
# print(f'time: {e-s:.2e}s')
# print()


# print(f'Iterative Deepening Depth-First Search')
# s = timer()
# result = iddfs(graph, start, target)
# e = timer()
# print(f"found target: '{result[-1]}'")
# print(f'time: {e-s:.2e}s')
# print()






"Bi-Directional Search"

def bidirectional_search_with_path(graph, start, goal):

    forward_queue = collections.deque([(start, [start])])
    backward_queue = collections.deque([(goal, [goal])])
    forward_visited = set([start])
    backward_visited = set([goal])

    while forward_queue and backward_queue:

        current_node_forward, path_forward = forward_queue.popleft()

        for neighbor in graph.get(current_node_forward, []):

            if neighbor not in forward_visited:

                forward_visited.add(neighbor)
                new_path = path_forward + [neighbor]
                forward_queue.append((neighbor, new_path))


        current_node_backward, path_backward = backward_queue.popleft()

        for neighbor in graph.get(current_node_backward, []):

            if neighbor in forward_visited:
                
                # Merge the forward and backward paths when a meeting point is found
                meeting_node = neighbor
                forward_path = next(path for node, path in forward_queue if node == meeting_node)
                return forward_path + path_backward[::-1]

            if neighbor not in backward_visited:

                backward_visited.add(neighbor)
                new_path = path_backward + [neighbor]
                backward_queue.append((neighbor, new_path))

    return []  # No path found





# Graph Creation

al_graph = ALGraph(weighted=False)

[al_graph.add_vertex(x) for x in "ABCDEFGHIJKLMNOP"]

[al_graph.add_edge("A", x, None) for x in "BC"]
[al_graph.add_edge("B", x, None) for x in "ADG"]
[al_graph.add_edge("C", x, None) for x in "AFE"]
[al_graph.add_edge("D", x, None) for x in "BH"]
[al_graph.add_edge("G", x, None) for x in "BH"]
[al_graph.add_edge("F", x, None) for x in "CI"]
[al_graph.add_edge("E", x, None) for x in "CK"]
[al_graph.add_edge("H", x, None) for x in "DGJMI"]
[al_graph.add_edge("I", x, None) for x in "FHK"]
[al_graph.add_edge("J", x, None) for x in "HPL"]
[al_graph.add_edge("K", x, None) for x in "IEMO"]
[al_graph.add_edge("P", x, None) for x in "JL"]
[al_graph.add_edge("L", x, None) for x in "JPN"]
[al_graph.add_edge("M", x, None) for x in "HKON"]
[al_graph.add_edge("O", x, None) for x in "KM"]
[al_graph.add_edge("N", x, None) for x in "LM"]

# al_graph.graph = {  
#     "A": ['B', 'C'],
#     "B": ['A', 'D', 'G'],
#     "C": ['A', 'F', 'E'],
#     "D": ['B', 'H'],
#     "E": ['C', 'K'],
#     "F": ['C', 'I'],
#     "G": ['B', 'H'],
#     "H": ['D', 'G', 'J', 'M', 'I'],
#     "I": ['F', 'H', 'K'],
#     "J": ['H', 'P', 'L'],
#     "K": ['E', 'I', 'M', 'O'],
#     "L": ['J', 'P', 'N'],
#     "M": ['H', 'K', 'O', 'N'],
#     "N": ['L', 'M'],
#     "O": ['K', 'M'],
#     "P": ['J', 'L']
# }

# for i in al_graph.graph:
#     print(f'"{i}": {al_graph.graph[i]}')




graph = al_graph.get_graph()

start = "A"
target = "N"


path = bidirectional_search_with_path(graph, start, target)

# Expected Output: ["A", "B", "D", "H", "J", "L", "N"]
print(path)











