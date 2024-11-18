#Construct the given tree, write a breadth first search function def
#bfs(graph, start_node, goal_node) which should return goal node if the
#data is found in the tree else return None.

def bfs(graph, start_node, goal_node):  # function for BFS
    visited = set()  # set for visited nodes so that no any nodes are repeated.
    queue = []  # Initialize a queue
    if start_node == goal_node:
        return start_node
     
    visited.add(start_node)# to add visited nodes of graph
    queue.append(start_node) #append = add

    while queue:          # Creating loop to visit each node
        path = queue.pop(0)
        # print '->' after each node except the last one
        print(path, end='->' if path != f'{goal_node}' else '')
        if path == goal_node:
            return path
     
        for neighbour in graph[path]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return None

graph = {
    '1': ['2', '3','4'],
    '2': ['5', '6'],
    '4': ['7','8'],
    '5': ['9', '10'],
    '7': ['11','12'],
    '3': [],
    '6': [],
    '8': [],
    '9': [],
    '10':[],
    '11': [],
    '12':[]
}

# Driver Code
start_node = '1'
goal_node = '8'
print("Following is the Breadth-First Search path:")

result = bfs(graph, start_node,goal_node)
if result is None:
    print("\nGoal node not found.")