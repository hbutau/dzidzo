# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_track_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='description',
        ),
    ]
