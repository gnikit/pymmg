import sys

from setuptools import find_packages
from skbuild import setup

CMAKE_GENERATOR = "Ninja" if sys.platform != "win32" else "Visual Studio 16 2019"

setup(
    name="pymmg",
    cmake_args=(["-G", CMAKE_GENERATOR]),
    packages=find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "mmgs=mmgs:main",
            "mmg2d=mmg2d:main",
            "mmg3d=mmg3d:main",
        ],
    },
    cmake_with_sdist=True,
)
