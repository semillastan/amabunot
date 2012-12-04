from django.conf.urls.defaults import *

from helpers.utils import replace_urlpattern
from accounts.views import *
from accounts.forms import RegistrationForm
from registration.views import register
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^', include('registration.urls')), #backends.default.
    url(r'^profile/$', profile, name='profile'),
    url(r'^forgot/password/$', forgot_password, name='forgot_password'),
    url(r'^profile/edit/$', edit_profile, name='edit_profile'),
    url(r'^profile/view/(?P<username>[\w|-]+)/$', profile, name='view_profile'),
    url(r'^change/password$', change_password, name='change-password'),
)

replacement = url(r'^register/$', direct_to_template, {'template':'404.html'}, name='registration_register')
replace_urlpattern(urlpatterns, replacement)
