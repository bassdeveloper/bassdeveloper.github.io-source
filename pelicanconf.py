#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rishabh Chakrabarti'
SITENAME = 'Bassdeveloper\'s Blog'
SITEURL = 'https://bassdeveloper.github.io'
SITETITLE = AUTHOR
SITESUBTITLE = 'Learning about Data'
SITEDESCRIPTION = '%s\'s Notes and Highlights' % AUTHOR
FAVICON = '/images/favicon.ico'
SITELOGO = '/images/RC.jpg'

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
LINKS = (('Learning', 'https://bassdeveloper.github.io/category/learning.html'),
('Data-Science','https://bassdeveloper.github.io/category/data-science.html'),('Business','https://bassdeveloper.github.io/category/business.html'))

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/Rishabh.Chakrabarti'),
('github', 'https://github.com/bassdeveloper/'),
('google-plus', 'https://plus.google.com/100116978271306424838'),)

DEFAULT_PAGINATION = 3


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Static Paths
STATIC_PATHS = ['images', 'pdfs','themes','assets']

# Plugins :
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['render_math','summary']

# Theme
THEME= './pelican-themes/Flex'
