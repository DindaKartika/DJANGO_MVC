# Generated by Django 2.1.5 on 2019-02-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_mentee_nick_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=255)),
                ('created', models.DateTimeField()),
                ('update', models.DateTimeField()),
            ],
        ),
    ]
