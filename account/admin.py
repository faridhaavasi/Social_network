from django.contrib import admin
from .models import User
from . import models
admin.site.register(User)
admin.site.register(models.Profile)
admin.site.register(models.Device)