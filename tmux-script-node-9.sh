tmux new -ds networkx_greedy_modularity 'conda activate snap-env; python basic_test.py configs-networkx/greedy_modularity_communities.yml False False; exec $SHELL'
sleep 3
tmux new -ds networkx_k_clique 'conda activate snap-env; python basic_test.py configs-networkx/k_clique.yml False False; exec $SHELL'
sleep 3
tmux new -ds networkx_label_propagation 'conda activate snap-env; python basic_test.py configs-networkx/label_propagation_communities.yml False False; exec $SHELL'
sleep 3
tmux new -ds networkx_lukes_partitioning 'conda activate snap-env; python basic_test.py configs-networkx/lukes_partitioning.yml False False; exec $SHELL'
sleep 3
tmux new -ds snap_cnm 'conda activate snap_env; python basic_test.py configs-snap/CNM.yml False False; exec $SHELL'
sleep 3
tmux new -ds snap_girvan_newman 'conda activate snap-env; python basic_test.py configs-snap/girvan_newman_email.yml False False; exec $SHELL'