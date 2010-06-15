dolmen.beaker
=============

Session Config
--------------

   >>> from zope.component import getUtility, queryUtility
   >>> from dolmen.beaker.interfaces import ISessionConfig

   >>> session_config = queryUtility(ISessionConfig)
   >>> session_config.get('key')
   'beaker.session.id' 


Starting with an Request

   >>> from zope.event import notify
   >>> from zope.publisher.browser import TestRequest
   >>> from zope.publisher.interfaces.http import IHTTPRequest
   >>> from zope.traversing.interfaces import BeforeTraverseEvent

First we create an instance of the Request

   >>> request = TestRequest()
   >>> IHTTPRequest.providedBy(request)
   True

We initalize our Session with the help of the BeforeTraverseEvent.
This event will make an instance of a Session Object in the Request.

   >>> ob = object()
   >>> notify(BeforeTraverseEvent(ob, request))

Do we get our BeakerSession Object?

   >>> from dolmen.beaker.interfaces import ISession
   >>> session = ISession(request)
   >>> session.__class__
   <class 'beaker.session.SessionObject'>

Let's assign an value to our session and save it?

   >>> session['foo'] = 'bar'
   >>> session.save()
   >>> session['foo']
   'bar'

   >>> from zope.publisher.interfaces import EndRequestEvent
   >>> notify(EndRequestEvent(ob, request))

   >>> request = TestRequest()
   >>> session = ISession(request)
   >>> session['foo']
   'bar'
