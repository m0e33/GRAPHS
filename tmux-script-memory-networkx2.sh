#tmux new -ds graphtool_minimize_blockmodel_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda activate snap-env; mprof run --output graphtool_minimize_blockmodel_wiki.dat --include-children --multiprocess --python python3 basic_test.py configs-graphtool/minimize_blockmodel_wiki.yml True False; exec $SHELL'
# tmux new -ds graphtool_minimize_blockmodel_friendster 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda activate snap-env; mprof run --output graphtool_minimize_blockmodel_friendster.dat --include-children --multiprocess --python python3 basic_test.py configs-graphtool/minimize_blockmodel_friendster.yml True False; exec $SHELL'

#tmux new -ds graphtool_mcmc_anneal_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output graphtool_mcmc_anneal_wiki.dat --include-children --multiprocess --python python3 basic_test.py configs-graphtool/mcmc_anneal_wiki.yml True False; exec $SHELL'
#tmux new -ds graphtool_mcmc_anneal_friendster 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output graphtool_mcmc_anneal_wiki_friendster.dat --include-children --multiprocess --python python3 basic_test.py configs-graphtool/mcmc_anneal_friendster.yml True False; exec $SHELL'
#
#tmux new -ds graphtool_multiflip_mcmc_sweep_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output graphtool_multiflip_mcmc_sweep_wiki.dat --include-children --multiprocess --python python3 basic_test.py configs-graphtool/multiflip_mcmc_sweep_wiki.yml True False; exec $SHELL'
#tmux new -ds graphtool_multiflip_mcmc_sweep_friendster 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output graphtool_multiflip_mcmc_sweep_friendster.dat --include-children --multiprocess --python python3 basic_test.py configs-graphtool/multiflip_mcmc_sweep_friendster.yml True False; exec $SHELL'

# tmux new -ds networkx_asyn_lpa_communities_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output networkx_asyn_lpa_communities_wiki.dat --include-children --multiprocess --python python3 basic_test.py configs-networkx/asyn_lpa_communities_wiki.yml; exec $SHELL'
# tmux new -ds networkx_async_fluid_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output networkx_async_fluid_wiki.dat --include-children --multiprocess --python python3 basic_test.py configs-networkx/async_fluid_wiki.yml; exec $SHELL'
tmux new -ds networkx_greedy_modularity_communities_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output networkx_greedy_modularity_communities_wiki.dat --include-children --multiprocess --python python3 basic_test.py configs-networkx/greedy_modularity_communities_wiki.yml; exec $SHELL'
tmux new -ds networkx_girvan_newman 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output networkx_girvan_newman.dat --include-children --multiprocess --python python3 basic_test.py configs-networkx/girvan_newman.yml; exec $SHELL'

# tmux new -ds networkx_k_clique_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output networkx_k_clique.dat --include-children --multiprocess --python python3 basic_test.py configs-networkx/k_clique_wiki.yml; exec $SHELL'
# tmux new -ds networkx_label_propagation_communities_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output networkx_label_propagation_communities_wiki.dat --include-children --multiprocess --python python3 basic_test.py configs-networkx/label_propagation_communities_wiki.yml; exec $SHELL'
# tmux new -ds networkx_lukes_partitioning_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output networkx_lukes_partitioning_wiki.dat --include-children --multiprocess --python python3 basic_test.py configs-networkx/lukes_partitioning_wiki.yml; exec $SHELL'

# tmux new -ds snap_CNM 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output snap_CNM.dat --include-children --multiprocess --python python3 basic_test.py configs-snap/CNM.yml; exec $SHELL'
# tmux new -ds snap_girvan_newman 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; mprof run --output snap_girvan_newman.dat --include-children --multiprocess --python python3 basic_test.py configs-snap/girvan_newman.yml; exec $SHELL'