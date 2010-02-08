# coding=utf-8
from django.template import Library, Node, TemplateSyntaxError, Variable, resolve_variable
from django import template

register = template.Library()

@register.tag(name="editable")
def do_editable(parser, token):
    """
    Make node editable for admin

    Usage::

       {% editable [object] %}

    Example::

        {% editable foo_object %}
    """
    bits = token.split_contents()    
    
    nodelist = parser.parse(('endeditable',))
    parser.delete_first_token()
    
    if len(bits) != 3:
        raise TemplateSyntaxError("%s tag requires exactly two arguments: object and variable to edit" % bits[0])
    
    return EditableNode(nodelist, bits[1], bits[2])

class EditableNode(template.Node):
    def __init__(self, nodelist, object, var):
        self.nodelist = nodelist
        self.object = Variable(object)
        self.var = var
    def render(self, context):
        obj = self.object.resolve(context)
        if not context['user'].has_perm('%s.can_edit' % obj.__class__.__name__):
            return self.nodelist.render(context);
        output = '<span class="editable" id="%s|%s|%i|%s">' % (obj.__class__.__name__, obj._meta.app_label, obj.id, self.var)
        output += self.nodelist.render(context) + '</span>'
        return output