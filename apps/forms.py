from django.forms import ModelForm

from apps.models import Course


class CourseModelForm(ModelForm):
    class Meta:
        model = Course
        fields = 'program' , 'session' , 'year'