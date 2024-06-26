# Django Admin Panel Customization

## Introduction and Setting up Peripherals?

```bash
django-admin startproject extremeadmin .
python manage.py startapp blog
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

```bash
python manage.py makemigrations
python manage.py migrate
```

Create new blog on admin site


## ModelAdmin class usage and configuration for ORM models

[Visit to site](https://faker.readthedocs.io/en/master/)
```bash
pip install faker
python manage.py shell
```

```python
from blog.models import Blog
from faker import Faker

faker = Faker()

for i in range(350):
    blog = Blog(title=faker.name(), body=faker.paragraph())
    blog.save()
```

```python
from blog.models import Blog
from faker import Faker

faker = Faker()

for i in range(350):
    blog = Blog(title=faker.name(), body=faker.paragraph(), broadcast=False)
    blog.save()
```

## Advanced ModelAdmin options

[Visit to site](https://django-ckeditor.readthedocs.io/en/latest/)
```bash
pip install django-ckeditor
```

## Relational Models in Admin App

```python
from blog.models import Blog, Comment
from faker import Faker

faker = Faker()

for blog in Blog.objects.iterator():
    comments = [Comment(comment=faker.paragraph(), blog=blog) for _ in range(3)]
    Comment.objects.bulk_create(comments)
```

Add three categories

## Manage User Accounts

Different types of user accounts

1. Non staff users -> is_staff = False & is_superuser = False
2. Staff users -> is_staff = True & is_superuser = False
3. Superusers -> is_staff = True & is_superuser = True

Create non staff user. Try logging to admin site as one
Create staff user. Login to admin site as one. Give view permissions to blogs, comments and categories. Edit staff user -> permissions
Create editor group. crud blog and comments, view category. Give to staff user

## Useful 3rd Party Libraries

[Visit to site](https://github.com/mrts/django-admin-list-filter-dropdown?tab=readme-ov-file)
```bash
pip install django-admin-list-filter-dropdown
```

[Visit to site](https://github.com/silentsokolov/django-admin-rangefilter)
```bash
pip install django-admin-rangefilter
```

[Visit to site](https://django-leaflet.readthedocs.io/en/latest/)
```bash
pip install django-leaflet
```

[Visit to site](https://django-geojson.readthedocs.io/en/latest/)
```bash
pip install django-geojson
```

[Visit to site](https://django-import-export.readthedocs.io/en/latest/)
```bash
pip install django-import-export
```

[Visit to site](https://django-jazzmin.readthedocs.io/)
```bash
pip install django-jazzmin
```

# Admin App Security and Optimized Operations

1. Publish under https
2. Not granting superuser privileges to everyone
3. Not giving the ability to delete models, especially those with critical values, to every group and every staff member
4. Keeping superusers limited to maintain control

[Visit to site](https://django-admin-honeypot.readthedocs.io/en/latest/)
```bash
pip install django-admin-honeypot
```

[Visit to site](https://pypi.org/project/django-admin-honeypot-updated-2021/)
```bash
pip install django-admin-honeypot-updated-2021
```

```bash
python manage.py migrate
```

# Extras

[Visit to site](https://pillow.readthedocs.io/en/stable/)
```bash
pip install Pillow
```
