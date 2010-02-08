# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.db.models import get_model
from django.contrib import admin
from django.template import RequestContext
from utils import get_data, object_from_param, final_form, get_widget, get_admin_form

from libe.models import *
#Article.libe.3.call_title
def get_form(request, object_def):
    """
    Return form for the dialog box
    """
    object, field = object_from_param(object_def)
    widget = get_widget(object, field)
    
    return HttpResponse(final_form(widget, object_def))

def update_field(request, object_def):
    object, field = object_from_param(object_def)
    if request.user.has_perm('%s.can_edit' % object.__class__.__name__):
        setattr(object, field, request.POST['data'])
        object.save()
    return HttpResponse(get_data(object, field))