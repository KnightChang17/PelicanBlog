#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Knight'
SITENAME = 'Knight blog'
SITEURL = 'https://knightchang17.github.io/PelicanBlog'
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = 'en'


PATH = 'content'
STATIC_PATHS = ['images']

THEME = '/home/knight/Public/PelicanBlog/pelican-themes/blueidea/'

DEFAULT_PAGINATION = 10
LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Archcyber', 'http://www.archcyber.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

