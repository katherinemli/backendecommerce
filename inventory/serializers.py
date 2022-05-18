from rest_framework import serializers
from .models import Product, Cart, Coupon


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = '__all__'
