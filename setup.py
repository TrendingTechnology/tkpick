import sys
from os import path
from setuptools import setup

from Tkpick import workbench


setupdir = path.dirname(__file__)

if sys.version_info < (3, 5):
    raise RuntimeError("Tkpick requires Python 3.5 or later")

with open(path.join(setupdir, "README.md"), encoding="ASCII") as f:
    long_description = f.read()


setup(
    name="Tkpick",
    version=workbench.__version__,
    packages=["Tkpick"],
    description="Get color of pixels with cursor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=workbench.__source__,
    author=workbench.__author__,
    author_email=workbench.__contact__,
    license="GPL-3.0",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    platforms=["Linux"],
    python_requires=">=3.5",
    install_requires=["pynput", "PyGObject"],
    keywords=["tkinter", "pick", "cursor", "pixel", "color"],
    package_data={"Tkpick": ["assets/*.*"]},
    data_files=[
        ("share/applications", ["tkpick.desktop"]),
        ("share/icons", ["Tkpick/assets/tkpick.png"]),
    ],
    entry_points={"gui_scripts": ["tkpick = Tkpick:main"]},
)
