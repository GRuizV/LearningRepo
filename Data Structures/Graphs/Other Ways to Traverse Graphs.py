from Graphs_Implementation import WAMGraph, WALGraph, ALGraph
import collections
import heapq


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






