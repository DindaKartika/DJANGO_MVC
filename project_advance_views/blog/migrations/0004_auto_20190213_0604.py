# Generated by Django 2.1.7 on 2019-02-13 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190213_0533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='favorite',
            new_name='comment',
        ),
    ]
