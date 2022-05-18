import csv
from inventory.models import Product

def run():
    file = open('')
    read_file = csv.reader(file)

    Product.objects.all().delete()
    for product in read_file:
        Product.objects.create(
            name=product[0],
            description=product[0],
            price=product[0],
            inventory_left=product[0],
        )
