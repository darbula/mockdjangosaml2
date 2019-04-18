from django.conf.urls import url
from mockdjangosaml2.views import login, assertion_consumer_service, logout


urlpatterns = [
    url(r'^login/$', login, name='saml2_login'),
    url(r'^acs/$', assertion_consumer_service, name='saml2_acs'),
    url(r'^logout/$', logout, name='saml2_logout'),
]
