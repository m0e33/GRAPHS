tmux new -ds evaluation_wiki_graphtool_minimize_blockmodel 'conda activate snap-env; python basic_evaluation.py -config=configs-graphtool/minimize_blockmodel_wiki.yml; exec $SHELL'
tmux new -ds evaluation_wiki_graphtool_mcmc_anneal 'conda activate snap-env; python basic_evaluation.py -config=configs-graphtool/mcmc_anneal_wiki.yml; exec $SHELL'
tmux new -ds evaluation_wiki_graphtool_multiflip_mcmc_sweep 'conda activate snap-env; python basic_evaluation.py -config=configs-graphtool/multiflip_mcmc_sweep_wiki.yml; exec $SHELL'
