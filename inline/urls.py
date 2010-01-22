from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^widget/(?P<object_def>.+)', 'django_inline.views.get_widget'),
    (r'^change(?P<object_def>.+)', 'django_inline.views.change'),
)