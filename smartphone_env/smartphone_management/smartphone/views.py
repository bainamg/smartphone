from django.shortcuts import render
from django.http import HttpResponse
from . models import Brand, PhoneModels
from . import views

# Create your views here.
def index(request):
    return render(request,'blank_layout.html')

def create_brands(request):
    if request.POST:
        brand_obj=Brand(Name=request.POST.get('brand_name'), Image=request.FILES.get('filename'))
        brand_obj.save()
        print("-- Brand", brand_obj.Name, "Created!!")
    return render(request,'create_band.html')

def create_models(request):
    if request.POST:
        print("----- ", request.POST, request.FILES)
        brand_obj=Brand.objects.get(id=request.POST.get('selected_brand'))
        model_obj=PhoneModels(brand=brand_obj, name=request.POST.get("model"),price=request.POST.get("price"),release_year=request.POST.get("year"),Image=request.FILES.get("modelfilename"))
        model_obj.save()
    brands=Brand.objects.all();
    print(brands)
    return render(request,'create_models.html', {'brands': brands})
def update_modes(request):
    return render(request,'update_models.html')
def list_brands(request):
    brand_obj=Brand.objects.all()
    return render(request,'list_brand.html',{'brands':brand_obj})
def list_models(request):
    return render(request,'sell.html')
