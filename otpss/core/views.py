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
from django.views.generic import ListView,TemplateView
from .idquestion import splitParagraph
from hitcount.views import HitCountDetailView
from taggit.models import Tag
import operator


def homepage(request):
    context = {'popular_posts': Assessment.objects.order_by('courseCode')[:3]}
    return render(request, "index.html", context)


class AssessmentSearchView(ListView):
    model = Assessment
    paginate_by = 5
    template_name = "resultPage.html"
    context_object_name = 'results'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        keyword = keyword.replace(',', " ")
        print(keyword)
        if keyword:
            query = SearchQuery(keyword)
            courseCode_vector = SearchVector('courseCode', weight='A')
            courseTitle_vector = SearchVector('courseTitle', weight='B')
            assessmentContent_vector = SearchVector('assessmentQuestion__content', weight='C')
            vectors = courseCode_vector + courseTitle_vector + assessmentContent_vector
            result = Assessment.objects.annotate(search=vectors).filter(search__icontains=keyword)

            result = result.annotate(rank=SearchRank(vectors, query)).order_by('id','-rank').distinct('id')
            finalQueryset = sorted(result, key=operator.attrgetter('rank'), reverse=True)

            return finalQueryset[:100]


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

@login_required
def upload_paper(request):
    if request.user == None:
        return redirect('/')
    common_tags = Assessment.tags.most_common()[:4]
    if request.method == 'POST':
        assessmentForm = AssessmentForm(request.POST)
        imageformset = ImageForm(request.POST, request.FILES)

        if assessmentForm.is_valid() and imageformset.is_valid():
            assessment_form = assessmentForm.save(commit=False)
            # change to upper case and remove white space
            course_Code = assessment_form.courseCode.replace(" ", "").upper()
            assessment_form.courseCode = course_Code
            assessment_form.user = request.user
            assessment_form.save()
            assessmentForm.save_m2m()
            text = ""
            for image in request.FILES.getlist('image'):
                photo = AssessmentImage(assessment=assessment_form, image=image)
                text += convert_img_to_txt(image)
                photo.save()
            for i in splitParagraph(text):
                Question.objects.create(assessment=assessment_form, content=i, date=timezone.now())

            return HttpResponseRedirect("")
    else:
        assessmentForm = AssessmentForm()
        imageformset = ImageForm()
    return render(request, 'upload.html', {'form': assessmentForm, 'ImageForm': imageformset,'common_tags':common_tags})


def viewAnswers(request, id_):
    question = get_object_or_404(Question, id=id_)
    lst = question.questionAnswer.all()

    if request.method == 'POST':
        answerForm = AnswerForm(request.POST)
        if answerForm.is_valid():
            answer_form = answerForm.save(commit = False)
            answer_form.question = question
            answer_form.user = request.user
            answer_form.created = timezone.now()
            answer_form.save()
            return redirect('/')
    answerForm = AnswerForm()
    return render(request, 'viewAnswers.html', {'question': question,'answerForm': answerForm})


# i dont need this
class AssessmentListView(generic.ListView):
    model = Assessment
    context_object_name = 'assessments'
    paginate_by = 5
    template_name = 'list_view.html'


class AssessmentDetailView(HitCountDetailView):
    model = Assessment
    template_name = 'assessmentDetailView.html'
    context_object_name = 'assessment'
    count_hit = True

    def get_context_data(self, **kwargs):
        myassessment = self.object
        context = super(AssessmentDetailView, self).get_context_data(**kwargs)
        context.update({
            'popular_posts': Assessment.objects.order_by('-hit_count_generic__hits')[:3],
            'similar_objects': myassessment.tags.similar_objects()[:3],
        })
        return context


def taggedAssessemnt(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    assessments = Assessment.objects.filter(tags=tag)

    context = {
        'tag': tag,
        'results': assessments,
    }
    return render(request, 'resultPage.html', context)
