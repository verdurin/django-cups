# -*- coding: utf-8 -*-
'''
Created on 21 mars 2012

@author: sramage
'''
'''
Custom settings for django_cups app
'''
from django.conf import settings

CUPS_SERVERS = getattr(settings, 'CUPS_SERVERS', {'Local':'localhost'})

