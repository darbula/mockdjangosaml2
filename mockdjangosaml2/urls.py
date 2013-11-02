from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'mockdjangosaml2.views',
    url(r'^login/$', 'login', name='saml2_login'),
    url(r'^acs/$', 'assertion_consumer_service', name='saml2_acs'),
    url(r'^logout/$', 'logout', name='saml2_logout'),
)
