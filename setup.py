from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


NAME = "LeagueOfEvents"
DESCRIPTION = "Create an event system for the League of Legends live game API"
URL = "https://github.com/agroth01/LeagueOfEvents"
EMAIL = "software.agroth@gmail.com"
AUTHOR = "Alexander Groth"
VERSION = "1.0.0"
REQUIRED = [
    "requests",
    "urllib3",
    "threading",
    "collections"
]

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    author = AUTHOR,
    author_email = EMAIL,
    install_requires = REQUIRED,
    url = URL,
    packages = ["leagueofevents"],
    long_description=long_description,
    long_description_content_type="text/markdown"
)
