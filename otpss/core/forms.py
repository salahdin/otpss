from django import forms
from .models import Assessment, AssessmentImage


class DateInput(forms.DateInput):
    input_type = 'date'


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = "__all__"
        exclude = ('user', "uploadDate",)
        widgets = {
            'assessmentDate': DateInput(),
        }


class ImageForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = AssessmentImage
        fields = ('image',)
