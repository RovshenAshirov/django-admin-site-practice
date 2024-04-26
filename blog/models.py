from django.db import models
from django.utils import timezone


class Blog(models.Model):
    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='başlık')
    body = models.TextField(verbose_name='İçerik')
    broadcast = models.BooleanField(default=True, verbose_name='yayın mı?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ekleme tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='guncelleme tarihi')

    class Meta:
        verbose_name = 'yazı'
        verbose_name_plural = 'yazılar'

    def __str__(self):
        return self.title

    @property
    def how_many_days_ago(self):
        different = timezone.now() - self.created_at
        return different.days
