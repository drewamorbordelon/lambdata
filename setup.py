"""Lambdata - a Collection of Data Science Functions"""

import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DECSCRIPTION = fh.read()

setuptools.setup(
    name="lambdata-drew",
    version="0.0.1",
    author="drewamorbordelon",
    description="A collection of data science functions",
    long_description=LONG_DECSCRIPTION,
    long_description_content="text/markdown",
    url='https://github.com/drewamorbordelon/lambdata',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]

)