# Brenden Price, Alpha Beta Debug Week 1, Written 04/19/21
# This file determines what applications/tables show up in the django admin portal
# To login you must run python manage.py createsuperuser. If error, python3 manage.py createsuperuser
# Email field is optional. You will not be able to see your password as you type it
from django.contrib import admin
from .models import Blog  # import the Blog table from the models file in the same directory as this file


# Register your models here.
@admin.register(Blog)  # This is a decorator. Don't worry about how to use it, just know that it is registering the app
# with the admin site.
class BlogAdmin(admin.ModelAdmin):
    """Provides meta data to the admin site about how to treat the provided data"""
    list_display = ['title', 'author', 'date', 'created_at', 'last_updated']  # In admin site, inside of Blog,
    # display these fields
