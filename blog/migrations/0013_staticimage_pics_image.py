# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_boto.s3.storage


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20151115_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticimage',
            name='pics_image',
            field=models.ImageField(storage=django_boto.s3.storage.S3Storage(), null=True, upload_to=b'', blank=True),
        ),
    ]
