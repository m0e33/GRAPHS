import glob

from benchmark.benchmark_factory import create_benchmarks_from_config
import logging
import sys
from data.csv_writer import append_line

logging.basicConfig(level=logging.DEBUG)

configuration_files = [
    'configuration-email-core-graphtools.yml',
    'configuration-email-core-networkx.yml',
    'configuration-email-core-snap.yml',
    'configuration-dblp-networkx.yml',
    'configuration-dblp-graphtools.yml',
    'configuration-dblp-snap.yml',
    'configuration-wiki-topcats-networkx.yml',
    'configuration-wiki-topcats-graphtools.yml',
    'configuration-friendster-networkx.yml',
    'configuration-friendster-graphtools.yml',
]

results_base_path = sys.argv[1]
output_file_path = sys.argv[2]


sample_fitness_path = results_base_path + "/fitness_*.txt"
sample_partition_path = results_base_path + "/partition_*.txt"


def build_header_fields():
    fitness_metrics_count = 0
    partition_metrics_count = 0
    fields = ['Network', 'Library', 'Algorithm', 'Time']
    with open(glob.glob(sample_fitness_path)[0], 'r') as fitness_file:
        for line in fitness_file:
            label = line.split(" ")[0]
            fitness_metric_name = label.split("-")[-1]
            fields.append(fitness_metric_name)
            fitness_metrics_count += 1

    with open(glob.glob(sample_partition_path)[0], 'r') as fitness_file:
        for line in fitness_file:
            label = line.split(" ")[0]
            partition_metric_name = label.split("-")[-1]
            fields.append(partition_metric_name)
            partition_metrics_count += 1

    return fields, fitness_metrics_count, partition_metrics_count

def deconstruct_name(benchmark_name):
    bn_network = ''
    bn_library = ''

    possible_librarys = ["NetworkX", "Graphtool", "Snap"]
    possible_graphs = ["EmailCore"]

    for lib in possible_librarys:
        if lib in benchmark_name:
            bn_library = lib
            benchmark_name = benchmark_name.removeprefix(lib)

    for graph in possible_graphs:
        if graph in benchmark_name:
            bn_network = graph
            benchmark_name = benchmark_name.removesuffix(graph)

    return bn_network, bn_library, benchmark_name


header_fields, fm_count, pm_cunt = build_header_fields()

append_line(output_file_path, header_fields)

for configuration in configuration_files:
    logging.info("Results extraction started for '" + configuration + "'\n")
    benchmarks = create_benchmarks_from_config("../" + configuration)
    for benchmark in benchmarks:
        benchmark_name = benchmark.result.name

        for time_measurement_file in glob.glob(results_base_path + "/time*.txt"):
            if benchmark_name in time_measurement_file:
                benchmark_values_row = []
                network, library, algorythm = deconstruct_name(benchmark_name)
                benchmark_values_row.append(network)
                benchmark_values_row.append(library)
                benchmark_values_row.append(algorythm)
                corresponding_partition_file = results_base_path + "/partition_" + "_".join([split_part for split_part in time_measurement_file.split("_")[1:]])
                corresponding_fitness_file = results_base_path + "/fitness_" + "_".join([split_part for split_part in time_measurement_file.split("_")[1:]])

                with open(time_measurement_file, "r") as f:
                    first_line = f.readline()
                    time_line = f.readline()
                    time_value = time_line.split(" ")[2][:-1]
                    benchmark_values_row.append(time_value)

                if len(glob.glob(corresponding_fitness_file)) != 0:
                    with open(glob.glob(corresponding_fitness_file)[0], "r") as f:
                        for fitness_metric_line in f:
                            fitness_metric_value = fitness_metric_line.split(" ")[2]
                            benchmark_values_row.append(fitness_metric_value)
                else:
                    [benchmark_values_row.append(0) for _ in range(fm_count)]

                if len(glob.glob(corresponding_partition_file)) != 0:
                    with open(glob.glob(corresponding_partition_file)[0], "r") as f:
                        for partition_metric_line in f:
                            partition_metric_value = partition_metric_line.split(" ")[2]
                            benchmark_values_row.append(partition_metric_value)
                else:
                    [benchmark_values_row.append(0) for _ in range(pm_cunt)]

                append_line(output_file_path, benchmark_values_row)
    # load all time files with name in it
    # extract libraryname, algorithm name and network name from name
    # extract time from file
    # print that line in a csv

    # load all precision files with name in it
    # extract metric values
    # append values
