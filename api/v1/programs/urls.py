from django.urls import path, re_path

from . import views

app_name = "api_v1_programs"


urlpatterns = [
    path('programs/', views.programs, name='programs'),
    path('courses/', views.courses, name='courses'),
    re_path(r'^start-courses/(?P<pk>.*)/$', views.start_course, name="start_course"),
]
