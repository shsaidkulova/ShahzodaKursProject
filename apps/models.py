from django.db import models
from django.db.models import Model, CharField, TextChoices, DateField, IntegerField, TimeField


class Course(Model):
    class ProgramType(TextChoices):
        GRADUATE = "graduate" ,  "Graduate"
        UNDERGRADUATE =  "undergraduate" ,  "Undergraduate"
        CONTINUING =  "continuing" ,  "Continuing"
        COMMUNITY_MUSIC =  "community_music" ,  "CommunityMusic"
    class SessionType(TextChoices):
        FALL = "fall" ,  "Fall"
        SPRING =  "spring" ,  "Spring"
        SUMMER =  "summer" ,  "Summer"
    class WeekDays(TextChoices):
        M = "m" ,  "M"
        TU =  "tu" ,  "Tu"
        W =  "w" ,  "W"
        TH =  "th" ,  "Th"
        F =  "f" ,  "F"
        S =  "s" ,  "S"
    class Season(TextChoices):
        SPRING = "spring" ,  "Spring"
        SUMMER =  "summer" ,  "Summer"
        FALL =  "fall" ,  "Fall"
    level = IntegerField(default=1)
    program = CharField(max_length=255 , choices=ProgramType.choices)
    session = CharField(max_length=255 , choices=SessionType.choices)
    year = IntegerField()
    hour = IntegerField(default=3)
    title = CharField(max_length=255)
    instructor = CharField(max_length=255)
    campus = CharField(max_length=255 , default="Webster Univ Tashkent Uzbekistan")
    room = CharField(max_length=255)
    days = CharField(max_length=255 , choices=WeekDays.choices , default=WeekDays.M)
    start_time = TimeField()
    end_time = TimeField()
    start_semester = DateField()
    end_semester = DateField()
    tm = CharField(max_length=50 , choices=Season.choices)


# python manage.py makemigrations
# python manage.py migrate



