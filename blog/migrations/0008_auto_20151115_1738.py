# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_boto.s3.storage


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150913_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='picture',
            field=models.ImageField(storage=django_boto.s3.storage.S3Storage(), null=True, upload_to=b''),
        ),
    ]
