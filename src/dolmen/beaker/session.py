#!/usr/bin/python
# -*- coding: utf-8 -*-

import grokcore.component as grok
from beaker.session import SessionObject
from dolmen.beaker.interfaces import ISession, ISessionConfig, ENVIRON_KEY
from zope.component import queryUtility
from zope.publisher import IEndRequestEvent
from zope.publisher.interfaces.http import IHTTPRequest
from zope.site.interfaces import IRootFolder
from zope.traversing.interfaces import IBeforeTraverseEvent


@grok.implementer(ISession)
@grok.adapter(IHTTPRequest)
def ZopeSession(request):
    """Adapter factory from a Zope request to a beaker session
    """
    return request.environ.get(ENVIRON_KEY, None)


def initializeSession(request, environ_key='beaker.session'):
    """Create a new session and store it in the request.
    """
    options = queryUtility(ISessionConfig)
    if options is not None:
        session = SessionObject(request.environ, **options)
        request.environ[ENVIRON_KEY] = session


def closeSession(request):
    """Close the session, and, if necessary, set any required cookies
    """
    session = ISession(request, None)
    if session is not None:
        if session.accessed():
            session.persist()
            sessionInstructions = session.request
            if sessionInstructions.get('set_cookie', False):
                if sessionInstructions['cookie_out']:
                    cookieObj = session.cookie[session.key]
                    
                    key = cookieObj.key
                    value = session.cookie.value_encode(cookieObj.value)[1]
                    
                    args = dict([(k,v) for k,v in cookieObj.items() if v])
                    args.setdefault('path', session._path)
                    
                    request.response.setCookie(key, value, **args)


@grok.subscriber(Interface, IBeforeTraverseEvent)
def configureSessionOnStart(event):
    initializeSession(event.request)


@grok.subscriber(Interface, IEndRequestEvent)
def persistSessionOnFailure(event):
    closeSession(event.request)

