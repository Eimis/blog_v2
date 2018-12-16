# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_boto.s3.storage


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_staticimage_pics_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticimage',
            name='landing_image',
            field=models.ImageField(storage=django_boto.s3.storage.S3Storage(), null=True, upload_to=b'', blank=True),
        ),
    ]
