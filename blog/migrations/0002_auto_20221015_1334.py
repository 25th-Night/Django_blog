# Generated by Django 3.2.13 on 2022-10-15 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='카테고리')),
                ('description', models.TextField(max_length=255, verbose_name='카테고리 안내')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='갱신일'),
        ),
    ]
