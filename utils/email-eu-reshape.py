from snap.snap import *
from networkx.readwrite.edgelist import write_edgelist
import networkx as nx
from networkx import read_edgelist


# relabel node in graph
with open('storage/email-Eu-core.txt', 'r') as edge_list:
  networkx_graph = nx.DiGraph((line.split()[0], line.split()[1]) for line in edge_list)


nodes, edges = networkx_graph.number_of_nodes(), networkx_graph.number_of_edges()
print(f"Loaded Graph with {nodes} nodes and {edges} edges")
networkx_graph = nx.relabel_nodes(networkx_graph, {'0': str(1005)},)

undirected_graph_path_networkx = 'storage/email-Eu-core-1005-networkx.txt'
undirected_graph_path = 'storage/email-Eu-core-undirected-1005.txt'

undirected_Networkx_graph = nx.to_undirected(networkx_graph)

write_edgelist(undirected_Networkx_graph, undirected_graph_path_networkx)

with open(undirected_graph_path_networkx, 'r') as networkx_format_file:
  with open(undirected_graph_path, 'w') as snap_format_file:
    for line in networkx_format_file:
      new_line = line.rsplit(' ', 1)[0]
      new_line += '\n'
      snap_format_file.write(new_line)

# relabel node in
with open('storage/email-Eu-core-department-labels.txt', 'r') as cmtys_old:
  with open('storage/email-EU-core-department-labels-1005.txt', 'w') as cmtys_new:
    for cmty in cmtys_old:

      cmty_set = set([int(node_id) for node_id in cmty.split('\t')])
      if 1006 in cmty_set:
        cmty_set.remove(1006)
        cmty_set.add(1005)

        new_cmty_line = "\t".join([str(node_id) for node_id in cmty_set])
        cmtys_new.write(new_cmty_line + "\n")
      else:
        cmtys_new.write(cmty)

undirected_graph_path = 'storage/email-Eu-core-undirected.txt'

# relabel node in communities

#with open('storage/com-dblp.all.cmty-old.txt', 'r') as cmtys_old:
  #with open('storage/com-dblp.all.cmty.txt', 'w') as cmtys_new:
    #for cmty in cmtys_old:

      #cmty_set = set([int(node_id) for node_id in cmty.split('\t')])
      #if 0 in cmty_set:
        #cmty_set.remove(0)
        #cmty_set.add(nodes)

        #new_cmty_line = "\t".join([str(node_id) for node_id in cmty_set])
        #cmtys_new.write(new_cmty_line + "\n")
      #else:
        #cmtys_new.write(cmty)

    #undirected_graph_path = 'storage/email-Eu-core-undirected.txt'

