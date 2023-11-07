from django.shortcuts import render
from django.http import HttpResponse
from . models import Brand, PhoneModels, Transactions
from django.contrib.auth.models import User
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
        model_obj=PhoneModels(brand=brand_obj, name=request.POST.get("model"),price=request.POST.get("price"),release_year=request.POST.get("year"),Image=request.FILES.get('modelfilename'))
        model_obj.save()
    brands=Brand.objects.all();
    print(brands)
    return render(request,'create_models.html', {'brands': brands})

def update_models(request):
    return render(request,'update_models.html')

def list_brands(request):
    brand_obj_list=Brand.objects.all()
    return render(request,'list_brand.html',{'brands':brand_obj_list})

def list_brand_models(request, brand_id):
    model_obj=PhoneModels.objects.filter(brand=brand_id)
    return render(request, 'list_brand_models.html', {"models":model_obj})

def sell_model(request,model_id):
    print("==========", request.POST)
    model_obj=PhoneModels.objects.get(id=model_id)
    if request.POST:
        user_obj = User.objects.get(id=1)
        transaction_obj=Transactions(Transaction_type=request.POST.get('transaction_mode'), Model=model_obj, User=user_obj, Amount=model_obj.price) 
        transaction_obj.save()

        
        model_count=model_obj.objects.value('count')
        print("------ model count:", model_count)
        reduce_count=PhoneModels(count=model_count)
        reduce_count.save()

    return render(request,'sell_model.html',{"model":model_obj})

def final(request):
    return render(request,'final.html')