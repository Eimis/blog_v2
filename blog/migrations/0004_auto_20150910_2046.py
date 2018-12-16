# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_staticimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staticimage',
            old_name='thoughs_image',
            new_name='thoughts_image',
        ),
    ]
