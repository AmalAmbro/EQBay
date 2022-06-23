from django.urls import path
from web.views import category_detail, getproducts, index, index_detail, category


app_name = 'web'

urlpatterns = [
    path('', index, name='index'),
    path('<str:industry>/', index_detail, name='index_detail'),
    path('<str:industry>/<str:main_category>/', category, name='category'),
    path('<str:industry>/<str:main_category>/<str:category>/', category_detail, name='category_detail'),
    path('get_products_ajax/$', getproducts, name='get_product'),
]