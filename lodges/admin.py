from django.contrib import admin
from .models import UserProfile, Lodge, Zone

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Lodge)
admin.site.register(Zone)
