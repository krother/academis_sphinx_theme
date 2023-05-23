from importlib.metadata import entry_points
from setuptools import setup

setup(
    name="academis_sphinx_theme",
    description="make theming subpages on academis.eu easy",
    author="Kristian Rother",
    author_email="kristian.rother@posteo.de",
    url="https://github.com/krother/academis_sphinx",
    license="MIT",

    entry_points = {
        'sphinx.html_themes': [
            'name_of_theme = academis_sphinx_theme',
        ]
    },

    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
