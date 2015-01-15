# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import books.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=30, choices=[(b'expert', b'Stru\xc4\x8dna literatura'), (b'classic', b'Knji\xc5\xbeevnost i beletristika'), (b'antiquarian', b'Antikvarne knjige'), (b'foreign', b'Strana literatura'), (b'encyclopedias_and_handbooks', b'Enciklopedije i priru\xc4\x8dnici'), (b'periodicals', b'Periodika'), (b'comics', b'Stripovi'), (b'ostala', b'Ostala literatura')])),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('docfile', models.FileField(default=b'images/default.jpg', null=True, upload_to=books.models.get_file_path, blank=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
