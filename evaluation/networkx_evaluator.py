from cdlib import NodeClustering

from evaluation.base_evaluator import BaseEvaluator
from tqdm import tqdm
from networkx.relabel import convert_node_labels_to_integers
from networkx.readwrite import read_edgelist


class NetworkxEvaluator(BaseEvaluator):
    def __init__(self, graph, communities, config):
        self._orig_graph = convert_node_labels_to_integers(read_edgelist(self._config.dataset_path))
        super(NetworkxEvaluator, self).__init__(graph, communities, config)

    def _convert_cmtys_to_node_clusterings(self):
        self._logger.info(self._logger_prefix + "Converting Networkx Communities to sets")
        cmty_lists = []
        for cmty in tqdm(list(self._communities)):
            cmty_lists.append([int(id) for id in cmty])

        self._logger.info(self._logger_prefix + "Converting Networkx Communities to CDLib node clusters")
        self._ac_cmty_nc = NodeClustering(cmty_lists, graph=self._orig_graph)

    def _get_number_of_nodes(self):
        return self._graph.number_of_nodes()