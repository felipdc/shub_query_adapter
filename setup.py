from setuptools import setup, find_packages

setup(
    name="shub_sql_adapter",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "sqlparse"
    ],
)
