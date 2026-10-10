from setuptools import find_packages, setup

setup(
    name="myproject",
    version="0.1.0",
    description="Навчальний проєкт для лабораторної роботи з CI/CD",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.10",
)
