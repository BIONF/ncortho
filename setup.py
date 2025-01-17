"""
ncOrtho - Targeted ortholog search for miRNAs
Copyright (C) 2021 Felix Langschied

ncOrtho is a free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ncOrtho is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ncOrtho.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ncOrtho",
    version="0.4.4",
    python_requires='>=3.7.0',
    description=" Targeted ortholog search for miRNAs ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Felix Langschied",
    author_email="langschied@bio.uni-frankfurt.de",
    url="https://github.com/felixlangschied/ncortho",
    packages=find_packages(),
    package_data={'': ['*']},
    install_requires=[
        'PyYAML',
        'biopython',
        'pyfaidx',
        'pyfiglet',
        'tqdm'
    ],
    entry_points={
        'console_scripts': ["ncCreate = ncOrtho.coreset.coreset:main",
                            "ncSearch = ncOrtho.ncortho:main",
                            "ncAnalyze = ncOrtho.analysis.ncAnalyze:main",
                            "ncCheck = ncOrtho.check.core_synteny:main"
                            ],
    },
    license="GPL-3.0",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
)
