tmux new -ds networkx_lukes_partitioning 'conda activate snap-env; python basic_test.py configs-networkx/lukes_partitioning.yml True True; exec $SHELL'
sleep 3
tmux new -ds snap_cnm 'conda activate snap_env; python basic_test.py configs-snap/CNM.yml True True; exec $SHELL'
sleep 3
tmux new -ds snap_girvan_newman 'conda activate snap-env; python basic_test.py configs-snap/girvan_newman.yml True True; exec $SHELL'