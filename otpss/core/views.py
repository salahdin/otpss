from django.shortcuts import render,get_object_or_404
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.generic.detail import DetailView
from django.core.files.storage import FileSystemStorage

"""def upload(request):

    ImageFormSet = modelformset_factory(AssessmentImage, form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
        assessmentForm = AssessmentForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=AssessmentImage.objects.none())

        if assessmentForm.is_valid() and formset.is_valid():
            post_form = assessmentForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                #this helps to not crash if the user
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = AssessmentImage(post=post_form, image=image)
                    photo.save()
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print("postForm.errors, formset.errors")
    else:
        assessmentForm = AssessmentForm()
        formset = ImageFormSet(queryset=AssessmentImage.objects.none())
    return render(request, 'index.html',
                  {'assessmentForm': assessmentForm, 'formset': formset})"""


"""class VehicleDetailView(DetailView):
    template_name = 'detail_view.html'
    queryset = Assessment.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Assessment, id=id_)


def list_vehicles(request):
    listx = Assessment.objects.all()
    context ={"assessment": listx}
    return render(request, "index.html", context)"""

def search(request):
    return render(request,"index.html")

def upload_paper(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')
