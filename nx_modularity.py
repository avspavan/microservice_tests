import networkx as nx

# Define the service's module dependencies as a graph
service_graph = nx.DiGraph()
service_graph.add_nodes_from(['module1', 'module2', 'module3', 'module4'])
service_graph.add_edges_from([('module1', 'module2'), ('module2', 'module3'), ('module3', 'module4')])

# Compute the modularity metric for the service
modularity = nx.algorithms.community.modularity(service_graph, [[n] for n in service_graph.nodes])

# Print the modularity metric
print(f"The modularity of the service is {modularity:.3f}")
