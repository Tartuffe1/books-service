# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20141129_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobitel',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zupanija',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
    ]
