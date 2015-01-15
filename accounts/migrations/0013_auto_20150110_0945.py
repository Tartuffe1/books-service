# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20150102_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='zupanija',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
    ]
