from django.contrib import admin
from . import models

# Register your models here.

class figusAdmin(admin.ModelAdmin):
    readonly_fields = ('figurita', )

admin.site.register(models.tipos_figus)
admin.site.register(models.figus_totales, figusAdmin)