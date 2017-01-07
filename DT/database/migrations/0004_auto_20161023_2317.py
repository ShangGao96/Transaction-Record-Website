# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20161020_0253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='day',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['day']},
        ),
    ]
