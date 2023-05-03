import sys
from general import intercept_io_and_run


def main():
    binary_name = "mmg3d"
    args = sys.argv[1:]
    intercept_io_and_run(binary_name, args)
