from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["keyring>=21", "progress>=1.5", "pyinquirer>=1", "pyinstaller>=3.6", "netmiko>=3.1"]

setup(
    name="netdevr",
    version="0.0.1",
    author="Liam Brown",
    author_email="liambrown@gmail.com",
    description="A simple network device manager for batch commands and backups.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/liamtbb/netdevr",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)