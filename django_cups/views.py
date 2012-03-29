from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template import RequestContext
from django_cups.models import Printer,FavoritePrinter
from django.utils import simplejson
from django.http import HttpResponse

def rtr(request,template,datadict={}):
    app = __import__(__name__)
    return render_to_response(template,datadict,context_instance=RequestContext(request,current_app=app))


def displayPrintForm(request):
    return rtr(request,'django_cups/print_form.html', {})



def getPrinterslist(request):
    '''
    return the printers list
    '''
    printers = Printer.objects.all()
    return rtr(request,'django_cups/printers_list.html', {'printers':printers})


def getFavoriteslist(request):
    '''
    return favorite printers list
    '''
    printers = FavoritePrinter.objects.getFavorites(request.user)
    return rtr(request,'django_cups/favorites_list.html', {'printers':printers})

def addFavorite(request,printer_id):
    '''
    add a new printer to favorite
    '''
    printer = get_object_or_404(Printer,pk=printer_id)
    printer.addToFavorite(request.user)
    return HttpResponse(simplejson.dumps({'status':True}))

def delFavorite(request,printer_id):
    '''
    remove a favorite printer
    '''
    printer = get_object_or_404(Printer,pk=printer_id)
    printer.delFromFavorite(request.user)
    return HttpResponse(simplejson.dumps({'status':True}))

def refreshPrinterslist(request):
    '''
    refresh printers cache list
    '''
    Printer.objects.updatePrinters()
    return HttpResponse(simplejson.dumps({'status':True})) 
