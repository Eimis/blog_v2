# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20151120_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staticfiles',
            old_name='talks_image',
            new_name='sounds_image',
        ),
    ]
