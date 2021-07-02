from benchmark.snap_benchmark import SnapBenchmark
from benchmark.benchmark_factory import create_benchmarks_from_config
import logging
import sys
from benchmark.benchmark_runner import BenchmarkRunner



logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.info("\n*************************************************\n"
         "*                                               *\n"
         "*             starting experiment               *\n"
         "*                                               *\n"
         "*************************************************\n")

    benchmarks = create_benchmarks_from_config('configuration.yml')
    runner = BenchmarkRunner(benchmarks)
    runner.run()
    runner.evaluate()
    runner.collect_results()
