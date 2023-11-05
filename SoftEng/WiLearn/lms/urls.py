from django.urls import path
from . import views


app_name = 'lms'
urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('inbox/', views.inbox, name='inbox'),
  path('add_course/', views.add_course, name='add_course'),
  path('create_announcement/', views.post_announcements, name='create_announcements'),
  path('profile/', views.profile, name='profile'),
  path('course/<int:id>/', views.inside_module, name='module'),
  path('course/<int:id>/create_module/<int:mod_num>/', views.create_module, name='create_module'),
]