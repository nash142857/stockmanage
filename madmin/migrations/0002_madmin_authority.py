# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='madmin',
            name='authority',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
