from benchmark.base_benchmark import Benchmark
from snap.snap import *
from benchmark.base_benchmark import AlgorithmNotFound
from evaluation.snap_evaluator import SnapEvaluator
from benchmark.base_benchmark import ISOLATED_NODES_EMAIL

class SnapBenchmark(Benchmark):
    def __init__(self, config: Benchmark.Configuration, load_graph: bool = True):
        super().__init__(config, load_graph)

    def _get_graph(self):
        self._logger.info(self._logger_prefix + f"Loading Graph from path: {self._config.dataset_path}")
        self._graph = LoadEdgeList(TUNGraph, self._config.dataset_path)
        self._adapt_graph_after_loading()
        nodes, edges = self._graph.GetNodes(), self._graph.GetEdges()
        self._logger.info(self._logger_prefix + f"Loaded Graph with {nodes} nodes and {edges} edges")

    def _run_algorithm(self):
        self._logger.info(self._logger_prefix + f"Trying to run {self._config.algorithm}")

        if(self._config.algorithm == "CNM"):
            result = self._measure_time_and_get_results(self._graph.CommunityCNM)
            modularity, com = result
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection: modularity: {modularity}")
            self._communities = com
            self.maybe_write_cmtys_to_file(self._communities)

        elif(self._config.algorithm == "CommunityGirvanNewman"):
            result = self._measure_time_and_get_results(self._graph.CommunityGirvanNewman)
            modularity, com = result
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection: modularity: {modularity}")
            self._communities = com
            self.maybe_write_cmtys_to_file(self._communities)

        else:
            raise AlgorithmNotFound(self._config.lib)

        self.result.evaluator = self._get_evaluator(com)

    def _get_evaluator(self, communities):
        return SnapEvaluator(self._graph, communities, self._config)

    def _adapt_graph_after_loading(self):
        # snap
        if 'email' in self._config.dataset_path:
            for node in ISOLATED_NODES_EMAIL:
                self._graph.AddNode(node)