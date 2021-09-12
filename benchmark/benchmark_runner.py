from dataclasses import asdict
from data.csv_writer import write_results
from datetime import datetime


class BenchmarkRunner:
    def __init__(self, benchmarks, decoupled_from_run: bool = False):
        self._benchmarks = benchmarks
        self.current_timestamp = datetime.now().strftime("%d-%b-%Y_%H:%M:%S")
        self._decoupled_from_run = decoupled_from_run

    def run(self):
        for benchmark in self._benchmarks:
            benchmark.run()

    def evaluate(self, execute_fitness: bool = True, execute_partition: bool = True):
        for benchmark in self._benchmarks:
            benchmark.result.evaluator.evaluate(execute_fitness, execute_partition)

    def collect_results(self, write_time: bool = True, write_fitness: bool = True, write_partition: bool = True):

        for benchmark in self._benchmarks:
            if write_time:
                write_results(
                    f"results_time/time_{self.current_timestamp}_{benchmark.result.name}.txt",
                    asdict(benchmark.result),
                    list(asdict(benchmark.result).keys()),
                )
            if write_fitness:
                write_results(
                    f"results_fitness/fitness_{self.current_timestamp}_{benchmark.result.name}.txt",
                    benchmark.result.evaluator.fitness_results,
                    list(benchmark.result.evaluator.fitness_results.keys()),
                )
            if write_partition:
                write_results(
                    f"results_partition/partition_{self.current_timestamp}_{benchmark.result.name}.txt",
                    benchmark.result.evaluator.partition_results,
                    list(benchmark.result.evaluator.partition_results.keys()),
                )
