# Brenden Price, Alpha Beta Debug Week 1, Written 04/19/21
# This file describes the database schema for the blog application within our website.
# This file is similar to the CREATE TABLE in SQL and automatically generates that SQL query in the migrations
# Whenever you update the tables in this file you must run python manage.py makemigrations, followed by
# python manage.py migrate. makemigrations creates the queries, migrate executes the changes. If you get
# and error with these commands, you may need to type python3 instead of python
from django.db import models
from django.contrib.auth.models import User  # Import django User table
from datetime import date  # Import date module from datetime package


# Create your models here.
class Blog(models.Model):
    """Defines the columns for the blog table. Inherits from models.Model"""
    title = models.CharField(max_length=255)  # Character field with max length of 255 characters
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author is a user
    body = models.TextField()  # Textfield
    date = models.DateField(default=date.today)  # Date field, autofill to today, is editable
    created_at = models.DateTimeField(auto_now_add=True)  # This field is not editable. It is set to the current time at
    # object creation
    last_updated = models.DateTimeField(auto_now=True)  # This field is not editable. It is set to the current time at
    # object update.
    # TODO: Add Likes
    # TODO: Add Comments
