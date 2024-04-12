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
