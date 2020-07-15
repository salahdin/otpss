from django import forms
from .models import Assessment, AssessmentImage, Answer, AssessmentFile

from django.contrib.admin import widgets

from taggit.forms import TagWidget


class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.Form):
    mydatetime = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)



class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = "__all__"
        exclude = ('user', "uploadDate",)
        widgets = {
            'assessmentDate': DateInput(),
            'tags': TagWidget(),
        }


class ImageForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'id': "files", 'name': "files[]"}))

    class Meta:
        model = AssessmentImage
        fields = ('image',)


class AnswerForm(forms.ModelForm):
    Answercontent = forms.CharField(widget=forms.Textarea, label='text area')

    class Meta:
        model = Answer
        fields = ('Answercontent', 'AnswerImage')


class AssessmentFileForm(forms.ModelForm):

    class Meta:
        model = AssessmentFile
        fields = ('document',)