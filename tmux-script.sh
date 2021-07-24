tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-graphtool/minimize_blockmodel.yml; exec $SHELL'
tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-graphtool/mcmc_anneal.yml; exec $SHELL'
tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-graphtool/multiflip_mcmc_sweep.yml; exec $SHELL'

tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-networkx/asyn_lpa_communities.yml; exec $SHELL'
tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-networkx/async_fluid.yml; exec $SHELL'
tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-networkx/girvan_newman.yml; exec $SHELL'
tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-networkx/greedy_modularity_communities.yml; exec $SHELL'
tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-networkx/label_propagation_communities copy.yml; exec $SHELL'
tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-networkx/label_propagation_communities.yml; exec $SHELL'
tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-networkx/lukes_partitioning.yml; exec $SHELL'

tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-snap/CNM.yml; exec $SHELL'
tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-snap/girvan_newman.yml; exec $SHELL'