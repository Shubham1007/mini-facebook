# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-14 06:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_friends'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Friends',
            new_name='Friend',
        ),
    ]
