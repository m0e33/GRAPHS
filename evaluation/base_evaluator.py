from abc import ABC, abstractmethod
from enum import Enum
from networkx.readwrite.edgelist import read_edgelist
import logging
from cdlib import NodeClustering
from cdlib.evaluation import adjusted_rand_index, f1, normalized_mutual_information


class ImportMode(Enum):
  CMTY_PER_LINE = "community_per_line"
  NODE_LABEL = "node_label"


class BaseEvaluator(ABC):
  def __init__(self, graph, communities, config):
    self._graph = graph
    self._communities = communities
    self._config = config
    self._gt_cmty_nc = None
    self._ac_cmty_nc = None

    # node clustering needs the base graph in a networkx or graph-tools format.
    # We go with graph tool here.
    self._orig_graph = read_edgelist(self._config.dataset_path)
    self.import_gt()

    self._logger = logging.getLogger(type(self).__name__)
    self._logger_prefix = f"{self._config.lib}:{self._config.algorithm}:"

  def evaluate(self):
    self._logger.info(self._logger_prefix + "Evaluating Results")
    self._convert_cmtys_to_node_clusterings()
    self._evaluate()

  def import_gt(self, mode=ImportMode.CMTY_PER_LINE):
    gt_sets = []
    if mode == ImportMode.CMTY_PER_LINE:
      with open(self._config.gt_path, "r") as stream:
        for line in stream:
          cmty = line.split("\t")
          cmty[-1] = cmty[-1].replace("\n", "")
          gt_sets.append(list(cmty))
    self._gt_cmty_nc = NodeClustering(gt_sets, graph=self._orig_graph)

  def purity(self):
    self._logger.info(self._logger_prefix + "Computing purity")
    sum_intersect = 0
    for ac_cmty in self._cmty_lists:
      max_intersect = 0
      for gt_cmty in self._gt_cmty_nc:
        max_intersect = max(len(ac_cmty.intersection(gt_cmty)), max_intersect)
      sum_intersect += max_intersect
    return sum_intersect / self._get_number_of_nodes()

  def rand_index(self):
    return adjusted_rand_index(self._ac_cmty_nc, self._gt_cmty_nc)

  def f1(self):
    return f1(self._ac_cmty_nc, self._gt_cmty_nc)

  def nmi(self):
    return normalized_mutual_information(self._ac_cmty_nc, self._gt_cmty_nc)

  @abstractmethod
  def _convert_cmtys_to_node_clusterings(self):
    pass

  @abstractmethod
  def _evaluate(self):
    pass

  @abstractmethod
  def _get_number_of_nodes(self):
    pass
