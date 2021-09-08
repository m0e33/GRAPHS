from pathlib import Path
from datetime import datetime

BASE_PATH = "benchmark/serialization/results/"


def get_com_path(config):
    graph = config.dataset_path.split("/")[1].split(".")[0]
    return graph + "/" + config.lib + "/" + config.algorithm


def write_com_to_file(communities, algorithm_specific_path):
    timestamp = datetime.now().strftime("%d-%b-%Y_%H-%M-%S")
    final_path = BASE_PATH + algorithm_specific_path
    Path(final_path).mkdir(parents=True, exist_ok=True)
    final_path = final_path + "/communities_" + timestamp + ".txt"
    with open(final_path, "w") as f:
        for community in communities:
            community_line = "\t".join([str(node_id) for node_id in community])
            f.write(community_line + "\n")


def read_com_from_file(path):
    communities = set()
    with open(path, "r") as f:
        for line in f:
            cmty = set([int(node_id) for node_id in line.split('\t')])
            communities.add(cmty)
    return communities
