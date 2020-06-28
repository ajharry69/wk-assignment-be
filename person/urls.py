from django.urls import re_path

from . import views

app_name = 'person'
urlpatterns = [
    re_path("^", views.PeopleView.as_view(), ),
]
