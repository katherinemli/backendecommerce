# Generated by Django 3.2.13 on 2022-05-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_alter_cart_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='times_used',
            field=models.IntegerField(null=True),
        ),
    ]
