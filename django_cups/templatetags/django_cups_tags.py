#! -*- coding: utf-8 -*-

# add extra tags to django template

from django import template
from django.core.urlresolvers import reverse
import os.path
register = template.Library()
from django_cups.models import Printer,FavoritePrinter

@register.inclusion_tag('django_cups/script.html')
def django_cups_script():
    pass

@register.inclusion_tag('django_cups/print_button.html')#, takes_context=True)
def django_cups_printbutton(button_text,view_func,arg):#context):
    print_url = reverse(view_func,args=[arg,])
    return {'button_text':button_text,'print_url':print_url}
    


