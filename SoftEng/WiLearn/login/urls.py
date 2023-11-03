from django.urls import path
from . import views


app_name = 'login'
urlpatterns = [
  path('', views.main, name='main'),
  path('courses/', views.courses, name='courses'),
]