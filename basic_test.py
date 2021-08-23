import distutils.util

from benchmark.benchmark_factory import create_benchmarks_from_config
import logging
from benchmark.benchmark_runner import BenchmarkRunner
import sys
import argparse


logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.info(
        "\n*************************************************\n"
        "*                                               *\n"
        "*             starting experiment               *\n"
        "*                                               *\n"
        "*************************************************\n"
    )

    parser = argparse.ArgumentParser()
    parser.add_argument('config', type=str, help='Execute partition evaluation')
    parser.add_argument('execute_fitness', type=bool, help='Execute fitness evaluation')
    parser.add_argument('execute_partition', type=bool, help='Execute partition evaluation')

    args = parser.parse_args()
    config = args.config
    execute_fitness = args.execute_fitness
    execute_partition = args.execute_partition

    configuration_files = [
        config,
    ]

    for configuration in configuration_files:
        logging.info("Starting to run '" + configuration + "'\n")
        benchmarks = create_benchmarks_from_config(configuration)
        for benchmark in benchmarks:
            runner = BenchmarkRunner([benchmark])
            try:
                runner.run()
            except Exception as e:
                logging.error("Failed to RUN '" + configuration + "': " + str(e))

            try:
                runner.evaluate(
                    execute_fitness=execute_fitness, execute_partition=execute_partition
                )
            except Exception as e:
                logging.error("Failed to EVALUATE '" + configuration + "': " + str(e))

            try:
                runner.collect_results()
            except Exception as e:
                logging.error(
                    "Failed to COLLECT_RESULTS for '" + configuration + "': " + str(e)
                )
            logging.info("Finished to run '" + configuration + "'\n")
