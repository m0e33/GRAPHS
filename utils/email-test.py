from networkx import read_edgelist


if __name__ == "__main__":
    # relabel node in graph
    # networkx_graph = read_edgelist('../storage/email-Eu-core-undirected-0.txt')
    #
    # for consec_node_id in range(networkx_graph.number_of_nodes()):
    #     if str(consec_node_id) not in networkx_graph.nodes:
    #         print(str(consec_node_id) + " not covered")

    old_path = '../storage/email-Eu-core.txt'
    edges = []
    edges_sets = []
    with open(old_path, 'r') as f:
        for line in f:
            edge = [int(node_id) for node_id in line.split(" ")]
            if set(edge) not in edges_sets and edge[0] != edge[1]:
                edges.append(edge)
                edges_sets.append(set(edge))
            else:
                print("found dublicated edge" + str(edge))

    new_path = '../storage/email-Eu-core-manual-undirected-0-test.txt'


    with open(new_path, 'w') as f:
        for edge in edges:
            edge_string = " ".join([str(node_id) for node_id in edge])
            edge_string += "\n"
            f.write(edge_string)
