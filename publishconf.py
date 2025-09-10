#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is intended for settings to be used when publishing the site.
# For development, use pelicanconf.py instead.

from pelicanconf import *
import os

# Production settings
SITEURL = os.environ.get('SITEURL', '')  # Set via CI for GitHub Pages
RELATIVE_URLS = False

# Uncomment and configure these for production:
# GOOGLE_ANALYTICS = 'UA-XXXXXXXXX-X'
# DISQUS_SITENAME = 'your-disqus-sitename'

# Feed settings for production
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/tag-%s.atom.xml'
TAG_FEED_RSS = 'feeds/tag-%s.rss.xml'

