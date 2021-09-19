# GRAPHS
See the report for full documenatation: 

## SET UP

1. `cd` into root directory
2. Create venv with `python3.9 -m venv .venv`
3. Activate venv with `source .venv/bin/activate`
4. Install dependencies with `pip3 install -r requirements.txt` (don't forget to upgrade pip)

## CREATE CONFIG

Create a config file (yaml), like the following example:

```
Snap_CNM_email:
  lib: "snap"
  dataset_path: "storage/email-Eu-core-manual-undirected-0-test.txt"
  algorithm: "CNM"
  gt_path: "storage/email-Eu-core-department-labels-0.txt"
  gt_is_overlapping: False
```

## RUN IT

1. `cd` into root
2. Run programm with `python3 main.py -config <config_path> [OPTIONAL -execute_partition] [OPTIONAL -execute_fitness]`

With the optional parameter -execute_partition, the result will autmatically be compared with the ground truth and several metrics will get computed. With the optional parameter -execute_fitness, the result will autmatically be analized (without ground truth) and several metrics will get computed. For the computation of the evaluation metrics we use the [CDLib Library](https://cdlib.readthedocs.io/en/latest/).
