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
        write_csv("time.csv", [asdict(benchmark.result) for benchmark in self._benchmarks], list(asdict(self._benchmarks[0].result).keys()))
        write_csv("fitness.csv", [benchmark.result.evaluator.fitness_results for benchmark in self._benchmarks],
                  list(self._benchmarks[0].result.evaluator.fitness_results.keys()))
        write_csv("partition.csv", [benchmark.result.evaluator.partition_results for benchmark in self._benchmarks],
                  list(self._benchmarks[0].result.evaluator.partition_results.keys()))