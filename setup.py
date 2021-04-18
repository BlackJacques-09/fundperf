from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name="fundperf",
    version="0.0.1",
    description="High level tools for Performance Analysis and reporting",
    author="Antoine Perrin",
    author_email="antoineperrin.pro2@gmail.com",
    package_dir={"": "src"},
    py_modules = ['fundperf'],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["workalendar","pandas","numpy","warnings","datetime"
        ],
    url = "https://github.com/ahgperrin/fundperf"
)
