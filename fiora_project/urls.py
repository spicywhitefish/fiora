from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', cache_page(60*15)(TemplateView.as_view(template_name="index.html")), name='home'),
    url(r'^/register$', 'fiora_project.views.register', name='register'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()
