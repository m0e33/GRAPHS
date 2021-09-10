tmux new -ds graphtool_minimize_blockmodel_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda activate snap-env; python3 main.py configs-graphtool/minimize_blockmodel_wiki.yml -mem_profiling; exec $SHELL'
tmux new -ds graphtool_mcmc_anneal_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; python3 main.py configs-graphtool/mcmc_anneal_wiki.yml -mem_profiling; exec $SHELL'
tmux new -ds graphtool_multiflip_mcmc_sweep_wiki 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; python3 main.py configs-graphtool/multiflip_mcmc_sweep_wiki.yml -mem_profiling; exec $SHELL'