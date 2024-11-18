#A* search:

import heapq

# Define the graph using a dictionary where each key represents a node and its value is another dictionary of connected nodes and their distances.
graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Define heuristic values representing straight-line distances to Bucharest (estimated)
heuristics = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Timisoara': 329,
    'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160,
    'Sibiu': 253, 'Rimnicu Vilcea': 193, 'Fagaras': 178, 'Pitesti': 98,
    'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80, 'Hirsova': 151,
    'Eforie': 161, 'Vaslui': 199, 'Iasi': 226, 'Neamt': 234
}

def a_star(graph, start, end):
    # Priority queue for nodes to explore
    open_set = []
    heapq.heappush(open_set, (heuristics[start], 0, start, []))

    # Set of explored nodes
    closed_set = set()

    while open_set:
        # Get the node with the lowest f(n) = g(n) + h(n)
        estimated_cost, actual_cost, node, path = heapq.heappop(open_set)
        
        if node in closed_set:
            continue

        path = path + [node]
        closed_set.add(node)

        if node == end:
            return path, actual_cost

        for neighbor, distance in graph[node].items():
            if neighbor not in closed_set:
                new_cost = actual_cost + distance
                heapq.heappush(open_set, (new_cost + heuristics[neighbor], new_cost, neighbor, path))

    return None, None

# Perform A* search from Timisoara to Neamt
path, total_cost = a_star(graph, 'Arad', 'Bucharest')

print("Optimal Path:", path)
print("Total Cost:", total_cost)
