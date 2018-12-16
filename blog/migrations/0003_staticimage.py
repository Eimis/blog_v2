# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_thought_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thoughs_image', models.ImageField(null=True, upload_to=b'')),
            ],
        ),
    ]
