from abc import ABC, abstractmethod
from enum import Enum
from networkx.readwrite.edgelist import read_edgelist
import logging
from dataclasses import dataclass
from cdlib import NodeClustering
import pyintergraph
from cdlib.evaluation import adjusted_rand_index, f1, normalized_mutual_information


class ImportMode(Enum):
  CMTY_PER_LINE = "community_per_line"
  NODE_LABEL = "node_label"

@dataclass
class EvaluatorResult:
  rand_index: float
  f1: float
  nmi: float


class BaseEvaluator(ABC):
  def __init__(self, graph, communities, config):
    self._graph = graph
    self._communities = communities
    self._config = config
    self._gt_cmty_nc = None
    self._ac_cmty_nc = None
    self.result = None

    # node clustering needs the base graph in a networkx or graph-tools format.
    # We go with graph tool here.
    self._orig_graph = read_edgelist(self._config.dataset_path)
    self.import_gt()

    self._logger = logging.getLogger(type(self).__name__)
    self._logger_prefix = f"{self._config.lib}:{self._config.algorithm}:"

  def evaluate(self):
    self._logger.info(self._logger_prefix + "Evaluating Results")
    self._convert_cmtys_to_node_clusterings()
    f1 = self.f1()
    nmi = self.nmi() if not self._config.gt_is_overlapping else None
    rand_index = self.rand_index() if not self._config.gt_is_overlapping else None

    self.result = EvaluatorResult(f1=f1, nmi=nmi, rand_index=rand_index)

  def import_gt(self, mode=ImportMode.CMTY_PER_LINE):
    gt_lists = []
    if mode == ImportMode.CMTY_PER_LINE:
      with open(self._config.gt_path, "r") as stream:
        for line in stream:
          cmty = line.split("\t")
          cmty[-1] = cmty[-1].replace("\n", "")
          gt_lists.append([int(id) for id in cmty])

    # For Debugging
    self._unique_values_gt_list = [x for l in gt_lists for x in l]
    self._unique_values_gt_set = set(self._unique_values_gt_list)

    self._gt_cmty_nc = NodeClustering(gt_lists, graph=self._orig_graph)

  @abstractmethod
  def _convert_cmtys_to_node_clusterings(self):
    pass

  """
  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  +                                                                         +
  +                                  METRICS                                +
  +                                                                         +
  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  """

  def rand_index(self):
    return adjusted_rand_index(self._gt_cmty_nc, self._ac_cmty_nc)

  def f1(self):
    return f1(self._ac_cmty_nc, self._gt_cmty_nc)

  def nmi(self):
    return normalized_mutual_information(self._ac_cmty_nc, self._gt_cmty_nc)


