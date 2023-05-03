from __future__ import annotations

import os
import sys
import tempfile
import meshio
import subprocess
from pathlib import Path
import platform


__all__ = ["intercept_io_and_run"]

ACCEPTED_EXTENSIONS = [".mesh", ".meshb"]


def intercept_io_and_run(binary_name: str, args: list[str]):
    """Intercepts the arguments from the argument list and scans for
    the explicit input and output options `in` and `out`. If the
    input or output is not a .mesh or .meshb file, it will be
    convert to and from .meshb to the requested file format.


    Parameters
    ----------
    binary_name : str
        mmgs, mmg2d, mmg3d
    args : list[str]
        Argument list
    """
    input_mesh = get_medit_filename("-in", args)
    output_mesh = get_medit_filename("-out", args)

    # Convert input mesh to .meshb
    if input_mesh:
        mesh = meshio.read(input_mesh)
        fh, tmp_input_mesh = tempfile.mkstemp(suffix=".meshb")
        os.close(fh)
        meshio.write(tmp_input_mesh, mesh)
        args[args.index("-in") + 1] = tmp_input_mesh

    if output_mesh:
        fh, tmp_output_mesh = tempfile.mkstemp(suffix=".meshb")
        os.close(fh)
        args[args.index("-out") + 1] = tmp_output_mesh

    res = run_mmg(binary_name, args)

    if output_mesh:
        mesh = meshio.read(tmp_output_mesh)
        meshio.write(output_mesh, mesh)

    # Cleanup
    if input_mesh:
        os.remove(tmp_input_mesh)
    if output_mesh:
        os.remove(tmp_output_mesh)

    sys.exit(res.returncode)


def get_medit_filename(arg_type: str, args: list[str]):
    if arg_type not in args:
        return ""
    try:
        idx = args.index(arg_type) + 1
    except ValueError:
        raise ValueError(f"Option: {arg_type} must be followed by a filename.")
    filename = args[idx]

    # Conversion will be handled by MMG
    if filename.lower().endswith(tuple(ACCEPTED_EXTENSIONS)):
        return ""

    return filename


def run_mmg(binary_name: str, args: list[str]):
    binary = Path(__file__).parent / binary_name
    if platform.system() == "Windows":
        binary = binary.with_suffix(".exe")
    else:
        binary = binary.parent / (binary.name + "_O3")

    return subprocess.run([binary] + args)
