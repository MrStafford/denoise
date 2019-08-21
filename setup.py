from setuptools import setup

setup(
    name="denoise",
    version="0.0.1",
    license="LICENCE.txt",
    description="Removes noise from a CSV file using a median filter",
    long_description=open("README.md").read(),
    author="Michael Stafford",
    author_email="michael@redmatter.com.au",
    packages=["denoise", "denoise.test"],
    entry_points={"console_scripts": ["denoise=denoise.denoise:run"]},
    install_requires=[
        "click  >= 7.0",
        "numpy  >= 1.16.4",
        "pandas >= 0.24.2",
        "scipy  >= 1.3.0",
        "pillow >= 6.1.0",
        "matplotlib >= 3.1.1",
    ],
)
