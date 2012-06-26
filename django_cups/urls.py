from django.conf.urls.defaults import *


urlpatterns = patterns('django_cups.views',
    (r'^displayPrintForm/$','displayPrintForm'),
    (r'^getPrinterslist/$','getPrinterslist'),
    (r'^refreshPrinterslist/$','refreshPrinterslist'),
    (r'^favourites/getlist/$','getFavouriteslist'),
    (r'^favourites/add/(?P<printer_id>\d+)$','addFavourite'),
    (r'^favourites/del/(?P<printer_id>\d+)$','delFavourite'),
)
