from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^get/(?P<book_id>\d+)/$','books.views.book', name='detail'),
    url(r'^add_book/$','books.views.add_book', name='add_book'),
    url(r'^book_edit/(?P<book_id>\d+)/$','books.views.book_edit', name='book_edit'),
    url(r'^book_delete/(?P<book_id>\d+)/$','books.views.book_delete', name='book_delete'),
    url(r'^category/(?P<book_category>\w+)/$','books.views.category', name='category'),
    url(r'^oglasi_korisnika/(?P<book_user>\w+)/$','books.views.oglasi_korisnika', name='oglasi_korisnika'),
    url(r'^search/$','books.views.search'),
)
