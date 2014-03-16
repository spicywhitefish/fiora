from django.conf.urls import patterns, url
 
urlpatterns = patterns('fiora_project.accounts',
    url(r'^register/?$', 'views.iama', name='accounts.views.iama'),
    url(r'^register/submit/?$', 'views.register', name='accounts.views.register'), 
)