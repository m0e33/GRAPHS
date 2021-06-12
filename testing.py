from benchmark.snap_benchmark import SnapBenchmark
from benchmark.benchmark_factory import create_benchmarks_from_config

if __name__ == "__main__":
    benchmarks = create_benchmarks_from_config('configuration.yml')
    for bm in benchmarks:
        print(bm)