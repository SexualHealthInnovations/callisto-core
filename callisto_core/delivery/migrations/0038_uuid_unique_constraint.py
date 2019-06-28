# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 20:47
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("delivery", "0037_u_uuid")]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        )
    ]
