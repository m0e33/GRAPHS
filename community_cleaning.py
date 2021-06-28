from snap.snap import LoadEdgeList, TUNGraph, SaveEdgeList
from networkx.readwrite.edgelist import read_edgelist
import math



if __name__ == "__main__":
  orig_gt_path = "storage/com-dblp.all.cmty.txt"
  new_gt_path = "storage/sub-com-dblp.all.cmty.txt"
  orig_graph_path = "storage/com-dblp.ungraph.txt"
  new_graph_path = "storage/sub-com-dblp.ungraph.txt"

  # graph subsampling
  dblp_graph = LoadEdgeList(TUNGraph, orig_graph_path, 0, 1)
  print("dblp-graph: Nodes %d, Edges %d" % (dblp_graph.GetNodes(), dblp_graph.GetEdges()))

  dblp_nodes = [node.GetId() for node in dblp_graph.Nodes()]

  sub_dblp_graph = dblp_graph.GetRndSubGraph(math.ceil(dblp_graph.GetNodes() * 0.05))
  sub_dblp_nodes = [node.GetId() for node in sub_dblp_graph.Nodes()]

  print("sub-dblp-graph: Nodes %d, Edges %d" % (sub_dblp_graph.GetNodes(), sub_dblp_graph.GetEdges()))
  SaveEdgeList(sub_dblp_graph, new_graph_path)



  # community subsampling
  netwokx_graph = read_edgelist(new_graph_path)

  new_nodes = netwokx_graph.nodes
  print("reread networkx nodes: ", len(new_nodes))
  old_community_nodes = set()
  new_community_nodes = set()
  gt_sets = []
  with open(orig_gt_path, "r") as old_file:
    with open(new_gt_path, "w") as   new_file:
      for line in old_file:
        cmty = line.split("\t")
        cmty[-1] = cmty[-1].replace("\n", "")
        cmty = set(cmty)
        old_community_nodes |= cmty
        intersection = cmty & new_nodes
        if len(intersection) != 0 & len(intersection) != 1:
          new_line = "\t".join([str(node_id) for node_id in intersection])
          new_line += "\n"
          new_file.write(new_line)
          
          # union
          new_community_nodes |= intersection

      # some algorithms for quality assessment have to get the same set of nodes in both actual and gt communities
      # because of that we have to include all nodes even if its nodes with no community in a single node community
      left_over_new_nodes = new_nodes - new_community_nodes
      for node in left_over_new_nodes:
        new_line = str(node) + "\n"
        new_file.write(new_line)

  # analysis

  old_networkx_graph = read_edgelist(orig_graph_path)
  print(new_community_nodes & new_nodes)
  print(old_community_nodes & old_networkx_graph.nodes)
  print("hello debugger")