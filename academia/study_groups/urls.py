from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_groups_list, name='study_groups_list'),
]
