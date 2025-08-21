from setuptools import setup, find_packages
from pathlib import Path

this_dir = Path(__file__).parent
readme = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="tf_toolbox",
    version="0.0.1",
    description="Time–frequency analysis toolbox (Python reimplementation of MATLAB TF)",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="LabPy",
    python_requires=">=3.9",
    packages=find_packages(where="."),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "mne>=1.6.0",
    ],
    include_package_data=True,
    license="BSD-3-Clause",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    project_urls={
        "Source": "https://example.com/tf_toolbox",
    },
)
