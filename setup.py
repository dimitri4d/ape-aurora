#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup  # type: ignore

extras_require = {
    "test": [  # `test` GitHub Action jobs uses this
        "pytest>=6.0,<7.0",  # Core testing package
        "pytest-xdist",  # multi-process runner
        "pytest-cov",  # Coverage analyzer plugin
        "hypothesis>=6.2.0,<7.0",  # Strategy-based fuzzer
    ],
    "lint": [
        "black>=22.3.0,<23.0",  # auto-formatter and linter
        "mypy>=0.910,<1.0",  # Static type analyzer
        "flake8>=3.8.3,<4.0",  # Style linter
        "isort>=5.10.1,<6.0",  # Import sorting linter
    ],
    "release": [  # `release` GitHub Action job uses this
        "setuptools",  # Installation tool
        "wheel",  # Packaging tool
        "twine",  # Package upload tool
    ],
    "dev": [
        "commitizen",  # Manage commits and publishing releases
        "pre-commit",  # Ensure that linters are run prior to commiting
        "pytest-watch",  # `ptw` test watcher/runner
        "IPython",  # Console for interacting
        "ipdb",  # Debugger (Must use `export PYTHONBREAKPOINT=ipdb.set_trace`)
    ],
}

# NOTE: `pip install -e .[dev]` to install package
extras_require["dev"] = (
    extras_require["test"]
    + extras_require["lint"]
    + extras_require["release"]
    + extras_require["dev"]
)

with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="ape-aurora",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="""ape-aurora: Ape Ecosystem Plugin for Aurora""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alberto Cevallos",
    author_email="albertocevallos@pm.me",
    url="https://github.com/albertocevallos/ape-aurora",
    include_package_data=True,
    install_requires=[
        "importlib-metadata ; python_version<'3.8'",
        "eth-ape>=0.2.1,<0.7.0",
    ],  # NOTE: Add 3rd party libraries here
    python_requires=">=3.7.2,<3.11",
    extras_require=extras_require,
    py_modules=["ape_aurora"],
    license="Apache-2.0",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"ape_aurora": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)