tmux new -ds evaluation_dblp_networkx_k_clique 'conda activate snap-env; python basic_evaluation.py -config=configs-networkx/k_clique_dblp.yml; exec $SHELL'
tmux new -ds evaluation_dblp_networkx_label_propagation 'conda activate snap-env; python basic_evaluation.py -config=configs-networkx/label_propagation_communities_dblp.yml; exec $SHELL'
tmux new -ds evaluation_dblp_networkx_girvan_newman 'conda activate snap-env; python basic_evaluation.py -config=configs-networkx/girvan_newman_dblp.yml; exec $SHELL'
