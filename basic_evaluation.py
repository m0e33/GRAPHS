
from benchmark.benchmark_factory import create_benchmarks_from_config
import logging
from benchmark.benchmark_runner import BenchmarkRunner
from datetime import datetime
import os.path

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
        "configs-graphtool/minimize_blockmodel_email.yml",
        "configs-graphtool/mcmc_anneal_email.yml",
        "configs-graphtool/multiflip_mcmc_sweep_email.yml",
        "configs-networkx/asyn_lpa_communities_email.yml",
        "configs-networkx/async_fluid_email.yml",
        "configs-networkx/greedy_modularity_communities_email.yml",
        "configs-networkx/k_clique_email.yml",
        "configs-networkx/label_propagation_communities_email.yml",
        "configs-networkx/girvan_newman_email.yml",
        "configs-snap/CNM_email.yml",
        "configs-snap/GN_email.yml",
        "configs-graphtool/minimize_blockmodel_dblp.yml",
        "configs-graphtool/mcmc_anneal_dblp.yml",
        "configs-graphtool/multiflip_mcmc_sweep_dblp.yml",
        "configs-networkx/asyn_lpa_communities_dblp.yml",
        "configs-networkx/async_fluid_dblp.yml",
        "configs-networkx/greedy_modularity_communities_dblp.yml",
        "configs-networkx/k_clique_dblp.yml",
        "configs-networkx/label_propagation_communities_dblp.yml",
        "configs-networkx/girvan_newman_dblp.yml",
        "configs-snap/CNM_dblp.yml",
        "configs-snap/GN_dblp.yml",
        "configs-graphtool/minimize_blockmodel_wiki.yml",
        "configs-graphtool/mcmc_anneal_wiki.yml",
        "configs-graphtool/multiflip_mcmc_sweep_wiki.yml",
        "configs-networkx/asyn_lpa_communities_wiki.yml",
        "configs-networkx/async_fluid_wiki.yml",
        "configs-networkx/greedy_modularity_communities_wiki.yml",
        "configs-networkx/k_clique_wiki.yml",
        "configs-networkx/label_propagation_communities_wiki.yml",
        "configs-snap/CNM_wiki.yml",
        "configs-snap/GN_wiki.yml",
    ]

    for configuration in configuration_files:
        if not os.path.isfile(configuration):
            print(f"No configuration found with name '{configuration}'")

    for configuration in configuration_files:
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

        else:
            print(f"No configuration found with name '{configuration}'")