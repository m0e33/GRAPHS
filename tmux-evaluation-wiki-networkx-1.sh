tmux new -ds evaluation_wiki_networkx_async_lpa_communities 'conda activate snap-env; python basic_evaluation.py -config=configs-networkx/asyn_lpa_communities_wiki.yml; exec $SHELL'
tmux new -ds evaluation_wiki_networkx_async_fluid 'conda activate snap-env; python basic_evaluation.py -config=configs-networkx/async_fluid_wiki.yml; exec $SHELL'
tmux new -ds evaluation_wiki_networkx_greedy_modularity 'conda activate snap-env; python basic_evaluation.py -config=configs-networkx/greedy_modularity_communities_wiki.yml; exec $SHELL'
