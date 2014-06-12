from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'quinyelax.views.quiniela', name='home'),
    url(r'^quiniela$', 'quinyelax.views.quiniela', name='quiniela'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
