# Generated by Django 2.0.6 on 2018-06-14 00:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('pubDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('slug', models.CharField(blank=True, max_length=255)),
                ('position', models.IntegerField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('pubDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('slug', models.CharField(blank=True, max_length=255)),
                ('position', models.IntegerField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('pubDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('slug', models.CharField(blank=True, max_length=255)),
                ('position', models.IntegerField(blank=True, unique=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programming.Language')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='article_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programming.Lists'),
        ),
        migrations.AddField(
            model_name='articles',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programming.Language'),
        ),
    ]