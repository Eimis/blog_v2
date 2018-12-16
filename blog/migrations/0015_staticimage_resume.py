# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_boto.s3.storage


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_staticimage_landing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticimage',
            name='resume',
            field=models.FileField(storage=django_boto.s3.storage.S3Storage(), null=True, upload_to=b'', blank=True),
        ),
    ]
