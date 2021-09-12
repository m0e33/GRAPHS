from benchmark.base_benchmark import Benchmark
import graph_tool.all as gt
from networkx.readwrite.edgelist import read_edgelist
import numpy as np
import pyintergraph
from evaluation.graphtool_evaluator import GraphToolEvaluator
from benchmark.base_benchmark import AlgorithmNotFound

def multiflip_mcmc_sweep(state):
    for i in range(1):  # this should be sufficiently large
        state.multiflip_mcmc_sweep(beta=np.inf, niter=1)
    return state


def mcmc_anneal(state):
    gt.mcmc_anneal(state, beta_range=(1, 10), niter=1, mcmc_equilibrate_args=dict(force_niter=10)) # from documentation
    return state


class GraphToolBenchmark(Benchmark):
    def __init__(self, config: Benchmark.Configuration):
        super().__init__(config)

    def _extract_communities(self, state):
        # hacky and not very cost efficient way to extract communities in the way we want it.

        membership = state.get_blocks()
        cmty_dict = {}
        for node in self._graph.vertices():
            node = int(self._graph.vertex_properties['node_label'][node])
            cmty = membership[node]
            if cmty not in cmty_dict.keys():
                cmty_dict[cmty] = list()
            cmty_dict[cmty].append(node)
        return cmty_dict.values()

    def _get_graph(self):
        self._logger.info(self._logger_prefix + f"Loading Graph from path: {self._config.dataset_path}")
        self._graph = read_edgelist(self._config.dataset_path)
        self._adapt_graph_after_loading()
        # self._graph = nx2gt(nxgraph)
        self._graph = pyintergraph.nx2gt(self._graph, labelname="node_label")

        nodes, edges = self._graph.num_vertices(), self._graph.num_edges()
        self._logger.info(self._logger_prefix + f"Loaded Graph with {nodes} nodes and {edges} edges")

    def _run_algorithm(self):
        self._logger.info(self._logger_prefix + f"Running Algo for GraphTool")
        self._logger.info(self._logger_prefix + f"Trying to run {self._config.algorithm}")

        if self._config.algorithm == "minimze_blockmodel":
            state = self._measure_time_and_get_results(gt.minimize_blockmodel_dl, self._graph)
            self._communities = self._extract_communities(state)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")
            self.maybe_write_cmtys_to_file(self._communities)

        elif self._config.algorithm == "multiflip_mcmc_sweep":
            state = gt.minimize_blockmodel_dl(self._graph)
            updated_state = self._measure_time_and_get_results(multiflip_mcmc_sweep, state)
            self._communities = self._extract_communities(updated_state)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")
            self.maybe_write_cmtys_to_file(self._communities)

        elif self._config.algorithm == "mcmc_anneal":
            state = gt.minimize_blockmodel_dl(self._graph)
            updated_state = self._measure_time_and_get_results(mcmc_anneal, state)
            self._communities = self._extract_communities(updated_state)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")
            self.maybe_write_cmtys_to_file(self._communities)

        else:
            raise AlgorithmNotFound(self._config.lib)

        self.result.evaluator = self._get_evaluator(self._communities)

    def _get_evaluator(self, communities):
        return GraphToolEvaluator(self._graph, communities, self._config)
