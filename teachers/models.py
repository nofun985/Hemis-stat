import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genders(models.Model):
    code = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.gender


class Degrees(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ranks(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    code = models.CharField(max_length=20, unique=True)
    faculty = models.CharField(max_length=200)

    def __str__(self):
        return self.faculty


class Department(models.Model):
    code = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=200)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, to_field='code')

    def __str__(self):
        return self.department


class EmploymentForm(models.Model):
    code = models.CharField(max_length=20, unique=True)
    employmentForm = models.CharField(max_length=50)

    def __str__(self):
        return self.employmentForm


class EmployeeType(models.Model):
    code = models.CharField(max_length=20, unique=True)
    employeeType = models.CharField(max_length=50)

    def __str__(self):
        return self.employeeType


class EmployeeStatus(models.Model):
    code = models.CharField(max_length=20, unique=True)
    employeeStatus = models.CharField(max_length=50)

    def __str__(self):
        return self.employeeStatus


class EmploymentStaff(models.Model):
    code = models.CharField(max_length=20, unique=True)
    employmentStaff = models.CharField(max_length=50)

    def __str__(self):
        return self.employmentStaff


class StaffPosition(models.Model):
    code = models.CharField(max_length=20, unique=True)
    staffPosition = models.CharField(max_length=50)

    def __str__(self):
        return self.staffPosition

class AcademicDegreeData(models.Model):
    place_of_defense = models.CharField(max_length=200, null=True, blank=True)
    council_number = models.CharField(max_length=200, null=True, blank=True)
    given_by_whom = models.CharField(max_length=100, null=True, blank=True)
    date_of_defense = models.DateField(null=True, blank=True)
    number_of_degree = models.CharField(max_length=100, null=True, blank=True)
    confirmed_date = models.DateField(null=True, blank=True)
    account_number = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateField(null=True, blank=True)
    changed = models.DateField(null=True, blank=True)
    academic_degree_file = models.FileField(upload_to='academicDegree/', null=True, blank=True)

    def __str__(self):
        return self.place_of_defense


class AcademicRankData(models.Model):
    place_of_defense = models.CharField(max_length=200, null=True, blank=True)
    council_number = models.CharField(max_length=200, null=True, blank=True)
    given_by_whom = models.CharField(max_length=100, null=True, blank=True)
    date_of_defense = models.DateField(null=True, blank=True)
    number_of_degree = models.CharField(max_length=100, null=True, blank=True)
    confirmed_date = models.DateField(null=True, blank=True)
    account_number = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateField(null=True, blank=True)
    changed = models.DateField(null=True, blank=True)
    academic_rank_file = models.FileField(upload_to='academicRank/', null=True, blank=True)

    def __str__(self):
        return self.place_of_defense

class Teachers(models.Model):
    full_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)
    employee_id_number = models.BigIntegerField()
    gender = models.ForeignKey(Genders, on_delete=models.CASCADE, to_field='code')
    birth_date = models.CharField(max_length=100)
    image = models.URLField()
    year_of_enter = models.CharField(max_length=20)
    academicDegree = models.ForeignKey(Degrees, on_delete=models.CASCADE, to_field='code')
    academicRank = models.ForeignKey(Ranks, on_delete=models.CASCADE, to_field='code')
    academicDegreeData = models.ForeignKey(AcademicDegreeData, on_delete=models.CASCADE, related_name='academic_degree_data_name', null=True, blank=True)
    academic_rank_data = models.ForeignKey(AcademicRankData, on_delete=models.CASCADE, related_name='academic_rank_data_name', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, to_field='code')
    employmentForm = models.ForeignKey(EmploymentForm, on_delete=models.CASCADE, to_field='code')
    employmentStaff = models.ForeignKey(EmploymentStaff, on_delete=models.CASCADE, to_field='code')
    staffPosition = models.ForeignKey(StaffPosition, on_delete=models.CASCADE, to_field='code')
    employeeStatus = models.ForeignKey(EmployeeStatus, on_delete=models.CASCADE, to_field='code')
    employeeType = models.ForeignKey(EmployeeType, on_delete=models.CASCADE, to_field='code')
    contact_number = models.CharField(max_length=100)
    decree_number = models.CharField(max_length=100, null=True, blank=True)
    contact_date = models.CharField(max_length=100, null=True, blank=True)
    decree_date = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.CharField(max_length=100, null=True, blank=True)
    hash = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name





