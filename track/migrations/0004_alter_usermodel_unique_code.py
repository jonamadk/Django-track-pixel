# Generated by Django 3.2.3 on 2021-05-20 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_usermodel_unique_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='unique_code',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
