import distutils.util

from benchmark.benchmark_factory import create_benchmarks_from_config
import logging
from benchmark.benchmark_runner import BenchmarkRunner
import sys

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.info(
        "\n*************************************************\n"
        "*                                               *\n"
        "*             starting experiment               *\n"
        "*                                               *\n"
        "*************************************************\n"
    )

    config = str(sys.argv[1])
    configuration_files = [
        config,
    ]

    execute_fitness = bool(distutils.util.strtobool(sys.argv[2]))
    execute_partition = bool(distutils.util.strtobool(sys.argv[3]))

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
