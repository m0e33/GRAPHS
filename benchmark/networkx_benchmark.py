from benchmark.base_benchmark import Benchmark


class NetworkxBenchmark(Benchmark):
    def __init__(self, config: Benchmark.Configuration):
        super().__init__(config)

    def _get_graph(self):
        self._logger.info(self._logger_prefix + f"Loading Graph from path: {self._config.dataset_path}")

    def _run_algorithm(self):
        self._logger.info(self._logger_prefix + f"Running Algo for Networkx")