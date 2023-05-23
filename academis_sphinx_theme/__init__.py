
from os import path

__version_info__ = (1, 0, 0)
__version__ = "1.0.0"


def setup(app):
    app.add_html_theme('academis_sphinx_theme', path.abspath(path.dirname(__file__)))
