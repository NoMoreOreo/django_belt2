# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LogReg', '0009_auto_20170202_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('poked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poked', to='LogReg.User')),
                ('poker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poker', to='LogReg.User')),
            ],
        ),
    ]