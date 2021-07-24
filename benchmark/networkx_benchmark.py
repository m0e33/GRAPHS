from benchmark.base_benchmark import Benchmark
from networkx.readwrite.edgelist import read_edgelist
from networkx.algorithms import community
from benchmark.base_benchmark import AlgorithmNotFound
from evaluation.networkx_evaluator import NetworkxEvaluator

def girvan_newman(graph):
    communities = community.girvan_newman(graph)
    return next(communities) # measure just first iteration

class NetworkxBenchmark(Benchmark):
    def __init__(self, config: Benchmark.Configuration):
        super().__init__(config)
        self._k = 10
        self._max_weight = 100

    def _get_graph(self):
        self._logger.info(self._logger_prefix + f"Loading Graph from path: {self._config.dataset_path}")
        self._graph = read_edgelist(self._config.dataset_path)
        nodes, edges = self._graph.number_of_nodes(), self._graph.number_of_edges()
        self._logger.info(self._logger_prefix + f"Loaded Graph with {nodes} nodes and {edges} edges")

    def _run_algorithm(self):
        self._logger.info(self._logger_prefix + f"Running Algo for Networkx")
        self._logger.info(self._logger_prefix + f"Trying to run {self._config.algorithm}")

        if (self._config.algorithm == "girvan_newman"):
            self._communities = self._measure_time_and_get_results(girvan_newman, self._graph)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")

        elif (self._config.algorithm == "async_fluid"):
            self._communities = self._measure_time_and_get_results(community.asyn_fluidc, self._graph, self._k)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")

        elif (self._config.algorithm == "asyn_lpa_communities"):
            self._communities = self._measure_time_and_get_results(community.asyn_lpa_communities, self._graph)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")

        elif (self._config.algorithm == "asyn_lpa_communities"):
            self._communities = self._measure_time_and_get_results(community.asyn_lpa_communities, self._graph)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")

        elif (self._config.algorithm == "label_propagation_communities"):
            self._communities = self._measure_time_and_get_results(community.label_propagation_communities, self._graph)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")

        elif (self._config.algorithm == "lukes_partitioning"):
            self._communities = self._measure_time_and_get_results(community.lukes_partitioning, self._graph, self._max_weight)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")

        elif (self._config.algorithm == "greedy_modularity_communities"):
            self._communities = self._measure_time_and_get_results(community.greedy_modularity_communities, self._graph)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")

        elif (self._config.algorithm == "k_clique_communities"):
            self._communities = self._measure_time_and_get_results(community.k_clique_communities, self._graph, self._k)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")

        else:
            raise AlgorithmNotFound(self._config.lib)

        self.result.evaluator = NetworkxEvaluator(self._graph, self._communities, self._config)
