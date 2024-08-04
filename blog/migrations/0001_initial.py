# Generated by Django 5.0.1 on 2024-07-31 06:22

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=100)),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=100)),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
                ('web_url', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('batch', models.ManyToManyField(to='blog.year')),
            ],
        ),
    ]
