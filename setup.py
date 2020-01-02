import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wr740n-netlimiter",
    version="1.0.0",
    author="Leonardo Guarnieri de Bastiani",
    author_email="leogbastiani@gmail.com",
    description="wr740n-netlimiter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leobastiani/wr740n-netlimiter",
    install_requires=[
        'docopt',
        'selenium',
        'urllib3',
    ],
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['netlimiter=wr740n_netlimiter:main'],
    },
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ]
)
