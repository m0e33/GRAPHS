from dataclasses import asdict
from data.csv_writer import write_results
from datetime import datetime


class BenchmarkRunner:
    def __init__(self, benchmarks):
        self._benchmarks = benchmarks
        self.current_timestamp = datetime.now().strftime("%d-%b-%Y_%H:%M:%S")

    def run(self):
        for benchmark in self._benchmarks:
            benchmark.run()

    def evaluate(self):
        for benchmark in self._benchmarks:
            benchmark.result.evaluator.evaluate()

    def collect_results(self):
        for benchmark in self._benchmarks:
            write_results(
                f"time_{self.current_timestamp}_{benchmark.result.name}.txt",
                asdict(benchmark.result),
                list(asdict(benchmark.result).keys()),
            )
            write_results(
                f"fitness_{self.current_timestamp}_{benchmark.result.name}.txt",
                benchmark.result.evaluator.fitness_results,
                list(benchmark.result.evaluator.fitness_results.keys()),
            )
            write_results(
                f"partition_{self.current_timestamp}_{benchmark.result.name}.txt",
                benchmark.result.evaluator.partition_results,
                list(benchmark.result.evaluator.partition_results.keys()),
            )
