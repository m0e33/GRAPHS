import argparse
import subprocess
from datetime import datetime

parser = argparse.ArgumentParser(description='Run benchmark framework')
parser.add_argument('-config', type=str, help='path to config')
parser.add_argument('-execute_fitness', type=bool, help='Run fitness evaluation')
parser.add_argument('-execute_partition', type=bool, help='Run partition evaluation')
parser.add_argument('-mem_profiling', type=bool, help='Run memory profiling wth memprof')

args = parser.parse_args()
config_path = args.config
execute_fitness = args.execute_fitness
execute_partition = args.execute_partition
mem_profiling = args.mem_profiling

if mem_profiling:
    current_time = datetime.now().strftime("%d-%b-%Y_%H:%M:%S")
    output_name = f"{config_path.split('/')[-1]}--{current_time}"
    subprocess.run(["mprof", "run", "--include-children", "--multiprocess", "--output", f"./mem_logs/{output_name}", "--python", "python3", "basic_test.py", str(config_path), str(execute_fitness), str(execute_partition)])
else:
    subprocess.run(
        ["python3", "basic_test.py", config_path, str(execute_fitness), str(execute_partition)])