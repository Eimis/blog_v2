# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_boto.s3.storage


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151115_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticimage',
            name='code_image',
            field=models.ImageField(storage=django_boto.s3.storage.S3Storage(), null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='staticimage',
            name='thoughts_image',
            field=models.ImageField(storage=django_boto.s3.storage.S3Storage(), null=True, upload_to=b''),
        ),
    ]