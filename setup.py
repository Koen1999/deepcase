import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepcase",
    version="1.0.2",
    author="Thijs van Ede",
    author_email="t.s.vanede@utwente.nl",
    description="DeepCASE: Semi-Supervised Contextual Analysis of Security "
                "Events",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Thijsvanede/DeepCASE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = (
        "scipy>=1.3.3",
        "tqdm>=4.56.0",
        "numpy>=1.17.4",
        "pandas>=1.2.1",
        "argformat>=0.0.3",
        "torch>=1.9.0",
        "scikit_learn>=0.24.2",
    ),
)
