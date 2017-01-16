#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rishabh Chakrabarti'
SITENAME = 'Bassdeveloper\'s Blog'
#SITEURL = 'https://bassdeveloper.github.io'
SITETITLE = AUTHOR
SITESUBTITLE = 'Data Specialist'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Facebook', 'https://www.facebook.com/Rishabh.Chakrabarti'),
        ('GitHub','#'),
        ('Pelican', 'https://getpelican.com/'),
        ('Python.org', 'https://python.org/'),
        ('Jinja2', 'https://jinja.pocoo.org/'),
        ('Add link','#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static Paths
STATIC_PATHS = ['images', 'pdfs']

# Plugins :
PLUGIN_PATHS = ['/home/flatfrog/code/pelican-plugins']
PLUGINS = ['render_math','summary']

# Theme
THEME="/home/flatfrog/code/pelican-themes/Flex"
