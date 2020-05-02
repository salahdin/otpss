from django import forms
from .models import Assessment, AssessmentImage,Answer


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
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'id': "files", 'name': "files[]"}))

    class Meta:
        model = AssessmentImage
        fields = ('image',)


class AnswerForm(forms.ModelForm):
    Answercontent = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        model=Answer
        fields=('Answercontent', 'AnswerImage')