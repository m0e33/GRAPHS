from enum import Enum
from typing import List
from benchmark.base_benchmark import Benchmark
from benchmark.snap_benchmark import SnapBenchmark
from benchmark.networkx_benchmark import NetworkxBenchmark
from benchmark.graph_tool_benchmark import GraphToolBenchmark
import yaml


class LibNotSupported(Exception):
    pass

class BenchmarkType(Enum):
    SNAP = 'snap'
    NETWORKX = 'networkx'
    GRAPHTOOL = 'graphtool'


def create_benchmarks_from_config(path: str, load_graph: bool = True) -> List[Benchmark]:
    with open(path, 'r') as stream:
        configurations = yaml.safe_load(stream)

    benchmarks: List[Benchmark] = []
    for name, config in configurations.items():
        lib = BenchmarkType(config['lib'])
        cfg = Benchmark.Configuration(name, **config)
        if lib == BenchmarkType.SNAP:
            benchmarks.append(SnapBenchmark(cfg, load_graph))
        elif lib == BenchmarkType.NETWORKX:
            benchmarks.append(NetworkxBenchmark(cfg, load_graph))
        elif lib == BenchmarkType.GRAPHTOOL:
            benchmarks.append(GraphToolBenchmark(cfg, load_graph))
        else:
            raise LibNotSupported(lib)

    return benchmarks
