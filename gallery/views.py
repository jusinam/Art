from django.shortcuts import render
from .models import Image,Category,Location


# Create your views here.
def art(request):
    art_images = Image.objects.all()
    categories = Category.objects.all()
    location_results = Location.objects.all()

    return render(request,'index.html',{'art_images':art_images,'categories':categories,'location_results':location_results})

def search_results(request):
    
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'index.html',{"message":message,"art_images": searched_image})

    else:
        message = "No Image for the searched term. Search again."
        return render(request, 'index.html',{"message":message})

def get_category(request,category):
    categories = Category.objects.all()
    location_results = Location.objects.all()
    category_result = Image.objects.filter(image_category__category_name = category)

    return render(request,'index.html',{'art_images':category_result,'categories':categories,'location_results':location_results})

def get_location(request,location):
    categories = Category.objects.all()
    location_results = Location.objects.all()
    location_result = Image.objects.filter(image_location__location_name= location)

    return render(request,'index.html',{'art_images':location_result,'categories':categories,'location_results':location_results})

