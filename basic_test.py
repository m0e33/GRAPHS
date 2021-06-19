from benchmark.snap_benchmark import SnapBenchmark
from benchmark.benchmark_factory import create_benchmarks_from_config
import logging
import sys



logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    print("*************************************************\n"
         "*                                               *\n"
         "*             starting experiment               *\n"
         "*                                               *\n"
         "*************************************************\n")

    benchmarks = create_benchmarks_from_config('configuration.yml')
    for bm in benchmarks:
        bm.run()