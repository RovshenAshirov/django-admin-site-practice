from django.contrib import admin
from blog.models import Blog

admin.site.site_title = 'Extreme Title'
admin.site.site_header = 'Extreme Admin Portal'  # It also appears on Login Page
admin.site.index_title = 'Welcome to Extreme Admin Portal'

admin.site.register(Blog)
