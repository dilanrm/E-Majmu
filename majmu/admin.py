from django.contrib import admin
from .models import Majmu


class MajmuAdmin(admin.ModelAdmin):
    list_display = ('name', 'page')


admin.site.register(Majmu, MajmuAdmin)