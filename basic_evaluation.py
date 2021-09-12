
from benchmark.benchmark_factory import create_benchmarks_from_config
import logging
from benchmark.benchmark_runner import BenchmarkRunner
from datetime import datetime

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


    configuration_files = [
        "configs-graphtool/mcmc_anneal_email.yml"
    ]

    for configuration in configuration_files:
        logging.info("Starting to run '" + configuration + "'\n")
        benchmarks = create_benchmarks_from_config(configuration)
        for benchmark in benchmarks:
            runner = BenchmarkRunner([benchmark])
            benchmark.create_evaluator_with_results_file()
            logging.info("Evaluation using results from file")

            try:
                runner.evaluate(
                    execute_fitness=True, execute_partition=True, results_from_file=True
                )
            except Exception as e:
                logging.error("Failed to EVALUATE '" + configuration + "': " + str(e), exc_info=True)

            try:
                runner.collect_results(True, True)
            except Exception as e:
                logging.error(
                    "Failed to COLLECT_RESULTS for '" + configuration + "': " + str(e), exc_info=True
                )
            logging.info("Finished to run '" + configuration + "'\n")
