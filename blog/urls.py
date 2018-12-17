from django.urls import path
from django.conf import settings
from django.conf.urls import static
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
    path(r'', hello, name='hello'),
    path('admin/', admin.site.urls),
    path('hello/', hello, name='hello'),
    path('code/', code, name='code'),
    # path('code/(?P<slug>[\w-]+)/', code_thought, name='code_thought'),
    path('thoughts/', thoughts, name='thoughts'),
    path('thoughts/(?P<slug>[\w-]+)/', thought, name='thought'),
    path('sounds/', sounds, name='sounds'),
    path('pics/', pics, name='pics'),
    path('contact/', contact, name='contact'),

] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
