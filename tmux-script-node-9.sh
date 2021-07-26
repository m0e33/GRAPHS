tmux new -ds graphtool_minimize_blockmodel_mcmc_sweep 'conda activate snap-env; python basic_test.py configs-graphtool/multiflip_mcmc_sweep.yml True True; exec $SHELL'
sleep 3
tmux new -ds networkx_asyn_lpa 'conda activate snap-env; python basic_test.py configs-networkx/asyn_lpa_communities.yml True True; exec $SHELL'
sleep 3