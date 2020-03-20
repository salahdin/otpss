from django.contrib import admin
from .models import *


class AssessmenInline(admin.TabularInline):
    model = Assessment


class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id','user','courseCode', 'courseTitle', 'uploadDate')
    search_fields = ['courseCode', ]


admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(AssessmentImage)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserVote)