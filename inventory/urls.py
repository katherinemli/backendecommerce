from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet, CouponViewSet


router = DefaultRouter()
router.register('product', ProductViewSet)
router.register('cart', CartViewSet)
router.register('coupon', CouponViewSet)

urlpatterns = [
    path('', include(router.urls))
]