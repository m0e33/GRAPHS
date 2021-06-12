from snap.snap import LoadEdgeList, TUNGraph, SaveEdgeList
import math

def intro():
    # save and load from a text file
    email_graph = LoadEdgeList(TUNGraph, "email-EU-core.txt", 0, 1)
    print("dblp-graph: Nodes %d, Edges %d" % (email_graph.GetNodes(), email_graph.GetEdges()))

    email_nodes = [node.GetId() for node in email_graph.Nodes()]

    print(email_graph.GetModularity(email_nodes))


    sub_dblp_graph = LoadEdgeList(TUNGraph, "0.05-com-dblp.ungraph.txt", 0, 1);
    modularity, CmtyV = sub_dblp_graph.CommunityCNM()
    for Cmty in CmtyV:
        print("Community: ")
        for NI in Cmty:
            print(NI)
    print("The modularity of the network is %f" % modularity)


if __name__ == '__main__':
    intro()