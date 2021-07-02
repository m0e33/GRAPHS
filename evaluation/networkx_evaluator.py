from cdlib import NodeClustering

from evaluation.base_evaluator import BaseEvaluator
from tqdm import tqdm


class NetworkxEvaluator(BaseEvaluator):
    def __init__(self, graph, communities, gt_path):
        super(NetworkxEvaluator, self).__init__(graph, communities, gt_path)

    def _convert_cmtys_to_node_clusterings(self):
        self._logger.info(self._logger_prefix + "Converting Networkx Communities to CDLib node clusters")
        cmty_lists = []
        for cmty in tqdm(list(self._communities)):
            cmty_lists.append([int(id) for id in cmty])

        # For Debugging
        self._unique_values_ac_list = [x for l in cmty_lists for x in l]
        self._unique_values_ac_set = set(self._unique_values_ac_list)

        self._ac_cmty_nc = NodeClustering(cmty_lists, graph=self._orig_graph)

    def _get_number_of_nodes(self):
        return self._graph.number_of_nodes()