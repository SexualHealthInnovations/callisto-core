# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("wizard_builder", "0029_populate_type")]

    operations = [
        migrations.AlterModelOptions(name="checkbox", options={}),
        migrations.AlterModelOptions(
            name="formquestion", options={"ordering": ["position"]}
        ),
    ]
