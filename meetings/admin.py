from django.contrib import admin
from .models import Meeting, Room

# Registering the models for the admin interface
admin.site.register(Meeting)
admin.site.register(Room)
