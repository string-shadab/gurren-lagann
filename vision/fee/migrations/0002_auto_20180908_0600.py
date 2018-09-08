# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-08 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fee', '0001_initial'),
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursefeedetail',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_fee_details', to='institute.SessionCourse'),
        ),
        migrations.AddField(
            model_name='coursefeedetail',
            name='fee_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fee_cources', to='fee.FeeType'),
        ),
    ]