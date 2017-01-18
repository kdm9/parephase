from setuptools import setup

setup(
    name="parestahp",
    install_requires=[
        "gffutils",
        "intervaltree",
        "numpy",
        "pysam",
    ],
    version="0.1.0",
    scripts=["parestahp"],
    author="Kevin D Murray",
    author_email="kdmpapers@gmail.com",
    description="Detects phasing of 5'PARE data around stop codons",
    license="MPL2",
    url="https://github.com/kdmurray91/parestahp",
    keywords="bioinformatics PARE RNA",
)
