# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0003_auto_20150321_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='madmin',
            name='adminname',
            field=models.CharField(unique=True, max_length=16),
            preserve_default=True,
        ),
    ]
