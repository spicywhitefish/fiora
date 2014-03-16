from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.cache import cache_page
from views import HomeView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^/?$', HomeView.as_view(template_name="index.html"), name='home'),
    url(r'^account/', include('fiora_project.accounts.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()
