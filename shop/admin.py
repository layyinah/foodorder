from django.contrib import admin
from .models import *
# Register your models here.
class CategAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug']
admin.site.register(categ,CategAdmin)

class ProdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'price', 'stock', 'img','available','desc']
    list_editable = ['price', 'stock', 'img','available','desc']
admin.site.register(products, ProdAdmin)