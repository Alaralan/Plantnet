# Generated by Django 3.2.8 on 2021-11-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='riego',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
