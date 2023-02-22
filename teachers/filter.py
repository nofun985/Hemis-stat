import django_filters
from .models import *


class ProductFilter(django_filters.FilterSet):
    employmentForm = django_filters.ModelChoiceFilter(
        queryset=EmploymentForm.objects.all(),
        empty_label="Ish o'rni",

    )
    department = django_filters.ModelChoiceFilter(
        queryset=Department.objects.all(),
        empty_label="Kafedra",

    )
    staffPosition = django_filters.ModelChoiceFilter(
        queryset=StaffPosition.objects.all(),
        empty_label="Lavozim",
    )
    class Meta:
        model = Teachers
        fields = ['employmentForm', 'department', 'staffPosition']
