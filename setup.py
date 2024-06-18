import sys

from setuptools import find_packages
from skbuild import setup

CMAKE_GENERATOR = "Ninja" if sys.platform != "win32" else "Visual Studio 17 2022"

setup(
    name="pymmg",
    cmake_args=(["-G", CMAKE_GENERATOR]),
    packages=find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "mmgs=pymmg.mmgs:main",
            "mmg2d=pymmg.mmg2d:main",
            "mmg3d=pymmg.mmg3d:main",
        ],
    },
    cmake_with_sdist=True,
)
