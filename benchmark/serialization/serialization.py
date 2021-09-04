BASE_PATH = "benchmark/serialization/results/"


def write_com_to_file(communities, algorithm_specific_path):
    with open(BASE_PATH + algorithm_specific_path, "w") as f:
        f.write(communities)


def read_com_from_file(library):
    pass