from rest_framework import serializers

from carService.models import Category, Brand
from carService.models.Product import Product
from carService.models.ProductCategory import ProductCategory
from carService.models.ProductImage import ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 2


class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=False, allow_null=False, required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        try:
            brand = Brand()
            brand.name = validated_data.get('name')
            brand.save()
            return brand
        except Exception:

            raise serializers.ValidationError("lütfen tekrar deneyiniz")


class BrandPageSerializer(serializers.Serializer):
    data = BrandSerializer(many=True)
    recordsTotal = serializers.IntegerField()
    recordsFiltered = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ProductSerializerr(serializers.Serializer):
    barcodeNumber = serializers.CharField()
    name = serializers.CharField()
    quantity = serializers.IntegerField()
    netPrice = serializers.DecimalField(max_digits=10, decimal_places=2)
    # productImage = serializers.ImageField()
    isOpen = serializers.BooleanField()
    taxRate = serializers.DecimalField(max_digits=10, decimal_places=2)
    # totalProduct = serializers.DecimalField(max_digits=5, decimal_places=2)
    # categories = serializers.ListField(child=serializers.IntegerField())
    categories = serializers.CharField()
    # images = serializers.ListField(child=serializers.CharField())
    productImage = serializers.CharField(allow_blank=True, allow_null=True)
    shelf = serializers.CharField(allow_null=True, allow_blank=True)
    brand = serializers.CharField()
    purchasePrice = serializers.DecimalField(max_digits=10, decimal_places=2)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        try:
            product = Product()
            product.name = validated_data.get('name')
            product.barcodeNumber = validated_data.get('barcodeNumber')
            product.isOpen = validated_data.get('isOpen')
            product.quantity = validated_data.get('quantity')
            product.taxRate = validated_data.get('taxRate')
            product.netPrice = validated_data.get('netPrice')
            product.shelf = validated_data.get('shelf')
            product.purchasePrice = validated_data.get('purchasePrice')
            product.totalProduct = validated_data.get('netPrice') + (
                    validated_data.get('netPrice') * validated_data.get('taxRate') / 100)

            if validated_data.get('productImage') is not None or validated_data.get('productImage') != '':
                product.productImage = validated_data.get('productImage')
            product.brand = Brand.objects.get(pk=int(validated_data.get('brand')))
            product.save()

            '''productImage = ProductImage()
            productImage.product = product
            productImage.image = validated_data.get('productImage')
            productImage.save()'''

            category = Category.objects.get(pk=int(validated_data.get('categories')))
            productCategory = ProductCategory()
            productCategory.product = product
            productCategory.category = category
            productCategory.save()
            '''for x in validated_data.get('categories'):
                category = Category.objects.get(pk=x)
                productCategory = ProductCategory()
                productCategory.product = product
                productCategory.category = category
                productCategory.save()
'''
            '''for x in validated_data.get('images'):
                productImage = ProductImage()
                productImage.product = product
                productImage.image = x
                productImage.save()'''

            return product

        except Exception:

            raise serializers.ValidationError("lütfen tekrar deneyiniz")
