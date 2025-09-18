import sys
from pathlib import Path

from pymmg.general import intercept_io_and_run


def main():
    """Entry point to mmg3d binary."""
    binary = Path(__file__).parent / "mmg3d"
    args = sys.argv[1:]
    intercept_io_and_run(binary, args)
