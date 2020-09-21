from django.shortcuts import render, HttpResponseRedirect

from Data_App.models import DataFile
from Data_App.forms import add_file_form


def index(request):
    data = DataFile.objects.all()
    return render(request, 'index.html', {'data':data})


def add_post(request):
    if request.method == 'POST':
        form = add_file_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_post = DataFile.objects.create(
                name = form.get('name'),
                parent = form.get('parent'),
            )
            return HttpResponseRedirect('/')
    else:
        form = add_file_form()
    return render(request, 'add_post_form.html', {'form': form})
