from django import forms

from Data_App.models import DataFile


class add_file_form (forms.Form):
    name = forms.CharField(max_length=20)
    parent = forms.ModelChoiceField(queryset=DataFile.objects.all(), blank=True, required=False)
