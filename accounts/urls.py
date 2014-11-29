from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/$','accounts.views.login'),
    url(r'^auth/$','accounts.views.auth_view'),
    url(r'^logout/$','accounts.views.logout'),
    url(r'^loggedin/$','accounts.views.loggedin'),
    url(r'^invalid/$','accounts.views.invalid_login'),
    url(r'^register/$', 'accounts.views.register', name='register'), 
    url(r'^register_success/$','accounts.views.register_success'),
    
    # View profiles
    url(r'^profile_detail/$','accounts.views.profile_detail', name='accounts_profile_detail'),
    url(r'^profile_detail/$','accounts.views.profile_edit', name='accounts_profile_edit'),
    url(r'^my_books/$','accounts.views.my_books', name='accounts_my_books'),
    
)
