from pathlib import Path

BASE_PATH = "benchmark/serialization/results/"


def write_com_to_file(communities, algorithm_specific_path):
    final_path = BASE_PATH + algorithm_specific_path
    Path(final_path).mkdir(parents=True, exist_ok=True)
    with open(final_path + "/communities.txt", "w") as f:
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
