from django.shortcuts import render, redirect
from directory.models import Directory
from .forms import TelephoneForm

# Create your views here.

def homepage(request):
    context = {
        'all_directory':  Directory.objects.all()
    }
    return render(request, 'directory/index.html', context)


def remove(request, id):
    Directory.objects.get(id=id).delete()
    return redirect('/')


def insert(request):
    form = TelephoneForm(request.POST or None, )
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
    return render(request, 'directory/insert.html', context)


def amend(request, id):
    instance = Directory.objects.get(id=id)
    form = TelephoneForm(request.POST or None,
                        request.FILES or None, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
    return render(request, 'directory/insert.html', context)

