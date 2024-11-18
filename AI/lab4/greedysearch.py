#Greedy first search:
import heapq

# Define the graph using adjacency lists
city_graph = {
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

# Define heuristic values representing straight-line distances to Bucharest
straight_line_distances = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Timisoara': 329,
    'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160,
    'Sibiu': 253, 'Rimnicu Vilcea': 193, 'Fagaras': 176, 'Pitesti': 100,
    'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80, 'Hirsova': 151,
    'Eforie': 161, 'Vaslui': 199, 'Iasi': 226, 'Neamt': 234
}

def greedy_bfs(graph, start, end):
    # Priority queue to store nodes to be explored
    frontier = []
    heapq.heappush(frontier, (straight_line_distances[start], start, []))

    # Set to track visited nodes
    explored = set()

    while frontier:
        # Extract the node with the lowest heuristic value
        _, current_city, route = heapq.heappop(frontier)

        if current_city in explored:
            continue

        route.append(current_city)
        explored.add(current_city)

        if current_city == end:
            return route

        for neighbor in graph[current_city]:
            if neighbor not in explored:
                heapq.heappush(frontier, (straight_line_distances[neighbor], neighbor, route[:]))

    return None

# Perform Greedy Best First Search from Arad to Bucharest
route = greedy_bfs(city_graph, 'Arad', 'Bucharest')

print("Path:", route)
