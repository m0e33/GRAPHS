from cdlib import NodeClustering

from evaluation.base_evaluator import BaseEvaluator

from networkx.relabel import convert_node_labels_to_integers
from networkx.readwrite import read_edgelist

class GraphToolEvaluator(BaseEvaluator):
    def __init__(self, graph, communities, config):
        self._orig_graph = convert_node_labels_to_integers(read_edgelist(config.dataset_path))
        super(GraphToolEvaluator, self).__init__(graph, communities, config)

    def set_block_state(self, state):
        self._block_state = state

    def _convert_cmtys_to_node_clusterings(self):
        self._logger.info(self._logger_prefix + "Converting GraphTool Communities to CDLib NodeClusterings")
        membership = self._communities.get_blocks()
        cmty_dict = {}
        for node in self._graph.vertices():
            node = int(self._graph.vertex_properties['node_label'][node])
            cmty = membership[node]
            if cmty not in cmty_dict.keys():
                cmty_dict[cmty] = list()
            cmty_dict[cmty].append(node)
        self._communities = cmty_dict.values()
        self._ac_cmty_nc = NodeClustering(list(cmty_dict.values()), graph=self._orig_graph)

    def _get_number_of_nodes(self):
        return self._graph.get_vertices().shape[0]