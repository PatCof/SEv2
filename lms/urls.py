from django.urls import path
from . import views


app_name = 'lms'
urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('inbox/', views.inbox, name='inbox'),
  path('add_course/', views.add_course, name='add_course'),
  path('create_announcement/', views.post_announcements, name='create_announcements'),
  path('edit_announcement/<int:a_id>', views.edit_announcements, name='edit_announcements'),
  path('profile/', views.profile, name='profile'),
  path('course/<int:id>/', views.inside_module, name='module'),
  path('course/<int:id>/create_module/<int:mod_num>/', views.create_module, name='create_module'),
  path('course/<int:id>/create_assignment/', views.create_assign, name='create_assign'),
  path('course/<int:id>/view_assignment/<int:assign_num>', views.edit_assign, name='edit_assign'),
  path('course/edit_course/<int:id>/', views.edit_course, name='edit_course'),
  path('course/<int:id>/view_module/<int:mod_num>/<int:mod_page>', views.modify_module, name='modify_module'),
]