from django.urls import path,include
from.import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('', views.frontpage, name="frontpage"),
    path('profile/<int:id_>', views.profileDetailView, name="profileDetailView"),
]