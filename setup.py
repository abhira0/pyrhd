import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrhd",
    version="0.0.8",
    author="abhira0",
    author_email="abhira0@protonmail.com",
    description="Scraper helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhira0/pyrhd",
    project_urls={"URL Shortener": "geekcrew.in/s"},
    license="NA",
    packages=setuptools.find_packages(),
    # packages=["pyrhd"],
    install_requires=["requests", "bs4", "sty"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: NA :: NA",
        "Operating System :: Windows 10",
    ],
)
