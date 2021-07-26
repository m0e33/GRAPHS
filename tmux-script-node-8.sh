tmux new -ds graphtool_minimize_blockmodel 'conda activate snap-env; python basic_test.py configs-graphtool/minimize_blockmodel.yml True True; exec $SHELL'
sleep 3
tmux new -ds graphtool_minimize_blockmodel_mcmc_aneal 'conda activate snap-env; python basic_test.py configs-graphtool/mcmc_anneal.yml True True; exec $SHELL'
sleep 3
