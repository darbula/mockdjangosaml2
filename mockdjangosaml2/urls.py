from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'mockdjangosaml2.views',
    url(r'^login/$', 'login', name='saml2_login'),
    url(r'^logout/$', 'logout', name='saml2_logout'),
)
