from snap.snap import *
from networkx.readwrite.edgelist import write_edgelist
import networkx as nx
from networkx import read_edgelist


if __name__=="__main__":
  # # relabel node in graph
  networkx_ungraph = read_edgelist('../final_storage/wiki-topcats.undirected.txt')
  networkx_relabled = nx.relabel.convert_node_labels_to_integers(networkx_ungraph, first_label=1)
  # # networkx_ungraph_relabeled = nx.relabel_nodes(networkx_ungraph, {'0': str(1006)})
  #
  write_edgelist(networkx_relabled, "../final_storage/wiki-topcats.undirected.txt", data=False, delimiter=" ")
  #
  # breakpoint()
  #
  # with open("../storage_new/email-Eu-core-relabled-undirected.txt", "w") as f:
  #   for edge in networkx_ungraph.edges():
  #     edge_string = " ".join([str(int(node)) for node in edge]) + "\n"
  #     f.write(edge_string)
  # count = 0
  # with open("../storage_new/wiki-topcats.relabled.txt", "r") as f:
  #   with open("../final_storage/wiki-topcats.undirected.txt", "w") as write_file:
  #     for idx, line in enumerate(f.readlines()):
  #       edge = [int(node_id) for node_id in line.split(' ')]
  #       if edge[0] == edge[1]:
  #         print(idx)
  #         count += 1
  #         print(f"--{count}")
  #         new_edge_string = f"{edge[0]} {edge[0]}\n"
  #         continue
  #       else:
  #         write_file.write(line)
#
# # relabel node in
# with open('storage/email-Eu-core-department-labels.txt', 'r') as cmtys_old:
#   with open('storage/email-EU-core-department-labels-1005.txt', 'w') as cmtys_new:
#     for cmty in cmtys_old:
#       cmty_set = set([int(node_id) for node_id in cmty.split('\t')])
#       if 1006 in cmty_set:
#         cmty_set.remove(1006)
#         cmty_set.add(1005)
#
#         new_cmty_line = "\t".join([str(node_id) for node_id in cmty_set])
#         cmtys_new.write(new_cmty_line + "\n")
#       else:
#         cmtys_new.write(cmty)
#
# undirected_graph_path = 'storage/email-Eu-core-undirected.txt'
#
# # relabel node in communities
#
# #with open('storage/com-dblp.all.cmty-old.txt', 'r') as cmtys_old:
#   #with open('storage/com-dblp.all.cmty.txt', 'w') as cmtys_new:
#     #for cmty in cmtys_old:
#
#       #cmty_set = set([int(node_id) for node_id in cmty.split('\t')])
#       #if 0 in cmty_set:
#         #cmty_set.remove(0)
#         #cmty_set.add(nodes)
#
#         #new_cmty_line = "\t".join([str(node_id) for node_id in cmty_set])
#         #cmtys_new.write(new_cmty_line + "\n")
#       #else:
#         #cmtys_new.write(cmty)
#
#     #undirected_graph_path = 'storage/email-Eu-core-undirected.txt'

