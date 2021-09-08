from benchmark.base_benchmark import Benchmark
from snap.snap import *
from benchmark.base_benchmark import AlgorithmNotFound
from evaluation.snap_evaluator import SnapEvaluator


class SnapBenchmark(Benchmark):
    def __init__(self, config: Benchmark.Configuration):
        super().__init__(config)

    def _get_graph(self):
        self._logger.info(self._logger_prefix + f"Loading Graph from path: {self._config.dataset_path}")
        self._graph = LoadEdgeList(TUNGraph, self._config.dataset_path, 0, 1)
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

        # write com to file.

        self.result.evaluator = SnapEvaluator(self._graph, com, self._config)


