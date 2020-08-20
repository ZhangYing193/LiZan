from django.urls import path, re_path

from . import views

urlpatterns = [
    path('users/', views.UserView.as_view()),
    re_path('usernames/(?P<username>\w{5,20})/count/', views.UsernameCountView.as_view()),
]
