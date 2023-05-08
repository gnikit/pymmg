# pymmg - Surface and volume remeshers

[![Build](https://github.com/gnikit/pymmg/actions/workflows/main.yml/badge.svg)](https://github.com/gnikit/pymmg/actions/workflows/main.yml)

Bringing [MMG](https://www.mmgtools.org/) surface and volume remeshers to Python.
This package is a wrapper around the MMG tools

## Features

- Surface remeshing
- Volume remeshing
- Area remeshing
- Adaptive mesh refinement
- Load multiple file formats using [`meshio`](https://github.com/nschloe/meshio)
  > [Abaqus](http://abaqus.software.polimi.it/v6.14/index.html) (`.inp`),
  > ANSYS msh (`.msh`),
  > [AVS-UCD](https://lanl.github.io/LaGriT/pages/docs/read_avs.html) (`.avs`),
  > [CGNS](https://cgns.github.io/) (`.cgns`),
  > [DOLFIN XML](https://manpages.ubuntu.com/manpages/jammy/en/man1/dolfin-convert.1.html) (`.xml`),
  > [Exodus](https://nschloe.github.io/meshio/exodus.pdf) (`.e`, `.exo`),
  > [FLAC3D](https://www.itascacg.com/software/flac3d) (`.f3grid`),
  > [H5M](https://www.mcs.anl.gov/~fathom/moab-docs/h5mmain.html) (`.h5m`),
  > [Kratos/MDPA](https://github.com/KratosMultiphysics/Kratos/wiki/Input-data) (`.mdpa`),
  > [Medit](https://people.sc.fsu.edu/~jburkardt/data/medit/medit.html) (`.mesh`, `.meshb`),
  > [MED/Salome](https://docs.salome-platform.org/latest/dev/MEDCoupling/developer/med-file.html) (`.med`),
  > [Nastran](https://help.autodesk.com/view/NSTRN/2019/ENU/?guid=GUID-42B54ACB-FBE3-47CA-B8FE-475E7AD91A00) (bulk data, `.bdf`, `.fem`, `.nas`),
  > [Netgen](https://github.com/ngsolve/netgen) (`.vol`, `.vol.gz`),
  > [Neuroglancer precomputed format](https://github.com/google/neuroglancer/tree/master/src/neuroglancer/datasource/precomputed#mesh-representation-of-segmented-object-surfaces),
  > [Gmsh](https://gmsh.info/doc/texinfo/gmsh.html#File-formats) (format versions 2.2, 4.0, and 4.1, `.msh`),
  > [OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file) (`.obj`),
  > [OFF](https://segeval.cs.princeton.edu/public/off_format.html) (`.off`),
  > [PERMAS](https://www.intes.de) (`.post`, `.post.gz`, `.dato`, `.dato.gz`),
  > [PLY](<https://en.wikipedia.org/wiki/PLY_(file_format)>) (`.ply`),
  > [STL](<https://en.wikipedia.org/wiki/STL_(file_format)>) (`.stl`),
  > [Tecplot .dat](http://paulbourke.net/dataformats/tp/),
  > [TetGen .node/.ele](https://wias-berlin.de/software/tetgen/fformats.html),
  > [SVG](https://www.w3.org/TR/SVG/) (2D output only) (`.svg`),
  > [SU2](https://su2code.github.io/docs_v7/Mesh-File/) (`.su2`),
  > [UGRID](https://www.simcenter.msstate.edu/software/documentation/ug_io/3d_grid_file_type_ugrid.html) (`.ugrid`),
  > [VTK](https://vtk.org/wp-content/uploads/2015/04/file-formats.pdf) (`.vtk`),
  > [VTU](https://vtk.org/Wiki/VTK_XML_Formats) (`.vtu`),
  > [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) ([TIN](https://en.wikipedia.org/wiki/Triangulated_irregular_network)) (`.wkt`),
  > [XDMF](https://xdmf.org/index.php/XDMF_Model_and_Format) (`.xdmf`, `.xmf`).

## Installation

```bash
pip install pymmg
```

> NOTE: you can the full-blown `pymmg` converter with `netcdf4` and `h5py` by doing:
> `pip install pymmg[all]`

## Usage

### Surface remeshing

```bash
python -m mmgs input.mesh output.mesh
```

### Volume remeshing

```bash
python -m mmg3d input.mesh output.mesh
```

### 2D remeshing

```bash
python -m mmg2d input.mesh output.mesh
```
