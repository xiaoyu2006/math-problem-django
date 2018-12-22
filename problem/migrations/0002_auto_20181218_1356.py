# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solve',
            name='name',
            field=models.TextField(default='Nemo', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problem',
            name='asker',
            field=models.TextField(max_length=25),
        ),
    ]
