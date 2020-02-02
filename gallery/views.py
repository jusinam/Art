from django.shortcuts import render
from .models import Image


# Create your views here.
def art(request):
    art_images = Image.objects.all()

    return render(request,'index.html',{'art_images':art_images})