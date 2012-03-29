from django.conf.urls.defaults import *


urlpatterns = patterns('django_cups.views',
    (r'^displayPrintForm/$','displayPrintForm'),
    (r'^getPrinterslist/$','getPrinterslist'),
    (r'^refreshPrinterslist/$','refreshPrinterslist'),
    (r'^favorites/getlist/$','getFavoriteslist'),
    (r'^favorites/add/(?P<printer_id>\d+)$','addFavorite'),
    (r'^favorites/del/(?P<printer_id>\d+)$','delFavorite'),
)