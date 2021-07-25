tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-graphtool/minimize_blockmodel.yml; exec $SHELL'
sleep 3
tmux new -ds graphtool_minimize_blockmodel-mcmc-aneal 'conda activate snap-env; python basic_test.py configs-graphtool/mcmc_anneal.yml; exec $SHELL'
sleep 3
tmux new -ds graphtool_minimize_blockmodel-mcmc-sweep'conda activate snap-env; python basic_test.py configs-graphtool/multiflip_mcmc_sweep.yml; exec $SHELL'
sleep 3
tmux new -ds networkx-asyn-lpa 'conda activate snap-env; python basic_test.py configs-networkx/asyn_lpa_communities.yml; exec $SHELL'
sleep 3
tmux new -ds networkx-async-fluid 'conda activate snap-env; python basic_test.py configs-networkx/async_fluid.yml; exec $SHELL'
sleep 3
tmux new -ds networkx-greedy-modularity 'conda activate snap-env; python basic_test.py configs-networkx/greedy_modularity_communities.yml; exec $SHELL'
sleep 3
tmux new -ds networkx-k-clique 'conda activate snap-env; python basic_test.py configs-networkx/k_clique.yml; exec $SHELL'
sleep 3
tmux new -ds networkx-label-propagation 'conda activate snap-env; python basic_test.py configs-networkx/label_propagation_communities.yml; exec $SHELL'
sleep 3
tmux new -ds networkx-lukes-partitioning 'conda activate snap-env; python basic_test.py configs-networkx/lukes_partitioning.yml; exec $SHELL'
sleep 3
tmux new -ds snap-cnm 'conda activate snap-env; python basic_test.py configs-snap/CNM.yml; exec $SHELL'
sleep 3
tmux new -ds snap-girvan-newman 'conda activate snap-env; python basic_test.py configs-snap/girvan_newman.yml; exec $SHELL'