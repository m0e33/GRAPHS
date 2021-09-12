"""Quality evaluation of benchmarks"""
import glob
from abc import ABC, abstractmethod
from dataclasses import dataclass
import time
import logging
from benchmark.serialization.serialization import write_com_to_file, get_com_folder_path, read_com_from_file

ISOLATED_NODES_EMAIL = [580, 633, 648, 653, 658, 660, 670, 675, 684, 691, 703, 711, 731, 732, 744, 746, 772, 798, 808]
STREAM = open('memory_profiler.log', 'w')


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

        write_cmtys_to_file: bool = True
        """Set to true, if you want the algorithms results to be serialized in a text file, standard: false"""

    def __init__(self, config: Configuration):
        self._config = config
        self._logger = logging.getLogger(self._config.name)
        self.result = BenchmarkResult(self._config.name)
        self._logger_prefix = f"{self._config.lib}:{self._config.algorithm}:"
        self._get_graph()

    def run(self,) -> None:
        self._run_algorithm()

    def create_evaluator_with_results_file(self):
        folder_path = get_com_folder_path(self._config)
        single_file = glob.glob(folder_path + "/communities_*.txt")[0]
        self._logger.info(self._logger_prefix + f"Using results file: {single_file}")

        self._communities = read_com_from_file(single_file)
        self.result.evaluator = self._get_evaluator(self._communities)

    @abstractmethod
    def _get_evaluator(self, communities):
        pass

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

    def maybe_write_cmtys_to_file(self, communities):
        if self._config.write_cmtys_to_file:
            write_com_to_file(communities, get_com_folder_path(self._config))

    def __repr__(self):
        return str(self._config)

    def _adapt_graph_after_loading(self):
        # networkx
        if 'email' in self._config.dataset_path:
            for node in ISOLATED_NODES_EMAIL:
                self._graph.add_node(node)


class AlgorithmNotFound(Exception):
    pass
