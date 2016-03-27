# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0006_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
