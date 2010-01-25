from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^widget/(?P<object_def>.+)', 'quickedit.views.get_widget'),
    (r'^change(?P<object_def>.+)', 'quickedit.views.change'),
)