from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^widget/(?P<object_def>.+)', 'quickedit.views.get_form'),
    (r'^update/(?P<object_def>.+)', 'quickedit.views.update_field'),
)