from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^widget/(?P<object_def>.+)', 'inline.views.get_widget'),
    (r'^change(?P<object_def>.+)', 'inline.views.change'),
)