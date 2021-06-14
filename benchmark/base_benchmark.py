from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging


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

        self._logger_prefix = f"{self._config.lib}:{self._config.algorithm}:"

    def run(self) -> None:
        self._get_graph()
        self._run_algorithm()
        # self._collect_results()

    @abstractmethod
    def _get_graph(self):
        pass

    @abstractmethod
    def _run_algorithm(self):
        pass

    # @abstractmethod
    # def _collect_results(self):
    #     pass


    def __repr__(self):
        return str(self._config)


class AlgorithmNotFound(Exception):
    pass