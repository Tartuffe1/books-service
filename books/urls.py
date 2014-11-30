from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^get/(?P<book_id>\d+)/$','books.views.book', name='detail'),
    url(r'^add_book/$','books.views.add_book'),
    url(r'^category/(?P<book_category>\w+)/$','books.views.category', name='category'),
    url(r'^oglasi_korisnika/(?P<book_id>\d+)/$','books.views.oglasi_korisnika', name='oglasi_korisnika'),
    url(r'^search/$','books.views.search'),
)
