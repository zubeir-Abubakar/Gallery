# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Location, Category, Image

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=('category',)      #pass in category article field. Value of filter_horizontal must be a list/tuple

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)

