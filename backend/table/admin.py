# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Table

# Register your models here.
admin.site.register(
    Table,
    list_display=["id", "name"],
    list_display_links=["id", "name"],
)