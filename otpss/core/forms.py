from django import forms
from .models import Assessment, AssessmentImage


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['courseCode', 'courseTitle', 'assessmentDate', 'uploadDate', ]


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = AssessmentImage
        fields = ('image',)
