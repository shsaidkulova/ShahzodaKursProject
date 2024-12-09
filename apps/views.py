from logging import Filter

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView

from apps.forms import CourseModelForm
from apps.models import Course


class HomeTemplateView(TemplateView):
    template_name = 'apps/filter.html'

class FilterView(ListView):
    queryset = Course.objects.order_by('level')
    template_name = 'apps/home.html'
    context_object_name = 'courses'

    def get_queryset(self):
        query = super().get_queryset()
        program = self.request.GET.get('program')
        session = self.request.GET.get('session')
        year = self.request.GET.get('year')
        return query.filter(program=program , session=session, year=year)





