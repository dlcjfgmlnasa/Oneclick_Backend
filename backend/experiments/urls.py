# -*- coding:utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.ExperimentView.as_view(),
        name='add experiments'
    ),
    path(
        'list/',
        views.ExperimentListView().as_view(),
        name='list experiments'
    ),
]
