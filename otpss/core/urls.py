from django.urls import path
from .import views

app_name = 'core'
urlpatterns = [
    path('home/',views.search,name = "home page")
    ]