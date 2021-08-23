import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrhd",
    version="0.0.4",
    author="abhira0",
    author_email="abhira0@protonmail.com",
    description="Scraper helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhira0/pyrhd",
    project_urls={"URL Shortener": "geekcrew.in/s"},
    license="NA",
    package_dir={"": "pyrhd"},
    packages=setuptools.find_packages(where="pyrhd"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: NA :: NA",
        "Operating System :: Windows 10",
    ],
)
