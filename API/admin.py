from django.contrib import admin
from .models import Products, Partners
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Products)
class productsxls(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass

@admin.register(Partners)
class partnersxls(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass