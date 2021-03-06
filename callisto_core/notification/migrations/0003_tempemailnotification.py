# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-24 14:49
from __future__ import unicode_literals

from django.db import migrations, models


def populate_temp_emails(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    EmailNotification = apps.get_model("notification", "EmailNotification")
    TempEmailNotification = apps.get_model("notification", "TempEmailNotification")
    for email in EmailNotification.objects.using(db_alias):
        temp_email = TempEmailNotification.objects.using(db_alias).create(
            name=email.name, subject=email.subject, body=email.body
        )
        for site in email.sites.all():
            temp_email.sites.add(site.id)


def delete_temp_emails(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    TempEmailNotification = apps.get_model("notification", "TempEmailNotification")
    TempEmailNotification.objects.using(db_alias).delete()


class Migration(migrations.Migration):

    dependencies = [("notification", "0002_emailnotification_sites")]

    operations = [
        migrations.CreateModel(
            name="TempEmailNotification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("subject", models.CharField(max_length=77)),
                ("body", models.TextField()),
                ("sites", models.ManyToManyField(to="sites.Site")),
            ],
        ),
        migrations.RunPython(populate_temp_emails, delete_temp_emails),
    ]
