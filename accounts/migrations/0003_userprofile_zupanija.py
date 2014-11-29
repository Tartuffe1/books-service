# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20141129_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='zupanija',
            field=models.CharField(default=datetime.datetime(2014, 11, 29, 8, 30, 42, 140000, tzinfo=utc), max_length=40, choices=[(b'zagrebacka', b'Zagreba\xe8ka \x9eupanija'), (b'krapinsko-zagorska', b'Krapinsko-zagorska \x9eupanija'), (b'sisacko-moslavacka', b'Sisa\xe8ko-moslava\xe8ka \x9eupanija'), (b'karlovacka', b'Karlova\xe8ka \x9eupanija'), (b'varazdinska', b'Vara\x9edinska \x9eupanija'), (b'koprivnicko-krizevacka', b'Koprivni\xe8ko-kri\x9eeva\xe8ka \x9eupanija'), (b'bjelovarsko-bilogorska', b'Bjelovarsko-bilogorska \x9eupanija'), (b'medjimurska', b'Me\xf0imurska \x9eupanija'), (b'grad-zagreb', b'Grad Zagreb'), (b'primorsko-goranska', b'Primorsko-goranska \x9eupanija'), (b'licko-senjska', b'Li\xe8ko-senjska \x9eupanija'), (b'istarska', b'Istarska \x9eupanija'), (b'viroviticko-podravska', b'Viroviti\xe8ko-podravska \x9eupanija'), (b'pozesko-slavonska', b'Po\x9ee\x9ako-slavonska \x9eupanija'), (b'brodsko-posavska', b'Brodsko-posavska \x9eupanija'), (b'osjecko-baranjska', b'Osje\xe8ko-baranjska \x9eupanija'), (b'vukovarsko-srijemska', b'Vukovarsko-srijemska \x9eupanija'), (b'zadarska', b'Zadarska \x9eupanija'), (b'sibensko-kninska', b'\x8aibensko-kninska \x9eupanija'), (b'splitsko-dalmatinska', b'Splitsko-dalmatinska \x9eupanija'), (b'dubrovacko-neretvanska', b'Dubrova\xe8ko-neretvanska \x9eupanija')]),
            preserve_default=False,
        ),
    ]
