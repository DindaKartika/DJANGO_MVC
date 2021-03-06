# Generated by Django 2.1.7 on 2019-02-12 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_challenge', models.CharField(max_length=255)),
                ('banyak_soal', models.CharField(max_length=3)),
                ('bobot_nilai', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Direksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('telepon', models.CharField(max_length=25)),
                ('jabatan', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LiveCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_live_code', models.CharField(max_length=255)),
                ('banyak_soal', models.CharField(max_length=3)),
                ('bobot_nilai', models.CharField(max_length=4)),
                ('tanggal_pelaksanaan', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelajaran', models.CharField(max_length=100)),
                ('jadwal_dimulai', models.DateTimeField()),
                ('jadwal_berakhir', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('telepon', models.CharField(max_length=25)),
                ('absen', models.CharField(max_length=3)),
                ('nilai_rata2', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('telepon', models.CharField(max_length=25)),
                ('mata_pelajaran', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran')),
            ],
        ),
        migrations.AddField(
            model_name='livecode',
            name='mata_pelajaran',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='mata_pelajaran',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran'),
        ),
    ]
