from django.contrib import admin
from apps.elements.models import Category, Type, Element


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    '''Admin View for Element'''
    save_as = True
    pass

admin.site.register(Category)
admin.site.register(Type)