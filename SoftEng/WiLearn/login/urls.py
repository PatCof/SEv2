from django.urls import path
from . import views
from .views import PassResetView, PassResetDoneView, PassResetConfirmView, PassResetCompleteView


app_name = 'login'
urlpatterns = [
  path('', views.main, name='main'),
  path('courses/', views.courses, name='courses'),
  path('logout/', views.custom_logout, name='logout'),

  path('password_reset/', PassResetView.as_view(),name='password_reset'),
  path('password_reset/done/', PassResetDoneView.as_view(),name='password_reset_done'),
  path('reset/<uidb64>/<token>/', PassResetConfirmView.as_view(),name='password_reset_confirm'),
  path('reset/done/', PassResetCompleteView.as_view(),name='password_reset_complete'),

]

