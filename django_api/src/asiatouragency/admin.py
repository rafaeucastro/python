from django.contrib import admin
from .models import Tour
# Registering your models in admin.py in a Django project is essential because it tells Django's admin site which models you want to manage through the built-in admin interface.
admin.site.register(Tour)