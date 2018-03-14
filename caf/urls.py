from sys import path

from django.conf.urls import include, url, patterns
from django.contrib import admin
# from gespa.admin import admin_site

urlpatterns = [
    # Examples:
    # url(r'^$', 'caf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^jet/', include('jet.urls', 'jet')), # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
    # url('grappelli/', include('grappelli.urls')), # grappelli URLS
    # url('admin/', admin.site.urls), # admin site

]

### disabilito il link "vedi sito" da tutte le pagine

admin.site.site_url = None
