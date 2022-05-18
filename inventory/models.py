from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    description = models.CharField(max_length=500, null=True)
    price = models.FloatField(null=True)
    inventory_left = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        inventory = Product.objects.get(id=self.id)
        self.inventory_left = inventory.inventory_left - 1
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]


class Coupon(models.Model):
    name = models.CharField(max_length=250, null=True)
    discount = models.FloatField(null=True)
    times_used = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        coupon = Coupon.objects.get(id=self.id)
        if coupon.times_used is None:
            self.times_used = 1
        else:
            self.times_used = coupon.times_used + 1
        super(Coupon, self).save(*args, **kwargs)

    class Meta:
        ordering = ["discount"]


class Cart(models.Model):
    product = models.ManyToManyField('Product', blank=True)
    coupon = models.ForeignKey(
        'Coupon',
        related_name='coupons',
        on_delete=models.CASCADE,
        null=True
    )
    price = models.FloatField(null=True)
    address = models.CharField(max_length=250, null=True, blank=True)

    def save(self, *args, **kwargs):
        print(self.price)
        super(Cart, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]

