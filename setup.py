import os
import sys

from skbuild import setup

setup(
    name="mmg",
    version="5.7.0",
    description="meshing library",
    python_requires=">=3.7",
    # long_description=open(os.path.join(os.getcwd(), "README.md")).read(),
    # long_description_content_type="text/markdown",
    author="Giannis Nikiteas",
    # author_email="wvermin@gmail.com",
    maintainer="Giannis Nikiteas",
    # keywords="fortran, formatter, format converter, dependency generator",
    # url="https://github.com/wvermin/findent",
    # license="BSD License 2.0",
    # platforms="Posix, Windows",
    # classifiers=[
    #     "Development Status :: 5 - Production/Stable",
    #     "Intended Audience :: Developers",
    #     "Intended Audience :: Science/Research",
    #     "License :: OSI Approved :: BSD License",
    #     "Operating System :: POSIX :: Linux",
    #     "Operating System :: Microsoft :: Windows",
    #     "Operating System :: MacOS :: MacOS X",
    #     "Programming Language :: Fortran",
    #     "Programming Language :: C++",
    #     "Topic :: Software Development",
    #     "Topic :: Text Processing",
    # ],
    # cmake_args=(
    #     ["-G", "Visual Studio 16 2019"] if sys.platform == "win32" else ["-G", "Ninja"]
    # ),
)
