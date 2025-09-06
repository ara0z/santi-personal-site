#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Basic site information
AUTHOR = 'Santiago Araoz'
SITENAME = 'Santiago Araoz'
SITEURL = 'http://localhost:8000'

# Path settings
PATH = 'content'
PAGE_PATHS = ['../pages']
ARTICLE_PATHS = ['']
STATIC_PATHS = ['images', 'extra']

# Theme configuration
THEME = 'themes/pelican-svbhack'

# Time and date
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('x', 'https://x.com/santiayz'),
    ('github', 'https://github.com/ara0z'),
    ('linkedin', 'https://www.linkedin.com/in/santiaraoz/'),
)

# Pagination
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme-specific settings for pelican-svbhack
TAGLINE = '- reading, tinkering, building'
HIDE_USER_LOGO = True

# Optional: Google Analytics (uncomment and add your tracking ID)
# GOOGLE_ANALYTICS = 'UA-XXXXXXXXX-X'

# Optional: Disqus comments (uncomment and add your sitename)
# DISQUS_SITENAME = 'your-disqus-sitename'

# Markdown extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Plugin settings (if you want to use plugins later)
# PLUGIN_PATHS = ['plugins']
# PLUGINS = ['readtime']

