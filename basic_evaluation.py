import argparse

from benchmark.benchmark_factory import create_benchmarks_from_config
import logging
from benchmark.benchmark_runner import BenchmarkRunner
from datetime import datetime
import os.path

parser = argparse.ArgumentParser(description='Run benchmark framework')
parser.add_argument('-config', type=str, help='path to config')

args = parser.parse_args()
configuration = args.config

timestamp = datetime.now().strftime("%d-%b-%Y_%H:%M:%S")
logging.basicConfig(level=logging.DEBUG)
rootLogger = logging.getLogger()
fileHandler = logging.FileHandler(f"logs/{timestamp}.log")
rootLogger.addHandler(fileHandler)

if __name__ == "__main__":
    logging.info(
        "\n*************************************************\n"
        "*                                               *\n"
        "*             starting evaluation               *\n"
        "*                                               *\n"
        "*************************************************\n"
    )

    if not os.path.isfile(configuration):
        print(f"No configuration found with name '{configuration}'")
        exit(1)

    logging.info("Starting to run '" + configuration + "'\n")
    if os.path.isfile(configuration):
        benchmarks = create_benchmarks_from_config(configuration)
        for benchmark in benchmarks:
            runner = BenchmarkRunner([benchmark])
            try:
                benchmark.create_evaluator_with_results_file()
                try:
                    runner.evaluate(
                        execute_fitness=True, execute_partition=True
                    )
                except Exception as e:
                    logging.error("Failed to EVALUATE '" + configuration + "': " + str(e), exc_info=True)

                try:
                    runner.collect_results(write_time=False, write_fitness=True, write_partition=True)
                except Exception as e:
                    logging.error(
                        "Failed to COLLECT_RESULTS for '" + configuration + "': " + str(e), exc_info=True
                    )
                logging.info("Finished to run '" + configuration + "'\n")
            except Exception as e:
                logging.error(
                    f"Failed to load evaluator / evaluate entirely: {str(e)}"
                )
