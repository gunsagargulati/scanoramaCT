import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scanoramaCT",
    version="0.0.2",
    author="Gunsagar Gulati",
    author_email="gunsagargulati@gmail.com",
    description="An adapted version of the Scanorama package by Brian Hie, Bryan Bryson, and Bonnie Berger for application to CytoTRACE.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gunsagargulati/scanoramaCT",
    download_url='https://github.com/gunsagargulati/scanoramaCT/archive/v0.0.2.tar.gz',
    packages=setuptools.find_packages(),
	install_requires=[
        'annoy>=1.11.5',
        'fbpca>=1.0',
        'intervaltree==2.1.0',
        'matplotlib>=2.0.2',
        'numpy>=1.12.0',
        'scipy>=1.0.0',
        'scikit-learn>=0.20rc1'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
