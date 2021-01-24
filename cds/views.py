from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import upload
from django.conf import settings
from detect.detect import detechImage
from django.core.files.storage import FileSystemStorage
from django.conf import settings
basedir = settings.BASE_DIR
import os
def home(request):
    return render(request, 'home.html');

def analysis(request):
    myfile = request.FILES['image']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    a = detechImage("F:/CDS"+uploaded_file_url)
    context = {
        'note':a
    }
    return render(request, 'home.html',context);
