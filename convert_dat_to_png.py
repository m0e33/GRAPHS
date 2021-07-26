import os
import subprocess
from pathlib import Path
import sys

if __name__=="__main__":
    path = Path(sys.argv[1])
    path_images = path.joinpath("images")
    if not path_images.is_dir():
        path_images.mkdir()
    for file in os.listdir(path):
        if ".dat" in file:
            file_path = path.joinpath(file)
            new_image_path = path_images.joinpath(file)
            if not new_image_path.is_file():
                print(f"{path_images.joinpath(file)}")

                command = ["mprof", "plot", "-f", file_path, "-o", f"{new_image_path}.png"]
                subprocess.call(command)
