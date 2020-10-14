# Configuration file for the Sphinx documentation builder.
#

# -- Project information -----------------------------------------------------

project = 'aiida-singledocs'
copyright = '2020, Francisco Ramirez'
author = 'Francisco Ramirez, Chris Sewell'


version = "0.0.1"
release = version

# -- General configuration ---------------------------------------------------

needs_sphinx = "2.0"
extensions = ["myst_nb", "sphinx_panels", "ablog", "sphinx.ext.intersphinx"]

myst_admonition_enable = True
myst_html_img_enable = True
jupyter_execute_notebooks = "auto"

blog_path = "stories/index"
blog_title = "Stories"
blog_post_pattern = ["stories/*.md", "stories/*.ipynb"]
post_redirect_refresh = 1
post_auto_excerpt = 3
post_auto_image = 1
fontawesome_included = True
html_sidebars = {
    "stories/index": ['tagcloud.html', 'archives.html', 'sbt-sidebar-nav.html'],
    "stories/*": [
        "sidebar-search-bs.html",
        "postcard.html",
        "recentposts.html",
        "tagcloud.html",
        "categories.html",
        "archives.html",
        "sbt-sidebar-nav.html",
        "sbt-sidebar-footer.html",
    ]
}

intersphinx_mapping = {
    "aiida": ("http://aiida-core.readthedocs.io/en/latest/", None),
}

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_book_theme"
# html_title = f"version: {version}"
# html_favicon = "_static/quantum-mobile-v4-text-square.png"
# html_logo = "_static/quantum_mobile_text_wide.png"
html_theme_options = {
    "home_page_in_toc": True,
    "repository_url": "https://github.com/aiidateam/aiida-blog",
    "repository_branch": "develop",
    "use_repository_button": True,
    "use_issues_button": True,
    "path_to_docs": "docs",
    "use_edit_page_button": True,
}
panels_add_bootstrap_css = False


def start_aiida(*args):
    import os
    import subprocess
    subprocess.check_call(["reentry", "scan"])
    try:
        print(subprocess.check_output(["locale-gen",  "en_US.UTF-8"]))
    except:
        pass
    print(subprocess.check_output(["locale"]))
    print(subprocess.check_output(["locale", "-a"]))
    # os.environ["LANG"] = "en_US.UTF-8"
    # os.environ["LC_ALL"] = "en_US.UTF-8"
    from aiida.manage.tests import _GLOBAL_TEST_MANAGER, BACKEND_DJANGO
    from aiida.common.utils import Capturing
    with Capturing():  # capture output of AiiDA DB setup
        _GLOBAL_TEST_MANAGER.use_temporary_profile(backend=BACKEND_DJANGO, pgtest=None)
    from aiida.manage.configuration import settings
    os.environ["AIIDA_PATH"] = settings.AIIDA_CONFIG_FOLDER

def end_aiida(*args):
    from aiida.manage.tests import _GLOBAL_TEST_MANAGER
    _GLOBAL_TEST_MANAGER.destroy_all()

def setup(app):
    app.connect('builder-inited', start_aiida)
    app.connect('build-finished', end_aiida)
