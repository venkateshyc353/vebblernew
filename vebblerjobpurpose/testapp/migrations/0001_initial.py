# Generated by Django 2.1.7 on 2019-03-27 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vebbler_coustmer_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('addres', models.CharField(max_length=250)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(default='aaaaaaaa@gmail.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='vebbler_ios_services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=250)),
                ('name', models.IntegerField()),
                ('device', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='vebbler_jobinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('feedback', models.TextField()),
                ('mobile', models.IntegerField()),
                ('addres', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='vebblerservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('cost', models.IntegerField()),
                ('contact', models.IntegerField()),
            ],
        ),
    ]