# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_staticimage_resume'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StaticImage',
            new_name='StaticFiles',
        ),
    ]
