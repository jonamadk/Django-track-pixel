# Generated by Django 3.2.3 on 2021-05-20 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_usermodel_counter_is'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='unique_code',
            field=models.UUIDField(default=12512),
            preserve_default=False,
        ),
    ]
