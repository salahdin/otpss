from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'
urlpatterns = [
    path('', views.homepage, name="home_page"),
    path('search/', views.AssessmentSearchView.as_view(), name="search"),
    path('list/', views.AssessmentListView.as_view(), name='list'),
    path('answer/<int:id_>', views.viewAnswers, name='view_answers'),
    path('upload/', views.upload_paper, name="upload"),
    path('upvote/<int:id_>', views.upvote, name="upvote"),
    path('downvote/<int:id_>', views.downvote, name="downvote"),
    path('assessment/<int:pk>', views.AssessmentDetailView.as_view(), name="assessment_detail_view"),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('tagged/<slug:slug>', views.taggedAssessemnt, name='tagged'),
    ]

"""if settings.DEBUG:
    #urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"""
