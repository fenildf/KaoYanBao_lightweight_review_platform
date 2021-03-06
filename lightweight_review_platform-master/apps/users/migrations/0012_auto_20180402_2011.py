# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-02 20:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180328_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_content', models.CharField(max_length=20, verbose_name='搜索内容')),
                ('user_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '所属用户',
                'verbose_name_plural': '所属用户',
            },
        ),
        migrations.AddField(
            model_name='userweaknesstag',
            name='score',
            field=models.IntegerField(default=1, verbose_name='弱项标签评分'),
        ),
    ]
