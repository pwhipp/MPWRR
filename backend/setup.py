import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="MPWRR",
    version="0.0.1",
    author="Paul Whipp <paul.whipp@gmail.com>",
    author_email="paul.whipp@gmail.com",
    description="A stack for the development and deployment of web services that support "
                "the operation and governance of clubs and organizations.",
    url="git@github.com:pwhipp/MPWRR.git",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"])
