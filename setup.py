from setuptools import setup, find_packages

long_desc = open("README.md").read()

name = 'PyForbes'
repo_slug = 'pyforbes/{}'.format(name.lower())
repo_url = 'https://github.com/{}'.format(repo_slug)

setup(
    name="pyforbes",
    version="1.0.3",
    author="laxmena",
    author_email="ConnectWith@laxmena.com",
    description="Python package to collect data from Forbes.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/laxmena/PyForbes",
    download_url="https://github.com/laxmena/PyForbes",
    project_urls={
        "Bug Tracker": "https://github.com/laxmena/PyForbes/issues",
        'CI: Circle': 'https://circleci.com/gh/{}'.format(repo_slug),
        'GitHub: repo': repo_url,
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
    install_requires=[
        "pandas>=1.1.3", 
        "numpy",
        "requests"
        ],
    extras_require={
        'docs': [
            'sphinx',
            'docutils',
            'alabaster',
            'setuptools'
        ]
    },
    packages=find_packages(include=["pyforbes", "pyforbes.*"]),
    python_requires=">=3.6",
    license="MIT",
    keywords="python forbes api pyforbes",
)
