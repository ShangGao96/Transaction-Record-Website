# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20161020_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='numTran',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
