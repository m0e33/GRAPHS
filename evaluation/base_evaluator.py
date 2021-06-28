from abc import ABC, abstractmethod
from enum import Enum
import logging
import sys


class ImportMode(Enum):
    CMTY_PER_LINE = "community_per_line"
    NODE_LABEL = "node_label"


def precision(a, b):
    return len(a.intersection(b)) / len(a)


def recall(a, b):
    return len(a.intersection(b)) / len(b)


def f1_score(b, a):
    return (2 * precision(b, a) * recall(b, a)) / (precision(b, a) + recall(b, a) + sys.float_info.epsilon)


def f1_score_sets(b, A):
    return max([f1_score(b, a) for a in A])



class BaseEvaluator(ABC):
    def __init__(self, graph, communities, config):
        self._graph = graph
        self._communities = communities
        self._config = config
        self._gt_cmtys = None
        self._cmty_sets = None
        self.import_gt()

        self._logger = logging.getLogger(type(self).__name__)
        self._logger_prefix = f"{self._config.lib}:{self._config.algorithm}:"

    def evaluate(self):
        self._logger.info(self._logger_prefix + "Evaluating Results")
        self._convert_cmtys_to_sets()
        purity = self.purity()
        avg_f1 = self.average_f1()
        self._logger.info(self._logger_prefix + f"Purity: {purity}, Avg F1: {avg_f1}")

    def import_gt(self, mode = ImportMode.CMTY_PER_LINE):
        gt_sets = []
        if mode == ImportMode.CMTY_PER_LINE:
            with open(self._config.gt_path, "r") as stream:
                for line in stream:
                    cmty = line.split("\t")
                    cmty[-1] = cmty[-1].replace("\n", "")
                    gt_sets.append(set(cmty))
        self._gt_cmtys = gt_sets

    def purity(self):
        self._logger.info(self._logger_prefix + "Computing purity")
        sum_intersect = 0
        for ac_cmty in self._cmty_sets:
            max_intersect = 0
            for gt_cmty in self._gt_cmtys:
               max_intersect = max(len(ac_cmty.intersection(gt_cmty)), max_intersect)
            sum_intersect += max_intersect
        return sum_intersect / self._get_number_of_nodes()

    def average_f1(self):
        self._logger.info(self._logger_prefix + "Computing Average f1 score")
        return sum([f1_score_sets(b, self._gt_cmtys) for b in self._cmty_sets])/len(self._cmty_sets) + sum([f1_score_sets(a, self._cmty_sets) for a in self._gt_cmtys])/len(self._gt_cmtys)

    @abstractmethod
    def _convert_cmtys_to_sets(self):
        pass

    @abstractmethod
    def _get_number_of_nodes(self):
        pass