#!/usr/bin/python
# -*- coding: utf-8 -*-

import grokcore.component as grok
from dolmen.beaker.interfaces import ISession


class ImmutableDict(dict):
    """A dict that can be updated only through the `update` or
    `setdefault` methods.
    """
    def __setitem__(self, key, value):
        raise NotImplementedError(
            'This dict cannot be altered through direct assignation')
        
    def __hash__(self):
        items = self.items()
        res = hash(items[0])
        for item in items[1:]:
            res ^= hash(item)
        return res


DEFAUT_CONFIG = ImmutableDict(
    invalidate_corrupt=True,
    type=None, 
    data_dir=None,
    key='beaker.session.id', 
    timeout=None,
    secret=None,
    log_file=None,
    )


grok.global_utility(DEFAUT_CONFIG, provides=ISession, direct=True)
