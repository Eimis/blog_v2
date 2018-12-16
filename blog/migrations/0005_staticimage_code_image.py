# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150910_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticimage',
            name='code_image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
