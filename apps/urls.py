
from django.contrib import admin
from django.urls import path, include

from apps.views import HomeTemplateView, FilterView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('filter-data', FilterView.as_view(), name='filter-data'),
]