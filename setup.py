import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyMAG",
    version="0.1.6",
    author="Giacomo Marchioro",
    author_email="giacomomarchioro@outlook.com",
    description="Libreria per la creazione di file XML secondo la versione 2.0.1 dello standard MAG ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/giacomomarchioro/pyMAG",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
