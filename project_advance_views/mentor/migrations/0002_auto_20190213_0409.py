# Generated by Django 2.1.7 on 2019-02-13 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='mata_pelajaran',
        ),
        migrations.AddField(
            model_name='mentor',
            name='kesan',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='mentor',
            name='nick_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.DeleteModel(
            name='MataPelajaran',
        ),
    ]
