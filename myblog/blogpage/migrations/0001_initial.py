# Generated by Django 5.0.3 on 2024-06-30 11:50

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('author', models.CharField(default='anonymous', max_length=200)),
                ('contents', django_ckeditor_5.fields.CKEditor5Field()),
                ('tags', models.CharField(max_length=200)),
                ('is_popular', models.BooleanField(default=False)),
                ('cover_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
