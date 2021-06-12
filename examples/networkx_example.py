from networkx.algorithms import community
import networkx as nx
import matplotlib.pyplot as plt
import logging
import argparse

parser = argparse.ArgumentParser(description='Community-Detection on Barbell Graph')
parser.add_argument('--m1', type=int, help='m1')
parser.add_argument('--m2', type=int, help='m2')

args = parser.parse_args()
m1 = int(args.m1)
m2 = int(args.m2)

logging.basicConfig(level = logging.DEBUG)

if __name__=="__main__":
    logging.info(f"Creating Barbell Graph")
    G = nx.barbell_graph(m1, m2)

    logging.info(f"Run Community Detection")
    communities_generator = community.girvan_newman(G)
    top_level_communities = next(communities_generator)
    next_level_communities = next(communities_generator)

    logging.info(f"Draw Graph")
    nx.draw(G)

    logging.info(f"Save file")
    plt.savefig('sample_graph.png')

    com = sorted(map(sorted, next_level_communities))
    logging.info(f"Commnities: {str(com)}")