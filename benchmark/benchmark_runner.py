from dataclasses import asdict
from data.csv_writer import write_csv


class BenchmarkRunner:
    def __init__(self, benchmarks):
        self._benchmarks = benchmarks

    def run(self):
        for benchmark in self._benchmarks:
             benchmark.run()

    def evaluate(self):
        for benchmark in self._benchmarks:
            benchmark.result.evaluator.evaluate()

    def collect_results(self):
        write_csv("test.csv", [asdict(benchmark.result) for benchmark in self._benchmarks], list(asdict(self._benchmarks[0].result).keys()))
        write_csv("test2.csv", [asdict(benchmark.result.evaluator.result) for benchmark in self._benchmarks],
                  list(asdict(self._benchmarks[0].result.evaluator.result).keys()))