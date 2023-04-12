from django.contrib import admin
from .models import Pet, PetSitter
# Register your models here.

admin.site.register(PetSitter)
admin.site.register(Pet)