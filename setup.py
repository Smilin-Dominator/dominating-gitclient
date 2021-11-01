from setuptools import setup

setup(
    name="GitClient",
    version="0.0",
    author="Devisha Padmaperuma",
    author_email="devisha.padmaperuma@gmail.com",
    packages=["gitclient"],
    description="A Simple GitClient Written In Python",
    install_requires=[
        "yaml",
        "rich"
    ]
)