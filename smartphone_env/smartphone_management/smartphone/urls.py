"""
URL configuration for smartphone_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_brand/',views.create_brands,name='CreateBrands'),
    path('create_models/',views.create_models,name='CreateModels'),
    path('update_models/',views.update_models,name='UpdateModels'),
    path('list_brands/',views.list_brands,name='ListBrands'),
    path('list_models/',views.list_models,name='ListModels'),
    path('list_brand_models/<int:brand_id>',views.list_brand_models,name='ListBrandModels'),
    path('',views.index,name='index')
]
