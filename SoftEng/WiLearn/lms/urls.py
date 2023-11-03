from django.urls import path
from . import views


app_name = 'lms'
urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('inbox/', views.inbox, name='inbox'),
  path('add_course/', views.add_course, name='add_course'),
  path('create_announcement/', views.post_announcements, name='create_announcements'),
  path('profile/', views.profile, name='profile'),
  path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
]