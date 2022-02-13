from django.contrib import admin
from profiles_api import models
# Register your models here.

# To show/enable in Django admin when new one is created

admin.site.register(models.UserProfile)
