# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("delivery", "0035_auto_20171122_1454")]

    operations = [
        migrations.RemoveField(model_name="sentreport", name="polymorphic_ctype"),
        migrations.DeleteModel(name="SentReport"),
    ]
