from abc import ABC, abstractmethod
from dataclasses import dataclass
import time
import logging
from memory_profiler import profile

STREAM = open('memory_profiler.log','w')

@dataclass
class Result:
    name: str
    total_time: float = 0
    some_other_random_number: float = 0


class Benchmark(ABC):

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

    def __init__(self, config: Configuration):
        self._config = config
        self._logger = logging.getLogger(self._config.name)

        self.result = Result(self._config.name)

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

    @profile(stream=STREAM)
    def _measure_time_and_get_results(self, function, *args, **kwargs):
        start = time.process_time()
        result = function(*args, **kwargs)
        end = time.process_time()
        total = end - start
        self.result.total_time = total
        self.result.some_other_random_number = 0
        self._logger.info(f"{total} seconds for algorithm")
        return result

    def __repr__(self):
        return str(self._config)


class AlgorithmNotFound(Exception):
    pass