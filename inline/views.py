from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from models import TestInlineModel
from django.db.models import get_model
from django.contrib import admin
from django.template import RequestContext

def get_widget(request, object_def):
    oclass, oapp, oid, ofield = object_def.split('.')
    omodel = get_model(oapp, oclass)
    obj = get_object_or_404(omodel, pk=int(oid))
    field = admin.site._registry[omodel].get_form(oid).base_fields[ofield]
    
    return HttpResponse('<form action="/django_inline/change/'+object_def+'/" method="post" id="django_inline">' + field.widget.render('data', getattr(obj, ofield)) \
                        + '<br /><input type="submit" value="ok" /></form>')

def change(request, object_def):
    object_def = object_def.replace('/','')
    oclass, oapp, oid, ofield = object_def.split('.')
    omodel = get_model(oapp, oclass)
    obj = get_object_or_404(omodel, pk=int(oid))
    if request.user.has_perm('%s.can_edit' % oclass):
        setattr(obj, ofield, request.POST['data'])
        obj.save()
    return HttpResponse(getattr(obj, ofield))

def test_view(request):
    test_object = TestInlineModel.objects.get(pk=1)
    return render_to_response('inline_test.html', RequestContext(request, {'test_object': test_object}))
    