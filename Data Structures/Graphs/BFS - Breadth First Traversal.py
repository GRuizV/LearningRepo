from Graphs_Implementation import WAMGraph, WALGraph, ALGraph
import collections


'The base algorithm'
def bfs(graph, start):

    visited = set()
    queue = collections.deque([start])
    
    while queue:

        node = queue.popleft()
        
        if node not in visited:

            visited.add(node)

            print(node) # Process the node (you can replace this with your own logic)

            # Enqueue unvisited neighbors
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)


'The Shortest Path form'
def shortest_path_bfs(graph, start, end):
    
    visited = set()
    queue = collections.deque([(start, [start])])  # Queue stores a tuple with the current node and the path so far

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path  # Found the shortest path

        if current not in visited:

            visited.add(current)

            for neighbor in graph.get(current, []):

                if neighbor not in visited:

                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

    return None  # No path found





'Testing'

# #Graph Creation
# al_graph = ALGraph(undir=False)

# [al_graph.add_vertex(x) for x in range(1,7)]

# [al_graph.add_edge(1,x) for x in range(2,4)]
# [al_graph.add_edge(2,x) for x in range(4,6)]
# al_graph.add_edge(3,6)
# al_graph.add_edge(5,6)

# print(al_graph)
# print()

# dummy_graph = al_graph.get_graph()
# start = 1

# print(f"BFS Traversal strating from node: '{start}'")

# bfs(dummy_graph, start)






'A more complex case'

#Graph Creation
al_graph = ALGraph(undir=False)

al_graph.graph = {

    "Boston": ["New York", "Providence"],
    "New York": ["Boston", "Philadelphia", "Providence"],
    "Philadelphia": ["New York", "Las Vegas"],
    "Providence": ["Boston", "New York", "Hartford"],
    "Hartford": ["Providence"],
    "San Francisco": ["Los Angeles", "Seattle"],
    "Los Angeles": ["San Francisco", "Las Vegas"],
    "Las Vegas": ["Los Angeles"],
    "Seattle": ["San Francisco"]
}

print(al_graph)




graph = al_graph.get_graph()
start_city = "Boston"
end_city = "San Francisco"
path = shortest_path_bfs(graph, start_city, end_city)

if path:
    print(f"Shortest path from {start_city} to {end_city}: {path}")
else:
    print(f"No path found from {start_city} to {end_city}")