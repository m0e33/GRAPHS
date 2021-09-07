import networkx as nx
networkx_graph = None

with open('storage/email-Eu-core-undirected.txt', 'r') as edge_list:
  networkx_graph = nx.DiGraph((line.split()[0], line.split()[1]) for line in edge_list )

nodes, edges = networkx_graph.number_of_nodes(), networkx_graph.number_of_edges()

print(len(list(networkx_graph)))

community_node_list = set()

with open('storage/email-Eu-core-department-labels.txt') as commnunities:
  for line in commnunities:
    nodes = line.split("\t")
    nodes = [node.replace("\n", "") for node in nodes]
    [community_node_list.add(node) for node in nodes]

network_nodes = set(list(networkx_graph))
# this yields the elements that are in the graph but not in the community file
print(network_nodes - community_node_list)

# this yields the elemnets that are in the community file but not in the graph
print(community_node_list - network_nodes)