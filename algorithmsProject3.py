"""
Algorithms Project 3, Part 3

This program allows the user to experiment with different graph-related algorithms
(Dijkstra's for shortest path tree, Kruskal's for MST) and their implications.

Carson Stell
"""
import networkx

def create_weighted_graph():
    # Initialize an undirected weighted graph
    G = networkx.Graph()
    
    # Add edges
    edges = [
        ('A', 'B', 22), ('A', 'C', 9),
        ('A', 'D', 12), ('B', 'C', 35),
        ('B', 'F', 36), ('B', 'H', 34),
        ('C', 'D', 4), ('C', 'E', 65),
        ('C', 'F', 42), ('D', 'E', 33),
        ('D', 'I', 30), ('E', 'F', 18),
        ('E', 'G', 23), ('F', 'G', 39),
        ('F', 'H', 24), ('G', 'H', 25),
        ('G', 'I', 21), ('H', 'I', 19)
    ]
    
    G.add_weighted_edges_from(edges)
    return G

def dijkstra_shortest_path_tree(G, start_node):
    shortest_path_tree = networkx.single_source_dijkstra_path(G, start_node)
    shortest_path_lengths = networkx.single_source_dijkstra_path_length(G, start_node)
    
    # Create new graph for the shortest path tree
    tree = networkx.Graph()
    
    # Add edges to the tree based on the shortest paths
    for target, path in shortest_path_tree.items():
        for i in range(len(path) - 1):
            tree.add_edge(path[i], path[i + 1], weight=G[path[i]][path[i + 1]]['weight'])
    
    return tree, shortest_path_lengths

def minimum_spanning_tree(G):
    mst = networkx.minimum_spanning_tree(G, weight='weight')
    
    # Create list to store edges in the order they were added to the MST
    mst_edges = list(mst.edges(data=True))
    
    # Sort edges by weight to show correct order of additions
    mst_edges.sort(key=lambda x: x[2]['weight'])
    return mst_edges

def main():
    G = create_weighted_graph()
    
    # Set the starting node for Dijkstra's algorithm
    start_node = 'A'
    
    # Get the shortest path tree from the starting node
    shortest_path_tree, shortest_path_lengths = dijkstra_shortest_path_tree(G, start_node)
    
    print("Would you like to find:\n\n1.\tShortest Path Tree\n2.\tMinimum Spanning Tree\n")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        print(f"\nShortest Path Tree from node {start_node}:")
        for u, v, data in shortest_path_tree.edges(data=True):
            print(f"Edge ({u}, {v}) - weight: {data['weight']}")
    
    elif choice == 2:
        mst_edges = minimum_spanning_tree(G)
        print("\nMinimum Spanning Tree:")
        for u, v, weight in mst_edges:
            print(f"Edge ({u}, {v}) - {weight}")

if __name__ == "__main__":
    main()