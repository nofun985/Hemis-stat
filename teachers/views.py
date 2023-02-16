from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def teacher(request):
    return render(request, 'html/teachers.html')


def teacher_add(request):
    return render(request, 'html/teacherAdd.html')


def teacher_info(request):
    return render(request, 'html/teacherInfo.html')
