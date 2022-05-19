from setuptools import setup

NAME = "LeagueOfEvents"
DESCRIPTION = "Create an event system for the League of Legends live game API"
URL = "https://github.com/agroth01/LeagueOfEvents"
EMAIL = "software.agroth@gmail.com"
AUTHOR = "Alexander Groth"
VERSION = "0.5.0"
REQUIRED = [
    "requests",
    "urllib3"
]

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    author = AUTHOR,
    author_email = EMAIL,
    install_requires = REQUIRED,
    url = URL,
    packages = ["leagueofevents"]
)
