from setuptools import setup

setup(
    name="parephase",
    install_requires=[
        "gffutils",
        "numpy",
        "pysam",
    ],
    version="0.2.0",
    scripts=["parephase"],
    author="Kevin D Murray",
    author_email="kdmpapers@gmail.com",
    description="Detects phasing of 5'PARE data around stop codons",
    license="MPL2",
    url="https://github.com/kdmurray91/parephase",
    keywords="bioinformatics PARE RNA",
)
