# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-03 14:50
from __future__ import unicode_literals

import bugbounty.models
from django.db import migrations, models
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter_name', models.TextField()),
                ('reporter_email', models.EmailField(max_length=254)),
                ('type', enumfields.fields.EnumField(enum=bugbounty.models.ReportType, max_length=200)),
                ('title', models.TextField()),
                ('details', models.TextField()),
                ('status', enumfields.fields.EnumField(enum=bugbounty.models.ReportStatus, max_length=200)),
            ],
        ),
    ]
