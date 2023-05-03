import platform
import subprocess
import sys
from pathlib import Path


def main():
    binary = Path(__file__).parent / "mmg3d"
    if platform.system() == "Windows":
        binary = binary.with_suffix(".exe")
    else:
        binary = binary.parent / (binary.name + "_O3")

    res = subprocess.run([binary] + sys.argv[1:])
    sys.exit(res.returncode)
