# Generated by Django 3.2.8 on 2021-11-20 18:16

from django.db import migrations, models
import django.db.models.deletion
import plants.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('motivo', models.CharField(choices=[('REC', 'Recomendación'), ('PET', 'Petición'), ('ERR', 'Error')], max_length=3)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tierra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/LANDS/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nameComun', models.CharField(blank=True, max_length=200, null=True)),
                ('temperatura', models.CharField(blank=True, max_length=20, null=True)),
                ('temperaturaExtrema', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=plants.models.file_directory_path)),
                ('riego', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cuidados', models.TextField(blank=True, null=True)),
                ('consejos', models.TextField(blank=True, null=True)),
                ('tierra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plants.tierra')),
            ],
        ),
    ]
