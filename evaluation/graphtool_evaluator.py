from evaluation.base_evaluator import BaseEvaluator


class GraphToolEvaluator(BaseEvaluator):
    def __init__(self, graph, communities, gt_path):
        super(GraphToolEvaluator, self).__init__(graph, communities, gt_path)


    def set_block_state(self, state):
        self._block_state = state

    def _convert_cmtys_to_sets(self):
        self._logger.info(self._logger_prefix + "Converting Graphtool Communities to actual python sets")
        membership = self._communities.get_blocks()
        cmty_dict = {}
        for node in range(self._get_number_of_nodes()):
            cmty = membership[node]
            if cmty not in cmty_dict.keys():
                cmty_dict[cmty] = set()
            cmty_dict[cmty].add(node)
        self._cmty_sets = list(cmty_dict.values())

    def _get_number_of_nodes(self):
        return self._graph.get_vertices().shape[0]