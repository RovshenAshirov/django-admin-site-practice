from django.contrib import admin
from django.utils import timezone

from blog.models import Blog

admin.site.site_title = 'Extreme Title'
admin.site.site_header = 'Extreme Admin Portal'  # It also appears on Login Page
admin.site.index_title = 'Welcome to Extreme Admin Portal'


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'broadcast', 'how_many_days_ago')
    list_filter = ('broadcast',)
    ordering = ('title', 'updated_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 50
    actions = ('get_broadcast',)
    date_hierarchy = 'updated_at'
    # fields = (('title', 'slug'), 'body', 'broadcast')
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), 'body'),
            'description': 'Yazı için genel ayarlar'
        }),
        ('Opsiyonel ayarlar', {
            'fields': ('broadcast',),
            'description': 'Opsiyonel ayarlar için bu kümeyi kullanabilirsiniz'
        })
    )

    def get_broadcast(self, request, queryset):
        count = queryset.update(broadcast=True)
        self.message_user(request, f"{count} adet yazı yayına alındı")

    get_broadcast.short_description = 'İşaretlenen yazıları yayına al'

    def how_many_days_ago(self, blog):
        different = timezone.now() - blog.created_at
        return different.days

    how_many_days_ago.short_description = 'Kaç gün önce'


admin.site.register(Blog, BlogAdmin)
