from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('teacher/', teacher, name='teacher'),
    path('teacher/add/', teacher_add, name='teacher_add'),
    path('teacher/info/<str:uuid>/', teacher_info, name='teacher_info'),
    path('data/', teacher_data, name='teacher_data'),
    path('merge/', merge_teachers, name='merge'),
    path('get-teacher/', get_teacher, name='search')
]