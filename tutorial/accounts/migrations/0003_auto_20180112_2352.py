# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-12 18:22
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('gwalior', django.db.models.manager.Manager()),
            ],
        ),
    ]
