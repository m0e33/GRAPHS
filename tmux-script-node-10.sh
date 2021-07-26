tmux new -ds networkx_k_clique 'conda activate snap-env; python basic_test.py configs-networkx/k_clique.yml True True; exec $SHELL'
sleep 3
tmux new -ds networkx_label_propagation 'conda activate snap-env; python basic_test.py configs-networkx/label_propagation_communities.yml True True; exec $SHELL'
sleep 3