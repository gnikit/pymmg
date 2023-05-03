# pymmg - Surface and volume remeshers

Bringing [MMG](https://www.mmgtools.org/) surface and volume remeshers to Python.
This package is a wrapper around the MMG tools

## Features

- Surface remeshing
- Volume remeshing
- Area remeshing
- Adaptive mesh refinement
- Load multiple file formats using [`meshio`](https://github.com/nschloe/meshio)

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
