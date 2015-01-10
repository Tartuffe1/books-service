# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20141205_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='zupanija',
            field=models.CharField(default=None, max_length=40, blank=True),
            preserve_default=True,
        ),
    ]
