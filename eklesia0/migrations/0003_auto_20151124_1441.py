# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eklesia0', '0002_auto_20151117_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membro',
            name='cargo',
        ),
        migrations.AddField(
            model_name='membro',
            name='cargo',
            field=models.ManyToManyField(related_name='+', null=True, blank=True, to='eklesia0.Cargo'),
        ),
    ]
