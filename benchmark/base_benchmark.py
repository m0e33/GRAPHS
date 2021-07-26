"""Quality evaluation of benchmarks"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
import time
import logging
# from memory_profiler import profile
from evaluation.base_evaluator import BaseEvaluator


STREAM = open('memory_profiler.log','w')

@dataclass
class BenchmarkResult:
    """Benchmark Results"""
    name: str
    evaluator = None
    total_time: float = 0
    process_time: float = 0


class Benchmark(ABC):
    """Benchmarks"""
    @dataclass
    class Configuration:

        name: str
        """Used to identify benchmark"""

        lib: str
        """Underlying library or framework"""

        dataset_path: str
        """Path to dataset on which benchmark is to be performed"""

        algorithm: str
        """Community detection algorithm"""

        gt_path: str
        """Path to ground truth labels for communities"""

        gt_is_overlapping: bool
        """True if ground-truth communites are overlapping"""

    def __init__(self, config: Configuration):
        self._config = config
        self._logger = logging.getLogger(self._config.name)
        self.result = BenchmarkResult(self._config.name)
        self._logger_prefix = f"{self._config.lib}:{self._config.algorithm}:"

    def run(self) -> None:
        self._get_graph()
        self._run_algorithm()

    @abstractmethod
    def _get_graph(self):
        pass


    @abstractmethod
    def _run_algorithm(self):
        pass

    # @profile(stream=STREAM)
    def _measure_time_and_get_results(self, function, *args, **kwargs):
        start_process = time.process_time()
        start_normal = time.time()
        result = function(*args, **kwargs)
        end_process = time.process_time()
        end_normal = time.time()
        total_process = end_process - start_process
        total_normal = end_normal - start_normal
        self.result.total_time = total_normal
        self.result.process_time = total_process
        self._logger.info(f"{total_normal} seconds for algorithm")
        return result

    def __repr__(self):
        return str(self._config)



class AlgorithmNotFound(Exception):
    pass
