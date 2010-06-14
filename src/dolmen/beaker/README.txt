dolmen.beaker
=============

Starting with an Request

   >>> from zope.publisher.browser import TestRequest
   >>> request = TestRequest()
   >>> from zope.publisher.interfaces.http import IHTTPRequest
   >>> IHTTPRequest.providedBy(request)
   True

   >>> from dolmen.beaker.interfaces import ISession
   >>> ISession(request)
