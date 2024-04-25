from django.contrib import admin
from blog.models import Blog

admin.site.site_title = 'Extreme Title'
admin.site.site_header = 'Extreme Admin Portal'  # It also appears on Login Page
admin.site.index_title = 'Welcome to Extreme Admin Portal'


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'broadcast')
    list_filter = ('broadcast',)
    ordering = ('title', 'updated_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 50
    actions = ('get_broadcast',)
    date_hierarchy = 'updated_at'

    def get_broadcast(self, request, queryset):
        count = queryset.update(broadcast=True)
        self.message_user(request, f"{count} adet yazı yayına alındı")

    get_broadcast.short_description = 'İşaretlenen yazıları yayına al'


admin.site.register(Blog, BlogAdmin)
