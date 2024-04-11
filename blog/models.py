from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='başlık')
    body = models.TextField(verbose_name='İçerik')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ekleme tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='guncelleme tarihi')

    class Meta:
        verbose_name = 'yazı'
        verbose_name_plural = 'yazılar'

    def __str__(self):
        return self.title
