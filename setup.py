import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="differintegral_sage",
    version="1.0.1",
    author="Evan McIntire",
    author_email="mcintire.evan@gmail.com",
    description="SageMath Implementation of Riemann–Liouville DifferIntegral Operator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcintireevan/differintegral-sage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires='>=3.6',
)