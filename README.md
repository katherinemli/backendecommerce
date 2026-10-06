# E-commerce API (Django REST)

**[Français](#français) · [English](#english)**

---

## Français

Backend d'une petite boutique en ligne : catalogue de produits avec inventaire, coupons de réduction et paniers d'achat. Associé à [frontecommerce](https://github.com/katherinemli/frontecommerce).

### Points forts
- Viewsets et serializers **Django REST Framework** pour les produits, les coupons et les paniers
- L'inventaire diminue automatiquement quand un produit est vendu; les coupons comptent combien de fois ils ont été utilisés
- Script d'amorçage pour charger des données d'exemple
- Déployé sur Heroku avec Gunicorn + PostgreSQL (SQLite en développement local)

### Technologies
Python · Django 3.2 · Django REST Framework · PostgreSQL · Gunicorn · Heroku

### Exécution locale
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## English

Backend for a small online store: product catalog with inventory, discount coupons and shopping carts. Paired with [frontecommerce](https://github.com/katherinemli/frontecommerce).

### Highlights
- **Django REST Framework** viewsets and serializers for products, coupons and carts
- Inventory decreases automatically when a product is sold; coupons track how many times they were used
- Seed script to load sample data
- Deployed on Heroku with Gunicorn + PostgreSQL (SQLite for local dev)

### Stack
Python · Django 3.2 · Django REST Framework · PostgreSQL · Gunicorn · Heroku

### Run locally
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---
Katherine Liberona Irarrázabal · [github.com/katherinemli](https://github.com/katherinemli)
