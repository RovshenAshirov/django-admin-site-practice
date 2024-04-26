from django.contrib import admin
from django.utils import timezone
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from rangefilter.filters import DateTimeRangeFilter
from blog.models import Blog, Comment, Category

admin.site.site_title = 'Extreme Title'
admin.site.site_header = 'Extreme Admin Portal'  # It also appears on Login Page
admin.site.index_title = 'Welcome to Extreme Admin Portal'


# class CommentInline(admin.StackedInline):
class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('comment', 'broadcast')
    extra = 1
    classes = ('collapse',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'broadcast', 'how_many_days_ago',
                    'how_many_comments_are_there')
    list_filter = ('broadcast', ("created_at", DateTimeRangeFilter),)
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
            'fields': ('broadcast', 'categories'),
            'description': 'Opsiyonel ayarlar için bu kümeyi kullanabilirsiniz',
            'classes': ('collapse',)
        })
    )
    inlines = (CommentInline,)
    # filter_vertical = ('categories',)
    filter_horizontal = ('categories',)

    def get_broadcast(self, request, queryset):
        count = queryset.update(broadcast=True)
        self.message_user(request, f"{count} adet yazı yayına alındı")

    get_broadcast.short_description = 'İşaretlenen yazıları yayına al'

    def how_many_days_ago(self, blog):
        different = timezone.now() - blog.created_at
        return different.days

    how_many_days_ago.short_description = 'Kaç gün önce'

    def how_many_comments_are_there(self, blog):
        return blog.comments.count()

    how_many_comments_are_there.short_description = "Kaç tane yorum var"


class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at', 'broadcast')
    list_per_page = 50
    list_editable = ('broadcast',)
    list_filter = (('blog', RelatedDropdownFilter),)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
