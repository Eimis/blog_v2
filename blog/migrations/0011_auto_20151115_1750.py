# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_staticimage_talks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staticimage',
            old_name='talks',
            new_name='talks_image',
        ),
    ]
