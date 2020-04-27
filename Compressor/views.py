from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from django.template import RequestContext
from PIL import Image


# Create your views here.
def home_view(request, *args, **kwargs):
    if request.method == 'POST' and request.FILES.get('file', False):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], request.POST['title'])
            return HttpResponseRedirect('/result_view')
        return HttpResponseRedirect('/')
    else:
        form = ImageUploadForm()
        return render(request, 'home.html', {'form': form})


def result_view(request, *args, **kwargs):
    files = {
        'image_source': 'vvv',
        'image_png': 'aaa',
        'image_jpeg': 'bbb'
    }
    v = 4
    return render(request, 'result_view.html', files)


def handle_uploaded_file(f, name):
    with open('files/source/' + name + '.bmp', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
