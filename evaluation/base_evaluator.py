from abc import ABC, abstractmethod
from enum import Enum
import logging
import glob

from cdlib import NodeClustering
from cdlib.evaluation import *
from collections import Counter
from tabulate import tabulate
from benchmark.serialization.serialization import read_com_from_file, get_com_path

class ImportMode(Enum):
    CMTY_PER_LINE = "community_per_line"
    NODE_LABEL = "node_label"


class BaseEvaluator(ABC):
    def __init__(self, graph, communities, config):
        self._graph = graph
        self._communities = communities
        self._gt_communites = None
        self._config = config
        self._gt_cmty_nc = None
        self._ac_cmty_nc = None
        self.result = None

        self.import_gt()

        self._logger = logging.getLogger(type(self).__name__)
        self._logger_prefix = f"{self._config.lib}:{self._config.algorithm}:"

    def _adapt_communities_for_gt(self, result, gt):
        if "dblp" in self._config.dataset_path:
            result_set = set([node for com in result for node in com])
            gt_set = set([node for com in gt for node in com])

            intersection = result_set ^ gt_set

            for node in intersection:
                for com in result:
                    if node in com:
                        com.remove(node)

        return result

    def _analyze_communities(self, communities, log_string = ""):
        self._logger.info(self._logger_prefix + f"Number of communities: {len(communities)}")

        lens = list(map(lambda com: len(com), communities))
        values = list(Counter(lens).keys())
        counts = list(Counter(lens).values())
        self._logger.info(self._logger_prefix + f"Node distribution over communities ({log_string})")
        self._logger.info(f"\n{tabulate([[value, count] for value, count in zip(values, counts)], headers=['Node Count in Com', 'Com Count'])}")

    def _compare_node_sets(self, com1, com2):
        com1_set = set([node for com in com1 for node in com])
        com2_set = set([node for com in com2 for node in com])

        self._logger.info(self._logger_prefix + f"Len com1: {len(com1_set)}")
        self._logger.info(self._logger_prefix + f"Len com2: {len(com2_set)}")

        self._logger.info(self._logger_prefix + f"Smallest node in com1: {min(com1_set)}")
        self._logger.info(self._logger_prefix + f"Smallest node in com2: {min(com2_set)}")

        self._logger.info(self._logger_prefix + f"Biggest node in com1: {max(com1_set)}")
        self._logger.info(self._logger_prefix + f"Biggest node in com2: {max(com2_set)}")

        self._logger.info(self._logger_prefix + f"Nodes not in Intersection: {com1_set ^ com2_set}")

    def evaluate(self, execute_fitness, execute_partition):
        self._logger.info(self._logger_prefix + "Evaluating Results")
        self._logger.info(self._logger_prefix + "Fitness execution flag: " + str(execute_fitness))
        self._logger.info(self._logger_prefix + "Partition execution flag: " + str(execute_partition))

        if not execute_fitness and not execute_partition:
            return

        self._communities = self._adapt_communities_for_gt(self._communities, self._gt_communites)
        self._convert_cmtys_to_node_clusterings()

        self._analyze_communities(self._communities, "RESULT")
        self._analyze_communities(self._gt_communites, "GROUND TRUTH")

        self._compare_node_sets(self._communities, self._gt_communites)

        def try_method(method):
            self._logger.info(self._logger_prefix + f"Trying to run {method.__name__}")
            try:
                return method().score
            except Exception as e:
                self._logger.error(self._logger_prefix + f"Fitness Function failed: {method.__name__} with error: {e}", exec_info=True)
                return None

        if execute_fitness:
            fitness_methods = [getattr(self, function) for function in dir(self)
                               if function.startswith("fitness_") and callable(getattr(self, function))]
            self.fitness_results = {f"{self._logger_prefix}-{fitness_method.__name__}": try_method(fitness_method) for
                                    fitness_method in fitness_methods}

        if execute_partition:
            partition_methods = [getattr(self, function) for function in dir(self)
                                if function.startswith("partition_") and callable(getattr(self, function))]
            self.partition_results = {f"{self._logger_prefix}--{partition_method.__name__}": try_method(partition_method)
                                  for partition_method in partition_methods}

    def import_gt(self, mode=ImportMode.CMTY_PER_LINE):
        gt_lists = []
        if mode == ImportMode.CMTY_PER_LINE:
            with open(self._config.gt_path, "r") as stream:
                for line in stream:
                    cmty = line.split("\t")
                    cmty[-1] = cmty[-1].replace("\n", "")
                    gt_lists.append([int(id) for id in cmty])

        self._gt_communites = gt_lists

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
