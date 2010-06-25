#!/usr/bin/python
# -*- coding: utf-8 -*-

import grokcore.component as grok

from beaker.util import parse_cache_config_options
from beaker.cache import CacheManager

from zope.component import queryUtility
from dolmen.beaker.interfaces import ISessionConfig

def setupCache():
    options = queryUtility(ISessionConfig)
    if options is not None:
        return parse_cache_config_options(options)
