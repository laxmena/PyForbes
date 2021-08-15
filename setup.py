import pyforbes

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requried = ["requests", "pandas>=1.3.1"]

setup(
    name="pyforbes",
    version=pyforbes.__version__,
    author="laxmena",
    author_email="ConnectWith@laxmena.com",
    description="Python package to collect data from Forbes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laxmena/PyForbes",
    download_url="https://github.com/laxmena/PyForbes",
    project_urls={
        "Bug Tracker": "https://github.com/laxmena/PyForbes/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial :: Investment",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
    ],
    install_requires=requried,
    package_dir={"": "pyforbes"},
    python_requires=">=3.6",
    license="MIT",
    keywords="forbes, forbes400, forbes list, forbes api, pyforbes",
)
