Mock djangosaml2
================
In projects that use ``djangosaml2`` in production environment it is usefull to have a mockup authentication system that can be used in development and testing environments i.e. when ``DEBUG = True``.

Install
-------
``pip install mockdjangosaml2``

Usage
-----
* in project's ``settings.py``::

    if DEBUG:
        INSTALLED_APPS += ('mockdjangosaml2',)
    else:
        INSTALLED_APPS += ('djangosaml2',)

* update project's ``urls.py`` file to include separate set of patterns for ``DEBUG = True`` case::

    if settings.DEBUG:
        urlpatterns += patterns('',
            (r'^saml2/', include('mockdjangosaml2.urls')),
        )
    else:
        urlpatterns += patterns('',
            (r'^saml2/', include('djangosaml2.urls')),
        )

* add mock users and their attributes to ``MOCK_SAML2_USERS`` in ``settings.py``. It should be formated as sample given in applications ``settings.py`` file.
