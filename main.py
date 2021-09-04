import argparse
import subprocess
from datetime import datetime

parser = argparse.ArgumentParser(description='Run benchmark framework')
parser.add_argument('-config', type=str, help='path to config')
parser.add_argument('-execute_fitness', action='store_true', help='Run fitness evaluation')
parser.add_argument('-execute_partition', action='store_true', help='Run partition evaluation')
parser.add_argument('-mem_profiling', action='store_true', help='Run memory profiling wth memprof')

args = parser.parse_args()
config_path = args.config
execute_fitness = args.execute_fitness
execute_partition = args.execute_partition
mem_profiling = args.mem_profiling

if mem_profiling:
    current_time = datetime.now().strftime("%d-%b-%Y_%H:%M:%S")
    output_name = f"{current_time}--{config_path.split('/')[-1]}"
    subprocess.run(["mprof", "run", "--include-children", "--multiprocess", "--output", f"./mem_logs/{output_name}", "--python", "python3", "basic_test.py", str(config_path), str(execute_fitness), str(execute_partition)])
else:
    subprocess.run(
        ["python3", "basic_test.py", config_path, str(execute_fitness), str(execute_partition)])