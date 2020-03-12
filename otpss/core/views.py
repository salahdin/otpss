from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views import generic
from .convert import *
from django.utils import timezone


def search(request):
    return render(request, "index.html")


def upload_paper(request):
    ImageFormSet = modelformset_factory(AssessmentImage,
                                        form=ImageForm, extra=3)
    if request.method == 'POST':
        assessmentForm = AssessmentForm(request.POST)
        imageformset = ImageFormSet(request.POST, request.FILES,
                                    queryset=AssessmentImage.objects.none())

        if assessmentForm.is_valid() and imageformset.is_valid():
            assessment_form = assessmentForm.save(commit=False)
            # change to upper case and remove white space
            course_Code = assessment_form.courseCode.replace(" ", "").upper()
            assessment_form.courseCode = course_Code
            assessment_form.user = request.user
            assessment_form.save()

            text = ""
            for form in imageformset.cleaned_data:
                if form:
                    image = form['image']
                    photo = AssessmentImage(assessment=assessment_form, image=image)

                    text += convert_img_to_txt(image)
                    photo.save()
            print(text)
            Question.objects.create(assessment=assessment_form, content=text, date=timezone.now())
            return HttpResponseRedirect("/")
    else:
        assessmentForm = AssessmentForm()
        imageformset = ImageFormSet(queryset=AssessmentImage.objects.none())
    return render(request, 'upload.html', {'form': assessmentForm, 'ImageForm': imageformset})


class AssessmentListView(generic.ListView):
    model = Assessment
    context_object_name = 'assessments'  # your own name for the list as a template variable
    paginate_by = 5
    template_name = 'list_view.html'
