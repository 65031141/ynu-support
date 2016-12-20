#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'胡矿'
SITENAME = u'信息技术中心 运维服务部 （65031141）'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

BAIDU_ANALYTICS = True

DEFAULT_DATE = u'fs'
USE_FOLDER_AS_CATEGORY = True

PLUGIN_PATHS = ['plugins']
PLUGINS = [ "plantuml" ]

THEME = u'./themes/medius'

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/CNAME'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'}
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('云南大学', 'http://www.ynu.edu.cn/'),
         ('信息技术中心', 'http://www.itc.ynu.edu.cn/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
