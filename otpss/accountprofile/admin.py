from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'studentId', 'program')
    search_fields = ['studentId', 'user']



admin.site.register(UserProfile, UserProfileAdmin)