from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.db.models import get_model
from django.contrib import admin
from django.template import RequestContext

from libe.models import *
from libe.quickedit_admin import *
#Article.libe.3.call_title
def get_widget(request, object_def):
    oclass, oapp, oid, ofield = object_def.split('.')#TODO @ybon put symbol in settings
    omodel = get_model(oapp, oclass)
    obj = get_object_or_404(omodel, pk=int(oid))
    field = admin.site._registry[omodel].get_form(oid).base_fields[ofield]
    
    return HttpResponse('<form action="/django_quickedit/change/' \
                        + object_def \
                        + '/" method="post" id="django_quickedit" onsubmit="return false;">' \
                        + field.widget.render('data', getattr(obj, ofield)) \
                        + '</form>')
    #TODO @ybon put URL in settings
def change(request, object_def):
    object_def = object_def.replace('/','')
    oclass, oapp, oid, ofield = object_def.split('.')
    omodel = get_model(oapp, oclass)
    obj = get_object_or_404(omodel, pk=int(oid))
    if request.user.has_perm('%s.can_edit' % oclass):
        setattr(obj, ofield, request.POST['data'])
        obj.save()
    return HttpResponse(getattr(obj, ofield))