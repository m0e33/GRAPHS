tmux new -ds networkx_asyn_lpa_communities_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; python3 main.py -config configs-networkx/asyn_lpa_communities_wiki.yml -mem_profiling; exec $SHELL'
tmux new -ds networkx_async_fluid_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; python3 main.py -config configs-networkx/async_fluid_wiki.yml -mem_profiling; exec $SHELL'
tmux new -ds networkx_greedy_modularity_communities_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; python3 main.py -config configs-networkx/greedy_modularity_communities_wiki.yml -mem_profiling; exec $SHELL'
tmux new -ds networkx_k_clique_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; python3 main.py -config configs-networkx/k_clique_wiki.yml -mem_profiling; exec $SHELL'
tmux new -ds networkx_label_propagation_communities_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; python3 main.py -config configs-networkx/label_propagation_communities_wiki.yml -mem_profiling; exec $SHELL'
tmux new -ds networkx_girvan_newman_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; python3 main.py -config configs-networkx/girvan_newman_wiki.yml -mem_profiling; exec $SHELL'