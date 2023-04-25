from django.contrib import admin

from app.models import Profile, Friend, ChatMessage

# Register your models here.
admin.site.register([Profile, Friend, ChatMessage])
