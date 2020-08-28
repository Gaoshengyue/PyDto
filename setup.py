from setuptools import setup

with open("README.md",encoding="utf-8") as f:
    long_description=f.read()
setup(
    name="python-dto",
    packages=["PyDto"],
    version="0.2.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Symoon",
    author_email="symoon.gao@gmail.com",
    url="https://github.com/Gaoshengyue/PyDto",
    download_url="https://github.com/Gaoshengyue/PyDto/releases/tag/0.2.1",
    keywords=["dto,DTO,Dto,PyDto,pydto,PyDto"],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent"

    ]
)