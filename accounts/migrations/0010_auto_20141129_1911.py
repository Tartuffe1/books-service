# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20141129_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='zupanija',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
    ]
