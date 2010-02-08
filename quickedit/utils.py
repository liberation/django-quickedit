# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.db.models import get_model
from django.contrib import admin
from django import forms

def get_data(object, field):
    """
    Returns the front data for a specific field.
    If a method is declared in the model, uses this.
    Otherwise use the default Python getter.
    """
    data = getattr(object, field)
    return data;

def get_widget(object, field):
    return get_admin_widget(object, field)

def object_from_param(param):
    """
    Returns a tuple with :
    – object
    – field name
    Param expected is : Model|app|id|field
    If instance not found, a 404 is raised.
    """
    class_name, app_name, id, field = param.split('|')#TODO @ybon put symbol in settings
    model = get_model(app_name, class_name)
    object = get_object_or_404(model, pk=int(id))
    return object, field

def object_to_param(object, field):
    return "%s|%s|%i|%s" % (object.__class__.__name__, object._meta.app_label, object.id, field)

def final_form(widgets, url_param):
    """
    Return the final form with inputs elements.
    url_param is standardised string for url param, coming from object_to_param
    """
    return '<form action="/quickedit/update/' \
            + url_param \
            + '" method="post" id="django_quickedit" onsubmit="return false;">' \
            + widgets \
            + '</form>'

def get_admin_form(object):
    return admin.site._registry[object.__class__].get_form(object.pk)

def get_admin_widget(object, field):
#    current_form = forms.Form
#    setattr(current_form, field, forms.CharField())
#    return current_form.as_p(current_form)
    data = get_data(object, field)
    form = get_admin_form(object)
    field = form.base_fields[field]
    return field.widget.render('data', data)    
