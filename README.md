# E-commerce API (Django REST)

Backend for a small online store: product catalog with inventory, discount coupons and shopping carts. Paired with [frontecommerce](https://github.com/katherinemli/frontecommerce).

## Highlights
- **Django REST Framework** viewsets and serializers for products, coupons and carts
- Inventory decreases automatically when a product is sold; coupons track how many times they were used
- Seed script to load sample data
- Deployed on Heroku with Gunicorn + PostgreSQL (SQLite for local dev)

## Stack
Python · Django 3.2 · Django REST Framework · PostgreSQL · Gunicorn · Heroku

## Run locally
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---
Katherine Liberona Irarrázabal · [github.com/katherinemli](https://github.com/katherinemli)
