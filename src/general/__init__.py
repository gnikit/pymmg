from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import meshio
from meshio._common import warn

__all__ = ["intercept_io_and_run"]

ACCEPTED_EXTENSIONS = [".mesh", ".meshb"]


def intercept_io_and_run(binary_name: str, args: list[str]):
    """Intercepts the arguments from the argument list and scans for
    the explicit input and output options `in` and `out`. If the
    input or output is not a .mesh or .mesh file, it will be
    convert to and from .mesh to the requested file format.


    Parameters
    ----------
    binary_name : str
        mmgs, mmg2d, mmg3d
    args : list[str]
        Argument list
    """
    fin_name = get_medit_filename("-in", args)
    fout_name = get_medit_filename("-out", args)
    has_help = "-h" in args or "--help" in args

    # If no output is given, then set the output to the default MMG output
    # i.e. fin_name.o.mesh but instead of MEDIT use the input file extension
    if fin_name and not fout_name and not has_help:
        fin_base, fin_ext = os.path.splitext(fin_name)
        fout_name = f"{fin_base}.o{fin_ext}"
        args.extend(["-out", fout_name])

    # Convert input mesh to .mesh
    if fin_name and not has_help:
        mesh = meshio.read(fin_name)
        fh, tmp_in_name = tempfile.mkstemp(suffix=".mesh")
        os.close(fh)
        meshio.write(tmp_in_name, mesh)
        args[args.index("-in") + 1] = tmp_in_name

    if fout_name and not has_help:
        fh, tmp_out_name = tempfile.mkstemp(suffix=".mesh")
        os.close(fh)
        args[args.index("-out") + 1] = tmp_out_name

    res = run_mmg(binary_name, args)

    if fout_name and not has_help:
        mesh = meshio.read(tmp_out_name)
        # Convert output mesh to requested format, guard against meshio failure
        try:
            meshio.write(fout_name, mesh)
        except meshio._exceptions.WriteError:
            warn(f"Unable to convert MEDIT file to {fout_name}")
            warn("Writing a .mesh file instead.")
            # Avoid conversion and just do a copy
            shutil.copyfile(tmp_out_name, f"{os.path.splitext(fout_name)[0]}.mesh")

        # Copy solution file from temporary location
        try:
            shutil.copyfile(
                f"{os.path.splitext(tmp_out_name)[0]}.sol",
                f"{os.path.splitext(fout_name)[0]}.sol",
            )
        # MMG can fail to change the output, in that case there won't be a
        # temporary solution file to copy
        except FileNotFoundError:
            pass

    # Cleanup
    if fin_name and not has_help:
        os.remove(tmp_in_name)
    if fout_name and not has_help:
        os.remove(tmp_out_name)
        os.remove(f"{os.path.splitext(tmp_out_name)[0]}.sol")

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


def run_mmg(binary: Path, args: list[str]):
    if platform.system() == "Windows":
        binary = binary.with_suffix(".exe")
    else:
        binary = binary.parent / (binary.name + "_O3")

    return subprocess.run([binary] + args)
