from benchmark.base_benchmark import Benchmark
from snap.snap import *
from benchmark.base_benchmark import AlgorithmNotFound


class SnapBenchmark(Benchmark):
    def __init__(self, config: Benchmark.Configuration):
        super().__init__(config)

    def _get_graph(self):
        self._logger.info(self._logger_prefix + f"Loading Graph from path: {self._config.dataset_path}")
        self._graph = LoadEdgeList(TUNGraph, self._config.dataset_path, 0, 1)

    def _run_algorithm(self):
        self._logger.info(self._logger_prefix + f"Trying to run {self._config.algorithm}")
        if(self._config.algorithm == "CNM"):
            modularity, CmtyV = self._graph.CommunityCNM()
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection: modularity: {modularity}")
        else:
            raise AlgorithmNotFound(self._config.lib)

