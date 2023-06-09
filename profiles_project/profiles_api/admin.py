from django.contrib import admin

# new imports
from profiles_api import models

# Register your models here.

# Register a UserProfile model to add it to admin interface
admin.site.register(models.UserProfile)