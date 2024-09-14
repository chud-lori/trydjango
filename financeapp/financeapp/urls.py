from django.conf.urls import patterns, include, url
from django.contrib import admin
# docstring in file under import
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'financeapp.views.home', name='home'),
    # this is blog
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
# end of line comment