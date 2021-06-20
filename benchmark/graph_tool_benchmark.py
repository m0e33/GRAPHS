from benchmark.base_benchmark import Benchmark
import graph_tool.all as gt
from networkx.readwrite.edgelist import read_edgelist
from networkx.convert import to_edgelist
from data.utils import nx2gt
import numpy as np
from benchmark.base_benchmark import AlgorithmNotFound

class GraphToolBenchmark(Benchmark):
    def __init__(self, config: Benchmark.Configuration):
        super().__init__(config)

    def _get_graph(self):
        self._logger.info(self._logger_prefix + f"Loading Graph from path: {self._config.dataset_path}")
        nxgraph = read_edgelist(self._config.dataset_path)
        self._graph = nx2gt(nxgraph)
        nodes, edges = self._graph.num_vertices(), self._graph.num_edges()
        self._logger.info(self._logger_prefix + f"Loaded Graph with {nodes} nodes and {edges} edges")


    def _run_algorithm(self):
        self._logger.info(self._logger_prefix + f"Running Algo for GraphTool")
        self._logger.info(self._logger_prefix + f"Trying to run {self._config.algorithm}")

        if (self._config.algorithm == "minimze_blockmodel"):
            communities = self._measure_time_and_get_results(gt.minimize_blockmodel_dl, self._graph)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")

        if (self._config.algorithm == "multiflip_mcmc_sweep"):
            state = gt.BlockState(self._graph)
            for i in range(1):  # this should be sufficiently large
                state.multiflip_mcmc_sweep(beta=np.inf, niter=10)
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")

        if (self._config.algorithm == "mcmc_anneal"):
            state = gt.BlockState(self._graph)
            self._measure_time_and_get_results(gt.mcmc_anneal, state, beta_range=(1, 10), niter=10, mcmc_equilibrate_args=dict(force_niter=10))
            self._logger.info(self._logger_prefix + f"Succesfully ran community detection.")

        else:
            raise AlgorithmNotFound(self._config.lib)