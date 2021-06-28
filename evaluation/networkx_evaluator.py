from cdlib import NodeClustering

from evaluation.base_evaluator import BaseEvaluator
from tqdm import tqdm


class NetworkxEvaluator(BaseEvaluator):
    def __init__(self, graph, communities, gt_path):
        super(NetworkxEvaluator, self).__init__(graph, communities, gt_path)

    def _evaluate(self):
        # purity = self.purity()
        #rand_index = self.rand_index()
        f1 = self.f1()
        nmi = self.nmi()
        # self._logger.info(self._logger_prefix + f"Purity: {purity}")
        # self._logger.info(self._logger_prefix + f"Rand index: {rand_index}")
        self._logger.info(self._logger_prefix + f"f1-score: {f1}")
        self._logger.info(self._logger_prefix + f"normalized information: {nmi}")

    def _convert_cmtys_to_node_clusterings(self):
        self._logger.info(self._logger_prefix + "Converting Networkx Communities to CDLib node clusters")
        top_level_cmtys = next(self._communities)
        next_level_communities = next(self._communities)
        cmty_lists = []
        for cmty in tqdm(list(next_level_communities)):
            cmty_lists.append(list(cmty))

        self._ac_cmty_nc = NodeClustering(cmty_lists, graph=self._orig_graph)

    def _get_number_of_nodes(self):
        return self._graph.number_of_nodes()