#Construct the tree as in the previous question, write a depth first search
#function def dfs(graph, start_node, goal_node) which should return goal
#node if the data is found in the tree else return None. 




def dfs(graph, start_node, goal_node):  # function for DFS
    visited = set()  # set for visited nodes so that no any nodes are repeated.
    stack = []  # Initialize a stack
    if start_node == goal_node:
        return start_node

    visited.add(start_node)  # to add visited nodes of graph
    stack.append(start_node)  # append = add

    while stack:  # Creating loop to visit each node
        path = stack.pop()
        # print '->' after each node except the last one
        print(path, end='->' if path != f'{goal_node}' else '')
        if path == goal_node:
            return path

        for neighbour in reversed(graph[path]):  # reversed to maintain order similar to BFS
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
    
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
print("Following is the Depth-First Search path:")
result = dfs(graph, start_node, goal_node)
if result is None:
    print("\nGoal node not found.")

