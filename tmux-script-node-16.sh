tmux new -ds networkx_async_fluid 'conda activate snap-env; python basic_test.py configs-networkx/async_fluid.yml True True; exec $SHELL'
sleep 3
tmux new -ds networkx_greedy_modularity 'conda activate snap-env; python basic_test.py configs-networkx/greedy_modularity_communities.yml True True; exec $SHELL'
sleep 3