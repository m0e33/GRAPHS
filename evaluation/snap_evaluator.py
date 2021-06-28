from evaluation.base_evaluator import BaseEvaluator


class SnapEvaluator(BaseEvaluator):
    def __init__(self, graph, communities, gt_path):
        super(SnapEvaluator, self).__init__(graph, communities, gt_path)

    def _evaluate(self):
        purity = self.purity()
        self._logger.info(self._logger_prefix + f"Purity: {purity}")

    def purity(self):
        self._logger.info(self._logger_prefix + "Computing purity")
        sum_intersect = 0
        for ac_cmty in self._cmty_sets:
            max_intersect = 0
            for gt_cmty in self._gt_cmtys:
               max_intersect = max(len(ac_cmty.intersection(gt_cmty)), max_intersect)
            sum_intersect += max_intersect
        return sum_intersect / self._get_number_of_nodes()


    def _convert_cmtys_to_sets(self):
        self._logger.info(self._logger_prefix + "Converting Snap Communities to actual python sets")
        self._cmty_sets = [set(cmty) for cmty in self._communities]

    def _get_number_of_nodes(self):
        return self._graph.GetNodes()