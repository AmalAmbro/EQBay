from django.contrib import admin

from products.models import Category, MainCategory, Product, ProductVariant, SubCategory


class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','industry']
    readonly_fields= ['date_added','date_updated']


admin.site.register(MainCategory, MainCategoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','category']
    readonly_fields= ['date_added','date_updated']


admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','category']
    readonly_fields= ['date_added','date_updated']


admin.site.register(SubCategory,SubCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    readonly_fields= ['date_added','date_updated']


admin.site.register(Product, ProductAdmin)

class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['id','product', 'model_name']
    readonly_fields= ['date_added','date_updated']


admin.site.register(ProductVariant, ProductVariantAdmin)
