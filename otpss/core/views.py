from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views import generic
from .convert import *
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views.generic import ListView
from django.db.models import Q
from .imagePreProcess import preProcessImage
from django.core.files import File

def homepage(request):
    return render(request, "index.html")


class AssessmentSearchView(ListView):
    model = Assessment
    paginate_by = 10
    template_name = "resultPage.html"
    context_object_name = 'results'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        if keyword:
            query = SearchQuery(keyword)
            courseCode_vector = SearchVector('courseCode', weight='A')
            courseTitle_vector = SearchVector('courseTitle', weight='B')
            assessmentContent_vector = SearchVector('assessmentQuestion__content', weight='C')
            vectors = courseCode_vector + courseTitle_vector + assessmentContent_vector
            result = Assessment.objects.annotate(search=vectors).filter(search=query)
            result = result.annotate(rank=SearchRank(vectors, query)).order_by('-rank')

            return result
        return {'error': 'no results '}


def upvote(request, id_):
    """
    after clicking the upvote button answer.votes is incremented (will be used for sorting results) and a new vote
    object is created :type id_: int
    """
    answer_ = get_object_or_404(Answer, pk=id_)
    if not request.method == 'POST':
        try:
            UserVote.objects.create(user=request.user, answer=answer_, vote_type='U')
            answer_.votes += 1
            answer_.save()
            print("works")
        except:
            print("error ")
    else:
        return redirect('core:upload')
    return redirect('core:list')


def downvote(request, id_):
    """
    after clicking the downvote button answer.votes is incremented (will be used for sorting results) and a new vote
    object is created :type id_: int
    """
    answer_ = get_object_or_404(Answer, pk=id_)
    if not request.method == 'POST':
        try:
            UserVote.objects.create(user=request.user, answer=answer_, vote_type='D')
            answer_.votes = answer_.votes - 1
            answer_.save()
            print("works")
        except:
            print("error ")
    else:
        return redirect('core:upload')
    return redirect('core:list')


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
            Question.objects.create(assessment=assessment_form, content=text, date=timezone.now())
            return HttpResponseRedirect("/")
    else:
        assessmentForm = AssessmentForm()
        imageformset = ImageFormSet(queryset=AssessmentImage.objects.none())
    return render(request, 'upload.html', {'form': assessmentForm, 'ImageForm': imageformset})


def viewAnswers(request, id_):
    question = get_object_or_404(Question, id=id_)
    return render(request, 'viewAnswers.html', {'question': question})


class AssessmentListView(generic.ListView):
    model = Assessment
    context_object_name = 'assessments'
    paginate_by = 5
    template_name = 'list_view.html'


"""class AssessmentDetailView(generic.DetailView):
    model = Assessment
    template_name = 'assessmentDetailView.html'
    context_object_name = 'assessment'

    def get_queryset(self, id, *args, **kwargs):
        assessment = get_object_or_404(Assessment, id=id)
        return assessment"""


def viewAssessment(request, id_):
    assessment: Assessment = get_object_or_404(Assessment, id=id_)
    return render(request, 'assessmentDetailView.html', {'assessment': assessment})
