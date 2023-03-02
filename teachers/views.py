from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.http import JsonResponse
from teachers.filter import ProductFilter
from teachers.utils import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import FileSystemStorage

from .forms import AcademicRankDataForm
from .models import Teachers


# Create your views here.


def index(request):
    return render(request, 'index.html')


def teacher(request):
    all_teachers = Teachers.objects.all()

    my_filter = ProductFilter(request.GET, queryset=all_teachers, )
    all_teachers = my_filter.qs
    count = all_teachers.count()

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
        "my_filter": my_filter,
    }

    return render(request, 'html/teachers.html', context)


def get_teacher(request):
    search = request.GET.get('search')
    payload = []
    if search:
        teacher_names = Teachers.objects.filter(full_name__icontains=search)
        for t_name in teacher_names:
            payload.append(t_name.full_name)

    return JsonResponse({
        'status': True,
        'data': payload,
    })


def teacher_info(request, id):
    teacher_info: Teachers = Teachers.objects.get(id=id)
    context = {
        "teacher_data": teacher_info
    }

    return render(request, 'html/teacherInfo.html', context)


# def teacher_add(request, uuid):
#     teacher_add_info = get_object_or_404(Teachers, uuid=uuid)
#     academic_rank_data = teacher_add_info.academicrankdata.first()
#     # academic_rank_data_list = list(academic_rank_data)
#
#     if request.method == 'POST':
#         form = AcademicRankDataForm(request.POST, request.FILES, instance=academic_rank_data)
#         if form.is_valid():
#             form.save()
#             # Redirect to the teacher detail page after updating the academic rank data.
#             return redirect('teacher_info', uuid=uuid)
#     else:
#         form = AcademicRankDataForm(instance=academic_rank_data)
#
#     context = {
#         'form': form,
#         'teacher_add_info': teacher_add_info,
#         # 'academic_rank_data_list': academic_rank_data_list
#     }
#     return render(request, 'html/teacherAdd.html', context)

def teacher_add(request, id):
    teacher_add = Teachers.objects.get(id=id)

    if request.method == 'POST':
        place_of_defense = request.POST.get('place_of_defense')
        council_number = request.POST.get('council_number')
        given_by_whom = request.POST.get('given_by_whom')
        date_of_defense = request.POST.get('date_of_defense')
        number_of_degree = request.POST.get('number_of_degree')
        confirmed_date = request.POST.get('confirmed_date')
        account_number = request.POST.get('account_number')
        created = request.POST.get('created')
        changed = request.POST.get('changed')
        academic_rank_file = request.FILES.get('academic_rank_file')

        # Save the uploaded file to a temporary location
        fs = FileSystemStorage()
        filename = fs.save(academic_rank_file.name, academic_rank_file)
        file_path = fs.path(filename)

        academic_rank_data = AcademicRankData.objects.create(
            place_of_defense=place_of_defense,
            council_number=council_number,
            given_by_whom=given_by_whom,
            date_of_defense=date_of_defense,
            number_of_degree=number_of_degree,
            confirmed_date=confirmed_date,
            account_number=account_number,
            created=created,
            changed=changed,
            academic_rank_file=file_path,
        )

        academic_rank_data.academic_rank_data_name.set([teacher_add])
        return redirect('teacher_info', id=id)

    context = {
        'teacher_add': teacher_add,
    }
    return render(request, 'html/teacherAdd.html', context)


def teacher_data(request):
    saveData()
    saveFacultet()
    saveDepartment()
    saveTeacher()
    return HttpResponse("Data written to database")


