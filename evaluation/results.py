import glob
from benchmark.benchmark_factory import create_benchmarks_from_config
import logging
from data.csv_writer import append_line

logging.basicConfig(level=logging.DEBUG)

configuration_files = [
    "configs-graphtool/minimize_blockmodel_email.yml",
    #"configs-snap/GN_wiki.yml",
]

result_partition_base_path = "../results_partition"
result_fitness_base_path = "../results_fitness"
result_time_base_path = "../results_time"
output_file_path = "../results_collection/results.csv"

sample_fitness_path = result_fitness_base_path + "/fitness_*.txt"
sample_partition_path = result_partition_base_path + "/partition_*.txt"


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

    possible_librarys = ["Networkx", "Graphtool", "Snap"]
    possible_graphs = ["email", "dblp", "wiki", "friendster"]

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
    benchmarks = create_benchmarks_from_config("../" + configuration, load_graph=False)
    for benchmark in benchmarks:
        benchmark_name = benchmark.result.name

        time_measurement_files = glob.glob(result_time_base_path + "/time*" + benchmark_name + ".txt")
        partition_measurement_files = glob.glob(result_partition_base_path + "/partition*" + benchmark_name + ".txt")
        fitness_measurement_files = glob.glob(result_fitness_base_path + "/fitness*" + benchmark_name + ".txt")

        if len(time_measurement_files) != 0 \
                and len(partition_measurement_files) != 0 \
                and len(fitness_measurement_files) != 0:

            latest_time_measurement = time_measurement_files[-1]
            latest_partition_measurement = partition_measurement_files[-1]
            latest_fitness_measurement = fitness_measurement_files[-1]

            benchmark_values_row = []
            network, library, algorithm = deconstruct_name(benchmark_name)
            benchmark_values_row.append(network)
            benchmark_values_row.append(library)
            benchmark_values_row.append(algorithm)

            with open(latest_time_measurement, "r") as f:
                first_line = f.readline()
                time_line = f.readline()
                time_value = time_line.split(" ")[2][:-1]
                benchmark_values_row.append(time_value)

            with open(glob.glob(latest_fitness_measurement)[0], "r") as f:
                for fitness_metric_line in f:
                    fitness_metric_value = fitness_metric_line.split(" ")[2][:-1]
                    benchmark_values_row.append(fitness_metric_value)

            with open(glob.glob(latest_partition_measurement)[0], "r") as f:
                for partition_metric_line in f:
                    partition_metric_value = partition_metric_line.split(" ")[2][:-1]
                    benchmark_values_row.append(partition_metric_value)

            append_line(output_file_path, benchmark_values_row)
        else:
            logging.info(f"No time or no fitness or no partition results found for benchmark '{benchmark_name}', "
                         f"aborting results collection")
            continue
