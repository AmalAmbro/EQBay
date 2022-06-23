import json
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from web.models import Industry
from products.models import Category, MainCategory, Product, SubCategory


def index(request):
    industries = Industry.objects.all()
    context ={
        "title":"Industry | Home",
        "industries": industries,
        "category_show":False,
    }
    return render(request, 'industry.html', context=context)


def index_detail(request,industry):
    industries = Industry.objects.all()
    # selected_industry = Industry.objects.filter()
    main_category = MainCategory.objects.filter( industry__name = industry )
    context = {
        "title":"Industry | Home",
        "industries": industries,
        "category_show":True,
        "industry": industry,
        "main_categories": main_category,
    }
    return render(request, 'industry.html',context=context)

def category(request, industry, main_category):
    categories = Category.objects.filter(category__name = main_category)
    context = {
        "title":"Sub-Categories",
        "categories": categories,
        "industry": industry,
        "show_sub_categories":False,
        "main_category": main_category,
    }
    return render(request, 'category.html', context=context)

def category_detail(request, industry, main_category, category):
    categories = Category.objects.filter(category__name = main_category)
    sub_categories = SubCategory.objects.filter(category__name = category)
    context = {
        "title":"Sub-Categories",
        "industry": industry,
        "main_category": main_category,
        "categories": categories,
        "category": category,
        "sub_categories":sub_categories,
        "show_sub_categories":True
    }
    return render(request, 'category.html', context=context)


# def get_products_ajax(request):
#     data = {}
#     if request.method == "POST":
#         sub_category = request.POST['subCat']
#         print(sub_category)
#         try:
#             subject = Product.objects.all()
#         except Exception:
#             data['error_message'] = 'error'
#             return JsonResponse(data)
#         return JsonResponse(list(subject.values('auto_id', 'name')), safe = False) 
#     else:
#         print("outside")

def getproducts(request):
    data = {}
    print("Request came inside")
    if request.method == "GET":
        sub_category_id = request.GET['sub_category']
        print(sub_category_id)
        try:
            selected_subcategory = SubCategory.objects.filter(auto_id = sub_category_id)
            print(selected_subcategory)
            products = Product.objects.filter(sub_category__in = selected_subcategory)
            print(products)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(products.values('auto_id', 'name')), safe = False) 
    else:
        print("outside")
        