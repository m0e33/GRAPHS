from cdlib import NodeClustering

from evaluation.base_evaluator import BaseEvaluator
from networkx.readwrite import read_edgelist


class GraphToolEvaluator(BaseEvaluator):
    def __init__(self, graph, communities, config):
        self._orig_graph = read_edgelist(config.dataset_path, nodetype=int)
        super(GraphToolEvaluator, self).__init__(graph, communities, config)

    def set_block_state(self, state):
        self._block_state = state

    def _convert_cmtys_to_node_clusterings(self):
        self._logger.info(self._logger_prefix + "Converting GraphTool Communities to CDLib NodeClusterings")
        self._ac_cmty_nc = NodeClustering(list(self._communities), graph=self._orig_graph)

    def _get_number_of_nodes(self):
        return self._graph.get_vertices().shape[0]