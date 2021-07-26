import os
import sys
path = str(sys.argv[1])

for file in os.listdir(path):
    if ".dat" in file:
        command = ["mprof", "plot", "-f", file, "-o", f"{file}.png"]