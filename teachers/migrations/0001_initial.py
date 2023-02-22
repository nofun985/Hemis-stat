# Generated by Django 4.1.5 on 2023-02-20 05:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegreeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_defense', models.CharField(blank=True, max_length=200, null=True)),
                ('council_number', models.CharField(blank=True, max_length=200, null=True)),
                ('given_by_whom', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_defense', models.DateField(blank=True, null=True)),
                ('number_of_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('confirmed_date', models.DateField(blank=True, null=True)),
                ('account_number', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateField(blank=True, null=True)),
                ('changed', models.DateField(blank=True, null=True)),
                ('academic_degree_file', models.FileField(blank=True, null=True, upload_to='academicDegree/')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicRankData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_defense', models.CharField(blank=True, max_length=200, null=True)),
                ('council_number', models.CharField(blank=True, max_length=200, null=True)),
                ('given_by_whom', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_defense', models.DateField(blank=True, null=True)),
                ('number_of_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('confirmed_date', models.DateField(blank=True, null=True)),
                ('account_number', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateField(blank=True, null=True)),
                ('changed', models.DateField(blank=True, null=True)),
                ('academic_degree_file', models.FileField(blank=True, null=True, upload_to='academicRank/')),
            ],
        ),
        migrations.CreateModel(
            name='Degrees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('department', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('employeeStatus', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('employeeType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('employmentForm', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('employmentStaff', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('faculty', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ranks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StaffPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('staffPosition', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('full_name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('third_name', models.CharField(max_length=50)),
                ('employee_id_number', models.BigIntegerField()),
                ('birth_date', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('year_of_enter', models.CharField(max_length=20)),
                ('contact_number', models.CharField(max_length=100)),
                ('decree_number', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_date', models.CharField(blank=True, max_length=100, null=True)),
                ('decree_date', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_at', models.CharField(blank=True, max_length=100, null=True)),
                ('hash', models.CharField(max_length=100)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('academicDegree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.degrees', to_field='code')),
                ('academicDegreeData', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.academicdegreedata')),
                ('academicRank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.ranks', to_field='code')),
                ('academicRankData', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.academicrankdata')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.department', to_field='code')),
                ('employeeStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.employeestatus', to_field='code')),
                ('employeeType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.employeetype', to_field='code')),
                ('employmentForm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.employmentform', to_field='code')),
                ('employmentStaff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.employmentstaff', to_field='code')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.genders', to_field='code')),
                ('staffPosition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.staffposition', to_field='code')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.faculty', to_field='code'),
        ),
    ]