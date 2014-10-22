from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# media files require this modules
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myheroku.views.home', name='home'),
    # url(r'^myheroku/', include('myheroku.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^whatever$', 'whatever.views.whatever'),
    url(r'^whatever/add/$', 'whatever.views.add'),
    (r'^books/', include('books.urls', namespace="books")),
    (r'^accounts/', include('userena.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
