from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'financeproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^user/', include('users.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^madmin/', include('madmin.urls')),
)
