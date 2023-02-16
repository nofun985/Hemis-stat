from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('teacher/', teacher, name='teacher'),
    path('teacher/add/', teacher_add, name='teacher_add'),
    path('teacher/info/', teacher_info, name='teacher_info')
]