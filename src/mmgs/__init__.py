import sys
from pathlib import Path

from general import intercept_io_and_run


def main():
    binary = Path(__file__).parent / "mmgs"
    args = sys.argv[1:]
    intercept_io_and_run(binary, args)
