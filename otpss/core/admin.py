from django.contrib import admin
from .models import *


class AssessmentImageInline(admin.TabularInline):
    model = AssessmentImage


class AssessmentAdmin(admin.ModelAdmin):
    inlines = [AssessmentImageInline]
    list_display = ('id', 'user', 'courseCode', 'courseTitle', 'uploadDate')
    search_fields = ['courseCode', ]

class AssessmentImageAdmin(admin.ModelAdmin):
    list_display = ('assessment', 'image')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('assessment', 'questionSnippet')
    search_fields = ['content']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('Answercontent', 'user', 'created', 'votes')

admin.site.register(UserFavoriteAssessment)
admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(AssessmentImage,AssessmentImageAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserVote)