import sys
from pathlib import Path

from general import intercept_io_and_run


def main():
    binary = Path(__file__).parent / "mmg2d"
    args = sys.argv[1:]
    intercept_io_and_run(binary, args)
