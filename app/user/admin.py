from django.contrib import admin as django_admin
from django_neomodel import admin as neo_admin
from .models import Person, Movie

# Register your models here.


class PersonAdmin(django_admin.ModelAdmin):
    list_display = ('name', 'age')


neo_admin.register(Person, PersonAdmin)
