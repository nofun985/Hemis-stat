from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import JsonResponse
from teachers.filter import ProductFilter
from teachers.utils import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Teachers


# Create your views here.


def index(request):
    return render(request, 'index.html')


def teacher(request):
    all_teachers = Teachers.objects.all()

    count = all_teachers.count()
    my_filter = ProductFilter(request.GET, queryset=all_teachers, )
    all_teachers = my_filter.qs

    items_per_page = 20
    paginator = Paginator(all_teachers, items_per_page)

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, display the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range, display the last page of results
        page_obj = paginator.page(paginator.num_pages)

    # Calculate the range of pages to display
    num_pages = paginator.num_pages
    if num_pages <= 7:
        page_range = range(1, num_pages + 1)
    elif page_obj.number <= 4:
        page_range = set(range(1, 6)) | {num_pages}
    elif page_obj.number >= num_pages - 3:
        page_range = {1} | set(range(num_pages - 4, num_pages + 1))
    else:
        page_range = {1} | set(range(page_obj.number - 2, page_obj.number + 3)) | {num_pages}

    # Calculate the starting and ending index of the items being displayed
    start_index = (page_obj.number - 1) * items_per_page + 1
    end_index = min(page_obj.number * items_per_page, count)

    # Create a list of tuples containing the index and item data
    items_with_index = [(i + start_index, item) for i, item in enumerate(page_obj)]

    context = {
        "page_obj": page_obj,
        "page_range": page_range,
        "count": count,
        "start_index": start_index,
        "end_index": end_index,
        "items_with_index": items_with_index,
        "my_filter": my_filter
    }

    return render(request, 'html/teachers.html', context)


def get_teacher(request):
    search = request.GET.get('search')
    payload = []
    if search:
        teacher_names = Teachers.objects.filter(full_name__startswith=search)
        for t_name in teacher_names:
            payload.append({
                'full_name': t_name.full_name
            })

    return JsonResponse({
        'status': True,
        'full_name': payload,
    })

def teacher_info(request, uuid):
    teacher_info = Teachers.objects.get(uuid=uuid)
    context = {
        "teacher_data": teacher_info
    }

    return render(request, 'html/teacherInfo.html', context)


def teacher_add(request):
    return render(request, 'html/teacherAdd.html')


def teacher_data(request):
    saveData()
    saveFacultet()
    saveDepartment()
    saveTeacher()
    return HttpResponse("Data written to database")


def merge_teachers(request):
    Merge()
    return HttpResponse("Data merge")
