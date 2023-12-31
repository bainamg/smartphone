from django.shortcuts import render
from django.http import HttpResponse
from . models import Brand, PhoneModels, Transactions
from django.contrib.auth.models import User
from . import views
import traceback   
from django.db.models import Max,Sum

# Create your views here.
def index(request):
    return render(request,'blank_layout.html')

def create_brands(request):
    try:
        if request.POST:
            brand_obj=Brand(Name=request.POST.get('brand_name'), Image=request.FILES.get('filename'))
            brand_obj.save()
            print("-- Brand", brand_obj.Name, "Created!!")
        return render(request,'create_band.html')
    except:
        return render(request,'exception.html')

    

def create_models(request):
    try:
        if request.POST:
            brand_obj=Brand.objects.get(id=request.POST.get('selected_brand'))
            model_obj=PhoneModels(brand=brand_obj, name=request.POST.get("model"),price=request.POST.get("price"),release_year=request.POST.get("year"),added_quantities=request.POST.get("added_quantities"),Image=request.FILES.get('modelfilename'))
            model_obj.save()
        return render(request,'create_models.html', {'brands': Brand.objects.all()})
    except Exception as e:
        message = traceback.format_exc()
        print(message)
        return render(request,'exception.html')
    
def update_models(request):
    if request.POST:
        brand_obj=Brand.objects.get(id=request.POST.get('selected_brand'))
        model_obj=PhoneModels.objects.get(id=request.POST.get('selected_model'))
        model_obj=PhoneModels(price=request.POST.get("price"),available_quatities=request.POST.get("available_quatities"))
        model_obj.save()
    return render(request,'update_models.html',{'brands': Brand.objects.all(),'models': PhoneModels.objects.all()})

def list_brands(request):
    brand_obj_list=Brand.objects.all()
    return render(request,'list_brand.html',{'brands':brand_obj_list})

def list_brand_models(request, brand_id):
    model_obj=PhoneModels.objects.filter(brand=brand_id)
    return render(request, 'list_brand_models.html', {"models":model_obj})

def sell_model(request,model_id):
    model_obj=PhoneModels.objects.get(id=model_id)
    return render(request,'sell_model.html',{"model":model_obj})

def final(request, model_id):
    try:
        model_obj=PhoneModels.objects.get(id=model_id)

        if request.POST:
            user_obj = User.objects.get(id=1)
            transaction_obj=Transactions(Transaction_type=request.POST.get('transaction_mode'), Model=model_obj, User=user_obj, Amount=model_obj.price) 
            transaction_obj.save()

            model_obj.item_sold=model_obj.item_sold+1
            quantity=model_obj.added_quantities-1
            if quantity<0:
                model_obj.is_available=False
                return render(request,'error.html')

            model_obj.save()
    
        
        return render(request,'final.html')
    except Exception as e:
        message = traceback.format_exc()
        print(message)
        return render(request,'exception.html')
    
def print_statics(request):
    print("---- in ")
    try:

        top_brand=PhoneModels.objects.values('brand_id').annotate(sum_item_sold=Sum('item_sold')).order_by('-sum_item_sold')[0]['sum_item_sold']
        brand_item_sold=PhoneModels.objects.values('brand_id').annotate(sum_item_sold=Sum('item_sold'))
        top_brands=[each_brand for each_brand in brand_item_sold if each_brand['sum_item_sold']==10]
        print(top_brands)
        
        brand_names=[]
        for b in top_brands:
            brand_obj=Brand.objects.filter(id=b['brand_id'])
            


            for name in brand_obj:
                brand_names.append(name.Name)
        
        max_itemsold=PhoneModels.objects.filter().aggregate(Max('item_sold'))['item_sold__max']
        top_selling_models=PhoneModels.objects.filter(item_sold=max_itemsold).order_by('name')
        #print(top_selling_models)
        return render(request,'static.html', {'model': top_selling_models,'b_names':brand_names})
    except Exception as e:
        message = traceback.format_exc()
        print(message)
        return render(request,'exception.html')
    




