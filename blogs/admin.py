# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from blogs.models import *
class PostaAdmin(admin.ModelAdmin):
    list_display = ('title','creatime')
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostaAdmin)