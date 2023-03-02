from django import forms
from .models import AcademicRankData


class AcademicRankDataForm(forms.ModelForm):
    class Meta:
        model = AcademicRankData
        fields = ['place_of_defense', 'council_number', 'given_by_whom', 'date_of_defense', 'number_of_degree', 'confirmed_date', 'account_number', 'created', 'changed', 'academic_rank_file']
        widgets = {
            'date_of_defense': forms.DateInput(attrs={'type': 'date'}),
            'confirmed_date': forms.DateInput(attrs={'type': 'date'}),
            'created': forms.DateInput(attrs={'type': 'date'}),
            'changed': forms.DateInput(attrs={'type': 'date'}),
        }