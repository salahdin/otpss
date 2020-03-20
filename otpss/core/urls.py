from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'
urlpatterns = [
                  path('', views.search, name="home_page"),
                  path('list/', views.AssessmentListView.as_view(), name='list'),
                  path('answer/<int:id_>',views.viewAnswers,name = 'view_answers'),
                  path('upload/', views.upload_paper, name="upload"),
                  path('upvote/<int:id_>', views.upvote, name="upvote"),
                  path('downvote/<int:id_>', views.downvote, name="downvote"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
