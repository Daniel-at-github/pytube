#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Unknown'
SITENAME = 'PyTube.org'

PATH = 'content'
#PATH = 'pyvideo-data/data'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = "Undefined"

AUTHOR_URL = AUTHOR_SAVE_AS = 'speaker/{slug}.html'
ARTICLE_URL = ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_LANG_URL = ARTICLE_LANG_SAVE_AS = '{category}/{slug}-{lang}.html'
DRAFT_URL = DRAFT_SAVE_AS = 'drafts/{category}/{slug}.html'
DRAFT_LANG_URL = DRAFT_LANG_SAVE_AS = 'drafts/{category}/{slug}-{lang}.html'
PAGE_URL = PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
CATEGORY_URL = CATEGORY_SAVE_AS = 'events/{slug}.html'
TAGS_URL = TAGS_SAVE_AS = 'tags.html'
# Hack to avoid this issue: https://github.com/getpelican/pelican/issues/1137
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
# End hack to avoid issue #1137
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'
CATEGORIES_SAVE_AS = 'events.html'
AUTHORS_SAVE_AS = 'speakers.html'

USE_FOLDER_AS_CATEGORY = False

# Feeds
FEED_RSS = 'rss.xml'
CATEGORY_FEED_RSS = 'events/%s/rss.xml'
AUTHOR_FEED_RSS = 'author/%s/rss.xml'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

THEME = 'themes/pytube-201601/'

GITHUB_URL = 'https://github.com/pytube/pytube'
CONTRIBUTE_URL = 'https://github.com/pytube/pytube/wiki/How-to-Contribute-Media'

PUBLISHER_URL = (os.environ.get('PUBLISHER_URL') or '').strip()
PUBLISHER_URL = PUBLISHER_URL or 'https://publisher.pytube.org/publish'

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

#import sys
#sys.path.append(os.path.abspath("."))
#from plugins import json_reader
PLUGIN_PATHS = ['plugins']
PLUGINS = ['json_reader', 'bin.plugins', 'extended_sitemap', 'bin.aggregations']
#PLUGINS = ['bin.plugins', 'extended_sitemap']
