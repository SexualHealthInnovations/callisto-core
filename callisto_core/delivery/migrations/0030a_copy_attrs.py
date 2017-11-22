# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 14:24
from __future__ import unicode_literals

from django.db import migrations


def copy_attrs(apps, schema_editor):
    current_database = schema_editor.connection.alias
    SentFullReport = apps.get_model('delivery.SentMatchReport')
    NewSentMatchReport = apps.get_model('delivery.NewSentMatchReport')
    for instance in SentFullReport.objects.using(current_database):
        new_instance = NewSentMatchReport.objects.create(
            sent=instance.sent,
            to_address=instance.to_address,
        )
        for report in instance.reports.all():
            new_instance.add(report)


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0030_newsentmatchreport_proxysentmatchreport'),
    ]

    operations = [
        migrations.RunPython(
            copy_attrs,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
