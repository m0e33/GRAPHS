tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-graphtool/minimize_blockmodel.yml False False; exec $SHELL'
sleep 3
tmux new -ds graphtool_minimize_blockmodel_mcmc_aneal 'conda activate snap-env; python basic_test.py configs-graphtool/mcmc_anneal.yml False False; exec $SHELL'
sleep 3
tmux new -ds graphtool_minimize_blockmodel_mcmc_sweep 'conda activate snap-env; python basic_test.py configs-graphtool/multiflip_mcmc_sweep.yml False False; exec $SHELL'
sleep 3
tmux new -ds networkx_asyn_lpa 'conda activate snap-env; python basic_test.py configs-networkx/asyn_lpa_communities.yml False False; exec $SHELL'
sleep 3
tmux new -ds networkx_async_fluid 'conda activate snap-env; python basic_test.py configs-networkx/async_fluid.yml False False; exec $SHELL'
sleep 3