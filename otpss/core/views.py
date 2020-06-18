import operator

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from django.views.generic import ListView, DetailView
from hitcount.views import HitCountDetailView
from taggit.models import Tag

from .convert import *
from .forms import *
from .idquestion import findQuestions
from .models import *


def homepage(request):
    """
    :function: direct users to landing page
    :param request:
    :return:
    """
    context = {'popular_posts': Assessment.objects.all().order_by('uploadDate')[:3]}
    return render(request, "index.html", context)


# class based view of the search tab
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

            # return a distinct queryset by ordering by id
            result = result.annotate(rank=SearchRank(vectors, query)).order_by('id', '-rank').distinct('id')
            # sort again using rank
            finalQueryset = sorted(result, key=operator.attrgetter('rank'), reverse=False)

            return finalQueryset[:100]

@login_required(login_url='/')
def upvote(request, id_):
    """
    after clicking the upvote button answer.votes is incremented (will be used for sorting results) and a new vote
    object is created :type id_: int
    """
    answer_ = get_object_or_404(Answer, pk=id_)
    try:
        UserVote.objects.get_or_create(user=request.user, answer=answer_, vote_type='U')
        answer_.votes += 1
        answer_.save()
    except:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/')
def downvote(request, id_):
    """
    after clicking the down button answer.votes is decremented (will be used for sorting results) and a new vote
    object is created :type id_: int
    """
    answer_ = get_object_or_404(Answer, pk=id_)
    try:
        UserVote.objects.create(user=request.user, answer=answer_, vote_type='D')
        answer_.votes -= 1
        answer_.save()
    except:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/')
def upload_paper(request):
    common_tags = Assessment.tags.most_common()[:4]
    # if user is not logged in redirect to landing page
    if request.user == None:
        return redirect('/')

    if request.method == 'POST':
        # make form instances with user post request as arguments
        assessmentForm = AssessmentForm(request.POST)
        imageformset = ImageForm(request.POST, request.FILES)
        documentForm = AssessmentFileForm(request.FILES)

        if assessmentForm.is_valid() and imageformset.is_valid():
            assessment_form = assessmentForm.save(commit=False)
            # change to upper case and remove white space
            course_Code = assessment_form.courseCode.replace(" ", "").upper()
            assessment_form.courseCode = course_Code
            assessment_form.user = request.user
            assessment_form.save()
            assessmentForm.save_m2m()

            # using ocr to convert multiple images to text
            text = ""
            for image in request.FILES.getlist('image'):
                photo = AssessmentImage(assessment=assessment_form, image=image)
                text += convert_img_to_txt(image)
                photo.save()

            # create question objects
            for i in findQuestions(text):
                Question.objects.create(assessment=assessment_form, content=i)

            if documentForm.is_valid():
                pass
            messages.success(request, 'successfully uploaded!')
            return HttpResponseRedirect("/")
    else:
        assessmentForm = AssessmentForm()
        imageformset = ImageForm()
        documentForm = AssessmentFileForm()
    context = {
        'form': assessmentForm,
        'documentForm': documentForm,
        'ImageForm': imageformset,
        'common_tags': common_tags
    }

    return render(request, 'upload.html', context)


def viewAnswers(request, id_):
    """
    :param request:
    :param id_:
    :return: python dict of objects with class name as key
    """
    # get question
    question = get_object_or_404(Question, id=id_)
    # get all answers associated with question ordered by the number of votes
    answers = question.questionAnswer.all().order_by('-votes')
    if request.method == 'POST':
        answerForm = AnswerForm(request.POST)
        if answerForm.is_valid():
            # create answer object
            answer_form = answerForm.save(commit=False)
            answer_form.question = question
            answer_form.user = request.user
            answer_form.created = timezone.now()
            answer_form.save()
            messages.success(request, 'question answered')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    answerForm = AnswerForm()
    context = {
        'question': question,
        'answerForm': answerForm,
        'answers': answers
    }
    return render(request, 'viewAnswers.html', context)


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
    """
    :function returns assessment objects that are related to the tag
    :param request:
    :param slug:
    :return: assessment objects
    """
    tag = get_object_or_404(Tag, slug=slug)
    assessments = Assessment.objects.filter(tags=tag)

    context = {
        'tag': tag,
        'results': assessments,
    }
    return render(request, 'resultPage.html', context)
