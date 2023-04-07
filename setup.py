# flake8: noqa
from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("LICENSE", encoding="utf-8") as f:
    license_text = f.read()

setup(
    name="EgeTelegramBot",
    version="0.2.6",
    description="Telegram bot created to solve the tasks of the USE",
    long_description=readme,
    author="Ilya Grigoryev",
    author_email="ilyagrigoryevworkmail@gmail.com",
    url="https://github.com/Ilya-Grigoriev/EgeTelegramBot",
    license=license_text,
    packages=find_packages(exclude=("tests")),
)
