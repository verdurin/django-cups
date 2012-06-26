from django.db import models
from django.contrib.auth.models import User
from django_cups.settings import CUPS_SERVERS
import cups

class PrinterManager(models.Manager):
    def updatePrinters(self,server_host=None):
        '''
        Update printers list
        if server_host is None, CUPS_SERVERS is used, see settings
        '''
        if server_host is None:
            servers = CUPS_SERVERS
        else:
            servers = {'':server_host}
        for server_name,host in servers.items():
            conn = cups.Connection(host)
            printers_list = conn.getPrinters()
            for name,values in printers_list.items():
                printer,created = self.get_or_create(server=host,name=name)
                printer.server_name=server_name
                printer.location = values.get('printer-location','')
                printer.info = values.get('printer-info','')
                printer.save()
                
    def getPrinters(self,server_host):
        '''
        return printers list for a specific host
        ''' 
        return self.filter(server=server_host)

class Printer(models.Model):
    class Meta:
        unique_together = [('server','name'),]
        ordering = ['server_name','name']
    objects = PrinterManager()
    server = models.CharField('Server',max_length=255)
    server_name = models.CharField('Server Name',max_length=255)
    name = models.CharField('Printer',max_length=255)
    info = models.CharField('Description',max_length=255)
    location = models.CharField('Location',max_length=255)
    
    def __unicode__(self):
        return '%s'%self.name
    
    def addToFavourite(self,user):
        '''
        Add to favourites list
        '''
        FavouritePrinter.objects.addPrinter(user,self)
    
    def delFromFavorite(self,user):
        '''
        Delete from favourites list
        '''
        favourites = self.favouriteprinter_set.filter(user=user)
        if favourites:
            favourites.delete()
        
    def printFile(self,filename,title='django_cups print',options={}):
        '''
        print a file
        filename must refer to a ps or pdf file
        '''
        conn = cups.Connection(self.server)
        conn.printFile(self.name, filename,title,options)
    
    def printTestPage(self):
        '''
        print a test page
        '''
        conn = cups.Connection(self.server)
        conn.printTestPage(self.name)

class FavouriteManager(models.Manager):
    def getFavourites(self,user):
        '''
        return all favourite printers for a user
        '''
        printers = self.filter(user=user)
        return printers
    
    def addPrinter(self,user,printer):
        '''
        add a new printer to favourite list
        '''
        printer,created = self.get_or_create(user=user,printer=printer)

class FavouritePrinter(models.Model):
    class Meta:
        unique_together = [('user','printer')]
        ordering = ['printer__server_name','printer__name']
    objects = FavouriteManager()
    user = models.ForeignKey(User)
    printer = models.ForeignKey(Printer)
    
    def __unicode__(self):
        return '%s'%self.printer.name
    
        
