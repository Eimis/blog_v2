from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin

from blog.views import code
# from blog.views import code_thought
from blog.views import contact
from blog.views import hello
from blog.views import thought
from blog.views import thoughts
from blog.views import sounds
from blog.views import pics


urlpatterns = [
    # TODO: redirect:
    url(r'^$', hello, name='hello'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello, name='hello'),
    url(r'^code/$', code, name='code'),
    # url(r'^code/(?P<slug>[\w-]+)/$$', code_thought, name='code_thought'),
    url(r'^thoughts/$', thoughts, name='thoughts'),
    url(r'^thoughts/(?P<slug>[\w-]+)/$', thought, name='thought'),
    url(r'^sounds/$', sounds, name='sounds'),
    url(r'^pics/$', pics, name='pics'),
    url(r'^contact/$', contact, name='contact'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        })
    )
