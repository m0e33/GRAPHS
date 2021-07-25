tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-graphtool/minimize_blockmodel.yml; exec $SHELL'
sleep 3
tmux new -ds graphtool_minimize_blockmodel_mcmc_aneal 'conda activate snap-env; python basic_test.py configs-graphtool/mcmc_anneal.yml; exec $SHELL'
sleep 3
tmux new -ds graphtool_minimize_blockmodel_mcmc_sweep 'conda activate snap-env; python basic_test.py configs-graphtool/multiflip_mcmc_sweep.yml; exec $SHELL'
sleep 3
tmux new -ds networkx_asyn_lpa 'conda activate snap-env; python basic_test.py configs-networkx/asyn_lpa_communities.yml; exec $SHELL'
sleep 3
tmux new -ds networkx_async_fluid 'conda activate snap-env; python basic_test.py configs-networkx/async_fluid.yml; exec $SHELL'
sleep 3
tmux new -ds networkx_greedy_modularity 'conda activate snap-env; python basic_test.py configs-networkx/greedy_modularity_communities.yml; exec $SHELL'
sleep 3
tmux new -ds networkx_k_clique 'conda activate snap-env; python basic_test.py configs-networkx/k_clique.yml; exec $SHELL'
sleep 3
tmux new -ds networkx_label_propagation 'conda activate snap-env; python basic_test.py configs-networkx/label_propagation_communities.yml; exec $SHELL'
sleep 3
tmux new -ds networkx_lukes_partitioning 'conda activate snap-env; python basic_test.py configs-networkx/lukes_partitioning.yml; exec $SHELL'
sleep 3
tmux new -ds snap_cnm 'conda activate snap_env; python basic_test.py configs-snap/CNM.yml; exec $SHELL'
sleep 3
tmux new -ds snap_girvan_newman 'conda activate snap-env; python basic_test.py configs-snap/girvan_newman.yml; exec $SHELL'