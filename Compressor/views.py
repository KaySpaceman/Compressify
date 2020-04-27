from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ImageUploadForm
from PIL import Image


# Create your views here.
def home_view(request, *args, **kwargs):
    if request.method == 'POST' and request.FILES.get('file', False):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], request.POST['title'])
            return HttpResponseRedirect('/result_view/?title=' + request.POST['title'])
        return HttpResponseRedirect('/')
    else:
        form = ImageUploadForm()
        return render(request, 'home.html', {'form': form})


def result_view(request, *args, **kwargs):
    name = request.GET['title']
    source = Image.open('static/source/' + name + '.bmp')

    with source:
        source.save('static/png/' + name + '.png')

    with source:
        source.save('static/jpeg/' + name + '.jpeg')

    files = {
        'image_source': 'source/' + name + '.bmp',
        'image_png': 'png/' + name + '.png',
        'image_jpeg': 'jpeg/' + name + '.jpeg'
    }

    return render(request, 'result_view.html', files)


def handle_uploaded_file(f, name):
    with open('static/source/' + name + '.bmp', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
