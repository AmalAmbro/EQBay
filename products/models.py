import uuid
from django.db import models
from ckeditor.fields import RichTextField


class MainCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.IntegerField()
    # creator = models.ForeignKey()
    # updater = models.ForeignKey()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    industry = models.ForeignKey('web.Industry', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Main Categories'

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.IntegerField()
    # creator = models.ForeignKey()
    # updater = models.ForeignKey()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    category = models.ForeignKey('products.MainCategory', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.IntegerField()
    # creator = models.ForeignKey()
    # updater = models.ForeignKey()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.IntegerField()
    # creator = models.ForeignKey()
    # updater = models.ForeignKey()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    main_category = models.ForeignKey('products.MainCategory', on_delete=models.CASCADE)
    category = models.ForeignKey('products.Category', blank=True, null=True, on_delete=models.CASCADE)
    sub_category = models.ForeignKey('products.SubCategory', blank=True, null=True, on_delete=models.CASCADE)
    image = models.FileField(upload_to='product/')
    description = RichTextField()
    features = RichTextField(null=True, blank=True)
    specifications = RichTextField(null=True, blank=True)
    dimensions = RichTextField(null=True, blank=True)
    test_method = RichTextField(null=True, blank=True)
    product_resource = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.IntegerField()
    # creator = models.ForeignKey()
    # updater = models.ForeignKey()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    model_name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Product Variants'

    def __str__(self):
        return str(self.product)
