# -*- coding: utf-8 -*-
#
# Sysystems Administration for Cyborgs build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".ext")))
from docs_meta import VersionMeta

# -- General configuration -----------------------------------------------------

extensions = ['sphinx.ext.todo']
templates_path = ['templates']
source_suffix = '.txt'
master_doc = 'contents'

git_name = 'administration'

project = u'Systems Administration for Cyborgs'
copyright = u'2012, Sam Kleinman and Contributors'

version = ''
release = '1'

exclude_patterns = []

pygments_style = 'sphinx'
intersphinx_mapping = {'http://docs.python.org/': None}

# -- Options for HTML output ---------------------------------------------------

current_git_commit = VersionMeta.commit
rst_epilog = ".. |commit| replace:: ``" + current_git_commit + "``"

html_theme = 'cyborg'
html_use_smartypants = True
html_theme_path = ['themes']
html_static_path = ['./source/.static']

html_title = "Systems Administration for Cyborgs"
html_short_title = html_title

html_logo = None
html_favicon = None

html_theme_options = { 
    'project': git_name, 
    'ga_code': 'UA-2505694-4'
}

html_sidebars = {
    '**': ['localtoc.html', 'relations.html', 'sourcelink.html'],
}

#html_title = None
#html_short_title = None
#html_logo = None
#html_favicon = None

html_use_index = True
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
htmlhelp_basename = 'cyborg-systems-administration'

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'letter'
latex_font_size = '10pt'
latex_documents = [
# (source start file, target name, title, author, documentclass [howto/manual]).
  ('contents', 'kleinman.systems-administraton-for-cyborgs.tex', u'Systems Administration for Cyborgs', u'Sam Kleinman', 'manual'),
]

#latex_use_parts = False
latex_show_pagerefs = True
latex_show_urls = False

#latex_logo = None
#latex_preamble = ''
#latex_appendices = []
latex_domain_indices = False


# -- Options for manual page output --------------------------------------------

man_pages = [
    ('index', 'systems-administraton-for-cyborgs', u'Systems Administration for Cyborgs',
     [u'Sam Kleinman'], 1)
]

# -- Options for Epub output ---------------------------------------------------

epub_title = u'Systems Administration for Cyborgs'
epub_author = u'Sam Kleinman'
epub_publisher = u'Sam Kleinman'
epub_copyright = u'2012, Sam Kleinman'

epub_tocdepth = 1
epub_tocdup = False

epub_scheme = 'URL'
epub_identifier = 'http://cyborginstitute.org/projects/administration/'

#epub_uid = ''
#epub_pre_files = []
#epub_post_files = []
#epub_exclude_files = []
