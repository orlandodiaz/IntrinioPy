import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intrinioPy",
    version="0.1.0",
    author="Orlando Diaz",
    author_email="orlandodiaz.dev@gmail.com",
    description="Intrinio client to fetch stocks from Screener API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/orlandodiaz/IntrinioPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests>=2.21.0', 'log3>=0.1.7'
    ])
