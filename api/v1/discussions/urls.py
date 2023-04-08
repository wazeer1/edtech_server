from django.urls import path, re_path

from . import views

app_name = "api_v1_discussions"


urlpatterns = [
    re_path(r'^questions/$', views.questions, name="question"),
    re_path(r'^add-question/$', views.add_questions, name="add_questions"),
]
