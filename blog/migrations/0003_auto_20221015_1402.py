# Generated by Django 3.2.13 on 2022-10-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221015_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '게시글', 'verbose_name_plural': '게시글 목록'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '카테고리', 'verbose_name_plural': '카테고리 목록'},
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, to='blog.Category', verbose_name='카테고리'),
        ),
    ]