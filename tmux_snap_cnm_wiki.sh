tmux new -ds snap_wiki_cnm 'source /hpi/fs00/share/complexnetSS2021/mosi/anaconda3/profile.d/conda.sh; conda init bash; conda activate snap-env; python3 main.py -config configs-snap/CNM_wiki.yml -mem_profiling; exec $SHELL'