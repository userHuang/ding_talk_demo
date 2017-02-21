from django.conf.urls import patterns, include, url

from django.contrib import admin
from account import users
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ding_talk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^user/$', users.users),
    url(r'^ding_approval/', include('ding_approval.urls')),
)
