from collections import defaultdict, deque

# Build the graph
def build_graph():
    edges = [
        ["A", "B"], ["A", "E"], ["A", "F"],
        ["B", "C"], ["B", "F"],
        ["C", "G"], ["C", "D"],
        ["D", "G"],
        ["E", "F"], ["E", "I"],
        ["F", "I"],
        ["G", "J"],
        ["H", "K"], ["H", "L"],
        ["I", "J"], ["I", "M"],
        ["K", "L"], ["K", "O"],
        ["L", "P"],
        ["M", "N"],
    ]
    
    graph = defaultdict(list)
    
    # create adjacency list from edge
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

# BFS
def bfs(adj, start):
    # Queue for BFS
    q = deque()
    
    # Dict track visited
    visited = {key: False for key in adj}
    
    # Mark first as visited, enqueue
    visited[start] = True
    q.append(start)

    # Iterate over queue
    while q:
        # Dequeue and print
        curr = q.popleft()
        print(curr, end=" ")

        # Get all adj vert of dequeue
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

# DFS
def dfs(adj, start, visited=None):
    if visited is None:
        visited = {key: False for key in adj}
    
    # Mark start as visit
    visited[start] = True
    print(start, end=" ")

    # Recur. all the vert adj to vert
    for neighbor in adj[start]:
        if not visited[neighbor]:
            dfs(adj, neighbor, visited)

# Add edge b/w two vert
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# MAIN **************************************************
if __name__ == "__main__":
    # Build the graph
    graph = build_graph()
    print("Graph:", graph)
    
    # preint BFS and DFS paths from A
    print("\nBFS starting from A: ")
    bfs(graph, "A")
    print("\n\nDFS starting from A: ")
    dfs(graph, "A")

    #check if paths exist for BFS/DFS
    start_node = "A"
    end_node = "D"
  