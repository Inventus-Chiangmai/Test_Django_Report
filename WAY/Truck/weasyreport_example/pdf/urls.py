
from django.contrib import admin
from django.urls import path, include

from .views import GeneratePDF

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('generate/pdf/',GeneratePDF.as_view()),
]