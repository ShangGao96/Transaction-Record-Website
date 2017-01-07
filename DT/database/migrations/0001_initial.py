# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('numTran', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('usage', models.CharField(max_length=20, choices=[('cloth', 'cloth'), ('restaurant', 'restaurant'), ('grocery', 'grocery'), ('bill', 'bill'), ('other', 'other')])),
                ('amount', models.FloatField()),
                ('des', models.TextField(blank=True, verbose_name='description')),
                ('day', models.ForeignKey(to='database.Day')),
            ],
            options={
                'ordering': ['amount'],
            },
        ),
    ]
