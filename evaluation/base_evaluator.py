from abc import ABC, abstractmethod
from enum import Enum
from networkx.readwrite.edgelist import read_edgelist
import logging
from dataclasses import dataclass
from cdlib import NodeClustering
import pyintergraph
from cdlib.evaluation import *


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

    partition_methods = [getattr(self, function) for function in dir(self)
                      if function.startswith("partition_") and callable(getattr(self, function))]

    fitness_methods = [getattr(self, function) for function in dir(self)
                      if function.startswith("fitness_") and callable(getattr(self, function))]

    def try_method(method):
      self._logger.info(self._logger_prefix + f"Trying to run {method.__name__}")
      try:
        return method().score
      except Exception as e:
        self._logger.info(self._logger_prefix + f"Fitness Function failed: {method.__name__} with error: {e}")
        return None

    self.fitness_results = {fitness_method.__name__ : try_method(fitness_method) for fitness_method in fitness_methods}
    self.partition_results = {partition_method.__name__: try_method(partition_method) for partition_method in partition_methods}



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
  +                            METRICS PARTITION                            +
  +                                                                         +
  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  """

  def partition_adjusted_rand_index(self):
    return adjusted_rand_index(self._gt_cmty_nc, self._ac_cmty_nc)

  def partition_f1(self):
    return f1(self._ac_cmty_nc, self._gt_cmty_nc)

  def partition_normalized_mutual_information(self):
    return normalized_mutual_information(self._ac_cmty_nc, self._gt_cmty_nc)

  def partition_nf1(self):
    return nf1(self._ac_cmty_nc, self._gt_cmty_nc)

  def partition_adjustet_normalized_mutual_information(self):
    return adjusted_mutual_information(self._ac_cmty_nc, self._gt_cmty_nc)

  def partition_omega(self):
    return omega(self._ac_cmty_nc, self._gt_cmty_nc)

  def partition_overlapping_normalized_mutual_information_LFK(self):
    return overlapping_normalized_mutual_information_LFK(self._ac_cmty_nc, self._gt_cmty_nc)

  def partition_overlapping_normalized_mutual_information_MGH(self):
    return overlapping_normalized_mutual_information_MGH(self._ac_cmty_nc, self._gt_cmty_nc)

  def partition_variation_of_information(self):
    return variation_of_information(self._ac_cmty_nc, self._gt_cmty_nc)

  """
  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  +                                                                         +
  +                                FITNESS                                  +
  +                                                                         +
  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  """

  def fitness_avg_distance(self):
    return avg_distance(self._orig_graph, self._ac_cmty_nc)

  def fitness_avg_embeddedness(self):
    return avg_embeddedness(self._orig_graph, self._ac_cmty_nc)

  def fitness_average_internal_degree(self):
      return average_internal_degree(self._orig_graph, self._ac_cmty_nc)

  def fitness_avg_transitivity(self):
    return avg_transitivity(self._orig_graph, self._ac_cmty_nc)

  def fitness_conductance(self):
    return conductance(self._orig_graph, self._ac_cmty_nc)

  def fitness_cut_ratio(self):
    return cut_ratio(self._orig_graph, self._ac_cmty_nc)

  def fitness_edges_inside(self):
    return edges_inside(self._orig_graph, self._ac_cmty_nc)

  def fitness_expansion(self):
    return expansion(self._orig_graph, self._ac_cmty_nc)

  def fitness_fraction_over_median_degree(self):
    return fraction_over_median_degree(self._orig_graph, self._ac_cmty_nc)

  def fitness_hub_dominance(self):
    return hub_dominance(self._orig_graph, self._ac_cmty_nc)

  def fitness_internale_edge_density(self):
    return internal_edge_density(self._orig_graph, self._ac_cmty_nc)

  def fitness_normalized_cut(self):
    return normalized_cut(self._orig_graph, self._ac_cmty_nc)

  def fitness_max_odf(self):
    return max_odf(self._orig_graph, self._ac_cmty_nc)

  def fitness_avg_odf(self):
    return avg_odf(self._orig_graph, self._ac_cmty_nc)

  def fitness_flake_odf(self):
    return flake_odf(self._orig_graph, self._ac_cmty_nc)

  def fitness_scale_density(self):
    return scaled_density(self._orig_graph, self._ac_cmty_nc)

  def fitness_significance(self):
    return significance(self._orig_graph, self._ac_cmty_nc)

  def fitness_size(self):
    return size(self._orig_graph, self._ac_cmty_nc)

  def fitness_surprise(self):
    return surprise(self._orig_graph, self._ac_cmty_nc)

  def fitness_triangle_participation_ratio(self):
    return triangle_participation_ratio(self._orig_graph, self._ac_cmty_nc)

  def fitness_purity(self):
    return purity(self._ac_cmty_nc)