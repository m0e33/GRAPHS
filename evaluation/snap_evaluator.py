from cdlib import NodeClustering
from networkx.relabel import convert_node_labels_to_integers
from networkx.readwrite import read_edgelist
from evaluation.base_evaluator import BaseEvaluator


class SnapEvaluator(BaseEvaluator):
    def __init__(self, graph, communities, config):
        self._orig_graph = read_edgelist(config.dataset_path, nodetype=int)
        super(SnapEvaluator, self).__init__(graph, communities, config)

    def purity(self):
        self._logger.info(self._logger_prefix + "Computing purity")
        sum_intersect = 0
        for ac_cmty in self._cmty_sets:
            max_intersect = 0
            for gt_cmty in self._gt_cmty_nc:
               max_intersect = max(len(ac_cmty.intersection(gt_cmty)), max_intersect)
            sum_intersect += max_intersect
        return sum_intersect / self._get_number_of_nodes()

    def _convert_cmtys_to_node_clusterings(self):
        self._logger.info(self._logger_prefix + "Converting Snap Communities to actual python sets")
        self._ac_cmty_nc = NodeClustering([list(cmty) for cmty in self._communities], graph=self._orig_graph)

    def _get_number_of_nodes(self):
        return self._graph.GetNodes()