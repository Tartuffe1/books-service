# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=15, choices=[(b'expert', b'Stru\xc4\x8dna literatura'), (b'classic', b'Knji\xc5\xbeevnost i beletristika'), (b'antiquarian', b'Antikvarne knjige'), (b'foreign', b'Strana literatura'), (b'encyclopedias', b'Enciklopedije i priru\xc4\x8dnici'), (b'periodicals', b'Periodika'), (b'comics', b'Stripovi'), (b'ostala', b'Ostala literatura')]),
            preserve_default=True,
        ),
    ]
