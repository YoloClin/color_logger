#!/usr/bin/env python
# based on pycommon v0.2
from setuptools import setup  # type: ignore


setup(
    name="color_logger",
    version="0.1",
    description="Color logs",
    author="Clin",
    author_email="yoloClin@github.com",
    packages=["color_logger"],
    url="",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    license="LICENSE.txt",
)
