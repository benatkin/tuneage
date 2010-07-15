from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import os

admin.autodiscover()

urlpatterns = patterns('',
    ('^$', 'django.views.generic.simple.redirect_to', {'url': '/admin/'}),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),

    url(
        r'^media/(.*)$',
        'django.views.static.serve',
        kwargs={'document_root': os.path.join(settings.PROJECT_PATH, 'media')}
    ),
)
