from benchmark.base_benchmark import Benchmark


class SnapBenchmark(Benchmark):
    def __init__(self, config: Benchmark.Configuration):
        super().__init__(config)

    def run(self):
        print(self._config)