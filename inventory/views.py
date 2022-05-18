from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Cart, Coupon
from .serializers import ProductSerializer, CartSerializer, CouponSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
