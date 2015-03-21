# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0002_madmin_authority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='madmin',
            name='username',
        ),
        migrations.AddField(
            model_name='madmin',
            name='adminname',
            field=models.CharField(default=b'', unique=True, max_length=16),
            preserve_default=True,
        ),
    ]
