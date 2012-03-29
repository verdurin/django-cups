# -*- coding: utf-8 -*-
'''
Created on 28 mars 2012

@author: sramage
'''
from django_cups.models import Printer

def printFile(server,printer_name,filename,title='django_cups print',options={}):
    printer = Printer.objects.get(server=server,name=printer_name)
    printer.printFile(filename,title,options)
    
    
    