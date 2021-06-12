from abc import ABC, abstractmethod
from dataclasses import dataclass


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

    @abstractmethod
    def run(self) -> None:
        pass

    def __repr__(self):
        return str(self._config)
