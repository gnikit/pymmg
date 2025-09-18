import sys
from pathlib import Path

from pymmg.general import intercept_io_and_run


def main():
    """Entry point to mmgs binary."""
    binary = Path(__file__).parent / "mmgs"
    args = sys.argv[1:]
    intercept_io_and_run(binary, args)
