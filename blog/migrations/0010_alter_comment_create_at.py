# Generated by Django 4.1.3 on 2022-11-23 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_comment_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 15, 21, 47, 195771, tzinfo=datetime.timezone.utc)),
        ),
    ]