# Generated by Django 4.2.11 on 2024-04-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ad')),
                ('broadcast', models.BooleanField(default=True, verbose_name='yayın mı?')),
            ],
            options={
                'verbose_name': 'kategori',
                'verbose_name_plural': 'kategoriler',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='blogs', to='blog.category'),
        ),
    ]
