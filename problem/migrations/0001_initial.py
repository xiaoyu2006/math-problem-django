# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=100)),
                ('text', models.TextField()),
                ('asker', models.TextField(max_length=25)),
                ('img', models.ImageField(upload_to=b'img', blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Solve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('name', models.TextField(max_length=25)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('problem', models.ForeignKey(to='problem.Problem')),
            ],
        ),
    ]
