from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    categories = models.ManyToManyField(to='blog.Category', related_name='blogs', blank=True)
    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='başlık')
    body = RichTextField(verbose_name='İçerik')
    broadcast = models.BooleanField(default=True, verbose_name='yayın mı?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ekleme tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='guncelleme tarihi')

    class Meta:
        verbose_name = 'yazı'
        verbose_name_plural = 'yazılar'

    def __str__(self):
        return self.title

    # @property
    # def how_many_days_ago(self):
    #     different = timezone.now() - self.created_at
    #     return different.days

    # @property
    # def how_many_comments_are_there(self):
    #     return self.comments.count()


class Comment(models.Model):
    blog = models.ForeignKey(to='blog.Blog', related_name='comments', on_delete=models.CASCADE, verbose_name='blog')
    comment = models.TextField(verbose_name='yorum')
    broadcast = models.BooleanField(default=True, verbose_name='yayın mı?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ekleme tarihi')

    class Meta:
        verbose_name = 'yorum'
        verbose_name_plural = 'yorumlar'

    def __str__(self):
        return f"{self.blog.title} - {self.comment}"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='kategorinin adı')
    broadcast = models.BooleanField(default=True, verbose_name='yayın mı?')

    class Meta:
        verbose_name = 'kategori'
        verbose_name_plural = 'kategoriler'

    def __str__(self):
        return self.name
