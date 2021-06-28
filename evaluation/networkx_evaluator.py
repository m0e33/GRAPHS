from evaluation.base_evaluator import BaseEvaluator


class NetworkxEvaluator(BaseEvaluator):
    def __init__(self, graph, communities, gt_path):
        super(NetworkxEvaluator, self).__init__(graph, communities, gt_path)

    def _evaluate(self):
        purity = self.purity()
        self._logger.info(self._logger_prefix + f"Purity: {purity}")



    def _convert_cmtys_to_sets(self):
        self._logger.info(self._logger_prefix + "Converting Networkx Communities to actual python sets")
        top_level_cmtys = next(self._communities)
        next_level_communities = next(self._communities)
        self._cmty_sets = [set(cmty) for cmty in list(next_level_communities)]

    def _get_number_of_nodes(self):
        return self._graph.number_of_nodes()