# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='usage',
            field=models.CharField(max_length=20, default='cloth', choices=[('cloth', 'cloth'), ('restaurant', 'restaurant'), ('grocery', 'grocery'), ('bill', 'bill'), ('other', 'other')]),
        ),
    ]
