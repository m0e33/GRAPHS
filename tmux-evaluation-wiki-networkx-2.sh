tmux new -ds evaluation_wiki_networkx_k_clique 'conda activate snap-env; python basic_evaluation.py -config=configs-networkx/k_clique_wiki.yml; exec $SHELL'
tmux new -ds evaluation_wiki_networkx_label_propagation 'conda activate snap-env; python basic_evaluation.py -config=configs-networkx/label_propagation_communities_wiki.yml; exec $SHELL'
tmux new -ds evaluation_wiki_networkx_girvan_newman 'conda activate snap-env; python basic_evaluation.py -config=configs-networkx/girvan_newman_wiki.yml; exec $SHELL'
